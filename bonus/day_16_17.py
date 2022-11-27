import PySimpleGUI as sg
from zip_creator import make_archive

file_select_label = sg.Text("Select files to compress:")
file_select_input = sg.Input()
file_select_button = sg.FilesBrowse("Choose", key="files")

directory_select_label = sg.Text("Select destination folder:")
directory_select_input = sg.Input()
directory_select_button = sg.FolderBrowse("Choose", key="folder")

compress_button = sg.Button("Compress")

result_label = sg.Text(key="result")

window = sg.Window("File Compressor",
                   layout=[[file_select_label, file_select_input, file_select_button],
                           [directory_select_label, directory_select_input, directory_select_button],
                           [compress_button, result_label]])

while True:
    event, values = window.read()
    print(event)
    print(values)

    filepaths = values["files"].split(";")
    folder = values["folder"]
    make_archive(filepaths, folder)

    window["result"].update(value="Compression successful")

# window.read()
window.close()
