import glob
import pandas as pd
from fpdf import FPDF
from pathlib import Path

filepaths = glob.glob("invoices/*.xlsx")
# print(files)

for filepath in filepaths:

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
    pdf.ln()

    df = pd.read_excel(filepath)

    # Table
    columns = df.columns
    pdf.set_font(family="Times", size=10, style="B")
    pdf.set_text_color(80, 80, 80)
    pdf.cell(w=30, h=8, txt=columns[0], align="L", border=1)
    pdf.cell(w=70, h=8, txt=columns[1], align="L", border=1)
    pdf.cell(w=35, h=8, txt=columns[2], align="L", border=1)
    pdf.cell(w=25, h=8, txt=columns[3], align="L", border=1)
    pdf.cell(w=30, h=8, txt=columns[4], align="L", border=1, ln=1)

    for index, row in df.iterrows():
        pdf.set_font(family="Times", size=10)
        pdf.set_text_color(80, 80, 80)
        pdf.cell(w=30, h=8, txt=str(row["product_id"]), align="L", border=1)
        pdf.cell(w=70, h=8, txt=str(row["product_name"]), align="L", border=1)
        pdf.cell(w=35, h=8, txt=str(row["amount_purchased"]), align="R", border=1)
        pdf.cell(w=25, h=8, txt=str(row["price_per_unit"]), align="R", border=1)
        pdf.cell(w=30, h=8, txt=str(row["total_price"]), align="R", border=1, ln=1)

    total_price = sum(df["total_price"])
    pdf.set_font(family="Times", size=10)
    pdf.set_text_color(80, 80, 80)
    pdf.cell(w=30, h=8, txt="", align="L", border=1)
    pdf.cell(w=70, h=8, txt="", align="L", border=1)
    pdf.cell(w=35, h=8, txt="", align="R", border=1)
    pdf.cell(w=25, h=8, txt="", align="R", border=1)
    pdf.cell(w=30, h=8, txt=str(total_price), align="R", border=1, ln=1)

    pdf.ln()

    pdf.set_font(family="Times", style="B", size=14)
    # pdf.set_text_color(80, 80, 80)
    pdf.cell(w=0, h=8, txt=f"The total due amount is {total_price} euros",
             ln=1, align="L")
    pdf.cell(w=0, h=8, txt=f"PythonHow",
             ln=1, align="L")

    pdf.output(f"pdf/{filename}.pdf")


