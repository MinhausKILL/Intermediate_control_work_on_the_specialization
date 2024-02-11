import csv
import easygui
from datetime import datetime

def save_notes(notes):
    with open('notes.csv', 'w', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['ID', 'Title', 'Body', 'Date/Time'])

        for note in notes:
            writer.writerow([note['id'], note['title'], note['body'], note['date_time']])
    easygui.msgbox('Notes saved successfully', title='Success')

def read_notes():
    notes = []
    try:
        with open('notes.csv', 'r') as file:
            reader = csv.reader(file, delimiter=';')
            next(reader)  # Skip header
            for row in reader:
                note = {'id': row[0], 'title': row[1], 'body': row[2], 'date_time': row[3]}
                notes.append(note)
    except FileNotFoundError:
        pass
    return notes

def show_notes(notes):
    for note in notes:
        print(f"ID: {note['id']} - {note['title']} ({note['date_time']})")
        print(note['body'])
        print()

def add_note():
    title = easygui.enterbox('Enter note title:', title='Add Note')
    body = easygui.enterbox('Enter note body:', title='Add Note')
    date_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return {'id': str(len(notes) + 1), 'title': title, 'body': body, 'date_time': date_time}

def edit_note(note):
    title = easygui.enterbox('Edit note title:', title='Edit Note', default=note['title'])
    body = easygui.enterbox('Edit note body:', title='Edit Note', default=note['body'])
    note['title'] = title
    note['body'] = body
    note['date_time'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return note

def delete_note():
    id = easygui.enterbox('Enter note ID to delete:', title='Delete Note')
    for note in notes:
        if note['id'] == id:
            notes.remove(note)
            return
    easygui.msgbox('Note not found', title='Error')

notes = read_notes()

while True:
    choice = easygui.buttonbox('Choose an action:', choices=['Add Note', 'Edit Note', 'Save Notes', 'Show all notes', 'Delete Note', 'Exit'])

    if choice == 'Add Note':
        note = add_note()
        notes.append(note)
    elif choice == 'Edit Note':
        id = easygui.enterbox('Enter note ID to edit:', title='Edit Note')
        for note in notes:
            if note['id'] == id:
                edited_note = edit_note(note)
                notes.remove(note)
                notes.append(edited_note)
                break
        else:
            easygui.msgbox('Note not found', title='Error')
    elif choice == 'Delete Note':
        delete_note()
    elif choice == 'Save Notes':
        save_notes(notes)
    elif choice == 'Show all notes':
        show_notes(notes)
    else:
        break