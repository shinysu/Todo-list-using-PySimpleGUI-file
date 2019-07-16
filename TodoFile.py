import PySimpleGUI as sg
from file_functions import file_write, file_read
fname = 'file1'

tasks = file_read(fname)

layout = [
    [sg.Text('ToDo')],
    [sg.InputText('', key='todo_item'), sg.Button(button_text='Add', key="add_save")],
    [sg.Listbox(values=tasks, size=(40, 10), key="items"), sg.Button('Delete'), sg.Button('Edit'), sg.Button('Exit')],
]

window = sg.Window('ToDo App', layout)
while True:  # Event Loop
    event, values = window.Read()
    if event == "add_save":
        tasks.append(values['todo_item'])
        window.FindElement('items').Update(values=tasks)
        window.FindElement('add_save').Update("Add")
        window.FindElement('todo_item').Update('')
        file_write(fname, tasks)

    elif event == "Delete":
        tasks.remove(values["items"][0])
        window.FindElement('items').Update(values=tasks)
        file_write(fname, tasks)

    elif event == "Edit":
        edit_val = values["items"][0]
        tasks.remove(values["items"][0])
        window.FindElement('items').Update(values=tasks)
        window.FindElement('todo_item').Update(value=edit_val)
        window.FindElement('add_save').Update("Save")
        file_write(fname, tasks)
    elif event == None or event == "Exit":
        break

window.Close()