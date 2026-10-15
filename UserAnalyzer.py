users = [
    {"name": "Alice", "age": 30, "active": True},
    {"name": "Bob", "age": 17, "active": True},
    {"name": "Charlie", "age": 25, "active": False},
    {"name": "David", "age": 40, "active": True}
]
def analyze_user(users):
        output = {
                "total": len(users),
                "active": sum(1 for user in users if user["active"]),
                "adult_active_users": [user["name"] for user in users if user["active"] and user["age"] >= 18]}
        return output


print(analyze_user(users))