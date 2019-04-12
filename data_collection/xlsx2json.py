#-*- coding: utf-8 -*-

from import_hedgehogs import *

# Dictionary {1: 'A', 2: 'B', ...}
# Note: we are limiting the allowed columns from A to Z
# adding more columns is possible but would complicate things
NUM2ALPHA = dict(zip(range(1, 27), string.ascii_lowercase))

JSON_INDENT = 4

MAX_ROWS = 100
MAX_COLUMNS = len(NUM2ALPHA)

RE_PATTERN_FOOTNOTE = re.compile(r'\[\d+]')
RE_PATTERN_YEAR_WORD = re.compile(r'^\d\d\d\d$')

MONTHS = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'july', 'aug', 'sep', 'oct', 'nov', 'dec']

# Should be changed to str for Python 3+
BASE_STRING_CLASS = str
# Should be changed to str for Python 3+
STRING_CLASS = str


class InvalidRow(Exception):
    pass


class InvalidCell(Exception):
    pass


def myprint(*args, **kwargs):
    """Helper print function"""
    pass#print(pprint.pformat(*args, **kwargs))


def remove_punctuation(text):
    """Method used to leave only letters, numbers and whitespace chars in text

    Arguments:
        text: the string that is currently being nodified

    Returns:
        res: string after modification 
    """
    if not isinstance(text, BASE_STRING_CLASS):
        return text
    res = []
    for c in text:
        if c.isalnum() or c.isspace():
            res.append(c)
    #print("return value", ''.join(res))
    return ''.join(res)


def prepare_for_matching(text):
    """Prepares string to be compared/matched

    Arguments:
        text: the string that will eventually be compared

    Returns:
        the string with punctuation removed
    """
    if not isinstance(text, BASE_STRING_CLASS):
        return text
    return ' '.join(remove_punctuation(text).lower().split())


def is_footnote(text):
    """Determines wheter string is a footnote

    Arguments:
        text: the string that is being checked

    Returns:
        true if string is a footnote and false
    """
    return RE_PATTERN_FOOTNOTE.match(text)


def convert_to_number(value):
    """Converts string (value) to an integer
    
    Arguments:
        string that will potentially be converted to an integer

    Throws: 
        ValueError if string cannot be converted to a number

    Returns:
        the integer value of string
    """
    value_original = value
    value = ''.join(value.split())
    myprint(value)
    if value.count('$') < 2:
        value = value.replace('$', '')
    else:
        raise ValueError('%s has too many $s to be a number' % value_original)
    myprint(value)
    value = value.replace(',', '')
    myprint(value)
    if value.startswith('(') and value.endswith(')'):
        value = value[1:-1]
        multiplier = -1
    else:
        multiplier = 1

    myprint(value)
    myprint(multiplier)

    try:
        value_number = multiplier * float(value)
    except ValueError:
        raise ValueError('Cannot convert %s to a number' % value_original)

    if len(value) > 1 and value.startswith('0') and not value.startswith('0.'):
        # Don't convert numbers with leading zeros such as CIK
        return value

    if int(value_number) == value_number:
        return int(value_number)
    else:
        return value_number


def get_cell(sheet, index):
    """Return cell object for sheet and index (of the form "A1")

    Arguments
        sheet: the specific xlxs file we are collecting data from
        index: the index/cell of the file we want

    Returns:
        the cell object in the xlxs file (sheet) at index (index)
    """
    return sheet[index]


def get_cell_value(sheet, index):
    """

    Return cell value for sheet and index (of the form "A1")

    Arguments
        sheet: the specific xlxs file we are collecting data from
        index: the index/cell of the file we want

    Returns:
        the value in the xlxs file (sheet) at index (index)
    """
    myprint('Getting value of cell %s' % index)
    value = get_cell(sheet, index).value
    myprint(type(value))
    myprint(value)
    #print("get_cell_value",value)
    if isinstance(value, BASE_STRING_CLASS):
        value = value.replace(u'\xa0', ' ')
        if value.strip() == "'":
            return None
        elif value.startswith("'") and value.count("'") == 1:
            # Remove "'" from the beginning
            value = value[1:]

        if is_footnote(value):
            return None

        try:
            value = convert_to_number(value)
        except ValueError:
            value = value
    elif isinstance(value, datetime.datetime):
        # datetime object handling
        return value.strftime('%d-%b-%y')
        # return value.isoformat()
    elif isinstance(value, bool):
        # datetime object handling
        return STRING_CLASS(value).lower()
    return value


