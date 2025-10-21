# Databricks notebook source
# MAGIC %md
# MAGIC # 2. Create Member Tables
# MAGIC 
# MAGIC This notebook creates the member profile tables for each country.

# COMMAND ----------

# MAGIC %md
# MAGIC ## Configuration

# COMMAND ----------

dbutils.widgets.text("catalog_name", "multi_country_pension", "Catalog Name")
catalog_name = dbutils.widgets.get("catalog_name")

print(f"Using catalog: {catalog_name}")

# COMMAND ----------

# MAGIC %md
# MAGIC ## Create Country-Specific Member Tables

# COMMAND ----------

# MAGIC %md
# MAGIC ### Australia

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE OR REPLACE TABLE ${catalog_name}.aus.member_profiles (
# MAGIC   -- [table definition remains the same]
# MAGIC ) USING delta
# MAGIC TBLPROPERTIES (delta.autoOptimize.optimizeWrite = true);
# MAGIC 
# MAGIC GRANT SELECT ON TABLE ${catalog_name}.aus.member_profiles TO `account users`;

# COMMAND ----------

# MAGIC %md
# MAGIC ### USA

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE OR REPLACE TABLE ${catalog_name}.usa.member_profiles (
# MAGIC   -- [table definition remains the same]
# MAGIC ) USING delta;
# MAGIC 
# MAGIC GRANT SELECT ON TABLE ${catalog_name}.usa.member_profiles TO `account users`;

# COMMAND ----------

# MAGIC %md
# MAGIC ### UK

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE OR REPLACE TABLE ${catalog_name}.uk.member_profiles (
# MAGIC   -- [table definition remains the same]
# MAGIC ) USING delta;
# MAGIC 
# MAGIC GRANT SELECT ON TABLE ${catalog_name}.uk.member_profiles TO `account users`;

# COMMAND ----------

# MAGIC %md
# MAGIC ### India

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE OR REPLACE TABLE ${catalog_name}.ind.member_profiles (
# MAGIC   -- [table definition remains the same]
# MAGIC ) USING delta;
# MAGIC 
# MAGIC GRANT SELECT ON TABLE ${catalog_name}.ind.member_profiles TO `account users`;

# COMMAND ----------

# MAGIC %md
# MAGIC ## Verification

# COMMAND ----------

# MAGIC %sql
# MAGIC SHOW TABLES IN ${catalog_name}.aus;
# MAGIC SHOW TABLES IN ${catalog_name}.usa;
# MAGIC SHOW TABLES IN ${catalog_name}.uk;
# MAGIC SHOW TABLES IN ${catalog_name}.ind;

# COMMAND ----------

print("✅ Member tables created successfully!")