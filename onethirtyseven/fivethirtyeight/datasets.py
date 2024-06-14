from pandas import read_csv, to_datetime

BASE_URL = 'https://projects.fivethirtyeight.com/polls/data/'

def favorability_polls():
    data = read_csv(BASE_URL + 'favorability_polls' + '.csv')
    data.start_date = to_datetime(data.start_date, format="mixed")
    data.end_date = to_datetime(data.end_date, format="mixed")
    data.created_at = to_datetime(data.created_at, format="mixed")
    return data

def favorability_averages():
    data = read_csv(BASE_URL + 'favorability_averages' + '.csv')
    data.date = to_datetime(data.date, format="mixed")
    return data

def generic_ballot_polls():
    data = read_csv(BASE_URL + 'generic_ballot_polls' + '.csv')
    data.start_date = to_datetime(data.start_date, format="mixed")
    data.end_date = to_datetime(data.end_date, format="mixed")
    data.created_at = to_datetime(data.created_at, format="mixed")
    data.election_date = to_datetime(data.election_date, format="mixed")
    return data

def generic_ballot_polls_historical():
    data = read_csv(BASE_URL + 'generic_ballot_polls_historical' + '.csv')
    data.start_date = to_datetime(data.start_date, format="mixed")
    data.end_date = to_datetime(data.end_date, format="mixed")
    data.created_at = to_datetime(data.created_at, format="mixed")
    data.election_date = to_datetime(data.election_date, format="mixed")
    return data

def generic_ballot_averages():
    data = read_csv(BASE_URL + 'generic_ballot_averages' + '.csv')
    data.election = to_datetime(data.election, format="mixed")
    return data

def governor_polls():
    data = read_csv(BASE_URL + 'governor_polls' + '.csv')
    data.start_date = to_datetime(data.start_date, format="mixed")
    data.end_date = to_datetime(data.end_date, format="mixed")
    data.created_at = to_datetime(data.created_at, format="mixed")
    data.election_date = to_datetime(data.election_date, format="mixed")
    return data

def governor_polls_historical():
    data = read_csv(BASE_URL + 'governor_polls_historical' + '.csv')
    data.start_date = to_datetime(data.start_date, format="mixed")
    data.end_date = to_datetime(data.end_date, format="mixed")
    data.created_at = to_datetime(data.created_at, format="mixed")
    data.election_date = to_datetime(data.election_date, format="mixed")
    return data

def recall_polls():
    data = read_csv(BASE_URL + 'recall_polls' + '.csv')
    data.start_date = to_datetime(data.start_date, format="mixed")
    data.end_date = to_datetime(data.end_date, format="mixed")
    data.created_at = to_datetime(data.created_at, format="mixed")
    return data

def president_approval_polls():
    data = read_csv(BASE_URL + 'president_approval_polls' + '.csv')
    data.start_date = to_datetime(data.start_date, format="mixed")
    data.end_date = to_datetime(data.end_date, format="mixed")
    data.created_at = to_datetime(data.created_at, format="mixed")
    return data

def president_approval_polls_historical():
    data = read_csv(BASE_URL + 'president_approval_polls_historical' + '.csv')
    data.start_date = to_datetime(data.start_date, format="mixed")
    data.end_date = to_datetime(data.end_date, format="mixed")
    data.created_at = to_datetime(data.created_at, format="mixed")
    return data

def vp_approval_polls():
    data = read_csv(BASE_URL + 'vp_approval_polls' + '.csv')
    data.start_date = to_datetime(data.start_date, format="mixed")
    data.end_date = to_datetime(data.end_date, format="mixed")
    data.created_at = to_datetime(data.created_at, format="mixed")
    return data

def congress_approval():
    data = read_csv(BASE_URL + 'congress_approval' + '.csv')
    data.start_date = to_datetime(data.start_date, format="mixed")
    data.end_date = to_datetime(data.end_date, format="mixed")
    data.created_at = to_datetime(data.created_at, format="mixed")
    return data

