# Databricks notebook source
# MAGIC %md
# MAGIC # 3. Create Unity Catalog Functions
# MAGIC 
# MAGIC This notebook creates the pension calculation functions.

# COMMAND ----------

# MAGIC %md
# MAGIC ## Configuration

# COMMAND ----------

dbutils.widgets.text("catalog_name", "multi_country_pension", "Catalog Name")
catalog_name = dbutils.widgets.get("catalog_name")

print(f"Using catalog: {catalog_name}")

# COMMAND ----------

# MAGIC %md
# MAGIC ## Australia Functions

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE OR REPLACE FUNCTION ${catalog_name}.aus.calculate_preservation_age(birth_date DATE)
# MAGIC RETURNS INT
# MAGIC RETURN CASE 
# MAGIC   WHEN year(birth_date) <= 1960 THEN 55
# MAGIC   WHEN year(birth_date) <= 1961 THEN 56
# MAGIC   WHEN year(birth_date) <= 1962 THEN 57
# MAGIC   WHEN year(birth_date) <= 1963 THEN 58
# MAGIC   WHEN year(birth_date) <= 1964 THEN 59
# MAGIC   ELSE 60
# MAGIC END;
# MAGIC 
# MAGIC GRANT EXECUTE ON FUNCTION ${catalog_name}.aus.calculate_preservation_age TO `account users`;

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE OR REPLACE FUNCTION ${catalog_name}.aus.project_super_balance(
# MAGIC   current_balance DECIMAL(15,2),
# MAGIC   current_age INT,
# MAGIC   retirement_age INT,
# MAGIC   salary DECIMAL(15,2),
# MAGIC   employee_contribution_rate DECIMAL(5,2),
# MAGIC   employer_contribution_rate DECIMAL(5,2),
# MAGIC   annual_return_rate DECIMAL(5,2)
# MAGIC )
# MAGIC RETURNS DECIMAL(15,2)
# MAGIC RETURN ROUND(
# MAGIC   current_balance * POWER(1 + annual_return_rate/100, retirement_age - current_age) +
# MAGIC   (salary * (employee_contribution_rate + employer_contribution_rate) / 100) * 
# MAGIC   (POWER(1 + annual_return_rate/100, retirement_age - current_age) - 1) / (annual_return_rate/100),
# MAGIC   2
# MAGIC );
# MAGIC 
# MAGIC GRANT EXECUTE ON FUNCTION ${catalog_name}.aus.project_super_balance TO `account users`;

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE OR REPLACE FUNCTION ${catalog_name}.aus.calculate_concessional_cap_utilization(
# MAGIC   ytd_contributions DECIMAL(15,2),
# MAGIC   carry_forward_balance DECIMAL(15,2)
# MAGIC )
# MAGIC RETURNS DECIMAL(15,2)
# MAGIC RETURN GREATEST(0, 27500 - ytd_contributions) + carry_forward_balance;
# MAGIC 
# MAGIC GRANT EXECUTE ON FUNCTION ${catalog_name}.aus.calculate_concessional_cap_utilization TO `account users`;

# COMMAND ----------

# MAGIC %md
# MAGIC ## USA Functions

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE OR REPLACE FUNCTION ${catalog_name}.usa.calculate_retirement_age(birth_date DATE)
# MAGIC RETURNS INT
# MAGIC RETURN CASE 
# MAGIC   WHEN year(birth_date) <= 1954 THEN 66
# MAGIC   WHEN year(birth_date) <= 1959 THEN 67
# MAGIC   ELSE 67
# MAGIC END;
# MAGIC 
# MAGIC GRANT EXECUTE ON FUNCTION ${catalog_name}.usa.calculate_retirement_age TO `account users`;

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE OR REPLACE FUNCTION ${catalog_name}.usa.calculate_social_security_benefit(
# MAGIC   birth_date DATE,
# MAGIC   retirement_age INT,
# MAGIC   average_indexed_earnings DECIMAL(15,2)
# MAGIC )
# MAGIC RETURNS DECIMAL(10,2)
# MAGIC RETURN CASE
# MAGIC   WHEN retirement_age = 67 THEN average_indexed_earnings * 0.90
# MAGIC   WHEN retirement_age < 67 THEN average_indexed_earnings * 0.75
# MAGIC   WHEN retirement_age = 70 THEN average_indexed_earnings * 1.24
# MAGIC   ELSE average_indexed_earnings * 1.08
# MAGIC END;
# MAGIC 
# MAGIC GRANT EXECUTE ON FUNCTION ${catalog_name}.usa.calculate_social_security_benefit TO `account users`;

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE OR REPLACE FUNCTION ${catalog_name}.usa.calculate_rmd_amount(
# MAGIC   account_balance DECIMAL(15,2),
# MAGIC   age INT
# MAGIC )
# MAGIC RETURNS DECIMAL(15,2)
# MAGIC RETURN CASE
# MAGIC   WHEN age < 73 THEN 0
# MAGIC   WHEN age BETWEEN 73 AND 79 THEN account_balance / (27.4 - (age - 72) * 0.2)
# MAGIC   WHEN age >= 80 THEN account_balance / (24.7 - (age - 79) * 0.5)
# MAGIC   ELSE 0
# MAGIC END;
# MAGIC 
# MAGIC GRANT EXECUTE ON FUNCTION ${catalog_name}.usa.calculate_rmd_amount TO `account users`;

# COMMAND ----------

# MAGIC %md
# MAGIC ## UK Functions

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE OR REPLACE FUNCTION ${catalog_name}.uk.calculate_retirement_age(birth_date DATE)
# MAGIC RETURNS INT
# MAGIC RETURN 67;
# MAGIC 
# MAGIC GRANT EXECUTE ON FUNCTION ${catalog_name}.uk.calculate_retirement_age TO `account users`;

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE OR REPLACE FUNCTION ${catalog_name}.uk.calculate_state_pension(
# MAGIC   ni_contribution_years INT
# MAGIC )
# MAGIC RETURNS DECIMAL(10,2)
# MAGIC RETURN CASE
# MAGIC   WHEN ni_contribution_years >= 35 THEN 221.20
# MAGIC   WHEN ni_contribution_years >= 10 THEN 221.20 * ni_contribution_years / 35
# MAGIC   ELSE 0
# MAGIC END;
# MAGIC 
# MAGIC GRANT EXECUTE ON FUNCTION ${catalog_name}.uk.calculate_state_pension TO `account users`;

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE OR REPLACE FUNCTION ${catalog_name}.uk.calculate_annual_allowance_utilization(
# MAGIC   total_contributions DECIMAL(15,2),
# MAGIC   threshold_income DECIMAL(15,2),
# MAGIC   adjusted_income DECIMAL(15,2)
# MAGIC )
# MAGIC RETURNS DECIMAL(15,2)
# MAGIC RETURN CASE
# MAGIC   WHEN threshold_income <= 200000 THEN GREATEST(0, 60000 - total_contributions)
# MAGIC   WHEN adjusted_income > 260000 THEN GREATEST(0, 10000 - total_contributions)
# MAGIC   ELSE GREATEST(0, 60000 - ((adjusted_income - 240000) / 2) - total_contributions)
# MAGIC END;
# MAGIC 
# MAGIC GRANT EXECUTE ON FUNCTION ${catalog_name}.uk.calculate_annual_allowance_utilization TO `account users`;

# COMMAND ----------

# MAGIC %md
# MAGIC ## India Functions

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE OR REPLACE FUNCTION ${catalog_name}.ind.calculate_retirement_age(birth_date DATE)
# MAGIC RETURNS INT
# MAGIC RETURN 58;
# MAGIC 
# MAGIC GRANT EXECUTE ON FUNCTION ${catalog_name}.ind.calculate_retirement_age TO `account users`;

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE OR REPLACE FUNCTION ${catalog_name}.ind.calculate_epf_projection(
# MAGIC   current_balance DECIMAL(15,2),
# MAGIC   years_to_retirement INT,
# MAGIC   monthly_salary DECIMAL(15,2),
# MAGIC   employee_rate DECIMAL(5,2),
# MAGIC   employer_rate DECIMAL(5,2),
# MAGIC   interest_rate DECIMAL(5,2)
# MAGIC )
# MAGIC RETURNS DECIMAL(15,2)
# MAGIC RETURN ROUND(
# MAGIC   current_balance * POWER(1 + interest_rate/100, years_to_retirement) +
# MAGIC   (monthly_salary * 12 * (employee_rate + employer_rate) / 100) * 
# MAGIC   (POWER(1 + interest_rate/100, years_to_retirement) - 1) / (interest_rate/100),
# MAGIC   2
# MAGIC );
# MAGIC 
# MAGIC GRANT EXECUTE ON FUNCTION ${catalog_name}.ind.calculate_epf_projection TO `account users`;

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE OR REPLACE FUNCTION ${catalog_name}.ind.calculate_gratuity_amount(
# MAGIC   last_drawn_salary DECIMAL(15,2),
# MAGIC   years_of_service DECIMAL(5,2)
# MAGIC )
# MAGIC RETURNS DECIMAL(15,2)
# MAGIC RETURN LEAST(
# MAGIC   (last_drawn_salary * years_of_service * 15) / 26,
# MAGIC   2000000
# MAGIC );
# MAGIC 
# MAGIC GRANT EXECUTE ON FUNCTION ${catalog_name}.ind.calculate_gratuity_amount TO `account users`;

# COMMAND ----------

# MAGIC %md
# MAGIC ## Grant Bulk Permissions (Alternative Approach)

# COMMAND ----------

# MAGIC %sql
# MAGIC -- Alternative: Grant EXECUTE on all functions in each schema
# MAGIC GRANT EXECUTE ON ALL FUNCTIONS IN ${catalog_name}.aus TO `account users`;
# MAGIC GRANT EXECUTE ON ALL FUNCTIONS IN ${catalog_name}.usa TO `account users`;
# MAGIC GRANT EXECUTE ON ALL FUNCTIONS IN ${catalog_name}.uk TO `account users`;
# MAGIC GRANT EXECUTE ON ALL FUNCTIONS IN ${catalog_name}.ind TO `account users`;

# COMMAND ----------

# MAGIC %md
# MAGIC ## Verification

# COMMAND ----------

# MAGIC %sql
# MAGIC SHOW FUNCTIONS IN ${catalog_name}.aus;
# MAGIC SHOW FUNCTIONS IN ${catalog_name}.usa;
# MAGIC SHOW FUNCTIONS IN ${catalog_name}.uk;
# MAGIC SHOW FUNCTIONS IN ${catalog_name}.ind;

# COMMAND ----------

# MAGIC %md
# MAGIC ## Test the Functions

# COMMAND ----------

# MAGIC %sql
# MAGIC -- Test Australian preservation age
# MAGIC SELECT 
# MAGIC   ${catalog_name}.aus.calculate_preservation_age('1980-06-15') as preservation_age;

# COMMAND ----------

print("✅ UC functions created and tested successfully!")