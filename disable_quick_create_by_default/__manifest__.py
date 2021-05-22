# Copyright 2020 Pharmasimple (https://www.pharmasimple.be)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Disable quick create by default",
    "category": "Tools",
    "summary": """
    Based on base_optional_quick_create,
    this module add a default value on avoid_quick_create
    to disable all quick create by default""",
    "version": "14.0.1.0.0",
    "author": "Pharmasimple",
    "license": "AGPL-3",
    "website": "https://github.com/akretion/phs-addons",
    "post_init_hook": "post_init_hook",
    "depends": [
        "base_optional_quick_create",
    ],
    "data": [],
    "installable": True,
    "application": False,
}
