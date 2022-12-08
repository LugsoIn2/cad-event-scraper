# CAD Event Scraper

## Run

### Set environment variables
- `export AWS_ACCESS_KEY=key`
- `export AWS_SECRET=secret`
- `export GOOGLE_EVENTS_URL=url`

### Set city to fetch

The script fetches data for all cities in the database 'tenants'.

Alternatively, you can suppress this by setting city environment variable:
- `export CITIES=konstanz,freiburg`

### Run script

Run `docker compose up --build` to run the scraper.