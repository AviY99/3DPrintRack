# Printing Notes

Target printer used during development: **Original Prusa i3 MK3S / MK3S+**, 0.4 mm nozzle.

## Recommended starting point

- Orientation: rear wall on the print bed, bottle openings upward.
- Layer height: **0.20 mm** is appropriate for the final large print.
- Infill: **5% Gyroid** was used successfully in the slicing tests.
- Perimeters: **4** recommended for the thin hex walls and connector zones.
- Supports: **OFF**.
- XY compensation / horizontal expansion: **0.00** unless a new physical coupon proves a correction is needed.
- Do not change flow only to tune the connector; use the coupon first.

The 2.5 mm hex walls and connector zones derive much of their strength from perimeters rather than infill, so increasing wall count is generally more useful than increasing infill.

## Non-intuitive slicer result: less CAD volume used more filament

R1-HOLE and R2-CHEVRON were sliced under the same EasyPrint conditions. The observed result was:

| Metric | R1-HOLE | R2-CHEVRON |
|---|---:|---:|
| CAD volume | **239.05 cm³** | **228.24 cm³** |
| CAD surface area | **148,681 mm²** | **155,235 mm²** |
| EasyPrint filament | **221 g** | **229 g** |
| Filament length | **74.15 m** | **76.83 m** |
| Print time | **15 h 59 min** | **16 h 13 min** |

R2 removes about **10.80 cm³** more CAD volume, yet the slicer predicts about **8 g more filament** and **14 minutes more print time**.

### Why

FDM material usage is not controlled by CAD volume alone. The chevron creates a much longer internal boundary and more vertical surface area. With multiple perimeters and low infill, those new surfaces are printed as dense perimeter lines, while uncut internal bulk may be represented mostly by low-density infill.

Therefore:

> **Lower CAD volume does not necessarily mean lower filament use or shorter print time.**

This is why R1-HOLE remains the functional efficiency choice, while R2-CHEVRON is retained for its visual/design value.

## Functional difference

- **R1-HOLE:** three Ø8.2 mm through-holes; lower observed filament/time and optional wall-mounting points.
- **R2-CHEVRON:** three symmetric through-chevron openings; lower CAD volume but higher observed sliced filament/time due to added perimeter area.
