import glob
import pandas as pd
from fpdf import FPDF
from pathlib import Path

filepaths = glob.glob("invoices/*.xlsx")
# print(files)

for filepath in filepaths:
    filename = Path(filepath).stem
    invoice_no = filename.split("-")[0]
    # date =
    # filename = file.split("\\")[1]
    # invoice_value_list = filename.split("-")
    # invoice_no = invoice_value_list[0]
    # date = invoice_value_list[1].strip(".xlsx")

    invoice_no = f"Invoice No: {invoice_no}"
    # date = f"Date: {date}"

    df = pd.read_excel(filepath)
    print(df.columns)

    # Header
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()
    pdf.set_font(family="Times", size=22, style="B")
    pdf.cell(w=0, h=12, txt=invoice_no, ln=1, align="L", border=0)
    # pdf.cell(w=0, h=12, txt=date, ln=1, align="L", border=0)

    # pdf.ln()
    # Table
    # pdf.set_font(family="Times", size=18, style="B")
    # for index, row in df.iterrows()
    # pdf.cell(w=35, h=12, txt="product_id", align="L", border=1)
    # pdf.cell(w=35, h=12, txt="product_id", align="L", border=1)
    pdf.output(f"pdf/{filename}.pdf")


