import json

def load_data():
    with open("data/ticket.json") as f:
        ticket = json.load(f)

    with open("data/logs.txt") as f:
        logs = f.read()

    with open("data/code_sample.java") as f:
        code = f.read()

    return ticket, logs, code
