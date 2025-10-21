# Databricks notebook source
# MAGIC %md
# MAGIC # 1. Setup Catalog and Schemas
# MAGIC 
# MAGIC This notebook creates the Unity Catalog and schemas for the pension advisor demo.

# COMMAND ----------

# MAGIC %md
# MAGIC ## Configuration
# MAGIC Set your catalog name and countries here:

# COMMAND ----------

dbutils.widgets.text("catalog_name", "multi_country_pension", "Catalog Name")
dbutils.widgets.text("country_schemas", "aus,uk,ind,usa", "Country Schemas (comma-separated)")

catalog_name = dbutils.widgets.get("catalog_name")
country_schemas = [s.strip().lower() for s in dbutils.widgets.get("country_schemas").split(",")]

print(f"Creating catalog: {catalog_name}")
print(f"Creating schemas for: {country_schemas}")

# COMMAND ----------

# MAGIC %md
# MAGIC ## Create Catalog

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE CATALOG IF NOT EXISTS ${catalog_name};
# MAGIC 
# MAGIC -- Grant permissions
# MAGIC GRANT ALL PRIVILEGES ON CATALOG ${catalog_name} TO `account users`;

# COMMAND ----------

# MAGIC %md
# MAGIC ## Create Schemas

# COMMAND ----------

for schema in country_schemas:
    print(f"Creating schema: {schema}")
    spark.sql(f"CREATE SCHEMA IF NOT EXISTS {catalog_name}.{schema}")

# Create audit schema
spark.sql(f"CREATE SCHEMA IF NOT EXISTS {catalog_name}.audit")

# COMMAND ----------

# MAGIC %md
# MAGIC ## Set Current Catalog

# COMMAND ----------

spark.sql(f"USE CATALOG {catalog_name}")

# COMMAND ----------

# MAGIC %md
# MAGIC ## Verification

# COMMAND ----------

# MAGIC %sql
# MAGIC SHOW SCHEMAS;

# COMMAND ----------

print("✅ Catalog and schemas setup complete!")
print(f"📁 Catalog: {catalog_name}")
print(f"📂 Schemas: {country_schemas + ['audit']}")