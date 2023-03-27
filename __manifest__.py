{
    'name': 'Customer Invoices Report',
    'version': '1.0',
    'category': 'Accounting/Accounting',
    'summary': 'Generate a PDF report of customer invoices',
    'author': 'Ashant Chalasani, assisted by AI',
    'depends': ['account'],
    'data': [
        'views/customer_invoices_report.xml',
        'reports/customer_invoices_report_template.xml',
    ],
    'application': False,
}
