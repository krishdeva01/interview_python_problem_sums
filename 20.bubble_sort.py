data = [
    {"city": "bengaluru", "zipcode": 4002923, "provider": "jio"},
    {"city": "mumbai", "zipcode": 400001, "provider": "airtel"},
    {"city": "bengaluru", "zipcode": 4001001, "provider": "airtel"},
    {"city": "bengaluru", "zipcode": 4002923, "provider": "airtel"},
    {"city": "Ahmedabad", "zipcode": 4002920, "provider": "airtel"},
    {"city": "Ahmedabad", "zipcode": 4002921, "provider": "jio"},
]

# Bubble sort based on city, then zipcode, then provider
n = len(data)
for i in range(n):
    for j in range(0, n - i - 1):
        a = data[j]
        b = data[j + 1]
        if (a["city"], a["zipcode"], a["provider"]) > (b["city"], b["zipcode"], b["provider"]):
            data[j], data[j + 1] = data[j + 1], data[j]

for item in data:
    print(item)
