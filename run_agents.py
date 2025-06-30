import subprocess
import random
import time

NUM_AGENTS = random.randint(2, 5)
print(f" Launching {NUM_AGENTS} AI Agents...")

processes = []

for i in range(NUM_AGENTS):
    print(f" Starting Agent {i + 1}")
    proc = subprocess.Popen(["python", "agent_simulator.py"])
    processes.append(proc)
    time.sleep(1)

try:
    for proc in processes:
        proc.wait()
except KeyboardInterrupt:
    print("Terminating agents...")
    for proc in processes:
        proc.terminate()
