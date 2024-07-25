import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

# Get job arguments
args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Read data from AWS Glue Data Catalog
datasource = glueContext.create_dynamic_frame.from_catalog(
    database="de-github-raw",
    table_name="raw_statistics_reference_data",
    transformation_ctx="datasource"
)

# Drop unwanted columns (excluding 'created_at')
cleaned_frame = datasource.drop_fields(['languages_used', 'licence'])

# Drop rows with missing values
cleaned_frame = DropNullFields.apply(frame=cleaned_frame)

# Define output path
output_path = "s3://de-on-github-cleansed-useast1-dev/github/raw_statistics"

# Save the cleaned data to S3 in Parquet format
sink = glueContext.write_dynamic_frame.from_options(
    frame=cleaned_frame,
    connection_type="s3",
    connection_options={"path": output_path},
    format="parquet"
)

job.commit()
