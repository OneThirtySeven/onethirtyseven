from requests import get
from json import loads
from pandas import DataFrame, concat
from datetime import datetime

def get_schedule(season = datetime.now().year - 1, season_type = 2):
    """ Grab ncaaf game_ids based on season and season type

    Parameters
    ----------
    season : int
         (Default value = datetime.now().year - 1)
    season_type : int
         (Default value = 2)
         1: pre-season | 2: regular-season | 3: post-season (no pre-season for ncaaf)

    Returns
    -------
        DataFrame with game_ids
    """

    # Arg Validation
    if season_type in [2, 3]:
        ValueError("season type must be 2 for regular season or 3 for post season")

    if type(season) != int:
        ValueError('season must be int')

    # Future args if number of games in a season exceeds 1000
    API_MAX_PAGE_SIZE = 1000
    PAGE = 1

    # body
    request_url = 'https://sports.core.api.espn.com/v2/sports/football/leagues/college-football/seasons/{}/types/{}/events?limit={}&page={}'.format(season, season_type, API_MAX_PAGE_SIZE, PAGE)
    schedule = get(request_url)
    schedule = loads(schedule.content.decode('utf-8'))
    schedule = DataFrame.from_dict(schedule.get('items'))
    schedule = schedule.rename(columns={"$ref": "url"})
    schedule['game_id'] = schedule['url'].apply(lambda x: x.replace('http://sports.core.api.espn.com/v2/sports/football/leagues/college-football/events/', '').replace('?lang=en&region=us', ''))

    # add meta data

    ## season_type
    if season_type == 2:
        schedule['season_type'] = 'regular'

    if season_type == 3:
        schedule['season_type'] = 'post'

    ## season
    schedule['season'] = season

    return schedule[['game_id', 'season', 'season_type', 'url']]

def get_schedule_full(season = datetime.now().year - 1):
    """ Wrapper for get_season() that pulls both regular and post season

    Parameters
    ----------
    season : int
        (Default value = datetime.now().year - 1)

    Returns
    -------
        DataFrame with game_ids split by regular and post season

    """

    try:
        regular_season = get_schedule(season, 2)

        if regular_season.shape[0] > 0:
            has_regular = True
        else:
            has_regular = False

    except:
        pass

    try:
        post_season = get_schedule(season, 3)

        if post_season.shape[0] > 0:
            has_post = True
        else:
            has_post = False
        
    except:
        pass

    if has_regular and has_post:
        schedule = concat([regular_season, post_season])
    
    if has_regular and not has_post:
        schedule = regular_season

    if not has_regular and not has_post:
        schedule = None
        Warning('No data available')
    
    return schedule

def get_game(game_id):
    """ Grabs json payload with game data

    Parameters
    ----------
    game_id : int
        

    Returns
    -------
        json formatted string

    """
    res = get('http://site.api.espn.com/apis/site/v2/sports/football/college-football/summary?event=' + str(game_id))
    return res.content.decode('utf-8')

def get_games_old(season):
    """

    Parameters
    ----------
    season :
        

    Returns
    -------

    """

    try:
        regular_season = get('https://sports.core.api.espn.com/v2/sports/football/leagues/college-football/seasons/' + str(season) + '/types/2/events?limit=1000')
        regular_season = loads(regular_season.content.decode('utf-8'))
        regular_season = DataFrame.from_dict(regular_season.get('items'))
        regular_season = regular_season.rename(columns={"$ref": "url"})
        regular_season['game_id'] = regular_season['url'].apply(lambda x: x.replace('http://sports.core.api.espn.com/v2/sports/football/leagues/college-football/events/', '').replace('?lang=en&region=us', ''))
        regular_season['season_type'] = 'regular'

        if regular_season.shape[0] > 0:
            has_regular = True
        else:
            has_regular = False

    except:
        pass

    try:
        post_season = get('https://sports.core.api.espn.com/v2/sports/football/leagues/college-football/seasons/' + str(season) + '/types/3/events?limit=1000')
        post_season = loads(post_season.content.decode('utf-8'))
        post_season = DataFrame.from_dict(post_season.get('items'))
        post_season = post_season.rename(columns={"$ref": "url"})
        post_season['game_id'] = post_season['url'].apply(lambda x: x.replace('http://sports.core.api.espn.com/v2/sports/football/leagues/college-football/events/', '').replace('?lang=en&region=us', ''))
        post_season['season_type'] = 'post'

        if post_season.shape[0] > 0:
            has_post = True
        else:
            has_post = False
        
    except:
        pass

    if has_regular and has_post:
        games = concat([regular_season, post_season])
    
    if has_regular and not has_post:
        games = regular_season

    if not has_regular and not has_post:
        games = None
        Warning('None data available')

    if has_regular or has_post:
        games['season'] = season
        games['extract_main'] = None
        games['extract_from_url'] = None

        for i in range(len(games)):
            game_id = games['game_id'].values[i]
            res = get('http://site.api.espn.com/apis/site/v2/sports/football/college-football/summary?event=' + game_id)
            games['extract_main'].values[i] = res.content.decode('utf-8')

            url = games['url'].values[i]
            res = get(url)
            games['extract_from_url'].values[i] = res.content.decode('utf-8')
    
    return games