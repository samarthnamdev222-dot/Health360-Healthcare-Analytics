# Health360 — Flask Dashboard

A responsive healthcare analytics dashboard built with Python + Flask, HTML, CSS and Chart.js.
The included figures are illustrative demo data, not real patient data and not copied from the linked Tableau workbook.
Tableau public dashboard link https://public.tableau.com/views/Health360_ComprehensiveHealthcareRiskDiseaseAnalytics_17935331219980/SmartHealthcareAnalyticsPatientRiskLifestyleInsights?:language=en-US&publish=yes&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link 

## Run on Windows

1. Install Python 3.10+.
2. Open this folder in VS Code.
3. In the terminal, create and activate a virtual environment (optional but recommended):

   ```powershell
   py -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

   If PowerShell blocks activation, you can run the app without activating the environment:
   ```powershell
   .\.venv\Scripts\python.exe -m pip install -r requirements.txt
   .\.venv\Scripts\python.exe app.py
   ```

4. Install Flask:
   ```powershell
   python -m pip install -r requirements.txt
   ```
5. Start the server:
   ```powershell
   python app.py
   ```
6. Open `http://127.0.0.1:5000` in your browser.

## Customize with your own data

Edit `SUMMARY`, `DISEASES`, and `AGE_GROUPS` in `app.py`, or replace them with values loaded from CSV/Excel/database.
The search field filters the disease table. The date range selector and navigation tabs are front-end demo controls.

## Important

- The dashboard uses sample values for demonstration. Verify all numbers before using them in a report or presentation.
- To make the website match the Tableau Story/Dashboard precisely, provide screenshots or export the underlying data; the public links may require Tableau access and do not expose the full workbook data to this starter app.
