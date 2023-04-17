from dateutil.relativedelta import relativedelta

from odoo import models, fields, api


class CustomerInvoicesReport(models.AbstractModel):
    _name = 'report.customer_invoices_report.report_invoices_document'
    _description = 'Customer Invoices Report'

    @api.model
    def _get_report_values(self, docids, data=None):
        docs = self.env['res.partner'].browse(docids)

        print("Partner ID : ", docs.name)
        # print("Partner ID : ", docs.partner_id)

        sale_orders = []
        orders = self.env['account.move'].search([
            ('partner_id', '=', docs.id),
            ('move_type', '=', 'out_invoice'),
            ('state', '!=', 'draft'),
            ('invoice_date', '>=', fields.Date.to_string(fields.date.today() - relativedelta(years=5))),])
        for order in orders:
            sale_orders.append(order)
        print(sale_orders)

        original_list = []
        original_lines = []
        total_amount = 0
        total_residual = 0

        for so in orders:
            if docs.name == so.partner_id.name:
                if so.move_type == 'out_invoice':
                    print("invoice Number : ", so.name)

                    total_amount = total_amount + so.amount_total
                    total_residual = total_residual + so.amount_residual

                    original_lines.append({
                        'name': so.name,
                        'invoice_date': so.invoice_date,
                        'amount_total': so.amount_total,
                        'amount_residual': so.amount_residual,
                    })

        original_list.append(
            {'original_lines': original_lines,
             'total_amount': total_amount,
             'total_residual': total_residual})

        print('Invoice Lines : ', original_lines)
        print('Invoice Wise : ', original_list)
        print('\n')

        return {
            'doc_ids': docs.ids,
            'doc_model': 'res.partner',
            'docs': docs,
            'data': data,
            'proforma': True,
            # 'get_invoices': self._get_invoices,
            # 'get_salesperson': self._get_salesperson,
            # 'Invoice': self.Invoice,

            'original_list': original_list,
        }
    #
    # def _get_invoices(self, docs):
    #     Invoice = self.env['account.move']
    #     domain = [
    #         ('partner_id', '=', docs.id),
    #         ('move_type', '=', 'out_invoice'),
    #         ('state', '!=', 'draft'),
    #         ('invoice_date', '>=', fields.Date.to_string(fields.date.today() - relativedelta(years=5))),
    #     ]
    #     return Invoice.docs(domain)
    #
    # def _get_salesperson(self, docs):
    #     return docs.user_id.name or ''
