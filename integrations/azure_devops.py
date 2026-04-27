def create_task(title, description):
    task = {
        "title": title,
        "description": description[:200],
        "status": "Created"
    }
    print("\n[Azure DevOps Task Created]")
    print(task)
