class Note:
    def __init__(self, title, content, subject):
        self.title = title
        self.content = content
        self.subject = subject

    def __str__(self):
        return f"Title: {self.title}\nContent: {self.content}\nSubject: {self.subject}"

class StudyAssistant:
    def __init__(self):
        self.notes = []

    def add_note(self, note):
        self.notes.append(note)

    def view_notes(self):
        for index, note in enumerate(self.notes, 1):
            print(index, note)

    def search_notes(self, keyword):
        found = False
        for note in self.notes:
            if keyword.lower() in note.title.lower():
                found = True
                print(note)
        if not found:
            print(f'No notes found matching {keyword}.')

class Task:
    def __init__(self, description): 
        self.description = description
        self.completed = False

    def mark_complete(self):
        self.completed = True

    def __str__(self):
        status = "x" if self.completed else " "
        return f"[{status}] {self.description}"


task1 = Task("Practice Python classes")

print(task1)

task1.mark_complete()

print(task1)


note1 = Note(
    "Python Dictionaries",
    "A dictionary stores data in key-value pairs.",
    "Python"
)

note2 = Note(
    "Python Classes",
    "A class is a blueprint for creating objects.",
    "Python"
)

assistant = StudyAssistant()

# assistant.add_note(note1)
# assistant.view_notes(note1)


# print(assistant.notes)

# print(note1)