from zad1 import Note, NoteBook
import sys
class Menu:
    def __init__(self):
        self.notebook = NoteBook()
        self.options = {"1": self.show_notes,
                        "2": self.search_notes,
                        "3": self.add_note,
                        "4": self.modify_note,
                        "5": self.quit}

    def show_menu(self):
        print("""
Menu natatnika:
1 - Pokaż wszystkie notatki
2 - Wyszukaj notatki
3 - Dodaj notatkę
4 - Zmdyfikuj notatkę
5 - Zakończ program
        """)

    def run(self):
        while True:
            self.show_menu()
            choice = input("Wybierz opcje: ")
            action = self.options.get(choice)
            if action:
                action()
            else:
                print(f"{choice} - to nie jest poprawny wybór!")

    def show_notes(self, notes = None):
        if not notes:
            notes = self.notebook.notes
        for note in notes:
            print(note)

    def search_notes(self):
        phraze = input("Podaj frazę której szukasz: ")
        notes = self.notebook.search(phraze)
        self.show_notes(notes)

    def add_note(self):
        text = input("Podaj text nowej notatki: ")
        self.notebook.add_note(text)
        print("Stworzono nową notatkę!")

    def modify_note(self):
        Id = int(input("Podaj id notatki, którą chcesz zmodyfikować: "))
        new_text = input("Podaj nowy text notatki: ")
        new_tag = input("Podaj nową etykiete notatki: ")
        if new_text:
            self.notebook.modify_text(Id, new_text)
        if new_tag:
            self.notebook.modify_tag(Id, new_tag)

    def quit(self):
        print("Koniec pracy z notatnikiem.")
        sys.exit(0)


Menu().run()

