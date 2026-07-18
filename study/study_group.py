import time
import json
import os
from study_element import load_elements
from study_element import file_path


def show_group_elements(elements, group_number):
    found = False
    print("-"*50)
    print(f"\n[+]  Elements in Group {group_number}")

    for elm in elements:
        if str(elm['group']) == str(group_number):
            found = True

            hypo = "[hypothetical]" if elm['number'] > 118 else ""
            print(f"{elm['number']:>3}  {elm['name']} ({elm['symbol']}){hypo}")

    if not found:
            print(f"Not elements found in Group {group_number}.")
    print("-"*50)

def main():
    elements = load_elements()

    if not elements:
        print("No elements loaded. Program stop.")
        return

    while True:
        try:
            group_input = input("Enter group number (1-18) or 'q' to 'quit': ").strip()

            if group_input.lower() in ("q", "quit"):
                print("Bye bye bro")
                break

            if not group_input:
                print("\n[Warning] Element group number can't be empty.")
                continue

            if not group_input.isdigit():
                print("\n[Warning]  Enter a valid group number between 1-18.")
                continue

            group_number = int(group_input)
            if 1 > group_number or group_number > 18:
                print("\n[Warning] Valid groups are 1-18 only.")
                continue

            print("Loading elements...")
            time.sleep(1.8)
            show_group_elements(elements, group_number)

        except KeyboardInterrupt:
            print("\n[Error] Keyboard interrupt detected. Exiting...")
            break
        except EOFError:
            print("\n[Error] EOF reached. Exiting...")
            break

if __name__ == "__main__":
    main()
