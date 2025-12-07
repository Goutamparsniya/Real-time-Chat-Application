candidates = [
    {"name": "John", "height": 175, "weight": 70, "eyesight": 20},
    {"name": "Alice", "height": 160, "weight": 55, "eyesight": 18},
    {"name": "Bob", "height": 185, "weight": 80, "eyesight": 22},
]

criteria = "height"
sorted_candidates = sorted(candidates, key=lambda x: x[criteria])
for candidate in sorted_candidates:
    print(candidate)
