import sys
import os
import time

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from study_element import load_elements

def show_period_elements(elements, period_number):
    found = False
    print("-"*50)
    print(f"\n[+] Elements in Period {period_number}")

    for elm in elements:
        if str(elm.get('period')) == str(period_number):
            found = True
            hypo = " [hypothetical]" if int(elm['number']) > 118 else ""
            print(f"{elm['number']:>3} {elm['name']} ({elm['symbol']}){hypo}")

    if not found:
        print(f"\nNo elements found in period {period_number}.")
    print("-"*50)

def main():
    elements = load_elements()
    if not elements:
        return

    while True:
        try:
            period_input = input("Enter period number (1-8) or 'q' to 'quit': ").strip()
            if period_input.lower() in ("q", "quit"):
                break
            if not period_input:
                continue
            if not period_input.isdigit() or not (1 <= int(period_input) <= 8):
                print("\n[Warning] Enter a valid period number between 1-8.")
                continue

            print("Loading elements...")
            time.sleep(1)
            show_period_elements(elements, period_input)

        except (KeyboardInterrupt, EOFError):
            break

if __name__ == "__main__":
    main()
