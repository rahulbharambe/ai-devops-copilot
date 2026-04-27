from openai import OpenAI

client = OpenAI(api_key="YOUR_API_KEY")

def analyze(ticket, logs, code):
    try:
        prompt = f"""
        You are an AI DevOps assistant.

        Analyze the following:

        Ticket:
        {ticket}

        Logs:
        {logs}

        Code:
        {code}

        Provide structured output:

        Root Cause:
        Fix:
        Impacted File:
        Priority:
        Prevention:
        """

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}]
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"Error occurred: {str(e)}"
