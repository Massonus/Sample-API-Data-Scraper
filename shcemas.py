from datetime import datetime

def format_date(date):
    return date.strftime("%Y-%m-%d %H:%M:%S") if isinstance(date, datetime) else None

def individual_data(todo):
    return {
        "id": str(todo["_id"]),
        "title": todo["title"],
        "description": todo["description"],
        "status": todo["is_completed"],
        "created_at": format_date(todo.get("creation")),
        "updated_at": format_date(todo.get("updated_at"))
    }

def todos_data(todos):
    return [individual_data(todo) for todo in todos]
