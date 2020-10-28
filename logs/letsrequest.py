# Author: Leo Espinoza

import credentials
import requests, json

clientInfo = {'Client-ID': credentials.client_id,
              'Client-Secret': credentials.client_secret}

baseURL = 'https://api.twitch.tv/helix/'

# getAuthenticated(cID) authenticates the client and adds an oAuth token to
# clientInfo.
def getAuthenticated(cInfo):
    authURL = 'https://id.twitch.tv/oauth2/token?client_id=' + cInfo['Client-ID'] + '&client_secret=' + cInfo['Client-Secret'] + '&grant_type=client_credentials'
    resp = requests.post(authURL)
    parseResp = json.loads(resp.text)
    # The following line is for DEBUGGING purposes
    # formatJson(parseResp)
    clientInfo['Authorization'] = 'Bearer ' + parseResp['access_token']

# getStreamerInfo(streamerName) returns information about a streamer given
# a streamer's name.
def getStreamerInfo(streamerName):
    streamerURL = baseURL + 'search/channels?query=' + streamerName
    getResp = requests.get(streamerURL, headers = clientInfo)
    print(getResp.status_code)
    getParse = json.loads(getResp.text)
    # print(getParse)
    # formatJson(getParse)
    print(getParse['data'][0])
    # get current top games

def topStreams():
    topGameURL = baseURL + "games/top"
    topResp = requests.get(topGameURL, headers = clientInfo)
    topParse = json.loads(topResp.text)
    formatJson(topParse)

# formatJson(jsonString) formats a json. This function is for
# debugging purposes. Prints readable json content.
def formatJson(jsonString):
    formattedJson = json.dumps(jsonString, indent=2)
    print(formattedJson)


streamer = 'nickmercs'

getAuthenticated(clientInfo)
getStreamerInfo(streamer)
# getStreamerInfo()