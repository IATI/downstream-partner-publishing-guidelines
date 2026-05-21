# Project-specific configuration for Sphinx documentation.
# This file contains settings that vary per repository.
# The main conf.py imports these values and can be synced across all repos.

# Project name (used for titles, headers, and Sphinx internals)
project = "IATI Downstream Partner Publishing Guidance"

# Eyebrow text: the smaller text that appears directly above the website title
eyebrow_text = "IATI Guidance: Downstream Partners"

# GitHub repository URL (for "Edit on GitHub" links)
github_repository = "https://github.com/IATI/downstream-partner-publishing-guidance"

# Supported languages for the documentation
languages = ["en", "fr", "es"]

redoc = [
    {
        "name": "Widgets API",
        "page": "api-docs/test-widget-api",
        "spec": "specifications/test-widget-api.yaml",
        "embed": True,
        "template": "_templates/redoc-custom.j2",
    }
]