def get_heading_row_height(sheet):
    """Determine the "height" of the header in rows. Based on actual files it can be 1-3

    Arguments:
        sheet:the sheet (xlxs file) which we are checking

    Returns:
        1, 2 or 3 depending upon which row the header is located in
    """
    myprint('Calling get_heading_row_height')
    # First check whether there is header text in the third row
    # cik-0001288776_2012-04-25_an-0001193125-12-182401.xlsx
    # has a third row with the text "Class A Common Stock" etc.
    for col in range(2, MAX_COLUMNS + 1):
        cell_value = get_cell_value(sheet, '%s%d' % (NUM2ALPHA[col], 3))
        if cell_value not in (None, '') and isinstance(cell_value, BASE_STRING_CLASS):
            words = prepare_for_matching(cell_value).split()
            myprint('Words for matching: %s' % repr(words))
            if 'class' in words and 'stock' in words:
                myprint('heading row height is 3')
                return 3
    # The code below runs if the return is not called in the
    # previous for loop
    # See whether row 2 is part of the header, e.g.:
    # cik-0000789019_2017-04-27_an-0001564590-17-007547.xlsx
    # has a date in the second row. Some files also have a
    # "Months Ended" + date text in the second row, e.g.:
    # cik-0000789019_2009-10-23_an-0001193125-09-212454.xlsx
    # but that is not important as matching the date should cover
    # that case
    for col in range(2, MAX_COLUMNS + 1):
        cell_value = get_cell_value(sheet, '%s%d' % (NUM2ALPHA[col], 2))
        if cell_value not in (None, '') and isinstance(cell_value, BASE_STRING_CLASS):
            words = prepare_for_matching(cell_value).split()
            # Check whether a month is part of words
            if set(MONTHS).intersection(set(words)):
                # Check whether a 4 digit year-number is part of words
                for word in words:
                    if RE_PATTERN_YEAR_WORD.match(word):
                        myprint('heading row height is 2')
                        return 2
    # The code below runs if the return is not called in the
    # previous for loop
    # The sheet has to have at least 1 row belonging to the heading
    myprint('heading row height is 1')
    return 1


def parse_col_heading(sheet, col):
    """Parse "months ended", date and "class stock" info from the column heading

    Arguments:
        sheet: the sheet (xlxs file) which we are checking
        col: the column from the sheet that will be parsed

    Returns:
        data at desired column in xlxs file (sheet)
    """
    heading_row_height = get_heading_row_height(sheet)
    myprint('Parsing col heading')
    col_heading = ''
    for row in range(1, heading_row_height + 1):
        cel_value = get_cell_value(
            sheet, '%s%d' % (NUM2ALPHA[col], row)
        )
        if cel_value and isinstance(cel_value, BASE_STRING_CLASS):
            col_heading += ' ' + cel_value
    words = prepare_for_matching(col_heading).split()
    try:
        ended_index = words.index('ended')
        months_ended = ' '.join(words[:ended_index + 1])
    except ValueError:
        ended_index = -1
        months_ended = None

    date_index = -1
    for i, word in enumerate(words[ended_index + 1:]):
        if RE_PATTERN_YEAR_WORD.match(word):
            date_index = i
            date = ' '.join(words[ended_index + 1:ended_index + date_index + 2])
            break
    if date_index == -1:
        date_index = 0
        date = None
        myprint("Date not found for column %s, "
                "this shouldn't happen" % NUM2ALPHA[col])
    header_custom_remainder = ' '.join(words[ended_index + date_index + 2:])
    if header_custom_remainder == '':
        header_custom_remainder = None

    myprint(months_ended)
    myprint(date)
    myprint(header_custom_remainder)
    return months_ended, date, header_custom_remainder


