import datetime

class Note:
    ID = 0
    def __init__(self, text, tag):
        self.text = text
        self.tag = tag
        type(self).ID += 1
        self.ID = type(self).ID
        self.date = datetime.date.today()

    def __str__(self):
        s = "Notatka:\n"
        for v, k in self.__dict__.items():
            s += f"{v}: {k}\n"
        return s

    def match(self, phraze):
        return phraze in self.text or phraze in self.tag

class NoteBook:
    def __init__(self):
        self.notes = []

    def add_note(self, text, tag = ""):
        self.notes.append(Note(text, tag))

    def modify_text(self, Id, new_text):
        for note in self.notes:
            if note.ID == Id:
                note.text = new_text
                break
            else:
                print(f"Brak notatki")

    def modify_tag(self, Id, new_tag):
        for note in self.notes:
            if note.ID == Id:
                note.tag = new_tag
                break
            else:
                print(f"Brak notatki")

    def search(self, phraze):
        # notes = []
        # for note in self.notes:
        #     if note.match(phraze):
        #         notes.append(note)
        # return notes
        return [note for note in self.notes if note.match(phraze)]

