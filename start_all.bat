@echo off
echo Activating virtual environment...
call venv\Scripts\activate.bat

echo Starting API Server...
start cmd /k "python app/main.py"

timeout /t 2 >nul

echo Starting Task Creator...
start cmd /k "python task_creator.py"

echo Launching AI Agents...
start cmd /k "python run_agents.py"
