from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED

ROOT = Path(__file__).resolve().parent

def make(out, prefix, pairs):
    out = ROOT / out
    out.parent.mkdir(parents=True, exist_ok=True)
    with ZipFile(out, "w", compression=ZIP_DEFLATED, compresslevel=9) as z:
        for src, suffix in pairs:
            p = ROOT / src
            if not p.exists():
                raise FileNotFoundError(p)
            z.write(p, prefix + suffix)

make(
    "R1-HOLE/packages/rack_V17T3_LITE_FINAL_R1_connectorfix_package.zip",
    "rack_V17T3_LITE_FINAL_R1_connectorfix_AF33_H65_back2p5_3xD8p2",
    [
        ("R1-HOLE/STL/V17T3_LITE_FINAL_R1_HOLE.stl", ".stl"),
        ("R1-HOLE/STL/V17T3_LITE_FINAL_R1_HOLE_print_plate.stl", "_print_plate.stl"),
        ("R1-HOLE/STEP-Onshape/V17T3_LITE_FINAL_R1_HOLE_Onshape.step", "_Onshape.step"),
        ("R1-HOLE/drawings/section.png", "_section.png"),
        ("R1-HOLE/drawings/connector_detail.png", "_connector_fix_detail.png"),
        ("R1-HOLE/validation/model.json", "_validation.json"),
        ("R1-HOLE/README.md", "_README.txt"),
    ],
)

make(
    "R1-HOLE/TEST-COUPON/packages/rack_V17T3_LITE_FINAL_R1_TEST_singlehex_topcorner_connectorfix_package.zip",
    "rack_V17T3_LITE_FINAL_R1_TEST_singlehex_topcorner_AF33_H32p5_connectorfix",
    [
        ("R1-HOLE/TEST-COUPON/STL/V17T3_LITE_FINAL_R1_TEST_HOLE.stl", ".stl"),
        ("R1-HOLE/TEST-COUPON/STEP/V17T3_LITE_FINAL_R1_TEST_HOLE.step", ".step"),
        ("R1-HOLE/TEST-COUPON/STL/V17T3_TEST_SIDE_MATE.stl", "_side_mate.stl"),
        ("R1-HOLE/TEST-COUPON/STEP/V17T3_TEST_SIDE_MATE.step", "_side_mate.step"),
        ("R1-HOLE/TEST-COUPON/STL/print_plate.stl", "_print_plate.stl"),
        ("R1-HOLE/TEST-COUPON/STEP/print_plate.step", "_print_plate.step"),
        ("R1-HOLE/TEST-COUPON/STL/assembled_check.stl", "_assembled_check.stl"),
        ("R1-HOLE/TEST-COUPON/STEP/assembled_check.step", "_assembled_check.step"),
        ("R1-HOLE/TEST-COUPON/drawings/section.png", "_section.png"),
        ("R1-HOLE/TEST-COUPON/drawings/assembled_section.png", "_assembled_section.png"),
        ("R1-HOLE/TEST-COUPON/validation/coupon.json", "_validation.json"),
        ("R1-HOLE/TEST-COUPON/README.md", "_README.txt"),
    ],
)

make(
    "R2-CHEVRON/packages/rack_V17T3_LITE_FINAL_R2_CHEVRON_package.zip",
    "rack_V17T3_LITE_FINAL_R2_CHEVRON_AF33_H65_back2p5",
    [
        ("R2-CHEVRON/STL/V17T3_LITE_FINAL_R2_CHEVRON.stl", ".stl"),
        ("R2-CHEVRON/STL/V17T3_LITE_FINAL_R2_CHEVRON_print_plate.stl", "_print_plate.stl"),
        ("R2-CHEVRON/STEP-Onshape/V17T3_LITE_FINAL_R2_CHEVRON_Onshape.step", "_Onshape.step"),
        ("R2-CHEVRON/drawings/section.png", "_section.png"),
        ("R2-CHEVRON/validation/model.json", "_validation.json"),
        ("R2-CHEVRON/README.md", "_README.txt"),
    ],
)

make(
    "R2-CHEVRON/TEST-COUPON/packages/rack_V17T3_LITE_FINAL_R2_TEST_CHEVRON_package.zip",
    "rack_V17T3_LITE_FINAL_R2_TEST_singlehex_topcorner_AF33_H32p5_chevron",
    [
        ("R2-CHEVRON/TEST-COUPON/STL/V17T3_LITE_FINAL_R2_TEST_CHEVRON.stl", ".stl"),
        ("R2-CHEVRON/TEST-COUPON/STEP/V17T3_LITE_FINAL_R2_TEST_CHEVRON.step", ".step"),
        ("R2-CHEVRON/TEST-COUPON/STL/V17T3_TEST_SIDE_MATE.stl", "_side_mate.stl"),
        ("R2-CHEVRON/TEST-COUPON/STEP/V17T3_TEST_SIDE_MATE.step", "_side_mate.step"),
        ("R2-CHEVRON/TEST-COUPON/STL/print_plate.stl", "_print_plate.stl"),
        ("R2-CHEVRON/TEST-COUPON/STEP/print_plate.step", "_print_plate.step"),
        ("R2-CHEVRON/TEST-COUPON/STL/assembled_check.stl", "_assembled_check.stl"),
        ("R2-CHEVRON/TEST-COUPON/STEP/assembled_check.step", "_assembled_check.step"),
        ("R2-CHEVRON/TEST-COUPON/drawings/section.png", "_section.png"),
        ("R2-CHEVRON/TEST-COUPON/drawings/assembled_section.png", "_assembled_section.png"),
        ("R2-CHEVRON/TEST-COUPON/validation/coupon.json", "_validation.json"),
        ("R2-CHEVRON/TEST-COUPON/README.md", "_README.txt"),
    ],
)
