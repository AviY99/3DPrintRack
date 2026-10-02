from pathlib import Path
import json
import trimesh

ROOT = Path(__file__).resolve().parent

STL_FILES = [
    ROOT / "R1-HOLE/STL/V17T3_LITE_FINAL_R1_HOLE.stl",
    ROOT / "R1-HOLE/STL/V17T3_LITE_FINAL_R1_HOLE_print_plate.stl",
    ROOT / "R2-CHEVRON/STL/V17T3_LITE_FINAL_R2_CHEVRON.stl",
    ROOT / "R2-CHEVRON/STL/V17T3_LITE_FINAL_R2_CHEVRON_print_plate.stl",
    ROOT / "R1-HOLE/TEST-COUPON/STL/V17T3_LITE_FINAL_R1_TEST_HOLE.stl",
    ROOT / "R1-HOLE/TEST-COUPON/STL/V17T3_TEST_SIDE_MATE.stl",
    ROOT / "R1-HOLE/TEST-COUPON/STL/assembled_check.stl",
    ROOT / "R1-HOLE/TEST-COUPON/STL/print_plate.stl",
    ROOT / "R2-CHEVRON/TEST-COUPON/STL/V17T3_LITE_FINAL_R2_TEST_CHEVRON.stl",
    ROOT / "R2-CHEVRON/TEST-COUPON/STL/V17T3_TEST_SIDE_MATE.stl",
    ROOT / "R2-CHEVRON/TEST-COUPON/STL/assembled_check.stl",
    ROOT / "R2-CHEVRON/TEST-COUPON/STL/print_plate.stl",
]

for path in STL_FILES:
    mesh = trimesh.load_mesh(path, force="mesh", process=False)
    mesh.merge_vertices()
    keep = mesh.area_faces > 1e-10
    mesh.update_faces(keep)
    mesh.remove_unreferenced_vertices()
    mesh.export(path)

VALIDATIONS = [
    (ROOT / "R1-HOLE/STL/V17T3_LITE_FINAL_R1_HOLE.stl", ROOT / "R1-HOLE/validation/model.json"),
    (ROOT / "R2-CHEVRON/STL/V17T3_LITE_FINAL_R2_CHEVRON.stl", ROOT / "R2-CHEVRON/validation/model.json"),
    (ROOT / "R1-HOLE/TEST-COUPON/STL/V17T3_LITE_FINAL_R1_TEST_HOLE.stl", ROOT / "R1-HOLE/TEST-COUPON/validation/coupon.json"),
    (ROOT / "R2-CHEVRON/TEST-COUPON/STL/V17T3_LITE_FINAL_R2_TEST_CHEVRON.stl", ROOT / "R2-CHEVRON/TEST-COUPON/validation/coupon.json"),
]

for stl_path, json_path in VALIDATIONS:
    mesh = trimesh.load_mesh(stl_path, force="mesh")
    data = json.loads(json_path.read_text(encoding="utf-8"))
    data["watertight"] = bool(mesh.is_watertight)
    data["bounds_mm"] = mesh.bounds.tolist()
    data["extents_mm"] = mesh.extents.tolist()
    data["volume_mm3"] = float(mesh.volume)
    data["surface_area_mm2"] = float(mesh.area)
    json_path.write_text(json.dumps(data, indent=2), encoding="utf-8")
