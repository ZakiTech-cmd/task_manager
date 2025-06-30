## How to Run the Project
### 1. Setup (only once)

Create a virtual environment and install dependencies:

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```
### Option 1: Run via Batch Script (Windows)

To start the entire system automatically:

```bash
.\start_all.bat
```

### Option 2: Run via Shell Script (macOS)
```bash
chmod +x start_all.sh
```
```bash
./start_all.sh
```

### Option 2: Run Manually (Step-by-Step)
1. Activate the virtual environment
```bash
venv\Scripts\activate
```
2. Start the API server
```bash
python main.py
```
Or (if your FastAPI app is under a package):
```bash
python -m app.main
```
3. Start the Task Creator
```bash
python task_creator.py
```
4. Start AI Agents
Run this in 2–5 separate terminals:
```bash
python agent_simulator.p
```
Or run them all at once:
```bash
python run_agents.py
```