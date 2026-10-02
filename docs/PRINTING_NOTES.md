# Printing Notes

The handoff preserves the following main slicing settings used for the R1/R2 comparison:

- Infill: **5% Gyroid**
- Perimeters: **4**
- Same print layout for both variants

No additional printer-specific settings are treated as canonical here unless they are revalidated and documented separately.

## Use the print-plate STL

Where a `*_print_plate.stl` file is provided, use it as the prepared print-layout version.

## Validate the connector with the coupon

The connector geometry is locked. Before changing connector dimensions, print the matching test coupon and verify fit first.

The R1 coupon was physically tested and the connector was reported as working very well.

## Slicer result

| Metric | R1-HOLE | R2-CHEVRON |
|---|---:|---:|
| CAD volume | 239.05 cm³ | 228.24 cm³ |
| Slicer weight | 221 g | 229 g |
| Filament length | 74.15 m | 76.83 m |
| Print time | 15:59 | 16:13 |

R2 has lower CAD volume but higher sliced material and time. The chevron creates more internal perimeter/surface, and with four perimeters these surfaces consume more material than the removed low-density infill would have used.

## STEP files

STEP files in this repository are intended for import into Onshape and are not native local Onshape documents.
