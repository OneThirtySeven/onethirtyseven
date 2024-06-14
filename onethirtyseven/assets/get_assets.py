from pkg_resources import resource_stream
from pandas import read_csv, concat

def ncaaf_teams():
    """Return a dataframe about the 68 different Roman Emperors.

    Contains the following fields:
        index          68 non-null int64
        name           68 non-null object
        name.full      68 non-null object
    ... (docstring truncated) ...

    """
    # This is a stream-like object. If you want the actual info, call
    # stream.read()
    stream = resource_stream(__name__, 'ncaaf_teams.csv')
    return read_csv(stream, encoding='latin-1')

def endpoints():
    """Return a dataframe about the 68 different Roman Emperors.

    Contains the following fields:
        index          68 non-null int64
        name           68 non-null object
        name.full      68 non-null object
    ... (docstring truncated) ...

    """
    # This is a stream-like object. If you want the actual info, call
    # stream.read()
    stream = resource_stream(__name__, 'ncaaf_teams.csv')
    return read_csv(stream, encoding='latin-1')

# def ncaaf_games():
#     """Return a dataframe of NCAAF Games

#     """
#     # This is a stream-like object. If you want the actual info, call
#     # stream.read()
#     stream_2023 = resource_stream(__name__, 'ncaaf_2023.csv')
#     ncaaf_2023 = read_csv(stream_2023)

#     stream_2022 = resource_stream(__name__, 'ncaaf_2022.csv')
#     ncaaf_2022 = read_csv(stream_2022)

#     return concat([ncaaf_2023, ncaaf_2022])