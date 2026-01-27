"""
Docstring for ui.menu
    main menu file
"""
def main_menu():
    """
    Docstring for main_menu
        main menu function
    """
    print("╔====== Main Menu ======╗")
    print("   1. New Game\n   2. Load Game\n   3. Quit")
    print("╚=======================╝")

    choice = input("> ")

    if choice == "1":
        return "new"

    elif choice == "2":
        return "load"

    elif choice == "3":
        return "quit"

    return main_menu()
