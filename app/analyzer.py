def detect_pattern(logs):
    issues = {}

    lines = logs.split("\n")

    for line in lines:
        if "Exception" in line:
            file = line.split("at")[-1].strip()
            issues[file] = issues.get(file, 0) + 1

    if not issues:
        return "No major patterns detected"

    most_common = max(issues, key=issues.get)

    return f"Most issues found in: {most_common} (occurrences: {issues[most_common]})"
