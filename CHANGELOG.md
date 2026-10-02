# Changelog

## R2-CHEVRON — frozen final
- Added the design-oriented final alternative.
- Replaced the three R1 Ø8.2 mm through-holes with three through-chevron openings.
- Chevron width: **19.36 mm**.
- Chevron height: **~16.77 mm**.
- Inner V depth: **~5.59 mm**.
- Outer angles: **60°**.
- Inner angles: **30°**.
- Minimum material thickness in the feature area: **~3.0 mm**.
- CAD volume: **~228.24157 cm³**.
- Outer envelope and connector geometry remain the same as R1.

## R1-HOLE — frozen final
- Final functional preferred version.
- 10-cell **4-3-2-1** layout.
- Internal hex AF: **33 mm**.
- Overall Z height/depth: **65 mm**.
- Hex wall: **2.5 mm**.
- Rear wall: **2.5 mm**.
- Three **Ø8.2 mm** through-holes.
- Approx. envelope: **184.624359 × 162.389374 × 65 mm**.
- CAD volume: **~239.0465 cm³**.
- The final connector geometry is the locked V16.8 profile.

## Connector validation
- The V16.8 re-entrant locking connector was physically printed and the test coupon fit was reported as working very well.
- Male: neck **5.20 mm**, head **8.20 mm**, depth **2.50 mm**.
- Female: mouth **5.70 mm**, inner width **8.70 mm**, depth **2.70 mm**.
- Side clearance: **0.25 mm per side**.
- Depth clearance: **0.20 mm**.

## Slicer comparison
Under the same main slicing settings (**5% Gyroid**, **4 perimeters**), R1 used **221 g / 74.15 m / 15:59**, while R2 used **229 g / 76.83 m / 16:13**. This documents the non-intuitive result that lower CAD volume can still require more material and time in FDM when new internal perimeter is introduced.
