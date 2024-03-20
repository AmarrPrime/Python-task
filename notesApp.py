from datetime import datetime, date
import json
import uuid

class Note:
    def __init__(self, id, name, content, createDate):
        self.id = id
        self.name = name
        self.content = content
        self.createDate = createDate

    def print(self):
        print("id:{0}   Name:{1}    CreateDate:{3}  content:{2} ".format(self.id,self.name,self.content,self.createDate))

class NoteService:

    filename = "NotesList.txt"
    dateFormat = "%Y-%m-%d"

    def __init__(self):
        self.notes = {}

    def add(self):
        name = input("Введите название записи: ")
        content = input("Введите тело заметки: ")
        id = str(uuid.uuid1())
        note = Note(id, name, content, date.today().strftime(self.dateFormat))
        self.notes[id] = note

    def delete(self):
        id = input("Введите id заметки на удаление: ")
        del self.notes[id]
    
    def edit(self):
        id = input("Введите id заметки на редактирование: ")
        name = input("Введите название записи: ")
        content = input("Введите тело заметки: ")
        self.notes[id].name = name
        self.notes[id].content = content

    def showList(self):
        for key in self.notes:
            self.notes[key].print()

    def filterByDate(self):
        dateString = input("Введите дату в формате гггг-мм-дд : ")
        for key in self.notes:
            if self.notes[key].createDate == dateString:
                self.notes[key].print()

    def writeToFile(self):
        file = open(self.filename,"w")
        notes = []
        for key in self.notes:
            note = self.notes[key].__dict__
            notes.append(note)
        fileContent = json.dumps(notes)
        file.write(fileContent)
        file.close()
    
    def readFromFile(self):
        file = open(self.filename,"r+")
        filecontent = file.read()
        file.close()
        self.notes = {}
        if len(filecontent) > 0:
            notes = json.loads(filecontent)
            for note in notes:
                self.notes[note["id"]] = Note(**note)

service = NoteService()
service.readFromFile()
while True:
    command = input("Введите команду из перечисленых (add, delete, edit, show, filter, exit): ")
    if command == "add":
        service.add()
    elif command == "delete":
        service.delete()
    elif command == "edit":
        service.edit()
    elif command ==  "show":
        service.showList()
    elif command ==  "filter":
        service.filterByDate()
    else:
        break
service.writeToFile()
