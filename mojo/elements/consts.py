from enum import Enum


class GeomType(Enum):
    PLANE = "plane"
    HFIELD = "hfield"
    SPHERE = "sphere"
    CAPSULE = "capsule"
    ELLIPSOID = "ellipsoid"
    CYLINDER = "cylinder"
    BOX = "box"
    MESH = "mesh"
    SDF = "sdf"


class SiteType(Enum):
    SPHERE = "sphere"
    CAPSULE = "capsule"
    ELLIPSOID = "ellipsoid"
    CYLINDER = "cylinder"
    BOX = "box"


class TextureMapping(Enum):
    PLANAR = "2d"
    CUBE = "cube"
    SKYBOX = "skybox"


class LightType(Enum):
    DIRECTIONAL = "directional"
    SPOTLIGHT = "spotlight"


class JointType(Enum):
    FREE = "free"
    BALL = "ball"
    SLIDE = "slide"
    HINGE = "hinge"
