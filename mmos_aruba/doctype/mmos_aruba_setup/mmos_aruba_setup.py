import frappe
from frappe.model.document import Document


class MMOSArubaSetup(Document):
    def validate(self) -> None:
        if self.sync_cron:
            frappe.utils.data.validate_cron(self.sync_cron)
