def analyze(ticket, logs, code):
    return """
Root Cause:
NullPointerException due to missing null check

Fix:
Add null validation before accessing object

Impacted File:
UserService.java

Priority:
High

Prevention:
Add validation and improve logging
"""