def scotus_approval_polls():
    data = read_csv(BASE_URL + 'scotus_approval_polls' + '.csv')
    data.start_date = to_datetime(data.start_date, format="mixed")
    data.end_date = to_datetime(data.end_date, format="mixed")
    data.created_at = to_datetime(data.created_at, format="mixed")
    return data

def approval_averages():
    data = read_csv(BASE_URL + 'approval_averages' + '.csv')
    data.date = to_datetime(data.date, format="mixed")
    return data

def president_polls():
    data = read_csv(BASE_URL + 'president_polls' + '.csv')
    data.start_date = to_datetime(data.start_date, format="mixed")
    data.end_date = to_datetime(data.end_date, format="mixed")
    data.created_at = to_datetime(data.created_at, format="mixed")
    data.election_date = to_datetime(data.election_date, format="mixed")
    return data

def president_polls_historical():
    data = read_csv(BASE_URL + 'president_polls_historical' + '.csv')
    data.start_date = to_datetime(data.start_date, format="mixed")
    data.end_date = to_datetime(data.end_date, format="mixed")
    data.created_at = to_datetime(data.created_at, format="mixed")
    data.election_date = to_datetime(data.election_date, format="mixed")
    return data

def presidential_general_averages():
    data = read_csv(BASE_URL + 'presidential_general_averages' + '.csv')
    data.date = to_datetime(data.date, format="mixed")
    return data

def president_primary_polls():
    data = read_csv(BASE_URL + 'president_primary_polls' + '.csv')
    data.start_date = to_datetime(data.start_date, format="mixed")
    data.end_date = to_datetime(data.end_date, format="mixed")
    data.created_at = to_datetime(data.created_at, format="mixed")
    data.election_date = to_datetime(data.election_date, format="mixed")
    return data

def president_primary_polls_historical():
    data = read_csv(BASE_URL + 'president_primary_polls_historical' + '.csv')
    data.start_date = to_datetime(data.start_date, format="mixed")
    data.end_date = to_datetime(data.end_date, format="mixed")
    data.created_at = to_datetime(data.created_at, format="mixed")
    data.election_date = to_datetime(data.election_date, format="mixed")
    return data

def presidential_primary_averages():
    data = read_csv(BASE_URL + 'presidential_primary_averages' + '.csv')
    data.date = to_datetime(data.date, format="mixed")
    return data

def house_polls():
    data = read_csv(BASE_URL + 'house_polls' + '.csv')
    data.start_date = to_datetime(data.start_date, format="mixed")
    data.end_date = to_datetime(data.end_date, format="mixed")
    data.created_at = to_datetime(data.created_at, format="mixed")
    data.election_date = to_datetime(data.election_date, format="mixed")
    return data

def house_polls_historical():
    data = read_csv(BASE_URL + 'house_polls_historical' + '.csv')
    data.start_date = to_datetime(data.start_date, format="mixed")
    data.end_date = to_datetime(data.end_date, format="mixed")
    data.created_at = to_datetime(data.created_at, format="mixed")
    data.election_date = to_datetime(data.election_date, format="mixed")
    return data

def senate_polls():
    data = read_csv(BASE_URL + 'senate_polls' + '.csv')
    data.start_date = to_datetime(data.start_date, format="mixed")
    data.end_date = to_datetime(data.end_date, format="mixed")
    data.created_at = to_datetime(data.created_at, format="mixed")
    data.election_date = to_datetime(data.election_date, format="mixed")
    return data

def senate_polls_historical():
    data = read_csv(BASE_URL + 'senate_polls_historical' + '.csv')
    data.start_date = to_datetime(data.start_date, format="mixed")
    data.end_date = to_datetime(data.end_date, format="mixed")
    data.created_at = to_datetime(data.created_at, format="mixed")
    data.election_date = to_datetime(data.election_date, format="mixed")
    return data