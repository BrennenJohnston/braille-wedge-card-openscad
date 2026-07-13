# Changelog

All notable changes to this project are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).
Versions below refer to the card generator unless a file is named explicitly.

## [1.1.0] - 2026-07-12

Expands the repo from one generator into three separate, self-contained,
MakerWorld-ready generators: the wedge card plus new sign and charm tools.

### Added

- **Multi-card layout** (card 1.1.0). New `[Multi-Card Layout]` tab:
  `card_layout` (`Single` / `All cards`), `rows_per_card` (default 8), and
  `card_gap_mm` (default 5). In All-cards mode long text is chunked into
  groups of `rows_per_card` lines and every card prints in one file, laid out
  front to back along −Y, each fused with its own support fins. Console
  reports the card count and total bed depth (warning above 250 mm).
- **`Braille_Sign_STL_Generator.scad` 1.0.0** — two-part ADA-style tactile
  sign: raised-letter plate (Liberation Sans, uppercase, 16 mm, 0.8 mm raise)
  plus braille plate (flat or 75° angled with break-away fins), split raised
  border, auto-fit sizing, and `sign_part` = Both / Letter plate / Braille
  plate. Ships with `Braille_Sign_STL_Generator.json` presets.
- **`Braille_Charm_STL_Generator.scad` 1.0.0** — braille charm/pendant
  generator: pendant shapes (circle, square, rounded rect, hexagon, oval)
  with border and keychain hole / bail loop, angled single-fin or flat
  printing, plus a bracelet C-clip shape that prints standing vertically with
  the braille rotated 90° to read along the band. Adapted from Nasif's Charm
  Maker and the Bracelet Clip Charm (both CC0). Ships with
  `Braille_Charm_STL_Generator.json` presets (Large/Small Bracelet Clip,
  Circle Pendant).
- **New card presets**: Manual 200 × 100 Card and All Cards (16 lines,
  2 cards); existing presets updated for the new parameters.
- **Test suite covers all three generators**: Customizer/preset tests are
  parametrized across the three files, a new MakerWorld source guard rejects
  `include`/`use` in any generator, and render smoke tests cover the two-card
  layout (2 bodies + bed-depth bbox), the two-plate sign and angled braille
  plate, and the bracelet clip and angled pendant charm. CI validates all
  three preset JSON files.

### Changed

- **Card first-run defaults** now match the latest print-tested configuration:
  auto-sizing on by default (`auto_size_card` = On; the manual 200 × 100 mm
  face is used when Off), grid capacity 26 × 8 (column slider max 40),
  `show_warnings` = Off (console warnings always print; the red 3D preview text
  is opt-in under `[Warnings]`), and `render_quality` = Medium for faster
  previews.

### Fixed

- **Charm border exported non-watertight STLs** (fixed vs. the adapted
  Charm Maker source).
  The raised border was extruded as a separate ring stacked on the charm
  body, leaving two coincident outer walls; on curved outlines (circle, oval,
  rounded rect, hexagon) the differing tessellations exported as T-junction
  open edges. The body and border are now carved from one extrusion, so every
  pendant shape exports watertight.

## [1.0.0] - 2026-07-05

First public release, split out of
[braille-stl-generator-openscad](https://github.com/BrennenJohnston/braille-stl-generator-openscad)
(where it incubated as `experimental/braille-business-card/`).

### Added

- **20 text rows.** `Line_1`…`Line_20`, with `_all_lines` as the single source
  of truth for every loop, warning, and layout module, and a documented recipe
  for extending past 20. `grid_rows` slider now reaches 20; manual face size up
  to 300 × 250 mm.
- **Print-bed size warning.** The console warns when the effective card face
  exceeds 250 mm in either direction.
- **Curated Customizer presets** (`Default Card`,
  `Compact Card (manual 75x25)`, `Large 20-Line Card`) with generic sample
  braille. Personal preset files matching `*.local.json` are gitignored.
- **Test suite + CI.** Customizer dropdown hygiene tests, source-invariant
  guards (including a mission guard that keeps embossing-era concepts out),
  and OpenSCAD render smoke tests asserting watertight single-body STLs with
  expected bounding boxes. GitHub Actions workflow runs lint + quick tests +
  render smoke on Ubuntu.
- Project docs: README (quick start, print guidance, troubleshooting,
  MakerWorld upload steps), research notes under `docs/`, PolyForm
  Noncommercial LICENSE.

### Changed

- **First-run defaults are the print-tested "Try 4" configuration** (with
  warnings kept On): fins every 25 mm (1.0 mm offset, 1.2 mm thick), six
  0.5 × 0.5 mm bridges per fin at 0.3 mm contact, 2 mm brim, 1.5 mm card,
  7.0 mm cell spacing, 11 × 5 grid, Rounded dot 1.6/0.35 + 1.4/0.35
  (0.7 mm total height — inside the ADA envelope), render quality High.

### Removed (vs. the experimental prototype)

- **All embossing-era concepts.** This is now a pure directly-readable card:
  `plate_type` / Counter Plate path, counter recess modules and parameters,
  row start/end indicators, the `_preset_*` routing shims, and the parent
  repo's test-system compatibility parameters are gone. `braille_card()` is a
  plain union of card body, dots, and preview-only warnings.

### Fixed

- **Floating-shell STL exports.** Dots seated exactly on the face plane (and
  the rounded dot's dome seated exactly on its base) could export as separate
  disconnected shells. Dots now embed 0.02 mm into the face and the dome
  overlaps its base, so every export fuses into one watertight solid.
- **Bridges above short fins.** With a small `fin_height_frac` the bridge
  ladder could start above the fin top, leaving floating prongs; the bridge
  span is now clamped to the fin.
- **Brim/card tangency.** The fin brim stopped exactly at the card's
  bottom-back corner, exporting a non-manifold self-touching boundary; the
  brim now stops just short of the card.
