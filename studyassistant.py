import json

class Note:
    def __init__(self, title, content, subject):
        self.title = title
        self.content = content
        self.subject = subject

    def __str__(self):
        return f"Title: {self.title}\nContent: {self.content}\nSubject: {self.subject}"

    def to_dict(self):
        return {
            "Title": self.title,
            "Content": self.content,
            "Subject": self.subject
        }
class StudyAssistant:
    def __init__(self):
        self.notes = []
        self.tasks = []
        self.load_notes()
        self.load_tasks()

    def add_note(self, note):
        self.notes.append(note)
    
    def view_notes(self):
        for index, note in enumerate(self.notes, 1):
            print(index, note)

    def search_notes(self, keyword):
            found = False
            for note in self.notes:
                if keyword.lower() in note.title.lower() or keyword.lower() in note.content.lower():
                    found = True
                    print(note)
            if not found:
                print(f'No notes found matching {keyword}.')

    def notes_to_dict(self):
        result = []
        for note in self.notes:
            new_note = note.to_dict()
            result.append(new_note)
        return result

    def save_notes(self):
            data = self.notes_to_dict()
            with open("notes.json", "w") as file:
                json.dump(data, file)
    
    def load_notes(self):
        with open("notes.json", "r") as file:
            data = json.load(file) 
            for note in data:
                new_note = Note(note["Title"], note["Content"], note["Subject"])
                self.notes.append(new_note)

    def add_task(self,task):
        self.tasks.append(task)

    def view_tasks(self):
        for index, task in enumerate(self.tasks,1):
            print(index, task)

    def delete_tasks(self, task_number):
        pass

    def tasks_to_dict(self):
        result = []
        for task in self.tasks:
            new_task = task.to_dict()
            result.append(new_task)
        return result

    def save_tasks(self):
        data = self.tasks_to_dict()
        with open("tasks.json", "w") as file:
            json.dump(data, file)

    def load_tasks(self):
        try:
            with open("tasks.json", "r") as file:
                data = json.load(file) 
                for task in data:
                    new_task = Task(task["description"], task["completed"])
                    self.tasks.append(new_task)
        except FileNotFoundError:
            pass

    

class Task:
    def __init__(self, description, completed=False): 
        self.description = description
        self.completed = completed

    def mark_complete(self):
        self.completed = True

    def __str__(self):
        status = "x" if self.completed else " "
        return f"[{status}] {self.description}"
    
    def to_dict(self):
        return {
            "description": self.description,
            "completed": self.completed
        }

def main():
    assistant = StudyAssistant()
    while True:
        print('''
==========================
      STUDY ASSISTANT      
===========================
1. Add note
2. View notes
3. Search notes
4. Add task
5. View tasks
6. Complete task
7. Exit
8. Delete task
''')
        choice = input("Choose an option: ")
        if choice == "1":
            title = input("Enter note title: ").strip()
            content = input("Enter note content: ").strip()
            subject = input("Enter note subject: ").strip()

            if not title or not content:
                print("Note title and content cannot be empty.")
            else:
                note = Note(title, content, subject)
                assistant.add_note(note)
                assistant.save_notes()
            

        elif choice == "2":
            assistant.view_notes()

        elif choice == "3":
            keyword = input("Enter search keyword: ")
            assistant.search_notes(keyword.strip())

        elif choice == "4":
            description = input("Enter task description: ").strip()

            if not description:
                print("Task description cannot be empty.")
            else:
                task = Task(description)
                assistant.add_task(task)
                assistant.save_tasks()

        elif choice == "5":
            assistant.view_tasks()

        elif choice == "6":
            try:
                completed = int(input("Enter task number to complete: "))
                if completed <= 0 or completed > len(assistant.tasks):
                    print("Task number not found")
                else:
                    task = assistant.tasks[completed -1]
                    task.mark_complete()
                    assistant.save_tasks()
            except ValueError:
                print("Please enter a valid task number.")
            except IndexError:
                print("Task number not found.")
            
        elif choice == "7":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please choose a number from 1 to 7.")
if __name__ == "__main__":
    main()
    
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

note3 = Note(
    "Python Basics",
    "Learn classes, objects, and methods.",
    "Study Plan"
)

task1 = Task(
   "Practice Python classes"
)

task2 = Task(
    "Review dictionaries"
)

task3 = Task(
    "Build a Python project"
)



assistant = StudyAssistant()

# assistant.add_note(note1)
# assistant.add_note(note2)
# assistant.add_note(note3)

# assistant.add_task(task1)
# assistant.add_task(task2)
# assistant.add_task(task3)

# task1.mark_complete()

# assistant.view_notes()
# assistant.view_tasks()

# assistant.search_notes("stores")
# assistant.search_notes("Java")



