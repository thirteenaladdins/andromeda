import datetime
import pandas as pd


# def pro_rata_weight(weight, total_quantity, pieces):
#     # print(total_quantity)
#     # print(pieces)
#     if weight:
#         calculated_weight = (
#             (float(weight) / float(total_quantity)) * float(pieces))
#         # print(calculated_weight)
#         # count += calculated_weight
#         print(calculated_weight)
#     else:
#         calculated_weight = ''

#     return calculated_weight


def generate_file_name():
    ##### UNIQUE FILE NAME ######
    basename = "invoice_extracted-data"
    suffix = datetime.datetime.now().strftime("%y%m%d_%H%M%S")

    # e.g. 'filename_120508_171442'
    file_name = "_".join([basename, suffix])
    return file_name


def generate_file(list_items):
    file_name = generate_file_name()
    df = pd.DataFrame(list_items)

    df.index = df.index + 1

    # TODO - Export and Save
    df.to_csv(f'../{file_name}.csv')
    return df

# this must only work with a certain library
def get_num_pages(pdf_file):
    number_of_pages = len(pdf_file.pages)
    return number_of_pages


# def calculate_quantity(gross_weight, net_weight, match_items):
#     total = int()

#     if net_weight or gross_weight:
#         for line in match_items:
#             sep = 'PC'

#             # take the first half of the list
#             list_first_half = line.split(sep, 1)[0]
#             split_list = list_first_half.split()

#             num_pieces = split_list[-1]
#             pieces = num_pieces.replace(',', '')

#             ###### calculate total quantity ########
#             total += int(pieces)
#     # print(total)
#     return total
