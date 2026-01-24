import frappe
from frappe.utils import data


@frappe.whitelist()
def get_nodes_summary() -> dict[str, int]:
    nodes = frappe.get_all(
        "MMOS Aruba Node",
        fields=["name", "state"],
    )
    summary = {"total": len(nodes)}
    states = frappe._dict()
    for node in nodes:
        states.setdefault(node.state or "unknown", 0)
        states[node.state or "unknown"] += 1
    summary["states"] = states
    return summary


@frappe.whitelist()
def update_node_status(node: str, state: str) -> None:
    if not frappe.db.exists("MMOS Aruba Node", node):
        frappe.throw(f"Nodo Aruba '{node}' non trovato")
    frappe.db.set_value("MMOS Aruba Node", node, "state", state)


@frappe.whitelist()
def trigger_sync() -> dict[str, str]:
    doc = frappe.get_single("MMOS Aruba Setup")
    doc.last_sync = data.now_datetime()
    doc.save(ignore_permissions=True)
    frappe.msgprint("Sync trigger registrato.")
    return {"last_sync": doc.last_sync}
