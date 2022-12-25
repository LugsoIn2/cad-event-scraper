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

## .env file
AWS_ACCESS_KEY=
AWS_SECRET=
#CITIES=
GOOGLE_EVENTS_URL=

## Terraform using
One for all after refactor:

[Terraform Repo](https://github.com/LugsoIn2/cad-terraform-all.git)

 
