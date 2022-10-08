# GSheet2Calendar
Parsing a Google sheet to a more user-friendly iCal.

## Usage
You can choose between following the instructions we provide [here](https://cytech-calendars.cleverapps.io/) or self-hosting the app yourself.

### Self-hosting
Requirements:
- A Python 3.10 run environment.
- A PostgreSQL database.
- An S3-type object storage.

Setup a python virtual environment.
```shell
python3 -m venv venv              # Create virtual environment
source ./venv/bin/activate        # Activate virtual environment
pip install -r requirements.txt   # Install dependencies
```

Set environment variables.
```shell
BUCKET_NAME=<S3 bucket to store ICS files>
POSTGRESQL_ADDON_URI=<connection URI to the PSQL db>
CELLAR_ADDON_HOST=<S3 host>
CELLAR_ADDON_KEY_ID=<S3 access key>
CELLAR_ADDON_KEY_SECRET=<S3 secret access key>
```

Populate database with a table named `timetables` and columns:
- `id`: Primary key.
- `gid`: Group ID, get this from the GSheet URL.
- `name`: The name given to the generated ICS files.
- `spreadsheet_id`: Spreadsheet ID, get this from the GSheet URL.

Set up a CRON-job to run `scrap.py` whenever you want.
