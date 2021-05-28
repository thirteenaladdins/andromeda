import fitz
import re
import pprint
from collections import namedtuple


# this is where I'm stuck
# define the pre

from Processing.preprocessor_templates import get_definitions
from Processing.match_definition import get_match_definition

print(fitz.__doc__)

# TODO dynamic selection with GUI here


# now that we have it at this stage we have to modularise it further


# how do we turn add all these?

# it's going to be a text editor sort of thing
# and we're going to add a new line
# each new line is highlighted -
# it can parsed by the engine
# each new line is turned into a string and added to the list as a variable


# data storage format for python - json or something else?


# TODO This is where we're going to start


# open the pdf document
# pass in the regex definitions - supplied via template / GUI

# we could pre-process the data further like removing new lines
# pre-process the data
# then print the data based on that input
# TODO in the GUI - set up terms for the preprocessor
# TODO - then the matching engine is the next part
# TODO then post processor
# TODO then extract that data and compile it into useable format

# mann + hummel item search


# regex_definitions = [test_string, test_footer, test_numbers]
# so we define the search criteria line by line and then reorganise and sort it after
# TODO we need to connect to this function and run every new definition through this script

# regex_definitions = [test_footer]
# DOTALL test compile - there will have to be different variables


# add flags as a separate argument later.

def regex_test_compiler(string):
    compile_regex = re.compile(string, flags=re.DOTALL)
    # compile_regex = re.compile(string)
    return compile_regex


# Add re.DOTALL in the sub function
# the re.DOTALL should be selected by choice when the
def remove_data(regex_pattern, repl, string):
    page_after_filter = re.sub(regex_pattern, repl, string, flags=re.DOTALL)
    return page_after_filter


# right now all I'm doing is removing data -
# pass functions in to map to data -
# TODO improve functionality of this function

def regex_preprocessor(regex_definitions, page_text):
    for regex_def in regex_definitions:
        page_text = remove_data(regex_def, "", page_text)

    return page_text


# replace items here...
# pre processor...?
def define_replace(string):
    pass


def find_matches(item_to_search, text):
    all_matches = re.findall(item_to_search, text)
    return all_matches

# Temporary function
# forget about headers

# Williams Regex - additional rules
def williams_remove_newline(page_text):
    mystring = page_text.replace('\n', ' ').replace('\r', '')
    return mystring
    pass 

# match commodity summary page and nothing else...
# this seems to run it once per page
def get_commodity_summary(pdf_text):
    pattern = re.compile(r'Total Charge.*', flags=re.DOTALL)
    
    matched_segement = re.findall(pattern, pdf_text)
    return matched_segement 

    
def is_number(x):
    '''
        Takes a word and checks if Number (Integer or Float).
    '''
    try:
        # only integers and float converts safely
        num = float(x)
        return True
    except ValueError as e: # not convertable to float
        return False
    
# def williams_generate_summary():


item_summary = namedtuple('items', 'tariff quantity mass charge')
# item_summary = namedtuple('Items', ['tariff', 'quantity', 'mass', 'charge'])

# list_items_1 = []

# modularise this whole thing
# we take the parse pages from the
def parse_pages(pdf_document, dropdown_value):
    # pdf_document = fitz.open(
    #     r'C:\\Users\\Mo_Am\Desktop\\ONE_PDF_ATTACH_FOR_ALL.pdf')

    # pdf_document = fitz.open(path_to_pdf)

    full_text = ''
    for page in pdf_document:
        page_text = page.get_text("text")

        # get the relevant process here for preprocessing the pages
        
        regex_definitions = get_definitions(dropdown_value)
        item_to_match = get_match_definition(dropdown_value)

        # TODO WILLIAMS PREPROCESSOR - come back and fix this later 

        

        # if the page needs to be run through the preprocessor
        # regex preprocessor - remove header and footer
        if regex_definitions:
            processed_page = regex_preprocessor(regex_definitions, page_text)
            full_text += processed_page

        # if not then add
        elif dropdown_value == 'Williams Spares':

            # page_text = williams_remove_newline(page_text)  
            list_items = []
            full_text += page_text  
            commodity_summary = get_commodity_summary(full_text)
            
            # turn the list into a string
            com_split = ' '.join(commodity_summary)
            
            split_again = com_split.split('\n')
            print(split_again)
            
            for item in split_again:
                # remove comma from each item
                cleaned_item = item.replace(',', '')
                print(cleaned_item)
                # add the item back to the list? or create a new list?
                list_items.append(cleaned_item)
                

            commodity_list = [ x for x in list_items if is_number(x)]
            
            
            
            # print(commodity_list)

            composite_list = [ commodity_list[x:x+4] for x in range(0, len(commodity_list), 4) ]
            pprint.pprint(composite_list)
            
            # return composite_list
            # pprint.pprint(composite_list) 

            # for line in composite_list:
            #     print(line[0], line[1], line[2], line[3])

            #     list_items.append(item_summary(line[0],
                                #   line[1], line[2], line[3]))
            
            # print(list_items)
            # return composite_list

        else:
            full_text += page_text

        
    
    define_item_search = regex_test_compiler(item_to_match)
    # all_matches = find_matches(define_item_search, full_text)

    # post processing here to get the values we wantx
    # print(all_matches)
    # pprint.pprint(all_matches)
    # for item in all_matches:

    # instead of split we'll use regex to get everything after a key word
    #     print(repr(item))
        # print(str(item))
        # print(item.split())
    return composite_list






