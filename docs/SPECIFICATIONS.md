# 3DPrintRack Specifications

## Shared base geometry

| Parameter | Value |
|---|---:|
| Cell count | **10** |
| Layout | **4-3-2-1** |
| Internal hex AF | **33 mm** |
| Overall Z height/depth | **65 mm** |
| Hex wall | **2.5 mm** |
| Rear wall | **2.5 mm** |
| Approx. outer envelope | **184.624359 × 162.389374 × 65 mm** |
| Connector | **V16.8 re-entrant locking connector** |

## R1-HOLE

- Functional preferred version
- Three **Ø8.2 mm** through-holes
- Holes may also be used as wall-mounting points
- CAD volume: **~239.0465 cm³**

## R2-CHEVRON

- Design-oriented alternative
- Three through-chevron openings instead of the Ø8.2 mm holes
- Chevron width: **19.36 mm**
- Chevron height: **~16.77 mm**
- Inner V depth: **~5.59 mm**
- Outer angles: **60°**
- Inner angles: **30°**
- Minimum material thickness in the area: **~3.0 mm**
- CAD volume: **~228.24157 cm³**
- Same outer envelope and connector geometry as R1

## Locked connector

See [../CONNECTOR_SPEC.md](../CONNECTOR_SPEC.md).

## Slicer comparison

Both variants were sliced with the same main settings:

- **5% Gyroid**
- **4 perimeters**
- Same print layout

| Metric | R1-HOLE | R2-CHEVRON |
|---|---:|---:|
| CAD volume | **239.05 cm³** | **228.24 cm³** |
| Slicer weight | **221 g** | **229 g** |
| Filament length | **74.15 m** | **76.83 m** |
| Print time | **15:59** | **16:13** |

### Interpretation

R2 removes about **10.8 cm³** of CAD volume compared with R1, yet it requires more filament and more print time in the recorded slice.

The reason is that the chevron creates additional internal perimeter and surface. With four perimeters, the newly created walls are printed densely, while bulk material that remains in the corner can be represented mostly by the low-density **5% infill**.

Therefore, in FDM, lower CAD volume does not necessarily mean lower filament use or shorter print time.

### Practical conclusion

- **R1-HOLE** is the preferred functional version and was also more efficient in the recorded slice.
- **R2-CHEVRON** is retained as the design-oriented alternative.

## STEP / Onshape

STEP files are intended for import into Onshape. There is no local native Onshape file in this repository.
