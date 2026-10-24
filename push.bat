@echo off
git add .
git commit -m "Auto Update: %date% - %time%"
git push origin main
echo ====================================
echo Done! Changes pushed to GitHub successfully by El-Boss.
echo ====================================