import PySimpleGUI as gui
from zip_creator import make_archive

select_label_uncompressed = gui.Text("Select files to compress:")
user_input1 = gui.Input()
choose_uncompressed_folder = gui.FilesBrowse("Choose", key='files')

select_label_destination = gui.Text("Select destination folder:")
user_input2 = gui.Input()
choose_destination_folder = gui.FolderBrowse("Choose", key='folder')

compress_button = gui.Button("Compress")

label_complete_message = gui.Text(" ", key="complete", text_color="green")

window = gui.Window("File Compressor",
                    layout=[
                        [select_label_uncompressed, user_input1, choose_uncompressed_folder],
                        [select_label_destination, user_input2, choose_destination_folder],
                        [compress_button, label_complete_message]
                    ])

while True:
    event, values = window.read()
    print(event, values)
    filepaths = values["files"].split(";")
    folder = values["folder"]
    make_archive(filepaths, folder)
    window['complete'].update(value="Compression Completed!")
    break

window.close()
