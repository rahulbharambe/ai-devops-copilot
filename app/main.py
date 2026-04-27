from analyzer import load_data
from ai_engine import analyze
from brd_generator import generate_brd
from integrations.servicenow import update_ticket
from integrations.azure_devops import create_task

def run():
    ticket, logs, code = load_data()

    result = analyze(ticket, logs, code)
    brd = generate_brd(result)

    update_ticket(ticket["id"], result)
    create_task("Fix Issue", result)

    print("\n=== OUTPUT ===")
    print(result)
    print("\n=== BRD ===")
    print(brd)

if __name__ == "__main__":
    run()
