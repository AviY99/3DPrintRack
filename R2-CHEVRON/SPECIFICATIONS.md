# R2-CHEVRON Specifications

| Parameter | Final value |
|---|---:|
| Layout | **10 cells, 4-3-2-1** |
| Internal hex AF | **33 mm** |
| Overall Z height/depth | **65 mm** |
| Hex wall | **2.5 mm** |
| Rear wall | **2.5 mm** |
| Corner feature | **3 through-chevron openings** |
| Chevron width | **19.36 mm** |
| Chevron height | **~16.77 mm** |
| Inner V depth | **~5.59 mm** |
| Outer angles | **60°** |
| Inner angles | **30°** |
| Minimum material thickness in feature area | **~3.0 mm** |
| CAD volume | **~228.24157 cm³** |
| Outer envelope | **Same as R1** |

## Connector

R2 uses exactly the same locked connector geometry as R1.

- Male neck: **5.20 mm**
- Male head: **8.20 mm**
- Male depth: **2.50 mm**
- Female mouth: **5.70 mm**
- Female inner width: **8.70 mm**
- Female depth: **2.70 mm**
- Side clearance: **0.25 mm per side**
- Total lateral difference: **0.50 mm**
- Depth clearance: **0.20 mm**

Canonical specification: [../CONNECTOR_SPEC.md](../CONNECTOR_SPEC.md).

## Test coupon

- Connector Z length on coupon: **32.5 mm**
- Same connector cross-section as the full model
- Chevron coupon includes a matching side-mate STL in the handed-off final files

## Recorded slicer result

Using the shared comparison settings (**5% Gyroid**, **4 perimeters**, same print layout):

- Weight: **229 g**
- Filament: **76.83 m**
- Print time: **16:13**

Although R2 has lower CAD volume than R1, it used more filament and more print time in the recorded slice because the chevrons introduce more internal perimeter/surface.

See [../docs/SPECIFICATIONS.md](../docs/SPECIFICATIONS.md).
