import frappe


def after_install() -> None:
    if frappe.db.exists("MMOS Aruba Account", "placeholder"):
        return

    doc = frappe.get_doc(
        {
            "doctype": "MMOS Aruba Account",
            "account_name": "placeholder",
            "endpoint": "https://api.aruba.it",
            "status": "Draft",
        }
    )
    doc.flags.ignore_mandatory = True
    doc.flags.ignore_permissions = True
    doc.insert()
