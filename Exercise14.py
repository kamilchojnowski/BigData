items = {"item 1": 45.50, "item 2":35, "item 3": 41.30, "item 4":55, "item 5 ": 24}

top_items = 3

for i in range(top_items):
    max_val = 0
    key = "invalid_key"
    for k, v in items.items():
        if v > max_val:
            max_val = v
            key = k
    to_display = items.pop(key)
    print(key, to_display)
