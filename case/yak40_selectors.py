from cadquery import Face, Selector, Vector, Workplane
import math

class AngledFaceSelector(Selector):
    def __init__(self, degree, tolerance=0.01):
        self.degree = degree
        self.tolerance = tolerance

    def filter(self, objectList):
        faces = [item for item in objectList if type(item) == Face]
        matchedFaces = []
        for face in faces:
            faceNormal = face.normalAt()
            faceAngle = Vector(0.0, 0.0, 1.0).getAngle(faceNormal)
            if abs(self.degree - math.degrees(faceAngle)) <= self.tolerance:
                matchedFaces.append(face)
            faceAngle = Vector(0.0, 0.0, -1.0).getAngle(faceNormal)
            if abs(self.degree - math.degrees(faceAngle)) <= self.tolerance:
                matchedFaces.append(face)
        return matchedFaces
