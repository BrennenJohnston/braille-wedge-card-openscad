# MakerWorld Listing — Braille Wedge Card STL Generator

Status: draft — ready to upload once the license pick is recorded and the gallery
photos are shot.

Written to the shared
[Accessible MakerWorld Documentation Standard](https://github.com/BrennenJohnston/accessible-makerworld-doc-standard/blob/main/ACCESSIBLE_MAKERWORLD_DOC_STANDARD.md).

---

## Upload fields

| Field | Value |
|-------|-------|
| Model title | `Braille Wedge Card Generator - Readable 3D-Printed Braille Cards (Parametric)` |
| Designer | Brennen Johnston |
| Category | Education > Other Education Models |
| License | a CC NonCommercial variant — see below |
| Upload file | `Braille_Wedge_Card_STL_Generator.scad` — this one file only |
| Tags | `braille`, `accessibility`, `assistive-technology`, `blindness`, `vision-impairment`, `tactile`, `business-card`, `educational`, `customizable`, `parametric`, `openscad`, `support-free`, `no-supports` |
| External link 1 | <https://openscad-assistive-forge.pages.dev/?example=braille-wedge-card> |
| External link 2 | <https://github.com/BrennenJohnston/braille-wedge-card-openscad> |

The repository is licensed PolyForm Noncommercial 1.0.0 and MakerWorld does not
offer PolyForm in its license list, so the pick has to be the closest Creative
Commons NonCommercial variant. Make that choice deliberately at upload time
rather than accepting the form's default — the licensing gate later in this
document sets out what is at stake. The first external link is the accessible
browser version of the same generator; the second is the source repository.

## Summary

A parametric generator for braille cards you can read straight off the printer —
no embosser, no paper, no post-processing beyond snapping off the built-in
supports. Paste pre-translated Unicode braille into the customizer and the card
sizes itself to fit, prints leaning back at 75° on its own break-away fins, and
comes out as one fused piece. The 75° lean is the angle a CHI 2024 study found
significantly faster and more comfortable to read than flat-printed braille.

## Description

*Paste into MakerWorld's description body.*

**What this makes**

A flat card with raised braille dots on a face that leans back 75° from the print
bed. The dots are readable directly off the printer. Behind the card, a row of
thin triangular support fins is fused to it by tiny snap-off bridges, with a
brim modelled underneath to anchor them to the bed — so the whole thing prints
with no slicer supports and exports as a single object. After printing you flex
the fins off and the card is done.

Use it for braille contact cards, labels, classroom material, door and shelf
labels, or any short tactile message.

**Why it leans back instead of lying flat**

Braille printed on a face angled 75–90° from the print bed reads significantly
faster and more comfortably than flat-printed braille, because near-vertical
printing moves the layer seams off the surface your finger reads. That result is
from Puerta, Crnovrsanin, South and Dunne, "The Effect of Orientation on the
Readability and Comfort of 3D-Printed Braille," CHI 2024
(https://doi.org/10.1145/3613904.3642719). This model targets 75° rather than 90°
because tilting the face back 15° turns the overhang under each dot into a gentle
cone that prints cleanly without support. Every other piece of the geometry — the
fins, the bridges, the brim — exists to make that angle printable in one pass.

**What you need to supply**

Pre-translated Unicode braille. MakerWorld's customizer cannot translate English
for you, so translate your text first at https://www.branah.com/braille-translator
and make sure the output is set to **Unicode braille** (dot patterns like
⠓⠑⠇⠇⠕) rather than ASCII/BRF braille (which looks like ordinary letters). Choose
Grade 1 for uncontracted braille — clearest for names and contact details — or
Grade 2 for contracted braille, which fits more in the same space.

If you would rather not translate by hand, the accessible browser version linked
above does it for you on your own device.

**Using the customizer**

1. Paste one line of Unicode braille into each of `Line_1` through `Line_8` under
   **Text Input - Pre-Translated Braille**. Lines 9 through 20 are under **More
   Braille Lines (Advanced)**.
2. Leave `auto_size_card` on `On`. The card then sizes itself to your text plus
   `auto_size_margin_mm` (6 mm) on each side, and it becomes impossible to
   overflow the grid.
3. Set `show_warnings` to `On` under **Warnings** before rendering. MakerWorld
   shows no OpenSCAD console, so this is how you see input problems — as red 3D
   text above the card in the preview. It is preview-only and is never exported.
4. If your text needs more than one card, set `card_layout` to `All cards` under
   **Multi-Card Layout**. The lines split into groups of `rows_per_card` (8) and
   every card lays out front to back on the bed, so the set prints in one job.
5. Generate, render, download the STL.

Everything else has a working default. The card face, dot geometry, fin spacing,
and bridge sizes are all adjustable if you want them.

**Print settings**

- Print it exactly as modeled. Do not rotate it. Do not add slicer supports.
- Layer height 0.1 mm. Braille standards cap dot height at 0.9 mm, so layer
  height is essentially the only lever on how smooth a dot feels.
- PLA or PETG. Both tested.
- No supports needed; a slicer brim is optional because one is already modelled
  under each fin.
- Slow the outer wall to 30–40 mm/s and keep acceleration modest. A thin leaning
  card is sensitive to ringing; input shaping helps a lot.
- After printing: flex or snip the fins off the back, then deburr the small nubs
  the bridges leave with a fingernail or fine sandpaper.
- Do not add lightening holes to the fins — the extra head motion costs a thin
  leaning part more than the saved filament is worth.

If the fins fall over or the bridges break mid-print, raise
`bridge_contact_mm` toward 0.4 mm or add more `bridge_count`. If the fins will
not snap off cleanly, lower `bridge_contact_mm` toward 0.2 mm.

**Dimensions**

Default `Rounded` dot: 1.6 mm base, 0.7 mm total height (0.35 mm tapered base
plus a 0.35 mm dome on a 1.4 mm diameter). That sits inside both the 2010 ADA
Standards §703.3 envelope and ISO 17049 — base 1.5–1.6 mm, height 0.6–0.7 mm
where the two overlap. Spacing follows BANA *Size and Spacing of Braille
Characters*: 7.0 mm between cells, 10.0 mm between lines, 2.5 mm between dots
inside a cell. A 20-line card at that spacing is about 209 mm tall.

These are dimensional targets, not a compliance claim. Automatic translation is
not the same as a certified transcription — for anything public, medical, or
legal, have a UEB-certified transcriber check the braille.

**An accessible alternative**

This generator also runs as a built-in tool in **OpenSCAD Assistive Forge**, an
accessibility-first browser customizer:
https://openscad-assistive-forge.pages.dev/?example=braille-wedge-card

It translates plain English to braille on your device with liblouis (UEB Grade 1
by default, Grade 2 available), is built for screen readers and keyboard
navigation, saves presets, works offline once installed, and names your
downloads after their content. Use it if the customizer here is difficult with
your screen reader. Nothing leaves your device in either tool.

**Credits**

- Design and code: Brennen Johnston.
- Orientation research: Puerta, Crnovrsanin, South, Dunne (CHI 2024).
- Break-away support fin technique: masukomi, "Manual Support Fins for 3D
  Printing," and Slant3D, "Stop Using Slicer Supports."
- Dot geometry adapted from the Braille Cylinder STL Generator, the parent
  project this was split from.

Two sibling generators use the same angled-printing technique: a two-part
ADA-style tactile sign generator and a braille charm, pendant and bracelet-clip
generator.

## Print profile notes

There is no `.3mf` to attach — this is a parametric model, and the geometry
depends on the user's text. State the settings as text in the description
instead, which is what the table above does.

If a print profile is added later, it must be for a specific fixed example card
(the default "hello world" card is the obvious candidate) and it needs its own
photograph of the actual printed result.

| Setting | Value |
|---------|-------|
| Layer height | 0.1 mm |
| Material | PLA Basic or PETG |
| Supports | none |
| Brim | optional (one is modelled) |
| Orientation | as modeled, no rotation |
| Outer wall speed | 30–40 mm/s |
| Infill | not critical; the card is nearly all perimeter |

## Gallery plan

1. **Cover — a printed card being read.** A finger resting on the raised dots of
   a finished card, fins already removed, card standing on its base.
   **Alt text:** A printed braille card standing at a backward lean on a desk,
   with a hand reading the raised dots on its angled front face.

2. **The card on the bed, fins still attached.** Side view showing the lean and
   the row of triangular fins behind it.
   **Alt text:** Side view of the card as it comes off the printer, leaning back
   about 75 degrees, with five thin triangular support fins standing behind it
   and connected by small bridges.

3. **Fins being snapped off.** Mid-removal, showing how little force it takes.
   **Alt text:** A hand flexing the support fins away from the back of a printed
   braille card; the fins have separated at the small bridge points.

4. **Dot close-up.** Macro of three or four dots, ideally lit to show the layer
   direction running across rather than up the dot.
   **Alt text:** Close-up of raised braille dots printed on the angled card face,
   each dot a smooth dome about 1.6 millimetres wide and 0.7 millimetres tall.

5. **Multi-card layout, printed.** Several cards printed in one job from
   `card_layout = All cards`.
   **Alt text:** Three braille cards printed in a single job, arranged one behind
   another on the print bed, each carrying eight lines of braille.

6. **Scale reference.** A card next to a standard business card or a ruler.
   **Alt text:** A printed braille card beside a ruler, showing a face about 100
   millimetres wide.

The cover must be a photograph of the actual printed object, not a render.
MakerWorld requires at least one real print photo per model and per print
profile.

## Pre-publish checklist

- [ ] **License pick recorded.** The repo is PolyForm Noncommercial 1.0.0, which
      MakerWorld does not offer. Choose the closest CC NonCommercial variant
      deliberately and note the choice here, because the MakerWorld pick governs
      the listing.
- [ ] **Single-file requirement verified.** Run `pytest tests -v` — the
      `test_source_guards.py` MakerWorld guard asserts there is no
      `include`/`use` in the `.scad`.
- [ ] **Customizer dropdown hygiene verified.** Same test run:
      `test_customizer.py` checks for `value:Label` option syntax, defaults that
      are not in their own option list, and duplicate options.
- [ ] **Creator Portal smoke test.** Upload, confirm the panel builds, render the
      defaults, download the STL, and confirm `show_warnings` = `On` produces
      visible red text on a deliberately bad input.
- [ ] **Every gallery image has alt text pasted into MakerWorld's field.**
- [ ] **Cover photo is a real printed object.**
- [ ] **Quick start linked from the description** — either the GitHub link to
      [`MAKERWORLD_QUICK_START.md`](MAKERWORLD_QUICK_START.md) or its content
      pasted into the instructions area.
