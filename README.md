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

## Terraform
We use a terraform setup with global state management over AWS S3 Backend.
The TF workspace for this service: FIXME
### Terraform AWS secrets for local testing
add a file with the following content and name "secrets.auto.tfvars" in the directory ./terraform/prod/
```sh
access_key = "id"
secret_key = "secret_key"
```
### Terraform Workspaces
ecr_repo_scraper = "ecr_repo_scraper" workspace
FIXME

