from awsglue.job import Job
from awsglue.dynamicframe import DynamicFrame

args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Script generated for node AWS Glue Data Catalog
AWSGlueDataCatalog_node1721773357825 = glueContext.create_dynamic_frame.from_catalog(database="de-github-raw", table_name="raw_statistics_reference_data", transformation_ctx="AWSGlueDataCatalog_node1721773357825")

# Script generated for node AWS Glue Data Catalog
AWSGlueDataCatalog_node1721773342668 = glueContext.create_dynamic_frame.from_catalog(database="de-github-cleaned", table_name="raw_statistics", transformation_ctx="AWSGlueDataCatalog_node1721773342668")

# Script generated for node Join
AWSGlueDataCatalog_node1721773357825DF = AWSGlueDataCatalog_node1721773357825.toDF()
AWSGlueDataCatalog_node1721773342668DF = AWSGlueDataCatalog_node1721773342668.toDF()
Join_node1721773386736 = DynamicFrame.fromDF(AWSGlueDataCatalog_node1721773357825DF.join(AWSGlueDataCatalog_node1721773342668DF, (AWSGlueDataCatalog_node1721773357825DF['name'] == AWSGlueDataCatalog_node1721773342668DF['name']), "right"), glueContext, "Join_node1721773386736")

# Script generated for node Drop Fields
DropFields_node1721774945000 = DropFields.apply(frame=Join_node1721773386736, paths=["licence", "languages_used"], transformation_ctx="DropFields_node1721774945000")

# Script generated for node Amazon S3
AmazonS3_node1721775144740 = glueContext.getSink(path="s3://de-on-github-analytics-useast1-dev", connection_type="s3", updateBehavior="UPDATE_IN_DATABASE", partitionKeys=[], enableUpdateCatalog=True, transformation_ctx="AmazonS3_node1721775144740")
AmazonS3_node1721775144740.setCatalogInfo(catalogDatabase="db_github_analytics",catalogTableName="final_analytics")
AmazonS3_node1721775144740.setFormat("glueparquet", compression="snappy")
AmazonS3_node1721775144740.writeFrame(DropFields_node1721774945000)
