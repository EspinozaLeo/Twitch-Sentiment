# Author: Leo Espinoza

import credentials
import requests, json

clientInfo = {'Client-ID': credentials.client_id,
              'Client-Secret': credentials.client_secret}

myHead = {'Client-ID': credentials.client_id,
           'Client-Secret': credentials.client_secret,
           'Authorization': 'OAuth ' + credentials.token[6:]}

baseURL = 'https://api.twitch.tv/helix/'

# getAuthenticated(cID) authenticates the client and adds a bearer token to
# clientInfo.
def getAuthenticated(cInfo):
    authURL = ('https://id.twitch.tv/oauth2/token?client_id='
    + cInfo['Client-ID']
    + '&client_secret='
    + cInfo['Client-Secret']
    + '&grant_type=client_credentials')
    resp = requests.post(authURL)
    parseResp = json.loads(resp.text)
    # DEBUG
    # formatJson(parseResp)
    clientInfo['Authorization'] = 'Bearer ' + parseResp['access_token']

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
            print('Did not revoke successfully!' + revokeResp.status_code)
    else:
        print('Token does not exist!')

#@NOT WORKING
# getOAUTH() validates an oauth token. NOT WORKING or analytics() NOT WORKING!
def getOAUTH():
    oauthURL = 'https://id.twitch.tv/oauth2/validate?scope=analytics:read:games'
    resp = requests.get(oauthURL, headers = clientInfo)
    print(resp.status_code)
    print('I am here')
    parseResp = json.loads(resp.text)
    formatJson(parseResp)

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
    else:
        print('You have not been authenticated.\n')

# topGames() prints the top games on Twitch at the time of request.
def topGames():
    if 'Authorization' in clientInfo:
        topGameURL = baseURL + 'games/top'
        topResp = requests.get(topGameURL, headers = clientInfo)
        topParse = json.loads(topResp.text)
        formatJson(topParse)
    else:
        print('Not authenticated!')

# topStreams() prints the top streamers on Twitch at the time of request.
def topStreams():
    if 'Authorization' in clientInfo:
        topStreamURL = baseURL + 'streams'
        topResp = requests.get(topStreamURL, headers = clientInfo)
        topParse = json.loads(topResp.text)
        formatJson(topParse)
    else:
        print('Not authenticated!')

#@NOT WORKING
# analytics() returns analytics about the first 5 games.
def analytics():
    if 'Authorization' in clientInfo:
        analyticsURL = baseURL + 'analytics/games?first=5'
        analyticResp = requests.get(analyticsURL, headers = clientInfo)
        print(analyticResp)
        analyticParse = json.loads(analyticResp.text)
        formatJson(analyticParse)
    else:
        print('Not authenticated!')

#@DEBUGGING
# formatJson(jsonString) formats and prints a json. This function is for
# debugging purposes.
def formatJson(jsonString):
    formattedJson = json.dumps(jsonString, indent=2)
    print(formattedJson)


streamer = 'nickmercs'

getAuthenticated(clientInfo)
topStreams()
print('\n\nFinished getting top streams\n\n')
getStreamerInfo(streamer)
print('\n\nFinished getting streamer info\n\n')

topGames()
print('\n\nFinished getting top games being streamed\n\n')
revokeToken()
