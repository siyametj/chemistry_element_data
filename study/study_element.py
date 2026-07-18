import json
import time

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(BASE_DIR, "../data/elements.json")

def load_elements():
    try:
        with open(file_path, "r") as file:
            data =  json.load(file)
        return data['elements']

    except json.JSONDecodeError:
        print(f"[Warning] path: '{file_path}' is corrupted.")

    except FileNotFoundError:
        print(f"[Warning] path: '{file_path}' is not found.")

def find_element(elements, query):
    query = query.lower().strip()

    for elm in elements:
        if (elm['name'].lower() == query
        or elm['symbol'].lower() == query
        or (str(elm["number"]) == query)):
            return elm

    return None

def show_element(elm):
    print("-"*50)
    print(f"[1] Name                          : {elm['name']} ({elm['symbol']})")
    print(f"[2] Atomic Number                 : {'___' if elm['number'] == 'null' else elm['number']}")
    print(f"[3] Atomic Mass                   : {'___' if elm['atomic_mass'] == 'null' else elm['atomic_mass']}")
    print(f"[4] Phase                         : {'___' if elm['phase'] == 'null' else elm['phase']}")
    print(f"[5] Category                      : {'___' if elm['category'] == 'null' else elm['category']}")
    print(f"[6] Group Number                  : {'___' if elm['group'] == 'null' else elm['group']}")
    print(f"[7] Period Number                 : {'___' if elm['period'] == 'null' else elm['period']}")
    print(f"[8] Block                         : {'___' if elm['block'] == 'null' else elm['block']}")
    print(f"[9] Density                       : {'___' if elm['density'] == 'null' else elm['density']}")
    print(f"[10] Melt Point                   : {'___' if elm['melt'] == 'null' else elm['melt']}")
    print(f"[11] Boil Point                   : {'___' if elm['boil'] == 'null' else elm['boil']}")
    print(f"[12] Molar Heat                   : {'___' if elm['molar_heat'] == 'null' else elm['molar_heat']}")
    print(f"[13] Electron Configuration       : {'___' if elm['electron_configuration'] == 'null' else elm['electron_configuration']}")
    print(f"[14] Shells                       : {'___' if elm['shells'] == 'null' else elm['shells']}")
    print("-"*50)
    print(f"[1] Appearance                    : {'___' if elm['appearance'] == 'null' else elm['appearance']}")
    print(f"[2] Discovered By                 : {'___' if elm['discovered_by'] == 'null' else elm['discovered_by']}")
    print(f"[3] Named By                      : {'___' if elm['named_by'] == 'null' else elm['named_by']}")
    print(f"[4] Ionization Energies           : {'___' if elm['ionization_energies'] == 'null' else elm['ionization_energies']}")
    print(f"[5] Electron Config. Semantic     : {'___' if elm['electron_configuration_semantic'] == 'null' else elm['electron_configuration_semantic']}")
    print("-"*50)
    print(f"[+] Summary: \n{'___' if elm['summary'] == 'null' else elm['summary']}")
    print("-"*50)

def main():
    elements = load_elements()

    while True:
        try:
            query = input("Enter element 'name' or 'symbol' or 'number': ")

            if not query:
                print("\n[Warning] Element name/symbol/number can't be empty.")
                continue

        except EOFError:
            print("\n[Error] 'EOF Error' reached. Program stop.")
            break

        except KeyboardInterrupt:
            print(f"\n[Error] Keyboard interrupt reached. Program stop.")
            break


        break

    element = find_element(elements, query)

    if element:
        print("\n[success] Good element. Element loading...")
        time.sleep(1.8)
        show_element(element)
    else:
        print("Sorry, element not found.")

if __name__ == "__main__":
    main()
