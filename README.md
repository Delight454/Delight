# Employee Payroll Processing System
==============================

A comprehensive Python-based system for processing employee salaries, generating payslips, and automated email distribution.


## Overview
--------

This system automates the entire payroll process workflow, handling everything from raw Excel data processing to final email delivery of payslips.


## Features
--------

* Processes employee salary data from Excel spreadsheets
* Generates professional PDF payslips
* Calculates net salaries with allowances and deductions
* Automates email delivery of payslips
* Maintains organized output structure


## Requirements
------------

* Python 3.x
* Required packages:
  * `pandas`
  * `fpdf`
  * `smtplib`
* Input Excel file (`employees.xlsx.xlsx`) with columns:
  * `NAME`
  * `EMPLOYEE ID`
  * `EMAIL`
  * `BASIC SALARY`
  * `ALLOWANCES`
  * `DEDUCTIONS`


## Setup Instructions
-------------------

### Install Dependencies

```bash
pip install pandas fpdf
```

### Input File Structure
Your Excel file should contain the following columns:

| Column Name | Description | Format |
|-------------|-------------|--------|
| NAME        | Employee name | Text   |
| EMPLOYEE ID | Unique identifier | Text |
| EMAIL       | Employee email | Email  |
| BASIC SALARY| Base monthly salary | Number |
| ALLOWANCES  | Additional benefits | Number |
| DEDUCTIONS  | Salary deductions | Number |

### Gmail SMTP Setup

1. Enable "Less secure app access" in Google Account settings
2. Generate an App Password if 2FA is enabled
3. Update the email credentials in the script:
   ```python
from_email = "your-email@gmail.com"
password = "your-app-password"
```

## Usage
-----

```python
# Run the script directly
python payroll_processor.py
```

The system will:
1. Process the Excel file
2. Generate PDF payslips in the `payslips` directory
3. Send emails to all employees with their payslips attached

## Output Format
--------------

Each generated payslip contains:

* Employee identification details
* Salary breakdown:
  * Basic salary
  * Allowances
  * Deductions
* Net salary calculation
* Professional formatting with clear headers

## Error Handling
-------------

The system includes comprehensive error handling for:
* File processing issues
* Email delivery failures
* Data validation errors

All errors are logged to console with appropriate status indicators.


## License
-------

MIT License

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
