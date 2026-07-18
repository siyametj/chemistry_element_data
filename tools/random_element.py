import sys
import os
import time
import random

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from search import load_elements

def show_elements(elm):
    hypo = " [hypothetical]" if elm['number'] > 118 else ""
    print("-"*50)
    print(f"[1] Name                          : {elm['name']} ({elm['symbol']}){hypo}")
    print(f"[2] Atomic Number                 : {elm['number']}")
    print(f"[3] Atomic Mass                   : {elm['atomic_mass']}")
    print(f"[4] Phase                         : {elm['phase']}")
    print(f"[5] Category                      : {elm['category']}")
    print("-"*50)

def main():
    elements = load_elements()
    if not elements:
        print("No elements data available.")
        return

    while True:
        try:
            cmd = input("Press Enter for random element or 'q' to quit: ").strip()
            if cmd.lower() in ('q', 'quit'):
                break

            elm = random.choice(elements)
            print("Picking a random element...")
            time.sleep(0.5)
            show_elements(elm)

        except (EOFError, KeyboardInterrupt):
            break

if __name__ == "__main__":
    main()
