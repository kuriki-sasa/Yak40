from typing import Dict
from cadquery import Edge, Location, Sketch, Vector, Vertex
import numpy
from cadquery.occ_impl.shapes import TopAbs_Orientation

def _tangent_angle(vector1: Vector, vector2: Vector):
    u = numpy.array([vector1.x, vector1.y])
    v = numpy.array([vector2.x, vector2.y])
    i = numpy.inner(u, v)
    n = numpy.linalg.norm(u) * numpy.linalg.norm(v)
    c = i / n
    angle = numpy.rad2deg(numpy.arccos(numpy.clip(c, -1.0, 1.0)))
    cross = numpy.cross(u, v)
    if cross < 0:
        angle *= -1
    return angle

def _edge_angle_map(sketch: Sketch) -> Dict[Edge, float]:
    face = sketch._faces
    d = face._entitiesFrom("Vertex", "Edge")
    d = dict((k, v) for k, v in d.items() if len(v) == 2)
    out = {}
    for pt, (edge1, edge2) in d.items():
        v0 = edge1.startPoint() - edge1.endPoint()
        v1 = edge2.startPoint() - edge2.endPoint()
        angle = _tangent_angle(v0, v1)
        if pt.wrapped.Orientation() != TopAbs_Orientation.TopAbs_FORWARD:
            angle *= -1
        out[pt] = angle
    return out

def inside_vertices(self: Sketch) -> Sketch:
    """select the vertices with positive angles between the edges."""
    mappings = _edge_angle_map(self)
    vertices = [k for k, v in mappings.items() if v < 0]
    self._selection = self._unique(vertices)
    return self
Sketch.inside_vertices = inside_vertices

def outside_vertices(self: Sketch) -> Sketch:
    """select the vertices with negative angles between the edges."""
    mappings = _edge_angle_map(self)
    vertices = [k for k, v in mappings.items() if v > 0]
    self._selection = self._unique(vertices)
    return self
Sketch.outside_vertices = outside_vertices

def center(self: Sketch, x: float, y: float) -> Sketch:
    """Shift local coordinates to the specified location."""
    self._selection = [Location((x, y, 0))]
    return self
Sketch.center = center
