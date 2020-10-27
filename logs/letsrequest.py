# Author: Leo Espinoza

import credentials
import requests, json

clientInfo = {'Client-ID': credentials.client_id,
              'Client-Secret': credentials.client_secret}

baseURL = 'https://api.twitch.tv/helix/'

# get current top games
url = baseURL + "games/top"

# postURL = 'https://id.twitch.tv/oauth2/token?client_id=41rrsier5hii7v88dqeja1tuitbu04&client_secret=tyclm8shejwsuiry8thbsif23j9btm&grant_type=client_credentials'



# getAuthenticated(cID) posts a request to the Twitch API and returns an
# access token.
def getAuthenticated(cInfo):
    authURL = 'https://id.twitch.tv/oauth2/token?client_id=' + cInfo['Client-ID'] + '&client_secret=' + cInfo['Client-Secret'] + '&grant_type=client_credentials'
    resp = requests.post(authURL)
    parseResp = json.loads(resp.text)

    # DEBUG
    # formatJson(parseResp)
    authenticateMe(parseResp['access_token'])
    return parseResp['access_token']

def getStreamerInfo(streamerName):
    getURL = baseURL + '/search/channels?query=' + streamerName
    getResp = requests.get(getURL)
    getParse = json.loads(getResp.text)
    formatJson(getParse)

# formatJson(jsonString) formats a json. This function is for
# debugging purposes.
def formatJson(jsonString):
    formattedJson = json.dumps(jsonString, indent=2)
    print(formattedJson)

def authenticateMe(aToken):
    # authURL = 'https://api.twitch.tv/helix/'
    authURL = 'https://api.twitch.tv/helix/search/channels?query=aceu'
    myHeader = {'Client-ID': credentials.client_id,
                'Authorization' : 'Bearer ' + aToken}
    resp = requests.get(authURL, headers = myHeader)
    getRespJson = json.loads(resp.text)
    formatJson(getRespJson)

accessToken = getAuthenticated(clientInfo)
# getStreamerInfo()