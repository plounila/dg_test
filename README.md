# Dagster issue reproduction project

This project is a reproduction of an issue with Dagster.
With version 1.10.5, the running the `launch_job.py` script will end up timing out during the GraphQL request.
With version 1.10.4, the script runs successfully.

## Steps to reproduce

0. Adjust the `pyproject.toml` file to use Dagster version `==1.10.5` (or the version you want to test)
1. Install dependencies: `uv sync`
2. Start virtual environment: `source .venv/bin/activate`
3. Run the Dagster server: `dagster dev -f example/assets.py`
4. Attempt to launch the example job: `python launch_job.py`

## Expected behavior

The script should run successfully, printing out the ID of the Dagster run that was launched.

## Actual behavior

We get a long error message, boiling down to a timeout error on the GraphQL request after 5 minutes.
When looking at the Dagster UI at <http://127.0.0.1:3000/locations/assets.py/jobs/example_job>, we can see that the
count of partitions to be materialized keeps increasing until the job eventually starts.
