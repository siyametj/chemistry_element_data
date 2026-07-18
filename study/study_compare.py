import sys
import os
import time

# Add parent directory to sys.path to allow sibling files to see each other
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from study_element import load_elements

def show_compare(elements, first_query, second_query):
    first_elm = None
    second_elm = None

    for elm in elements:
        if (str(elm['number']) == str(first_query) or
            elm['symbol'].lower() == str(first_query).lower() or
            elm['name'].lower() == str(first_query).lower()):
            first_elm = elm
        if (str(elm['number']) == str(second_query) or
            elm['symbol'].lower() == str(second_query).lower() or
            elm['name'].lower() == str(second_query).lower()):
            second_elm = elm

    if not first_elm or not second_elm:
        print("[Error] One or both elements not found")
        return

    print('-'*50)
    print(f"Comparing {first_elm['name']}({first_elm['symbol']}) VS {second_elm['name']}({second_elm['symbol']})")
    print('-'*50)

    fields = ['number', 'atomic_mass', 'phase', 'category', 'group', 'period', 'density', 'melt', 'boil']
    for fl in fields:
        first_val = first_elm.get(fl, "N/A")
        second_val = second_elm.get(fl, "N/A")
        print(f"{fl.capitalize():<15}: {str(first_val):<20} | {second_val}")
    print("-"*50)

def main():
    elements = load_elements()
    if not elements:
        print("No elements loaded. Program stop.")
        return

    while True:
        try:
            first_query = input("Enter first element (name/symbol/number) or 'q' to quit: ").strip()
            if not first_query: continue
            if first_query.lower() in ('q', 'quit'): break

            second_query = input("Enter second element (name/symbol/number) or 'q' to quit: ").strip()
            if not second_query: continue
            if second_query.lower() in ('q', 'quit'): break

            print("Comparing elements...")
            time.sleep(1)
            show_compare(elements, first_query, second_query)

        except (KeyboardInterrupt, EOFError):
            print("\nExiting comparison...")
            break

if __name__ == "__main__":
    main()
