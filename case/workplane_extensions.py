import math
from typing import Optional
from cadquery import Solid, Vector, Workplane, Sketch, Location, exporters

def drillHole(
    self: Workplane,
    diameter: float,
    depth: Optional[float] = None,
    tipAngle: float = 118,
    clean: bool = True,
) -> Workplane:
    if depth is None:
        depth = self.largestDimension()

    boreDir = Vector(0, 0, -1)
    r = diameter / 2.0

    hole = Solid.makeCylinder(r, depth, Vector(), boreDir)
    h = r / math.tan(math.radians(tipAngle / 2.0))
    tipCone = Solid.makeCone(r, 0.0, h, Vector(0, 0, -depth), boreDir)
    res = hole.fuse(tipCone)

    return self.cutEach(lambda loc: res.moved(loc), True, clean)
Workplane.drillHole = drillHole