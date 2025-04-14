from dagster_graphql import DagsterGraphQLClient

client = DagsterGraphQLClient(
    hostname="localhost:3000",
)

job = client.submit_job_execution(
    job_name="example_job",
    tags={
        "dagster/asset_partition_range_start": "2020-01-01 00:00:00",
        "dagster/asset_partition_range_end": "2025-03-31 23:00:00",
    },
)

print(job)
