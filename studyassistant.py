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


note1 = Note(
    "Python Dictionaries",
    "A dictionary stores data in key-value pairs.",
    "Python"
)

assistant = StudyAssistant()

assistant.add_note(note1)

print(assistant.notes)

print(note1)