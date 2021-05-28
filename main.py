import os
import datetime

import traceback
from operator import itemgetter
from itertools import groupby

import PySimpleGUI as sg
import fitz
import tkinter
# import pdfplumber
import re
from reusable_functions import generate_file

from GUI.simple_GUI import layout
from Extraction.regex_engine import parse_pages

window = sg.Window('Tariff Extractor', layout, default_element_size=(32, 1),)

# TODO run this through main function
# fuck this program is a mess. 
while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Exit'):
        break

    # the option should at least be there
    # select which option from the dropdown menu
    if event in 'OK':
        file_path = values[0]

        try:

            pdf_document = fitz.open(file_path)
            print(pdf_document)
            dropdown_value = values['-DROPDOWN-']

            # pass this value to the engine
            list_items = parse_pages(pdf_document, dropdown_value)

            # print(list_items)
            generate_file(list_items)

            # TODO extraction completed in - x amount of time
            sg.popup_auto_close('Extraction Complete.')

            # TODO allow the app to run more than once in a row and produce accurate results

            # this is a temporary fix
            # window.close()
        except Exception as e:
            # TODO make a more friendly popup here?
            tb = traceback.format_exc()

            sg.Print(f'Something went wrong. Here is the info:', e, tb)

window.close()

# I used some new techniques because Regex and split wasn't working. 
# I found a new way to do the same thing when the old way wasn't working

# TODO time to add an installer and a new interface. 
# TODO lets do this

# there has to be multiple file support and special rules for Ifor Williams
# this is going to work.
# the EAD to T1 converter is going to be a bespoke tool that works specifically for that task

# TODO put checks everywhere. Check if something exists and if it doesn't then do something else

# TODO struggling to add loading spinner as well now
# TODO add the totals to the bottom of the command line output
# come back to that later

# I've just realised something.

# I have found one invoice with a freight charge - I'm not sure what to do with it
# I'll probably just put a disclaimer at the top - double check all the values -
# make sure what the tariffs are there

# TODO extract data without formatting any of it - so each line will be extracted
# then what we'll do is add an option to format the data?
# Not sure. We could possibly specify how to clean the data

# TODO choose file output location
# TODO - extract other - so this one will be a generic tariff search
# try to find the totals of the invoices, the countries of origin


# TODO can't seem to work out how to total each column at the moment
# move onto the next thing.
# I think it's finally time to tackle electrolux

# TODO Add disclaimer
# TODO add freight charges to the bottom, need to find an invoice that has it on it
# TODO country names

# Try to make the extraction as general purpose and generic as possible.
# I need to make functions that can be reused across invoices
# the program has to become more general purpose over time, more reusable
# with every iteration there has to be something that makes it better

###### Final Touches ######
# TODO consolidate the file before output - not sure about this one.
# TODO check PDF is valid - check for file path
# TODO elctrolux
# TODO warning at the top of the CSV
# TODO create more robust system

# TODO add support for multiple file types
# TODO T1 - extract table from documents

# TODO auto updater for pyinstaller?