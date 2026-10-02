# 3DPrintRack

Modular 3D-printed triangular rack for hobby paint bottles.

This repository contains two frozen final variants built from the same validated V17T.3-Lite geometry:

- **R1-HOLE** — functional version with three Ø8.2 mm through-holes at the triangle corners. The holes also provide an optional wall-mounting point.
- **R2-CHEVRON** — design-oriented version that replaces the three corner holes with symmetric through-chevron openings.

Both variants keep the same 10-cell 4-3-2-1 layout, AF33 bottle cells, 2.5 mm hex walls, 65 mm print depth/height, 2.5 mm rear wall, and the same production-proven V16.8 male/female connector geometry.

## Repository layout

```text
R1-HOLE/
├── STL/
├── STEP-Onshape/
├── TEST-COUPON/
│   ├── STL/
│   ├── STEP/
│   └── drawings/
├── drawings/
├── validation/
├── README.md
└── SPECIFICATIONS.md

R2-CHEVRON/
├── STL/
├── STEP-Onshape/
├── TEST-COUPON/
│   ├── STL/
│   ├── STEP/
│   └── drawings/
├── drawings/
├── validation/
├── README.md
└── SPECIFICATIONS.md

docs/
├── CONNECTOR_SPEC.md
└── PRINTING_NOTES.md

CHANGELOG.md
```

## Connector status

The connector cross-section is locked and physically validated:

- Male neck/head: **5.2 / 8.2 mm**
- Male depth: **2.5 mm**
- Female mouth/inner: **5.7 / 8.7 mm**
- Female depth: **2.7 mm**
- Nominal lateral clearance: **0.25 mm per side**
- Depth clearance: **0.20 mm**

See `docs/CONNECTOR_SPEC.md` for the full specification and validation notes.

## Important slicer finding

R2-CHEVRON has lower CAD volume than R1-HOLE, but in the user's same EasyPrint slice it used **more filament and slightly more time** because the chevron creates substantially more perimeter/surface area. This result is documented in `docs/PRINTING_NOTES.md`.

## CAD / Onshape

The `STEP-Onshape/` folders contain STEP solids intended for import into Onshape. These are not native cloud Onshape documents.

## Status

Both **R1-HOLE** and **R2-CHEVRON** are frozen final configurations. Changes should be made as new revisions rather than overwriting these versions.
