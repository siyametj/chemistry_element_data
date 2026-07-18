import json
import time
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(BASE_DIR, "..", "data", "elements.json")

def load_elements():
    try:
        with open(file_path, "r") as file:
            data =  json.load(file)
        return data['elements']

    except json.JSONDecodeError:
        print(f"[Warning] path: '{file_path}' is corrupted.")

    except FileNotFoundError:
        print(f"[Warning] path: '{file_path}' is not found.")

def search_elements(elements, query):
    query = query.strip().lower()
    result = []

    for elm in elements:
        if (
            query in elm['name'].lower() or
            query in elm['symbol'].lower() or
            query == str(elm['number'])
        ):
            result.append(elm)

    return result

def show_result(results):
    if not results:
        print("[+] No elements found matching your search")
        return

    print(f"Found: {len(results)} element(s):")
    print("-"*50)

    for elm in results:
        hypo = "[hypothetical]" if elm['number'] > 118 else ""
        print(f"{elm['number']:>3}  {elm['name']} ({elm['symbol']}) {hypo}")
    print("-"*50)

def main():
    elements = load_elements()

    if not elements:
        return

    while True:
        try:
            query = input("Enter keyword (name/symbol/number) or 'q' to quit: ").strip()
            if query.lower() in ('q', 'quit'):
                print("Bye Bye Bro")
                break

            print("Searching elements...")
            time.sleep(1.8)
            results = search_elements(elements, query)

            show_result(results)

        except EOFError:
            print("\n[Error] 'EOF Error' reached. Program stop.")
            break

        except KeyboardInterrupt:
            print(f"\n[Error] Keyboard interrupt reached. Program stop.")
            break



if __name__ == "__main__":
    main()
