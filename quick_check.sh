#!/bin/bash
echo "🔍 Quick check..."
echo "📁 Directories found:"
ls -d app/ agent/ config/ utils/ tests/ notebooks/ deployment/ 2>/dev/null || echo "Some directories missing"
echo "📄 Key files:"
ls app/main.py app/pages/*.py requirements.txt 2>/dev/null | wc -l | xargs echo "Files found:"
