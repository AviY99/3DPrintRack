# 3DPrintRack

Modular 3D-printed rack with two frozen final variants.

## Final variants

### R1-HOLE
Functional preferred version.

- 10 cells in a 4-3-2-1 layout
- Internal hex AF: **33 mm**
- Overall Z height/depth: **65 mm**
- Hex wall: **2.5 mm**
- Rear wall: **2.5 mm**
- Three **Ø8.2 mm** through-holes
- Approx. envelope: **184.624359 × 162.389374 × 65 mm**
- CAD volume: **~239.0465 cm³**
- Holes may also be used as wall-mounting points

### R2-CHEVRON
Design-oriented alternative.

- Same base geometry as R1
- Replaces the three Ø8.2 mm holes with three through-chevron openings
- Chevron width: **19.36 mm**
- Chevron height: **~16.77 mm**
- Inner V depth: **~5.59 mm**
- Outer angles: **60°**
- Inner angles: **30°**
- Minimum material thickness in the area: **~3.0 mm**
- CAD volume: **~228.24157 cm³**
- Same outer envelope and connector geometry as R1

## Connector

Both variants use the same physically validated and locked **V16.8 re-entrant locking connector**.

See [CONNECTOR_SPEC.md](CONNECTOR_SPEC.md).

## Slicer comparison

Both variants were sliced with the same main settings: **5% Gyroid** and **4 perimeters**.

| Metric | R1-HOLE | R2-CHEVRON |
|---|---:|---:|
| CAD volume | 239.05 cm³ | 228.24 cm³ |
| Slicer weight | 221 g | 229 g |
| Filament length | 74.15 m | 76.83 m |
| Print time | 15:59 | 16:13 |

Despite its lower CAD volume, R2 uses more filament and slightly more print time because the chevrons add internal perimeter and surface area. See [docs/SPECIFICATIONS.md](docs/SPECIFICATIONS.md) and [docs/PRINTING_NOTES.md](docs/PRINTING_NOTES.md).

## Repository layout

```text
3DPrintRack/
├── README.md
├── CHANGELOG.md
├── CONNECTOR_SPEC.md
├── docs/
│   ├── SPECIFICATIONS.md
│   ├── CONNECTOR_SPEC.md
│   └── PRINTING_NOTES.md
├── R1-HOLE/
│   ├── README.md
│   ├── SPECIFICATIONS.md
│   ├── STL/
│   ├── STEP-Onshape/
│   ├── TEST-COUPON/
│   │   ├── README.md
│   │   ├── STL/
│   │   ├── STEP/
│   │   └── previews/
│   └── drawings/
├── R2-CHEVRON/
│   ├── README.md
│   ├── SPECIFICATIONS.md
│   ├── STL/
│   ├── STEP-Onshape/
│   ├── TEST-COUPON/
│   │   ├── README.md
│   │   ├── STL/
│   │   ├── STEP/
│   │   └── previews/
│   └── drawings/
└── validation/
```

Additional validation/drawing folders already present in the repository are retained.

## STEP / Onshape

Files in `STEP-Onshape/` and coupon `STEP/` folders are STEP files intended for import into Onshape. They are not native local Onshape documents.

## Status

R1-HOLE and R2-CHEVRON are parallel frozen final variants. The connector geometry is locked; do not alter it without an explicit new revision and validation.
