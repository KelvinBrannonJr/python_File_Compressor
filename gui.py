import PySimpleGUI as gui
from zip_creator import make_archive

select_label_uncompressed = gui.Text("Select files to compress:")
input_compress = gui.Input(key='compress_input')
choose_uncompressed_folder = gui.FilesBrowse("Choose", key='files')

select_label_destination = gui.Text("Select destination folder:")
input_destination = gui.Input(key='destination_input')
choose_destination_folder = gui.FolderBrowse("Choose", key='folder')

compress_button = gui.Button("Compress")

label_complete_message = gui.Text(" ", key="complete")

window = gui.Window("File Compressor",
                    layout=[
                        [select_label_uncompressed, input_compress, choose_uncompressed_folder],
                        [select_label_destination, input_destination, choose_destination_folder],
                        [compress_button, label_complete_message]
                    ])

while True:
    event, values = window.read()
    if event == gui.WIN_CLOSED:
        break
    else:
        print(event, values)
        filepaths = values["files"].split(";")
        folder = values["folder"]
        make_archive(filepaths, folder)
        window['complete'].Update(value="Compression Completed!")
        window['compress_input'].Update(value="")
        window['destination_input'].Update(value="")


window.close()
