import time
from app.analyzer import load_data, detect_pattern
from ai_engine import analyze
from brd_generator import generate_brd
from integrations.servicenow import update_ticket
from integrations.azure_devops import create_task

def listen_for_ticket():
    print("🟢 Listening for ServiceNow tickets...\n")
    time.sleep(2)  # simulate wait
    return True

def run_pipeline():
    ticket, logs, code = load_data()

    print("⚡ Trigger received from ServiceNow\n")

    result = analyze(ticket, logs, code)
    pattern = detect_pattern(logs)
    brd = generate_brd(result)

    update_ticket(ticket["id"], result)
    create_task("Fix Issue", result)

    print("\n=== AI OUTPUT ===")
    print(result)

    print("\n=== PATTERN DETECTION ===")
    print(pattern)

    print("\n=== RECOMMENDATION ===")
    print("Consider refactoring frequently failing components.")

    print("\n=== BRD ===")
    print(brd)

    print("\n=== SYSTEM NOTE ===")
    print("This is a simulated AI-driven DevOps automation pipeline.")

if __name__ == "__main__":
    if listen_for_ticket():
        run_pipeline()
