import requests
import uuid

def GetMCVersionFromMod(Mod, FullVersion=False):
    NameList = Mod.split('-')
    Version = NameList[1]
    VersionList = Version.split('.')
    SimpleVersion = f'{VersionList[0]}.{VersionList[1]}'
    if len(VersionList) == 3:
        FullVersionStr = f'{SimpleVersion}.{VersionList[2]}'
        if FullVersion:
            return FullVersionStr
        else:
            return SimpleVersion
    else:
        return SimpleVersion


def GetSessionID(Username, Password):
    # Url = f'https://login.minecraft.net?user={Username}&password={Password}&version=13'
    Url = "https://authserver.mojang.com/authenticate"
    # LoginInfo = requests.post(Url)
    # LoginInfoList = LoginInfo.split(':')
    # SessionID = LoginInfoList[3]
    token = str(uuid.uuid4())
    requestData = GetAuthenticationBody(Username, Password, token)
    response = requests.post(url=Url, json=requestData)
    responseData = response.json()

    SessionID = responseData['accessToken']
    return SessionID

def GetAuthenticationBody(username, password, token):
    body = {
        "agent":  {
            "name": "Minecraft",
            "version": 1
        },
        "username": username,
        "password": password,
        "clientToken": token,
        "requestUser": True
    }
    return body