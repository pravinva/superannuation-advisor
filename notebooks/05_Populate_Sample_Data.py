# Databricks notebook source
# MAGIC %md
# MAGIC # 5. Populate Sample Data
# MAGIC 
# MAGIC This notebook populates sample member data for testing.

# COMMAND ----------

# MAGIC %md
# MAGIC ## Configuration

# COMMAND ----------

dbutils.widgets.text("catalog_name", "multi_country_pension", "Catalog Name")
catalog_name = dbutils.widgets.get("catalog_name")

print(f"Using catalog: {catalog_name}")

# COMMAND ----------

# MAGIC %md
# MAGIC ## Insert Sample Australian Members

# COMMAND ----------

# MAGIC %sql
# MAGIC INSERT INTO ${catalog_name}.aus.member_profiles VALUES
# MAGIC (
# MAGIC   'AUS001', 'Sarah', 'Wilson', '1980-06-15', 'FEMALE', 'MARRIED', 2, 
# MAGIC   'EMPLOYED', 'ANZ Bank', '2015-03-01', 120000.00, 'ANNUALLY', 285000.00,
# MAGIC   'MORTGAGED', 850000.00, 450000.00, 75000.00, 9.5, 10.5, 5000.00,
# MAGIC   '123456789', 'AustralianSuper', 'INDUSTRY', 60, 285000.00, 0.0, 22000.00, 8000.00,
# MAGIC   current_timestamp(), current_timestamp(), 'SAMPLE'
# MAGIC ),
# MAGIC (
# MAGIC   'AUS002', 'James', 'Thompson', '1972-11-22', 'MALE', 'SINGLE', 0,
# MAGIC   'EMPLOYED', 'Telstra', '2008-07-15', 95000.00, 'ANNUALLY', 420000.00,
# MAGIC   'OWNED', 650000.00, 0.00, 120000.00, 7.0, 9.5, 2000.00,
# MAGIC   '987654321', 'AMP', 'RETAIL', 58, 420000.00, 0.0, 25000.00, 15000.00,
# MAGIC   current_timestamp(), current_timestamp(), 'SAMPLE'
# MAGIC ),
# MAGIC (
# MAGIC   'AUS003', 'Emma', 'Chen', '1985-03-10', 'FEMALE', 'MARRIED', 1,
# MAGIC   'EMPLOYED', 'Woolworths', '2018-09-12', 85000.00, 'ANNUALLY', 185000.00,
# MAGIC   'RENTING', 0.00, 0.00, 45000.00, 10.0, 12.5, 1000.00,
# MAGIC   '456123789', 'Hostplus', 'INDUSTRY', 60, 185000.00, 0.0, 18000.00, 5000.00,
# MAGIC   current_timestamp(), current_timestamp(), 'SAMPLE'
# MAGIC ),
# MAGIC (
# MAGIC   'AUS004', 'Michael', 'Brown', '1965-08-30', 'MALE', 'DIVORCED', 2,
# MAGIC   'EMPLOYED', 'BHP', '1995-01-15', 150000.00, 'ANNUALLY', 650000.00,
# MAGIC   'OWNED', 950000.00, 0.00, 250000.00, 12.5, 13.5, 7500.00,
# MAGIC   '789123456', 'Colonial First State', 'RETAIL', 60, 650000.00, 150000.00, 27000.00, 20000.00,
# MAGIC   current_timestamp(), current_timestamp(), 'SAMPLE'
# MAGIC );

# COMMAND ----------

# MAGIC %md
# MAGIC ## Insert Sample USA Members

# COMMAND ----------

# MAGIC %sql
# MAGIC INSERT INTO ${catalog_name}.usa.member_profiles VALUES
# MAGIC (
# MAGIC   'USA001', 'Michael', 'Johnson', '1978-03-10', 'MALE', 'MARRIED', 3,
# MAGIC   'EMPLOYED', 'Microsoft', '2012-08-01', 145000.00, 'ANNUALLY', 385000.00,
# MAGIC   'MORTGAGED', 950000.00, 520000.00, 150000.00, 8.0, 6.0, 6500.00,
# MAGIC   '1234', '401K', 38, '2043-03-10', false, 12500.00,
# MAGIC   current_timestamp(), current_timestamp(), 'SAMPLE'
# MAGIC ),
# MAGIC (
# MAGIC   'USA002', 'Jennifer', 'Davis', '1971-12-05', 'FEMALE', 'MARRIED', 2,
# MAGIC   'EMPLOYED', 'Google', '2015-11-15', 165000.00, 'ANNUALLY', 520000.00,
# MAGIC   'MORTGAGED', 1200000.00, 680000.00, 220000.00, 10.0, 8.0, 8500.00,
# MAGIC   '5678', '401K', 42, '2036-12-05', false, 18500.00,
# MAGIC   current_timestamp(), current_timestamp(), 'SAMPLE'
# MAGIC ),
# MAGIC (
# MAGIC   'USA003', 'Robert', 'Williams', '1982-07-22', 'MALE', 'SINGLE', 0,
# MAGIC   'EMPLOYED', 'Amazon', '2019-04-01', 125000.00, 'ANNUALLY', 195000.00,
# MAGIC   'RENTING', 0.00, 0.00, 75000.00, 6.0, 5.0, 3000.00,
# MAGIC   '9012', '401K', 32, '2047-07-22', false, 8500.00,
# MAGIC   current_timestamp(), current_timestamp(), 'SAMPLE'
# MAGIC );

# COMMAND ----------

# MAGIC %md
# MAGIC ## Insert Sample UK Members

# COMMAND ----------

