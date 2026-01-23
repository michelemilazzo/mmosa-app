import frappe


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
