import requests

global API_DEFINITION_VERSION

API_DEFINITION_VERSION = "v1.07.0"


def CheckForUpdates():

    with requests.get("https://api.cloudmore.com/swagger/v1/swagger.json") as url:
        data = url.json()
        if data.get("info").get("version") == API_DEFINITION_VERSION:
            return 0

    return 1

async def Update():

    pass

def main():
    try:

        ret = CheckForUpdates()
        if ret == 0:
            print("API Definition is up to date!")
        else:
            print ("Updating API Definition ....  ")

    except Exception as e:
        print(e)

if __name__ == '__main__':
    main()
