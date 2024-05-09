import rhinoinside
rhinoinside.load()
import System
import Rhino
from Rhino import Geometry as rg


# for now, you need to explicitly use floating point
# numbers in Point3d constructor
pts = System.Collections.Generic.List[Rhino.Geometry.Point3d]()
pts.Add(rg.Point3d(0.0,0.0,0.0))
pts.Add(rg.Point3d(1.0,0.0,0.0))
pts.Add(rg.Point3d(1.5,2.0,0.0))

crv = rg.Curve.CreateInterpolatedCurve(pts,3)
print (crv.GetLength())
