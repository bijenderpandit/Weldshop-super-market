# Fabrication Pallet Parts Dashboard (Flask + Blueprints + SQLite)

Web dashboard for managing **pallet parts** and **assembly parts**, with **admin/user roles**, **add/subtract transactions**, and **Excel import/export**.

## Features
- Login with roles (**admin**, **user**)
- Pallet header fields: **Pallet ID**, **Date**, **Location**, **Project Code**, **BOT (product)**
- Line items per pallet: **Part Type** (Pallet/Assembly), **Part Name**, **SAP Code**, **Quantity**
- Users can **add/subtract** quantities; every change creates a **transaction history** entry
- Admin can **export/import Excel (.xlsx)**

## Setup (Windows / PowerShell)

```powershell
cd C:\Weldshop
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Run

```powershell
$env:FLASK_APP = "app.py"
$env:FLASK_ENV = "development"
python app.py
```

### Access Dashboard

**Same Computer:**
- Open: `http://127.0.0.1:5000` or `http://localhost:5000`

**Other Devices (Laptop/Mobile on Same Network):**
1. Find your computer's IP address:
   ```powershell
   ipconfig
   ```
   Look for **IPv4 Address** under your active network adapter (usually starts with `192.168.x.x` or `10.x.x.x`)

2. On other device's browser, open:
   ```
   http://YOUR_IP_ADDRESS:5000
   ```
   Example: `http://192.168.1.100:5000`

**Note:** Make sure both devices are on the same Wi-Fi/network and Windows Firewall allows port 5000.

## Initialize DB + create first admin

```powershell
python -m flask --app app.py init-db
python -m flask --app app.py create-admin --username admin --password admin123
```

Then login with the admin and create users.

## Excel import format

Import supports a workbook with a sheet named **Items** containing these columns:
- `pallet_id` (required)
- `date` (optional, `YYYY-MM-DD`)
- `location` (optional)
- `project_code` (optional)
- `bot_product` (optional)
- `part_type` (required: `PALLET` or `ASSEMBLY`)
- `part_name` (required)
- `sap_code` (required)
- `qty` (required, integer)

Admin can also export a template from the Admin page.


