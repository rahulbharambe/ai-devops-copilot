from analyzer import load_data, detect_pattern
from ai_engine import analyze
from brd_generator import generate_brd
from integrations.servicenow import update_ticket
from integrations.azure_devops import create_task

def run():
    ticket, logs, code = load_data()

    print("🔍 Running AI Analysis...\n")

    result = analyze(ticket, logs, code)

    pattern = detect_pattern(logs)

    brd = generate_brd(result)

    update_ticket(ticket["id"], result)
    create_task("Fix Issue", result)

    print("\n=== AI OUTPUT ===")
    print(result)

    print("\n=== PATTERN DETECTION ===")
    print(pattern)

    print("\n=== BRD ===")
    print(brd)

if __name__ == "__main__":
    run()
