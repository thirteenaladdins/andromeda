# TODO just make this better
# DRY


def get_definitions(dropdown_value):
    if dropdown_value == 'Mann + Hummel':
        test_header = r"MANN\+ HUMMEL.*origin"
        # test_header = r"MANN\+HUMMEL"
        # test_header_2 = r"MANN\+ HUMMEL"
        test_footer = r"Our published terms.*"
        # test_footer = r"Invoice.*"
        other_text = r"Total net"
        test_numbers = r"- \d.*"
        regex_definitions = [test_header, test_footer, test_numbers]
        return regex_definitions

# this isn't exactly what I'm going for.
# I'll come back to this
    elif dropdown_value == 'Electrolux':
        return 
    elif dropdown_value == 'Williams Spares':
        pass
    else:
        pass


# electrolux - requires preprocess to remove all new lines from each page
# new_item = re.compile(r' \d{6}.*%', flags=re.DOTALL)
