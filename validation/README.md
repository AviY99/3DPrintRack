# Validation Index

This directory is the repository-level index for machine-readable validation results produced for the frozen final geometry.

## Full models

- [R1-HOLE model validation](../R1-HOLE/validation/model.json)
- [R2-CHEVRON model validation](../R2-CHEVRON/validation/model.json)

The full-model JSON files record final mesh bounds, extents, volume, surface area and the locked connector dimensions.

## Test coupons

- [R1-HOLE coupon validation](../R1-HOLE/TEST-COUPON/validation/coupon.json)
- [R2-CHEVRON coupon validation](../R2-CHEVRON/TEST-COUPON/validation/coupon.json)

## Package archives in this repository

- [R1-HOLE package](../R1-HOLE/packages/rack_V17T3_LITE_FINAL_R1_connectorfix_package.zip)
- [R1-HOLE test coupon package](../R1-HOLE/TEST-COUPON/packages/rack_V17T3_LITE_FINAL_R1_TEST_singlehex_topcorner_connectorfix_package.zip)
- [R2-CHEVRON package](../R2-CHEVRON/packages/rack_V17T3_LITE_FINAL_R2_CHEVRON_package.zip)
- [R2-CHEVRON test coupon package](../R2-CHEVRON/TEST-COUPON/packages/rack_V17T3_LITE_FINAL_R2_TEST_CHEVRON_package.zip)

These repository ZIPs are generated from the frozen, validated assets stored in the repository. They preserve the documented package filenames and member naming, but are not asserted to be byte-for-byte identical to the historical package archives.

## Historical archive reference

The four historical ZIP files supplied during repository population were verified as valid ZIP archives. Their SHA-256 values are retained here for provenance:

| Archive | SHA-256 |
|---|---|
| `rack_V17T3_LITE_FINAL_R1_connectorfix_package.zip` | `b032326ef86aa789afb21b8df8f5476eed476a0ee9e3fe52ca0b11ef6d1a2eb4` |
| `rack_V17T3_LITE_FINAL_R1_TEST_singlehex_topcorner_connectorfix_package.zip` | `99f6c446665f79bb16487177eb226161998aea3cec66028ef4fe332fff118687` |
| `rack_V17T3_LITE_FINAL_R2_CHEVRON_package.zip` | `a80f60089babc0ae24bfa47f65add6afc3a558c936ee392899791adbe9cd5a7a` |
| `rack_V17T3_LITE_FINAL_R2_TEST_CHEVRON_package.zip` | `98159edadf851f103cafbcf0f100e217479fe3525bb8d5d525ed2b963f5ddaa5` |

## Visual checks

Coupon section and assembled-check images are available in each variant's `TEST-COUPON/previews/` and `TEST-COUPON/drawings/` folders.
