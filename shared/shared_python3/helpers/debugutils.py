from collections import defaultdict

def display_defaultdict(map:defaultdict):
    for key, value in map.items():
        print(f"DEBUG: key={key} value={value}")