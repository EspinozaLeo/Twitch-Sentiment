# Author: Leo Espinoza

import requests, json

clientID = {'Client-ID': 'ENTER ID HERE'}
clientSecret = {'Client-Secret': 'ENTER '}
baseURL = 'https://api.twitch.tv/helix/'

# get current top games
url = baseURL + "games/top"

# postURL = 'https://id.twitch.tv/oauth2/token?client_id=41rrsier5hii7v88dqeja1tuitbu04&client_secret=tyclm8shejwsuiry8thbsif23j9btm&grant_type=client_credentials'



# getAuthenticated(cID) posts a request to the Twitch API and returns an
# access token.
def getAuthenticated(cID):
    authURL = 'https://id.twitch.tv/oauth2/token?client_id=' + cID['Client-ID'] + '&client_secret=<enter value>&grant_type=client_credentials'
    resp = requests.post(authURL)
    parseResp = json.loads(resp.text)

    # DEBUG
    # formatJson(parseResp)

    return parseResp['access_token']


# formatJson(jsonString) formats a json. This function is for
# debugging purposes.
def formatJson(jsonString):
    formattedJson = json.dumps(jsonString, indent=2)
    print(formattedJson)

accessToken = getAuthenticated(clientID)
print(accessToken)