import dagster as dg

five_minute_partitions = dg.TimeWindowPartitionsDefinition(
    cron_schedule="*/5 * * * *",
    start="2020-01-01 00:00:00",
    end="2025-03-31 23:55:00",
    fmt="%Y-%m-%d %H:%M:%S"
)

@dg.asset(partitions_def=five_minute_partitions)
def example_asset(context: dg.AssetExecutionContext) -> None:
    _ = context.partition_key_range
    # context.log.info(f"Processing partition {partition.start} - {partition.end}")

example_job = dg.define_asset_job(name="example_job", selection="example_asset", partitions_def=five_minute_partitions)

defs = dg.Definitions(assets=[example_asset], jobs=[example_job])