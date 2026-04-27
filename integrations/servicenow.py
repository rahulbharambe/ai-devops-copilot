def update_ticket(ticket_id, analysis):
    response = {
        "ticket_id": ticket_id,
        "status": "Updated",
        "analysis_summary": analysis[:200]
    }
    print("\n[ServiceNow API Response]")
    print(response)
