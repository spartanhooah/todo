import PySimpleGUI as sg

file_select_label = sg.Text("Select files to compress:")
file_select_input = sg.Input()
file_select_button = sg.FilesBrowse("Choose")


directory_select_label = sg.Text("Select destination folder:")
directory_select_input = sg.Input()
directory_select_button = sg.FolderBrowse("Choose")

compress_button = sg.Button("Compress")

window = sg.Window("File Compressor",
                   layout=[[file_select_label, file_select_input, file_select_button],
                           [directory_select_label, directory_select_input, directory_select_button],
                           [compress_button]])

window.read()
window.close()
