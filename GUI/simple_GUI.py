import PySimpleGUI as sg

# sg.theme('LightGrey1')
sg.theme('Dark Blue 3')

# dropdown_menu = ["Mann + Hummel", "Electrolux", "Williams Spares"]
# dropdown_menu = ["Mann and Hummel"]
dropdown_menu = ["Williams Spares"]


layout = [[sg.Text('Select File')],

          [sg.Input(), sg.FileBrowse()],
          [sg.Text('Choose Company')],
          [sg.Combo(values=dropdown_menu,
                    default_value='Williams Spares', enable_events=True, size=(30, 6), key='-DROPDOWN-')],
          #   [sg.Text('Enter Gross Weight')],
          #   [sg.Input('', size=(20, 4), enable_events=True, key='-GROSS-')],
          #   [sg.Input('', size=(20, 4), key='-GROSS-')],
          #   [sg.Text('Enter Net Weight')],
          #   [sg.Input('', size=(20, 4), enable_events=True, key='-NET-')],
          #   [sg.Input('', size=(20, 4), key='-NET-')],
          [sg.Checkbox('Convert EU countries', default=False, key="-EU-")],
          #   [sg.Input(key='-SAVEAS-FILENAME-', visible=False,
          #             enable_events=True), sg.FileSaveAs()],
          [sg.Button('OK'), sg.Button('Exit')]]

