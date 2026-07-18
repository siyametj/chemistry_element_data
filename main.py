import os
import time

def clear():
    os.system("clear" if os.name == "posix" else "cls")

def pasuse():
    input("\nPress Enter to continue...")

def run(cmd):
    clear()
    os.system(cmd)
    pasuse()

def main():
    while True:
        clear()

        print("-"*50)
        print("CHEMISTRY ELEMENT STUDY - MAIN MENU")
        print("-"*50)

        print("1. Study Element (by name / symbol / number)")
        print("2. Study by Group")
        print("3. Study by Period")
        print("4. Compare Two Elements")
        print("5. Search Elements")
        print("6. Random Element")
        print("0. Exit")
        print("-"*50)

        while True:
            try:
                choice = input("Choose option: ").strip()

                if not choice:
                    continue

                if not choice.isdigit():
                    continue

                match choice:
                    case "1":
                        run("python3 study/study_element.py")
                        break

                    case "2":
                        run("python3 study/study_group.py")
                        break

                    case "3" :
                        run("python3 study/study_period.py")
                        break

                    case "4" :
                        run("python3 study/study_compare.py")
                        break

                    case "5" :
                        run("python3 tools/search.py")
                        break

                    case "6" :
                        run("python3 tools/random_element.py")
                        break
                    
                    case "0":
                        print("Bye Bye Bro.")
                        time.sleep(1.8)
                        exit()

                    case _:
                        print("Invalid choice.")
                        time.sleep(1.8)

            except KeyboardInterrupt:
                print("\n[Error] Keyboard interrupt detected. Exiting...")
                break
            except EOFError:
                print("\n[Error] EOF reached. Exiting...")
                break

if __name__ == "__main__":
    main()
