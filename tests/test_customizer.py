"""
OpenSCAD Customizer Validation Tests

Verifies that the Customizer dropdown definitions in all three braille
generators (wedge card, sign, charm) are correct and won't cause duplicate
option issues in the UI.

The `value:Label` format can cause duplicate dropdown entries in some OpenSCAD
versions. The recommended format is:
  param = "DefaultLabel"; // [Label1, Label2, Label3]

where the default value exactly matches one of the dropdown options.

License: PolyForm Noncommercial 1.0.0
"""

import json
import re

import pytest

from conftest import ALL_SCAD_FILES

SCAD_IDS = [f.stem for f in ALL_SCAD_FILES]


@pytest.fixture(params=ALL_SCAD_FILES, ids=SCAD_IDS)
def scad_file(request):
    return request.param


@pytest.fixture
def scad_content(scad_file):
    return scad_file.read_text(encoding="utf-8")


class TestCustomizerDropdowns:
    """Customizer dropdown definition hygiene (all generators)."""

    def test_scad_file_exists(self, scad_file):
        assert scad_file.exists(), f"OpenSCAD file not found: {scad_file}"

    def test_no_value_colon_label_format(self, scad_content):
        """
        Dropdowns must not use the problematic 'value:Label' format.

        Note: this does NOT apply to range sliders, which use `// [min:step:max]`.
        """
        dropdown_lines_with_colon = []
        for line in scad_content.split("\n"):
            if "=" not in line or line.strip().startswith("//"):
                continue

            bracket_match = re.search(r"//\s*\[([^\]]+)\]", line)
            if not bracket_match:
                continue

            bracket_content = bracket_match.group(1)

            # Skip range sliders: only numbers, colons, periods (e.g. "1:1:20")
            if re.match(r"^-?[\d.]+:-?[\d.]+:-?[\d.]+$", bracket_content.strip()):
                continue

            if re.search(r"[a-zA-Z]\w*:[A-Z]", bracket_content):
                dropdown_lines_with_colon.append(line.strip())

        if dropdown_lines_with_colon:
            pytest.fail(
                "Found dropdown definitions using problematic 'value:Label' format.\n"
                "This format can cause duplicate entries in OpenSCAD Customizer.\n"
                "Problematic lines:\n"
                + "\n".join(f"  - {line}" for line in dropdown_lines_with_colon)
                + '\n\nRecommended format: param = "DefaultLabel"; // [Label1, Label2]'
            )

    def test_dropdown_default_matches_option(self, scad_content):
        """
        Dropdown default values must match one of the options exactly.

        If the default doesn't match an option, OpenSCAD may show both the
        default and the closest option as separate entries.
        """
        dropdown_pattern = r'(\w+)\s*=\s*"([^"]+)"\s*;\s*//\s*\[([^\]]+)\]'

        mismatches = []
        for match in re.finditer(dropdown_pattern, scad_content):
            var_name = match.group(1)
            default_value = match.group(2)
            options = [opt.strip() for opt in match.group(3).split(",")]

            if default_value not in options:
                mismatches.append(
                    {"variable": var_name, "default": default_value, "options": options}
                )

        if mismatches:
            msg = "Dropdown default values don't match any option:\n"
            for m in mismatches:
                msg += f"  - {m['variable']}: default '{m['default']}' not in {m['options']}\n"
            msg += "\nThis can cause duplicate entries in OpenSCAD Customizer."
            pytest.fail(msg)

    def test_no_duplicate_dropdown_options(self, scad_content):
        """Dropdown options must not contain duplicates."""
        dropdown_pattern = r'(\w+)\s*=\s*"[^"]+"\s*;\s*//\s*\[([^\]]+)\]'

        duplicates = []
        for match in re.finditer(dropdown_pattern, scad_content):
            var_name = match.group(1)
            options = [opt.strip() for opt in match.group(2).split(",")]
            seen = set()
            for opt in options:
                if opt in seen:
                    duplicates.append({"variable": var_name, "duplicate": opt})
                seen.add(opt)

        if duplicates:
            msg = "Dropdown definitions contain duplicate options:\n"
            for d in duplicates:
                msg += f"  - {d['variable']}: duplicate option '{d['duplicate']}'\n"
            pytest.fail(msg)


class TestPresetsFile:
    """The shipped Customizer presets must stay consistent with each .scad."""

    @pytest.fixture
    def presets(self, scad_file):
        presets_file = scad_file.with_suffix(".json")
        assert presets_file.exists(), f"Presets file not found: {presets_file}"
        return json.loads(presets_file.read_text(encoding="utf-8"))

    @pytest.fixture
    def scad_params(self, scad_content):
        """All top-level Customizer parameter names declared in the .scad."""
        # Cut at the calculated-values marker: only declarations above it are
        # Customizer parameters.
        marker = "CALCULATED VALUES"
        content = scad_content.split(marker)[0]
        names = set()
        for match in re.finditer(
            r"^(\w+)\s*=\s*[^=]", content, flags=re.MULTILINE
        ):
            names.add(match.group(1))
        return names

    def test_presets_use_only_existing_parameters(self, presets, scad_params):
        """Every key in every preset must be a real Customizer parameter."""
        unknown = {}
        for set_name, params in presets["parameterSets"].items():
            bad = [k for k in params if k not in scad_params]
            if bad:
                unknown[set_name] = bad

        if unknown:
            pytest.fail(
                "Presets reference parameters that don't exist in the .scad "
                f"(stale names from a refactor?): {unknown}"
            )

    def test_presets_contain_no_personal_text(self, presets):
        """
        Shipped preset text must be generic sample braille only.

        Guards against personal contact details (the '@' sign, '.com'-style
        sequences) sneaking back into the shipped presets. The braille cell
        for the at-sign prefix in UEB email addresses is ⠈ (U+2808) followed
        by ⠁; full personal data scrubbing is a review step, but this catches
        the known patterns.
        """
        email_marker = "\u2808\u2801"  # ⠈⠁ = UEB "@a..." as in name@...
        for set_name, params in presets["parameterSets"].items():
            for key, value in params.items():
                if key.startswith("Line_") and email_marker in value:
                    pytest.fail(
                        f"Preset '{set_name}' {key} looks like it contains an "
                        "email address in braille. Shipped presets must use "
                        "generic sample text only (keep personal sets in a "
                        "*.local.json file)."
                    )


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
