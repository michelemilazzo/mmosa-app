from frappe import _


def get_data():
    return [
        {
            "module_name": "MMOS Aruba",
            "label": _("Setup Panel"),
            "type": "page",
            "link": "mmos-aruba-setup",
            "icon": "octicon octicon-settings",
            "description": "Pannello per rivedere rapidamente le API key e il ruolo predefinito Aruba.",
        }
    ]
