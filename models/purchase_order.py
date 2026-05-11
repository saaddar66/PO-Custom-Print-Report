from odoo import models, api, fields

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    # Stored related field makes binding_domain extremely reliable in the UI
    order_type_name = fields.Char(
        related='order_type.name', 
        store=True, 
        string="Order Type Name"
    )

    def action_print_purchase_order_type(self):
        """
        Redirects to the specific report based on the order_type.
        This method is called from a server action bound to the Print menu.
        """
        self.ensure_one()
        if self.order_type_name == 'Import':
            return self.env.ref('print_po_type.action_report_purchase_order_import').report_action(self)
        elif self.order_type_name == 'Local':
            return self.env.ref('print_po_type.action_report_purchase_order_local').report_action(self)
        
        # Default behavior
        return self.env.ref('purchase.action_report_purchase_order').report_action(self)
