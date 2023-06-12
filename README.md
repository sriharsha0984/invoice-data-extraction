# Invoice Data Extraction

This project aims to extract structured data from invoices using Python and the `invoice2data` library. It utilizes PyPDF2 for reading PDF files and invoice templates provided by the `invoice2data` library.

## Requirements

- Python 3.x
- PyPDF2
- invoice2data

## Installation

1. Clone the repository:

git clone https://github.com/sriharsha0984/invoice-data-extraction.git

2. Install the required packages:

pip install -r requirements.txt



## Usage

1. Place the PDF invoices that you want to extract data from in the `pdfs/` directory.

2. Create invoice templates in the `templates/` directory. You can refer to the documentation of the `invoice2data` library for more details on creating templates.

3. Update the `pdf_path` variable in the script (`extract_invoice_data.py`) with the correct path to the PDF files.

4. Run the script to extract data from the invoices and generate a CSV file:
python extract_invoice_data.py


5. The extracted data will be saved in the `output.csv` file.

## Error Handling

If there are any errors during the extraction process, they will be logged in the `error_logs.txt` file. You can refer to this file to identify any issues encountered during the extraction.

## Contributing

Contributions are welcome! If you have any suggestions, improvements, or bug fixes, please feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

