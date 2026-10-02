# Connector Specification — V16.8 Locked Profile

This connector geometry is shared by **R1-HOLE**, **R2-CHEVRON**, and their test coupons.

| Parameter | Male | Female |
|---|---:|---:|
| Neck / mouth width | **5.20 mm** | **5.70 mm** |
| Head / inner width | **8.20 mm** | **8.70 mm** |
| Depth | **2.50 mm** | **2.70 mm** |
| Nominal lateral clearance | **0.25 mm per side** | **0.25 mm per side** |
| Nominal depth clearance | **0.20 mm** | **0.20 mm** |

## Clearance derivation

- 8.70 − 8.20 = **0.50 mm total**, i.e. **0.25 mm per side**.
- 5.70 − 5.20 = **0.50 mm total**, i.e. **0.25 mm per side**.
- 2.70 − 2.50 = **0.20 mm depth clearance**.

## Geometry status

- Connector concept: **V16.8 locking / re-entrant sliding connector**.
- Connector cross-section: **LOCKED**.
- Full-part connector length along Z: **65 mm**.
- Test-coupon connector length along Z: **32.5 mm**.
- The cross-section is identical in the full model and coupons.

## Validation history

The connector profile was physically printed and tested successfully before the final Lite revisions, including successful fit with Prusament/Prusa PLA and eSUN PLA. The final R1/R2 models retain this same locked cross-section.

A later Lite perimeter-trimming operation accidentally clipped the two upper male rails on the sloped sides. In R1 this was corrected by restoring the original V17T.3 material locally around those connector zones. Post-fix male depth is **2.500 mm** on both upper connectors, and R2 preserves the corrected R1 connector geometry unchanged.

## Change rule

Do **not** alter connector dimensions to compensate for a printer, filament, layer height, or slicer change without first printing the matching test coupon. Dimensional compensation should be a last resort because the current connector profile is production-proven.
