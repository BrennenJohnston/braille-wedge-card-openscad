# Project Facts — braille-wedge-card-openscad (always active)

Directly readable braille cards printed leaning at 75° (wedge support).
Working branch: main.

1. Main model: Braille_Wedge_Card_STL_Generator.scad.
2. Named checks: powershell -ExecutionPolicy Bypass -File scripts\scad-check.ps1
   (after every .scad edit) and python -m pytest tests/ -v (before commits).
   CI renders with OpenSCAD 2026.01.03 — same as the local canonical binary.
3. Canonical braille constants (do not change without my approval): dot
   spacing 2.5 / cell 6.5 / line 10.0 mm; dot map [[0,0],[1,0],[2,0],[0,1],
   [1,1],[2,1]] = dots 1–6. Full geometry specs live in
   braille-cylinder-stl-generator\docs\specifications\.
4. The 75° print angle is load-bearing for dot quality: geometry changes must
   preserve printability at that angle (overhangs, dot dome orientation) —
   flag anything that would change the print orientation.
