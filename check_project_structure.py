#!/usr/bin/env python3
"""
Project Structure Verification Script
Run this to check if all required files have been created
"""

import os
import sys
from pathlib import Path

# Expected file structure
EXPECTED_FILES = [
    # Root files
    "requirements.txt",
    "README.md", 
    ".gitignore",
    
    # App files
    "app/main.py",
    "app/pages/1_⚙️_Configuration.py",
    "app/pages/2_��_Chat.py", 
    "app/pages/3_📊_Analytics.py",
    "app/components/ui_components.py",
    "app/components/progress_bars.py",
    "app/components/country_themes.py",
    
    # Agent files
    "agent/core/agent_orchestrator.py",
    "agent/core/planner.py",
    "agent/core/executor.py",
    "agent/core/synthesizer.py",
    "agent/core/judge.py",
    "agent/tools/base_tool.py",
    "agent/tools/pension_calculators/aus_super_calculator.py",
    "agent/tools/pension_calculators/usa_pension_calculator.py",
    "agent/tools/pension_calculators/uk_pension_calculator.py",
    "agent/tools/pension_calculators/india_pension_calculator.py",
    "agent/prompts/system_prompts.py",
    "agent/validation/input_validator.py",
    
    # Config files
    "config/settings.py",
    "config/country_configs.py",
    
    # Utils files
    "utils/db_utils.py",
    "utils/mlflow_utils.py", 
    "utils/callback_handlers.py",
    
    # Test files
    "tests/test_agent.py",
    "tests/test_tools.py",
    
    # Notebook files
    "notebooks/01_Setup_Catalog_and_Schemas.py",
    "notebooks/02_Create_Member_Tables.py",
    "notebooks/03_Create_UC_Functions.py",
    "notebooks/04_Create_Audit_Tables.py",
    "notebooks/05_Populate_Sample_Data.py",
]

# Expected directories (should have __init__.py)
EXPECTED_DIRS = [
    "app",
    "app/pages",
    "app/components", 
    "agent",
    "agent/core",
    "agent/tools",
    "agent/tools/pension_calculators",
    "agent/tools/data_retrieval",
    "agent/prompts",
    "agent/validation",
    "data",
    "data/models",
    "data/audit", 
    "data/schemas",
    "config",
    "utils",
    "tests",
    "notebooks",
    "deployment",
]

def check_project_structure():
    """Check if all expected files and directories exist"""
    print("🔍 Checking project structure...")
    print("=" * 60)
    
    # Get current directory
    current_dir = Path.cwd()
    project_name = current_dir.name
    print(f"Project: {project_name}")
    print(f"Location: {current_dir}")
    print()
    
    # Check directories
    print("📁 Checking directories...")
    missing_dirs = []
    for dir_path in EXPECTED_DIRS:
        full_path = current_dir / dir_path
        if full_path.exists() and full_path.is_dir():
            print(f"  ✅ {dir_path}/")
            
            # Check for __init__.py in Python packages
            if dir_path not in ["notebooks", "deployment"]:  # These don't need __init__.py
                init_file = full_path / "__init__.py"
                if not init_file.exists():
                    print(f"     ⚠️  Missing: {dir_path}/__init__.py")
        else:
            print(f"  ❌ {dir_path}/")
            missing_dirs.append(dir_path)
    
    print()
    
    # Check files
    print("📄 Checking files...")
    missing_files = []
    for file_path in EXPECTED_FILES:
        full_path = current_dir / file_path
        if full_path.exists() and full_path.is_file():
            # Check if file has content
            file_size = full_path.stat().st_size
            status = "✅" if file_size > 0 else "⚠️ (empty)"
            print(f"  {status} {file_path} ({file_size} bytes)")
        else:
            print(f"  ❌ {file_path}")
            missing_files.append(file_path)
    
    print()
    print("=" * 60)
    
    # Summary
    total_expected = len(EXPECTED_DIRS) + len(EXPECTED_FILES)
    total_found = (len(EXPECTED_DIRS) - len(missing_dirs)) + (len(EXPECTED_FILES) - len(missing_files))
    
    print("📊 SUMMARY:")
    print(f"Directories: {len(EXPECTED_DIRS) - len(missing_dirs)}/{len(EXPECTED_DIRS)} created")
    print(f"Files: {len(EXPECTED_FILES) - len(missing_files)}/{len(EXPECTED_FILES)} created") 
    print(f"Overall: {total_found}/{total_expected} ({total_found/total_expected*100:.1f}%)")
    print()
    
    if missing_dirs:
        print("🚨 Missing directories:")
        for dir_path in missing_dirs:
            print(f"  - {dir_path}/")
    
    if missing_files:
        print("🚨 Missing files:")
        for file_path in missing_files:
            print(f"  - {file_path}")
    
    if not missing_dirs and not missing_files:
        print("🎉 All files and directories created successfully!")
        print("Next steps:")
        print("1. Populate the notebooks with the provided code")
        print("2. Run them in Databricks in order (01-05)")
        print("3. Then populate the Python files")
    else:
        print(f"\n💡 Run the touch commands again to create missing items")

def get_missing_files_commands():
    """Generate touch commands for missing files"""
    current_dir = Path.cwd()
    missing_commands = []
    
    for file_path in EXPECTED_FILES:
        full_path = current_dir / file_path
        if not full_path.exists():
            # Create parent directories first
            parent_dir = full_path.parent
            if not parent_dir.exists():
                missing_commands.append(f"mkdir -p {parent_dir}")
            missing_commands.append(f"touch {file_path}")
    
    return missing_commands

if __name__ == "__main__":
    check_project_structure()
    
    # Optional: Show commands to fix missing files
    current_dir = Path.cwd()
    missing_files = [f for f in EXPECTED_FILES if not (current_dir / f).exists()]
    
    if missing_files:
        print("\n🔧 To create missing files, run these commands:")
        print("```bash")
        commands = get_missing_files_commands()
        for cmd in commands:
            print(cmd)
        print("```")
