import json

def load_data():
    with open("data/ticket.json") as f:
        ticket = json.load(f)

    with open("data/logs.txt") as f:
        logs = f.read()

    with open("data/code_sample.java") as f:
        code = f.read()

    return ticket, logs, code


def detect_pattern(logs):
    issues = {}

    for line in logs.split("\n"):
        if "Exception" in line:
            file = line.split("at")[-1].strip()
            issues[file] = issues.get(file, 0) + 1

    if not issues:
        return "No major patterns detected"

    most_common = max(issues, key=issues.get)

    return f"Most issues found in: {most_common}"
