import pandas as pd
import os
from fpdf import FPDF
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

# -------------------- Step 1: Load and Process Excel --------------------
# Load the Excel file
df = pd.read_excel("employees.xlsx.xlsx")

# Clean numeric columns (remove commas and convert to float)
df['BASIC SALARY'] = df['BASIC SALARY'].replace({',': ''}, regex=True).astype(float)
df['ALLOWANCES'] = df['ALLOWANCES'].replace({',': ''}, regex=True).astype(float)
df['DEDUCTIONS'] = df['DEDUCTIONS'].replace({',': ''}, regex=True).astype(float)

# Calculate net salary
df['NET SALARY'] = df['BASIC SALARY'] + df['ALLOWANCES'] - df['DEDUCTIONS']

# Optional: Display the DataFrame
print(df)

# -------------------- Step 2: Generate Payslip PDFs --------------------
# Create directory for payslips
output_dir = "payslips"
os.makedirs(output_dir, exist_ok=True)

# Function to generate a payslip PDF in USD
def generate_payslip(row):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", 'B', 16)
    
    # Header
    pdf.cell(0, 10, "Employee Payslip", ln=True, align="C")
    pdf.ln(10)
    
    # Employee Info
    pdf.set_font("Arial", '', 12)
    pdf.cell(0, 10, f"Employee Name: {row['NAME']}", ln=True)
    pdf.cell(0, 10, f"Employee ID: {row['EMPLOYEE ID']}", ln=True)
    pdf.cell(0, 10, f"Email: {row['EMAIL']}", ln=True)
    pdf.ln(5)

    # Salary Details
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(0, 10, "Salary Breakdown:", ln=True)
    pdf.set_font("Arial", '', 12)
    pdf.cell(0, 10, f"Basic Salary: $ {row['BASIC SALARY']:.2f}", ln=True)
    pdf.cell(0, 10, f"Allowances: $ {row['ALLOWANCES']:.2f}", ln=True)
    pdf.cell(0, 10, f"Deductions: $ {row['DEDUCTIONS']:.2f}", ln=True)
    pdf.ln(5)

    # Net Salary
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(0, 10, f"Net Salary: $ {row['NET SALARY']:.2f}", ln=True)

    # Save PDF
    filename = os.path.join(output_dir, f"{row['EMPLOYEE ID']}.pdf")
    pdf.output(filename)
    print(f"✅ Saved payslip for {row['NAME']} -> {filename}")

# Generate payslips for all employees
for _, row in df.iterrows():
    generate_payslip(row)

# -------------------- Step 3: Send Payslip via Email --------------------
def send_email(to_email, subject, body, attachment):
    from_email = "lindsaychimanga198@gmail.com"  # Your Gmail
    password = "komr xwmd wnds rhqk"              # App password (not your main Gmail password)

    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    # Add email body
    msg.attach(MIMEText(body, 'plain'))

    # Attach the PDF
    with open(attachment, "rb") as file:
        part = MIMEApplication(file.read(), Name=os.path.basename(attachment))
        part['Content-Disposition'] = f'attachment; filename="{os.path.basename(attachment)}"'
        msg.attach(part)

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(from_email, password)
        server.sendmail(from_email, to_email, msg.as_string())
        server.quit()
        print(f"📧 Email sent to {to_email}")
    except Exception as e:
        print(f"❌ Failed to send email to {to_email}")
        print(str(e))

# Send emails with payslips
for _, row in df.iterrows():
    to_email = row['EMAIL']
    name = row['NAME']
    emp_id = row['EMPLOYEE ID']
    payslip_path = os.path.join(output_dir, f"{emp_id}.pdf")

    subject = "Your Payslip for This Month"
    body = f"""Dear {name},

Please find your payslip for this month attached.

Best regards,
HR Department
"""
    send_email(to_email, subject, body, payslip_path)
