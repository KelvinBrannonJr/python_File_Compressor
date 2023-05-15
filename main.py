import PySimpleGUI as gui

select_label_uncompressed = gui.Text("Select files to compress:")
user_input1 = gui.Input()
choose_uncompressed_folder = gui.FilesBrowse("Choose")

select_label_destination = gui.Text("Select destination folder:")
user_input2 = gui.Input()
choose_destination_folder = gui.FolderBrowse("Choose")

compress_button = gui.Button("Compress")

window = gui.Window("File Compressor",
                    layout=[
                        [select_label_uncompressed, user_input1, choose_uncompressed_folder],
                        [select_label_destination, user_input2, choose_destination_folder],
                        [compress_button]
                    ])

window.read()
window.close()