# MAGIC %sql
# MAGIC INSERT INTO ${catalog_name}.uk.member_profiles VALUES
# MAGIC (
# MAGIC   'UK001', 'David', 'Wilson', '1975-11-18', 'MALE', 'MARRIED', 2,
# MAGIC   'EMPLOYED', 'HSBC', '2010-06-15', 88000.00, 'ANNUALLY', 320000.00,
# MAGIC   'MORTGAGED', 650000.00, 320000.00, 120000.00, 7.5, 8.5, 4000.00,
# MAGIC   'AB123456C', 185.00, 22, 0.0, 'ENROLLED',
# MAGIC   current_timestamp(), current_timestamp(), 'SAMPLE'
# MAGIC ),
# MAGIC (
# MAGIC   'UK002', 'Sophie', 'Taylor', '1982-04-30', 'FEMALE', 'SINGLE', 0,
# MAGIC   'EMPLOYED', 'BBC', '2016-09-22', 72000.00, 'ANNUALLY', 280000.00,
# MAGIC   'RENTING', 0.00, 0.00, 65000.00, 5.0, 6.0, 2500.00,
# MAGIC   'CD987654E', 165.50, 15, 0.0, 'ENROLLED',
# MAGIC   current_timestamp(), current_timestamp(), 'SAMPLE'
# MAGIC );

# COMMAND ----------

# MAGIC %md
# MAGIC ## Insert Sample India Members

# COMMAND ----------

# MAGIC %sql
# MAGIC INSERT INTO ${catalog_name}.ind.member_profiles VALUES
# MAGIC (
# MAGIC   'IND001', 'Raj', 'Patel', '1973-09-12', 'MALE', 'MARRIED', 2,
# MAGIC   'EMPLOYED', 'Tata Consultancy', '2005-03-15', 1800000.00, 'ANNUALLY', 2800000.00,
# MAGIC   'OWNED', 12500000.00, 0.00, 3500000.00, 12.0, 12.0, 100000.00,
# MAGIC   'ABCDE1234F', '101234567890', 1850000.00, 950000.00, 2500000.00, 800000.00,
# MAGIC   current_timestamp(), current_timestamp(), 'SAMPLE'
# MAGIC ),
# MAGIC (
# MAGIC   'IND002', 'Priya', 'Sharma', '1977-12-08', 'FEMALE', 'MARRIED', 1,
# MAGIC   'EMPLOYED', 'Infosys', '2012-07-01', 2200000.00, 'ANNUALLY', 3200000.00,
# MAGIC   'MORTGAGED', 18000000.00, 8500000.00, 4200000.00, 10.0, 12.0, 120000.00,
# MAGIC   'FGHIJ5678K', '102345678901', 2200000.00, 1000000.00, 3200000.00, 1200000.00,
# MAGIC   current_timestamp(), current_timestamp(), 'SAMPLE'
# MAGIC );

# COMMAND ----------

# MAGIC %md
# MAGIC ## Insert Sample Audit Data

# COMMAND ----------

# MAGIC %sql
# MAGIC INSERT INTO ${catalog_name}.audit.chat_interactions VALUES
# MAGIC (
# MAGIC   'INT-001', 'AUS001', 'AUS', 'What is my super balance at retirement?',
# MAGIC   'Based on your current balance of $285,000...', 'VALID', 
# MAGIC   ARRAY('aus.project_super_balance', 'aus.calculate_preservation_age'),
# MAGIC   ARRAY('Calculate retirement projection', 'Check preservation age'),
# MAGIC   'Response meets quality standards', 4.8, 2450,
# MAGIC   current_timestamp(), 'SESS-001', 'EXP-001'
# MAGIC );

# COMMAND ----------

# MAGIC %md
# MAGIC ## Verification

# COMMAND ----------

# MAGIC %sql
# MAGIC -- Check data counts
# MAGIC SELECT 'Australia' as country, COUNT(*) as member_count FROM ${catalog_name}.aus.member_profiles
# MAGIC UNION ALL
# MAGIC SELECT 'USA', COUNT(*) FROM ${catalog_name}.usa.member_profiles
# MAGIC UNION ALL
# MAGIC SELECT 'UK', COUNT(*) FROM ${catalog_name}.uk.member_profiles
# MAGIC UNION ALL
# MAGIC SELECT 'India', COUNT(*) FROM ${catalog_name}.ind.member_profiles;

# COMMAND ----------

# MAGIC %sql
# MAGIC -- Preview Australian data
# MAGIC SELECT 
# MAGIC   member_id, first_name, last_name, date_of_birth, salary_amount, total_balance
# MAGIC FROM ${catalog_name}.aus.member_profiles 
# MAGIC LIMIT 3;

# COMMAND ----------

# MAGIC %sql
# MAGIC -- Test function with real data
# MAGIC SELECT 
# MAGIC   member_id,
# MAGIC   first_name,
# MAGIC   ${catalog_name}.aus.calculate_preservation_age(date_of_birth) as preservation_age,
# MAGIC   ${catalog_name}.aus.project_super_balance(
# MAGIC     total_balance, 
# MAGIC     FLOOR(datediff(current_date(), date_of_birth)/365.25),  -- current age
# MAGIC     ${catalog_name}.aus.calculate_preservation_age(date_of_birth),  -- retirement age
# MAGIC     salary_amount,
# MAGIC     employee_contribution_rate,
# MAGIC     employer_contribution_rate,
# MAGIC     7.0  -- 7% annual return
# MAGIC   ) as projected_balance
# MAGIC FROM ${catalog_name}.aus.member_profiles
# MAGIC LIMIT 3;

# COMMAND ----------

print("✅ Sample data populated successfully!")
print("📊 Sample members created:")
print("   - Australia: 4 members")
print("   - USA: 3 members") 
print("   - UK: 2 members")
print("   - India: 2 members")
print("   - Audit: Sample interaction logged")