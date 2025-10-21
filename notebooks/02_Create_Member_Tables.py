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
# MAGIC  CREATE OR REPLACE TABLE ${catalog_name}.aus.member_profiles (
# MAGIC    member_id STRING,
# MAGIC    first_name STRING,
# MAGIC    last_name STRING,
# MAGIC    date_of_birth DATE,
# MAGIC    gender STRING,
# MAGIC    marital_status STRING,
# MAGIC    dependents_count INT,
# MAGIC    employment_status STRING,
# MAGIC    employer_name STRING,
# MAGIC    employment_start_date DATE,
# MAGIC    salary_amount DECIMAL(15,2),
# MAGIC    salary_frequency STRING,
# MAGIC    total_balance DECIMAL(15,2),
# MAGIC    home_ownership_status STRING,
# MAGIC    property_value DECIMAL(15,2),
# MAGIC    mortgage_balance DECIMAL(15,2),
# MAGIC    other_assets DECIMAL(15,2),
# MAGIC    employee_contribution_rate DECIMAL(5,2),
# MAGIC    employer_contribution_rate DECIMAL(5,2),
# MAGIC    voluntary_contribution_amount DECIMAL(15,2),
# MAGIC    tfn_number STRING,
# MAGIC    super_fund_name STRING,
# MAGIC    super_fund_type STRING,
# MAGIC    preservation_age INT,
# MAGIC    total_super_balance DECIMAL(15,2),
# MAGIC    transfer_balance_cap_utilization DECIMAL(15,2),
# MAGIC    concessional_contributions_ytd DECIMAL(15,2),
# MAGIC    non_concessional_contributions_ytd DECIMAL(15,2),
# MAGIC    created_date TIMESTAMP,
# MAGIC    last_updated TIMESTAMP,
# MAGIC    data_source STRING 
# MAGIC  ) USING delta
# MAGIC  TBLPROPERTIES (delta.autoOptimize.optimizeWrite = true); 
# MAGIC
# MAGIC
# MAGIC GRANT SELECT ON TABLE ${catalog_name}.aus.member_profiles TO `account users`;

# COMMAND ----------

# MAGIC %md
# MAGIC ### USA

# COMMAND ----------

# MAGIC %sql
# MAGIC  CREATE OR REPLACE TABLE ${catalog_name}.usa.member_profiles (
# MAGIC    member_id STRING,
# MAGIC    first_name STRING,
# MAGIC    last_name STRING,
# MAGIC    date_of_birth DATE,
# MAGIC    gender STRING,
# MAGIC    marital_status STRING,
# MAGIC    dependents_count INT,
# MAGIC    employment_status STRING,
# MAGIC    employer_name STRING,
# MAGIC    employment_start_date DATE,
# MAGIC    salary_amount DECIMAL(15,2),
# MAGIC    salary_frequency STRING,
# MAGIC    total_balance DECIMAL(15,2),
# MAGIC    home_ownership_status STRING,
# MAGIC    property_value DECIMAL(15,2),
# MAGIC    mortgage_balance DECIMAL(15,2),
# MAGIC    other_assets DECIMAL(15,2),
# MAGIC    employee_contribution_rate DECIMAL(5,2),
# MAGIC    employer_contribution_rate DECIMAL(5,2),
# MAGIC    voluntary_contribution_amount DECIMAL(15,2),
# MAGIC    ssn_last_four STRING,
# MAGIC    plan_type STRING,
# MAGIC    social_security_credits INT,
# MAGIC    medicare_eligibility_date DATE,
# MAGIC    rmd_required BOOLEAN,
# MAGIC    hsa_balance DECIMAL(15,2),
# MAGIC    created_date TIMESTAMP,
# MAGIC    last_updated TIMESTAMP,
# MAGIC    data_source STRING 
# MAGIC  ) USING delta;
# MAGIC
# MAGIC GRANT SELECT ON TABLE ${catalog_name}.usa.member_profiles TO `account users`;

# COMMAND ----------

# MAGIC %md
# MAGIC ### UK

# COMMAND ----------

# MAGIC %sql
# MAGIC  CREATE OR REPLACE TABLE ${catalog_name}.uk.member_profiles (
# MAGIC    member_id STRING,
# MAGIC    first_name STRING,
# MAGIC    last_name STRING,
# MAGIC    date_of_birth DATE,
# MAGIC    gender STRING,
# MAGIC    marital_status STRING,
# MAGIC    dependents_count INT,
# MAGIC    employment_status STRING,
# MAGIC    employer_name STRING,
# MAGIC    employment_start_date DATE,
# MAGIC    salary_amount DECIMAL(15,2),
# MAGIC    salary_frequency STRING,
# MAGIC    total_balance DECIMAL(15,2),
# MAGIC    home_ownership_status STRING,
# MAGIC    property_value DECIMAL(15,2),
# MAGIC    mortgage_balance DECIMAL(15,2),
# MAGIC    other_assets DECIMAL(15,2),
# MAGIC    employee_contribution_rate DECIMAL(5,2),
# MAGIC    employer_contribution_rate DECIMAL(5,2),
# MAGIC    voluntary_contribution_amount DECIMAL(15,2),
# MAGIC    ni_number STRING,
# MAGIC    state_pension_forecast DECIMAL(15,2),
# MAGIC    ni_contribution_years INT,
# MAGIC    lifetime_allowance_used DECIMAL(15,2),
# MAGIC    auto_enrollment_status STRING,
# MAGIC    created_date TIMESTAMP,
# MAGIC    last_updated TIMESTAMP,
# MAGIC    data_source STRING 
# MAGIC  ) USING delta;
# MAGIC GRANT SELECT ON TABLE ${catalog_name}.uk.member_profiles TO `account users`;

# COMMAND ----------

# MAGIC %md
# MAGIC ### India

# COMMAND ----------

# MAGIC %sql
# MAGIC  CREATE OR REPLACE TABLE ${catalog_name}.ind.member_profiles (
# MAGIC    member_id STRING,
# MAGIC    first_name STRING,
# MAGIC    last_name STRING,
# MAGIC    date_of_birth DATE,
# MAGIC    gender STRING,
# MAGIC    marital_status STRING,
# MAGIC    dependents_count INT,
# MAGIC    employment_status STRING,
# MAGIC    employer_name STRING,
# MAGIC    employment_start_date DATE,
# MAGIC    salary_amount DECIMAL(15,2),
# MAGIC    salary_frequency STRING,
# MAGIC    total_balance DECIMAL(15,2),
# MAGIC    home_ownership_status STRING,
# MAGIC    property_value DECIMAL(15,2),
# MAGIC    mortgage_balance DECIMAL(15,2),
# MAGIC    other_assets DECIMAL(15,2),
# MAGIC    employee_contribution_rate DECIMAL(5,2),
# MAGIC    employer_contribution_rate DECIMAL(5,2),
# MAGIC    voluntary_contribution_amount DECIMAL(15,2),
# MAGIC    pan_number STRING,
# MAGIC    uan_number STRING,
# MAGIC    epf_balance DECIMAL(15,2),
# MAGIC    nps_balance DECIMAL(15,2),
# MAGIC    gratuity_entitlement DECIMAL(15,2),
# MAGIC    ppf_balance DECIMAL(15,2),
# MAGIC    created_date TIMESTAMP,
# MAGIC    last_updated TIMESTAMP,
# MAGIC    data_source STRING 
# MAGIC  ) USING delta; 
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
