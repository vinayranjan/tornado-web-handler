"""Custom user functions."""
import pandas as pd

# all your functions will ggo here.........

filename = 'data/transaction_report.csv'


def read_data_file():
    """Read data file."""
    main_data = pd.read_csv(filename, encoding='utf-8')
    return main_data


def get_filter(main_data, filtername='Month'):
    """Get filter params."""
    filters = main_data[filtername].unique()
    return filters


def filter_data(data):
    """Responsible for filtering all filter data."""
    return data


def get_filter_str(handler):
    """Create the complete filter str including previous filters."""
    return ''


def barchart_data(handler):
    """Create a bar chart."""
    # print get_argument("month", None, True)
    main_data = read_data_file()
    full_data = main_data
    main_data = filter_data(full_data)
    return full_data, main_data