def parse_cell(sheet, row, col):
    """ Parse value at index row, col in xlxs file (sheet)

    Arguments:
        sheet: the xlxs file being parsed
        row: the row with the cell we are checking
        col: the column with the cell we are checking

    Throws:
        InvalidCell if cell cannot be parsed

    Returns:
        list row_element with time, date, and header value in that order
    """
    cell_key = '%s%d' % (NUM2ALPHA[col], row)
    #print("cell_key", cell_key)
    cell_value = get_cell_value(sheet, cell_key)
    if cell_value not in (None, ''):
        row_element = OD(
            [('value', cell_value)]
        )
        months_ended, date, header_custom_remainder = parse_col_heading(sheet, col)
        if months_ended:
            row_element['time'] = months_ended
        if date:
            row_element['date'] = date
        if header_custom_remainder:
            row_element['header_custom_remainder'] = header_custom_remainder

        return row_element
    else:
        raise InvalidCell('Invalid cell %s, skipping...' % cell_key)


def parse_row(sheet, row):
    """Parse sheet's row with data (i.e. non-heading row)

    Arguments:
        sheet: the xlxs file with the row being parsed
        row: the row which the function will parse

    Throws:
        InvalidCell if cell in the row cannot be parsed

    Returns:
        list with row elements in order and parsed with time,date, and header_data

    """
    myprint('Parsing row %d' % row)
    first_cell_key = 'A' + STRING_CLASS(row)
    #print('first_cell_key', first_cell_key)
    first_cell = get_cell(sheet, first_cell_key)
    row_key = get_cell_value(sheet, first_cell_key)
    # Skip non-valid rows
    if not row_key:
        raise InvalidRow('Invalid row %d, skipping...' % row)
    myprint('Parsing row %d, %s' % (row, STRING_CLASS(row_key)))

    row_elements = [row_key]
    # Iterate through all columns for this row:
    months_ended_old = None
    for col in range(2, MAX_COLUMNS + 1):
        try:
            row_element = parse_cell(sheet, row, col)
            if 'time' not in row_element:
                if 'date' in row_element:
                    # If there isn't any months_ended for the current
                    # row element set the previous one
                    if months_ended_old:
                        row_element['time'] = months_ended_old
            else:
                months_ended_old = row_element['time']
            row_elements.append(row_element)
        except InvalidCell as e:
            myprint(e)
    return row_elements


