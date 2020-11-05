# Author: Leo Espinoza

import credentials
import requests, json

clientInfo = {'Client-ID': credentials.client_id,
              'Client-Secret': credentials.client_secret}

baseURL = 'https://api.twitch.tv/helix/'

# getAuthenticated(cID) authenticates the client and adds a bearer token to
# clientInfo.
def getAuthenticated(cInfo):
    authURL = 'https://id.twitch.tv/oauth2/token?client_id=' + cInfo['Client-ID'] + '&client_secret=' + cInfo['Client-Secret'] + '&grant_type=client_credentials'
    resp = requests.post(authURL)
    parseResp = json.loads(resp.text)
    # DEBUG
    # formatJson(parseResp)
    clientInfo['Authorization'] = 'Bearer ' + parseResp['access_token']
    # DEBUG
    # print('Successful authentication\n\n')

# getStreamerInfo(streamerName) returns information about a streamer given
# a streamer's name.
# Requirements: clientInfo must contain an authenticated bearer token.
def getStreamerInfo(streamerName):
    if 'Authorization' in clientInfo:
        streamerURL = baseURL + 'search/channels?query=' + streamerName
        getResp = requests.get(streamerURL, headers = clientInfo)
        getParse = json.loads(getResp.text)
        # print(getParse)
        # formatJson(getParse)
        print(getParse['data'][0])
        # get current top games
    else:
        print('You have not been authenticated.\n')

# topStreams() prints the top games on Twitch at the time of request.
def topStreams():
    if 'Authorization' in clientInfo:
        topGameURL = baseURL + 'games/top'
        topResp = requests.get(topGameURL, headers = clientInfo)
        topParse = json.loads(topResp.text)
        formatJson(topParse)
    else:
        print('Not authenticated!')

# revokeToken() revokes an authenticated token.
# Requirements: clientInfo must contain an authenticated bearer token.
def revokeToken():
    if 'Authorization' in clientInfo:
        revokeURL = ('https://id.twitch.tv/oauth2/revoke?client_id='
               + clientInfo['Client-ID']
               + '&token='
               + clientInfo['Authorization'][7:])
        revokeResp = requests.post(revokeURL)
        print(revokeResp.text)
        if revokeResp.status_code is 200:
            print('Revoke successful.\n')
            del clientInfo['Authorization']
        else:
            print(revokeResp.status_code)
    else:
        print('Token does not exist!')

# formatJson(jsonString) formats a json. This function is for
# debugging purposes. Prints readable json content.
def formatJson(jsonString):
    formattedJson = json.dumps(jsonString, indent=2)
    print(formattedJson)


streamer = 'nickmercs'

getAuthenticated(clientInfo)
getStreamerInfo(streamer)
print('\n\nFinished getting streamer info')
revokeToken()
