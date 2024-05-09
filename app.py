import rhinoinside
import ghhops_server as hs

rhinoinside.load()
# register hops app as middleware\
import System
import Rhino
from Rhino import Geometry as rg
import math

hops = hs.Hops(app=rhinoinside)


@hops.component(
    "/testhops2",
    name="Test",
    description="Test Hops functionality",
    inputs=[
        hs.HopsCurve("Edges", "edges", "Front Facades"),
    ],
    outputs=[
        hs.HopsCurve("Test 1", "test1", "foo"),
        hs.HopsInteger("Test 2", "test2", "bar"),
    ],
)

def testhops2(edges):
    """ Find Secondary Edges """

    def secondary_edges(edges_arg):
        all_add_crvs = []
        all_add_angle = []
        print(edges_arg)
        edges_arg = [edges_arg]
        print(edges_arg)
        for crv in edges_arg:
            print(crv)
            end_t = rg.Curve.DivideByCount(crv, 1, True)
            print(end_t)
            end_pt = [rg.Curve.PointAt(crv, x) for x in end_t]
            print(end_pt)
            crv_line = rg.Line(end_pt[0], end_pt[1])
            mid_t = rg.Curve.DivideByCount(crv, 2, False)
            mid_pt = rg.Curve.PointAt(crv, mid_t[0])
            add_crvs = []
            add_angles = []
            for add_crv in edges_arg:
                add_mid_t = rg.Curve.DivideByCount(add_crv, 2, False)
                add_mid_pt = rg.Curve.PointAt(add_crv, add_mid_t[0])
                pt_dist_mid = rg.Point3d.DistanceTo(add_mid_pt, mid_pt)
                if pt_dist_mid > 1:
                    end_ts = rg.Curve.DivideByCount(add_crv, 1, True)
                    end_pts = [rg.Curve.PointAt(add_crv, x) for x in end_ts]
                    add_crv_line = rg.Line(end_pts[0], end_pts[1])
                    add_crvs.append(add_crv_line)
                    end_t = rg.Curve.DivideByCount(add_crv, 1, True)
                    end_pt = [rg.Curve.PointAt(add_crv, x) for x in end_t]
                    add_crv_line = rg.Line(end_pt[0], end_pt[1])
                    vector_1 = crv_line.Direction
                    vector_2 = add_crv_line.Direction
                    int_angle = rg.Vector3d.VectorAngle(vector_1, vector_2)
                    add_angle = math.degrees(int_angle)
                    add_angles.append(add_angle)
            all_add_crvs.append(add_crvs)
            all_add_angle.append(add_angles)
        return all_add_crvs, all_add_angle

    sec_def = secondary_edges(edges)

    test = sec_def[0]
    test2 = sec_def[1]

    return test, test2

#
# @hops.component(
#     "/testdef",
#     name="TestDef",
#     description="Test Hops functionality",
#     inputs=[
#         hs.HopsPoint("Corner", "corner_pts", "Corner Points"),
#         hs.HopsCurve("Typos", "typos", "Typo Shapes"),
#         hs.HopsCurve("Edges", "edges", "Front Facades"),
#         hs.HopsSurface("Shapes", "shapes", "Typo Surface"),
#         hs.HopsInteger("Branch", "org_bra", "Original Typo Number"),
#         hs.HopsInteger("Corner Type", "c_type", "Corner Typo Boolean"),
#     ],
#     outputs=[
#         hs.HopsCurve("Test 1", "test1", "bleh"),
#         hs.HopsInteger("Test 2", "test2", "bleh2"),
#     ],
# )
#
# def testdef(corner_pts, typos, edges, shapes, org_bra, c_type):
#     ''' Find Secondary Edges '''
#
#     def secondary_edges(edges, corner_pts_list):
#         all_add_crvs = []
#         all_add_angle = []
#         edges = [edges]
#         for crv in edges:
#             end_t = rg.Curve.DivideByCount(crv, 1, True)
#             end_pt = [rg.Curve.PointAt(crv, x) for x in end_t]
#             crv_line = rg.Line(end_pt[0], end_pt[1])
#             mid_t = rg.Curve.DivideByCount(crv, 2, False)
#             mid_pt = rg.Curve.PointAt(crv, mid_t[0])
#             add_crvs = []
#             add_angles = []
#             for add_crv in edges:
#                 add_mid_t = rg.Curve.DivideByCount(add_crv, 2, False)
#                 add_mid_pt = rg.Curve.PointAt(add_crv, add_mid_t[0])
#                 pt_dist_mid = rg.Point3d.DistanceTo(add_mid_pt, mid_pt)
#                 if pt_dist_mid > 1:
#                     end_ts = rg.Curve.DivideByCount(add_crv, 1, True)
#                     end_pts = [rg.Curve.PointAt(add_crv, x) for x in end_ts]
#                     add_crv_line = rg.Line(end_pts[0], end_pts[1])
#                     add_crvs.append(add_crv_line)
#                     end_t = rg.Curve.DivideByCount(add_crv, 1, True)
#                     end_pt = [rg.Curve.PointAt(add_crv, x) for x in end_t]
#                     add_crv_line = rg.Line(end_pt[0], end_pt[1])
#                     vector_1 = crv_line.Direction
#                     vector_2 = add_crv_line.Direction
#                     int_angle = rg.Vector3d.VectorAngle(vector_1, vector_2)
#                     add_angle = math.degrees(int_angle)
#                     add_angles.append(add_angle)
#             all_add_crvs.append(add_crvs)
#             all_add_angle.append(add_angles)
#         return all_add_crvs, all_add_angle
#
#     sec_def = secondary_edges(edges, corner_pts)
#     # test = th.list_to_tree(sec_def[0])
#     # test2 = th.list_to_tree(sec_def[1])
#
#     test = sec_def[0]
#     test2 = sec_def[1]
#
#     return test, test2

if __name__ == "__main__":
    hops.start(debug=True)