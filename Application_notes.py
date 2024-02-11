import csv
import os
import easygui
from datetime import datetime

notes_file = 'notes.csv'

def load_notes():
    notes = []
    if os.path.exists(notes_file):
        with open(notes_file, 'r', newline='') as file:
            reader = csv.reader(file, delimiter=';')
            for row in reader:
                notes.append({'id': row[0], 'title': row[1], 'body': row[2], 'date': row[3]})
    return notes

def save_notes(notes):
    with open(notes_file, 'w', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        for note in notes:
            writer.writerow([note['id'], note['title'], note['body'], note['date']])

def show_notes(notes):
    for note in notes:
        print(f"ID: {note['id']} - {note['title']} ({note['date']})")
        print(note['body'])
        print()

def add_note():
    title = easygui.enterbox('Enter note title:')
    body = easygui.enterbox('Enter note body:')
    date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return {'id': str(len(notes)+1), 'title': title, 'body': body, 'date': date}

def edit_note():
    id_to_edit = easygui.enterbox('Enter note ID to edit:')
    for note in notes:
        if note['id'] == id_to_edit:
            note['title'] = easygui.enterbox('Enter new note title:', note['title'])
            note['body'] = easygui.enterbox('Enter new note body:', note['body'])
            note['date'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            break

def delete_note():
    id_to_delete = easygui.enterbox('Enter note ID to delete:')
    for note in notes:
        if note['id'] == id_to_delete:
            notes.remove(note)
            break

notes = load_notes()

while True:
    choice = easygui.choicebox('Select an action:', choices=['Show all notes', 'Add a note', 'Edit a note', 'Delete a note', 'Exit'])
    
    if choice == 'Show all notes':
        show_notes(notes)
    elif choice == 'Add a note':
        new_note = add_note()
        notes.append(new_note)
        save_notes(notes)
    elif choice == 'Edit a note':
        edit_note()
        save_notes(notes)
    elif choice == 'Delete a note':
        delete_note()
        save_notes(notes)
    elif choice == 'Exit':
        break