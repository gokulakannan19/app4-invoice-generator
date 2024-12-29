import glob
import pandas as pd
from fpdf import FPDF
from pathlib import Path

filepaths = glob.glob("invoices/*.xlsx")
# print(files)

for filepath in filepaths:
    df = pd.read_excel(filepath)

    filename = Path(filepath).stem
    invoice_no = filename.split("-")[0]
    date = filename.split("-")[1]

    invoice_no = f"Invoice No: {invoice_no}"
    date = f"Date: {date}"

    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()

    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=0, h=8, txt=invoice_no, ln=1, align="L", border=0)
    pdf.cell(w=0, h=8, txt=date, ln=1, align="L", border=0)

    # pdf.ln()
    # Table
    # pdf.set_font(family="Times", size=18, style="B")
    # for index, row in df.iterrows()
    # pdf.cell(w=35, h=12, txt="product_id", align="L", border=1)
    # pdf.cell(w=35, h=12, txt="product_id", align="L", border=1)
    pdf.output(f"pdf/{filename}.pdf")


