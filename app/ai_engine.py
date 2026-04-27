import openai

openai.api_key = "YOUR_API_KEY"

def analyze(ticket, logs, code):
    prompt = f"""
    Analyze:

    Ticket: {ticket}
    Logs: {logs}
    Code: {code}

    Give:
    - Root Cause
    - Fix
    - File Name
    - Prevention
    - Priority
    """

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )

    return response['choices'][0]['message']['content']
