# CAD Event Scraper

Scraping is not a crime

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
```
AWS_ACCESS_KEY=xxx (key)
AWS_SECRET=xxx (secret)
CMD_EXEC='http://chrome:4444/wd/hub' (localhost for Kubernetes)
```
```
EV_TABLE_NAME= (event table name in aws dynamodb)
TEN_TABLE_NAME= (tenants table name in aws dnyamodb)
```
```
CITIES="generic" / "Konstanz" (generic for all cities, otherwise select city)
SCRAPER_NAME="GOOGLE" / "KULA" / "BFK" (type of scraper)
EVENTS_URL= (url of website to scrape)
```

## Terraform using
One for all after refactor:

[Terraform Repo](https://github.com/LugsoIn2/cad-terraform-all.git)

 
