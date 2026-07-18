import os
import time
import json
import random

file_path = "../data/elements.json"
daily_file = "daily_elements.json"
def load_elements():
    try:
        with open(file_path, "r") as file:
            data = json.load(file)
        return data['elements']
    except json.JSONDecodeError:
        print(f"[Warning] path: '{file_path}' is corrupted.")

    except FileNotFoundError:
        print(f"[Warning] path: '{file_path}' is not found.")

def save_daily_element(elm):
    with open(daily_file, "w") as file:
        json.dump(elm, file, indent=4)

def load_daily_element():
    if os.path.exists(daily_file):
        with open(daily_file, "r") as file:
            return json.load(file)
    return None

def show_element(elm):
    hypo = "[hypothetical]" if elm['number'] > 118 else ""
    print("-"*50)
    print(f"[1] Daily Element                 : {elm['name']} ({elm['symbol']}) {hypo}")
    print(f"[2] Atomic Number                 : {elm['number']}")
    print(f"[3] Phase                         : {elm['phase']}")
    print(f"[4] Category                      : {elm['category']}")
    print(f"[5] Summary                       : {elm['summary'][:150]}...")
    print("-"*50)

def main():
    elements = load_elements()
    if not elements:
        return

    today_elm = load_daily_element()
    if not today_elm:
        today_elm = random.choice(elements)
        save_daily_element(today_elm)

    print("Your element for today:")
    time.sleep(1)
    show_element(today_elm)

if __name__ == "__main__":
    main()
