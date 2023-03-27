from odoo import models, fields, api

class CustomerInvoicesReport(models.AbstractModel):
    _name = 'report.customer_invoices_report.report_invoices'
    _description = 'Customer Invoices Report'

    @api.model
    def _get_report_values(self, docids, data=None):
        customers = self.env['res.partner'].browse(docids)
        return {
            'doc_ids': docids,
            'doc_model': 'res.partner',
            'docs': customers,
            'data': data,
            'get_invoices': self._get_invoices,
            'get_salesperson': self._get_salesperson,
        }

    def _get_invoices(self, customer):
        Invoice = self.env['account.move']
        domain = [
            ('partner_id', '=', customer.id),
            ('move_type', '=', 'out_invoice'),
            ('state', '!=', 'draft'),
            ('invoice_date', '>=', fields.Date.to_string(fields.date.today() - relativedelta(years=5))),
        ]
        return Invoice.search(domain)

    def _get_salesperson(self, customer):
        return customer.user_id.name or ''
