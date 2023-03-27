# Customer Invoices Report

This Odoo module generates a PDF report of customer invoices for the last 5 years, grouped by customers. Each customer's invoices are displayed on a separate page.

## Features

- Generate a PDF report of customer invoices in the last 5 years
- Group invoices by customers, with one page per customer
- Display a table with columns: invoice number, date of invoice, amount_paid, and amount_pending
- Print the name, address, and phone number of the customer contact person in the header of the PDF
- Print the name of the salesperson in the footer of the PDF
- Include a cover page with the text "Ashant Chalasani, assisted by AI"

## Installation

To install this module, copy the `customer_invoices_report` folder to the `addons` directory of your Odoo installation.

Then, go to the "Apps" menu in the Odoo web interface, click "Update Apps List", and search for "Customer Invoices Report". Click "Install" to install the module.

## Usage

After installing the module, go to the "Contacts" menu and select a customer. Click the "Print" button and choose "Customer Invoices Report" to generate the PDF report.

## License

This module is available under the [GNU Affero General Public License v3 (AGPL-3)](https://www.gnu.org/licenses/agpl-3.0.en.html).

## Support

If you need help or have any questions, please feel free to contact Ashant Chalasani at <your_email@example.com>.