def parse_sheet(sheet):
    """Calls other methods to parse an entire xlxs file

    Arguments:
        sheet: the xlxs file which will be parsed (getting time, date, and header_data)

    Returns:
        json sheet with xlxs file data properly formatted

    """
    heading_row_height = get_heading_row_height(sheet)
    # For every col in the heading we merge all rows to get the title
    sheet_title = ''
    for row in range(1, heading_row_height + 1):
        cell_value = get_cell_value(sheet, 'A%d'%row)
        if cell_value not in (None, '') and isinstance(cell_value, BASE_STRING_CLASS):
            sheet_title += ' ' + cell_value
    sheet_title = ' '.join(sheet_title.split())
    json_sheet = OD([
        ('title', sheet_title)
    ])

    # The object whose keys are bold A cells (other cols are empty),
    # and whose elements are non-bold rows
    multi_row_object_key = None
    multi_row_object_elements = None
    row_elements_old = []
    # Iterate through all rows that are below the heading
    for row in range(heading_row_height + 1, MAX_ROWS + 1):
        try:
            row_elements = parse_row(sheet, row)
        except InvalidRow as e:
            myprint(e)
            row_elements_old = []
            continue
        if len(row_elements) == 1:
            # This is a title row. Check whether previous row was also
            # a title row.
            if len(row_elements_old) == 0:
                multi_row_object_key = STRING_CLASS(row_elements[0])
                multi_row_object_elements = OD()
            elif len(row_elements_old) == 1:
                # Previous row was also a title row. This is the case for,
                # e.g.:
                # footnotes_cik-0000320193_2016-01-27_an-0001193125-16-439878.xlsx
                # where the sheet "Cash and Available-for-Sale Sec" has
                # multiple title rows
                assert multi_row_object_key not in ('', None)
                multi_row_object_key += ' ' + STRING_CLASS(row_elements[0])
            else:
                # Previous row was a data row, and it was the last element
                # of a multi_row_object.
                # Save the current/old multi_row_object
                json_sheet[multi_row_object_key] = multi_row_object_elements
                # Initialize new multi_row_object
                multi_row_object_key = STRING_CLASS(row_elements[0])
                multi_row_object_elements = OD()
        elif len(row_elements) == 0:
            # Skip empty row
            pass
        else:
            # data row has 2 or more elements
            # There are cases when the first row below the title
            # isn't a title row. In such cases (specified by Ranjit) we
            # set the multi_row_object key to be the sheet title
            if multi_row_object_key is None:
                # Create new
                multi_row_object_key = STRING_CLASS(sheet_title)
                multi_row_object_elements = OD()
                # continue the script as normal
            # if only one element don't save as list
            myprint('Saving one element into multi_row_object_elements')
            myprint(row_elements)
            if len(row_elements) == 2:
                multi_row_object_elements[row_elements[0]] = row_elements[1]
            else:
                multi_row_object_elements[row_elements[0]] = row_elements[1:]
        row_elements_old = row_elements
    # Save the last multi_row_object as the loop doesn't catch it
    if multi_row_object_key:
        json_sheet[multi_row_object_key] = multi_row_object_elements
    return json_sheet


def convert(input_file_name, output_file_name):
    """Main function for converting xlsx files to json

    Arguments:
        input_file_name: the xlxs file which we be converted to json
        output_file_name: the name that the json file (output) will be named
    """
    myprint('Parsing workbook %s' % input_file_name)
    wb = openpyxl.load_workbook(
        input_file_name,
        guess_types=False,
        data_only=True
    )
    sheet_names = wb.sheetnames

    # Main json list
    json_result = []
    for sheet_name in sheet_names:
        # The block below was specified by Ranjit, but unfortunately
        # the ~2009 files when parsed return completely empty json objects
        # if sheet_name != 'Document and Entity Information'\
        #         and sheet_name.upper() != sheet_name:
        #     # the "Document and Entity Information" sheet should be always
        #     # included, and for the remaining sheets, only those with all caps
        #     continue
        myprint('Processing sheet:')
        myprint(sheet_name)
        sheet = wb[sheet_name]
        json_result.append(parse_sheet(sheet))

    with io.open(output_file_name, 'w', encoding='utf-8') as output_file:
        output_file.write(
            str(
                json.dumps(
                    json_result,
                    indent=JSON_INDENT,
# Commented out because str is python3 and accounts for encoding specifications
#                     ensure_ascii=False,
#                     encoding='utf-8'
                )
            )
        )


def main():
    # print(repr(' $ (22)'.decode('utf-8')))
    # print(convert_to_number(' $ (22)'))
    # return
    cli_parser = OptionParser(
        usage='usage: %prog <input.xlsx> [output.json]'
        )
    (options, args) = cli_parser.parse_args()

    # Input file checks
    if len(args) < 1:
        cli_parser.error("You have to supply at least 1 argument")
    input_file_name = args[0]
    if not os.path.exists(input_file_name):
        cli_parser.error("The input file %s you supplied does not exist" % input_file_name)

    # Output file checks
    # If supplied, the second argument is treated as the output file name
    if len(args) > 1:
        output_file_name = args[1]
    else:
        # Set the output file name based on the input file
        output_file_name = os.path.splitext(input_file_name)[0] + '.json'
    if os.path.exists(output_file_name):
        os.remove(output_file_name)

    convert(input_file_name, output_file_name)

if __name__ == "__main__":
    main()
