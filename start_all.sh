#!/bin/bash

echo "Activating virtual environment..."
source venv/bin/activate

echo "Starting API Server..."
osascript -e 'tell app "Terminal"
    do script "source venv/bin/activate && python app/main.py"
end tell'

sleep 2

echo "Starting Task Creator..."
osascript -e 'tell app "Terminal"
    do script "source venv/bin/activate && python task_creator.py"
end tell'

echo "Launching AI Agents..."
osascript -e 'tell app "Terminal"
    do script "source venv/bin/activate && python run_agents.py"
end tell'
