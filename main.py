## Problem 1
# Fetch users which are active and age >= 18
users = [
    {"name": "Alice", "age": 30, "active": True},
    {"name": "Bob", "age": 17, "active": True},
    {"name": "Charlie", "age": 25, "active": False},
    {"name": "David", "age": 40, "active": True}
]

# Solution 1
for user in users: 
    if user["active"] is True and user["age"] >= 18:
        print(user["name"]);

# Solution 2
user = [user["name"] for user in users if user["active"] is True and user["age"]>= 18]

print(user);

## Problem 2
# return the words frequency
text = "python is great and python is powerful"
words = text.split()
frequency = {}
for word in words:
    if word in frequency:
        frequency[word] = frequency[word] + 1;
    else:
        frequency[word] = 1;

print(frequency)