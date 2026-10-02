# R1-HOLE Specifications

| Parameter | Final value |
|---|---:|
| Layout | **10 cells, 4-3-2-1** |
| Max XY envelope | **184.624 × 162.389 mm** |
| Print depth / height | **65.0 mm** |
| Internal hex across flats | **33.0 mm** |
| Hex wall | **2.5 mm** |
| Rear wall | **2.5 mm** |
| Corner feature | **3 × Ø8.2 mm through-hole** |
| CAD volume | **239.047 cm³** |
| CAD surface area | **148,681 mm²** |
| Main STL | **watertight** |
| STEP | **single solid validated** |

## Connector

- Male neck/head: **5.2 / 8.2 mm**
- Male depth: **2.5 mm**
- Female mouth/inner: **5.7 / 8.7 mm**
- Female depth: **2.7 mm**
- Side clearance: **0.25 mm per side**
- Depth clearance: **0.20 mm**

## Connector-fix verification

The two upper male rails had been clipped by an earlier Lite perimeter reduction. In this frozen R1 revision they were restored to the original V17T.3 geometry:

- Left upper male depth: **2.500003 mm**
- Right upper male depth: **2.500004 mm**
- Corresponding female depth: **2.700003 mm**

## R1 test coupon

| Parameter | Value |
|---|---:|
| Hex count | **1** |
| Main coupon bbox | **38.00 × 67.044 × 32.50 mm** |
| Height | **32.5 mm** |
| AF | **33.0 mm** |
| Rear wall | **2.5 mm** |
| Corner hole | **Ø8.2 mm through** |
| Side mate | included |
| CAD assembled overlap area | **2.57×10⁻⁵ mm²** (numerical tolerance) |

The coupon is intended to validate the corner geometry and the locked male/female connector before committing to a full print.
