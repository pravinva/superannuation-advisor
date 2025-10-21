# Databricks notebook source
# MAGIC %md
# MAGIC # 4. Create Audit Tables
# MAGIC 
# MAGIC This notebook creates audit tables for logging interactions and agent traces.

# COMMAND ----------

# MAGIC %md
# MAGIC ## Configuration

# COMMAND ----------

dbutils.widgets.text("catalog_name", "multi_country_pension", "Catalog Name")
catalog_name = dbutils.widgets.get("catalog_name")

print(f"Using catalog: {catalog_name}")

# COMMAND ----------

# MAGIC %md
# MAGIC ## Chat Interactions Audit Table

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE OR REPLACE TABLE ${catalog_name}.audit.chat_interactions (
# MAGIC   interaction_id STRING,
# MAGIC   member_id STRING,
# MAGIC   country_code STRING,
# MAGIC   user_question STRING,
# MAGIC   agent_response STRING,
# MAGIC   input_validation_result STRING,
# MAGIC   tools_used ARRAY<STRING>,
# MAGIC   planning_steps ARRAY<STRING>,
# MAGIC   judge_feedback STRING,
# MAGIC   response_quality_score DECIMAL(3,2),
# MAGIC   processing_time_ms INT,
# MAGIC   timestamp TIMESTAMP,
# MAGIC   session_id STRING,
# MAGIC   experiment_id STRING
# MAGIC ) USING delta
# MAGIC TBLPROPERTIES (delta.autoOptimize.optimizeWrite = true);
# MAGIC 
# MAGIC GRANT SELECT, MODIFY ON TABLE ${catalog_name}.audit.chat_interactions TO `account users`;

# COMMAND ----------

# MAGIC %md
# MAGIC ## Agent Traces Table

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE OR REPLACE TABLE ${catalog_name}.audit.agent_traces (
# MAGIC   trace_id STRING,
# MAGIC   interaction_id STRING,
# MAGIC   step_number INT,
# MAGIC   step_type STRING,
# MAGIC   step_input STRING,
# MAGIC   step_output STRING,
# MAGIC   step_duration_ms INT,
# MAGIC   llm_calls ARRAY<STRUCT<prompt: STRING, response: STRING, tokens_used: INT>>,
# MAGIC   tools_called ARRAY<STRUCT<tool_name: STRING, parameters: STRING, result: STRING>>,
# MAGIC   timestamp TIMESTAMP
# MAGIC ) USING delta;
# MAGIC 
# MAGIC GRANT SELECT, MODIFY ON TABLE ${catalog_name}.audit.agent_traces TO `account users`;

# COMMAND ----------

# MAGIC %md
# MAGIC ## Model Evaluation Results Table

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE OR REPLACE TABLE ${catalog_name}.audit.model_evaluations (
# MAGIC   evaluation_id STRING,
# MAGIC   model_name STRING,
# MAGIC   evaluation_type STRING,
# MAGIC   dataset_used STRING,
# MAGIC   accuracy_score DECIMAL(5,4),
# MAGIC   quality_score DECIMAL(3,2),
# MAGIC   response_time_ms INT,
# MAGIC   total_queries INT,
# MAGIC   successful_queries INT,
# MAGIC   evaluation_date DATE,
# MAGIC   parameters MAP<STRING, STRING>
# MAGIC ) USING delta;
# MAGIC 
# MAGIC GRANT SELECT, MODIFY ON TABLE ${catalog_name}.audit.model_evaluations TO `account users`;

# COMMAND ----------

# MAGIC %md
# MAGIC ## Usage Analytics Table

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE OR REPLACE TABLE ${catalog_name}.audit.usage_analytics (
# MAGIC   date DATE,
# MAGIC   country_code STRING,
# MAGIC   total_interactions INT,
# MAGIC   avg_processing_time_ms INT,
# MAGIC   avg_quality_score DECIMAL(3,2),
# MAGIC   most_used_tools ARRAY<STRING>,
# MAGIC   unique_users INT
# MAGIC ) USING delta;
# MAGIC 
# MAGIC GRANT SELECT, MODIFY ON TABLE ${catalog_name}.audit.usage_analytics TO `account users`;

# COMMAND ----------

# MAGIC %md
# MAGIC ## Bulk Grant Alternative

# COMMAND ----------

# MAGIC %sql
# MAGIC -- Alternative: Grant permissions on all tables in audit schema
# MAGIC GRANT SELECT, MODIFY ON ALL TABLES IN ${catalog_name}.audit TO `account users`;

# COMMAND ----------

# MAGIC %md
# MAGIC ## Verification

# COMMAND ----------

# MAGIC %sql
# MAGIC SHOW TABLES IN ${catalog_name}.audit;

# COMMAND ----------

print("✅ Audit tables created successfully!")