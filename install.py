import os
import zipfile
import shutil
import requests


def generateClient():
    link = None

    headers = {'Content-type': 'application/json'}

    with requests.post(url="https://generator.swagger.io/api/gen/clients/python",data='{ "options": { "packageName": "cloudmore_sdk" }, "swaggerUrl":"https://api.cloudmore.com/swagger/v1/swagger.json"}',params=None,headers=headers) as url:
        data = url.json()
        print(data)
        link = data.get("link")

    r = requests.get(link,allow_redirects=True)

    try:
        open('python_client_generated.zip', 'xb').write(r.content)

        zip_ref = zipfile.ZipFile('python_client_generated.zip', 'r')


        zip_ref.extractall()

        os.remove("python_client_generated.zip")
    except Exception as e:
        print(e)
   # source_folder = r"./python-client/*"
   # destination_folder = r"."

   # for file_name in os.listdir(source_folder):
   #     source = source_folder + file_name
   #     destination = destination_folder + file_name
  #      shutil.move(source, destination)
 #       print('Moved:', file_name)

#
def checkForUpdates():
    version = "v0.0.0"
    try:
        with open('api_version.txt', 'r') as file:
            version = file.read()
    except Exception as e:
        print(e)

    with requests.get("https://api.cloudmore.com/swagger/v1/swagger.json") as url:
        data = url.json()

    if data.get("info").get("version") == version:
        return 0

    return 1

def update():

    version = "v0.0.0"

    try:
        if os.path.isdir("swagger_client"):
            shutil.rmtree("swagger_client")
            shutil.rmtree("test")
            shutil.rmtree("docs")
            shutil.rmtree("build")
            os.remove("setup.py")
            os.remove("tox.ini")
            os.remove("requirements.txt")
            os.remove("test-requirements.txt")

        os.remove("api_version.txt")
    except Exception as e:
        print(e)

    generateClient()

    with requests.get("https://api.cloudmore.com/swagger/v1/swagger.json") as url:
        data = url.json()
        version = data.get("info").get("version")




    with open('api_version.txt', 'w') as file:
        file.write(version)

def main():
    try:

        print("Checking for updates ...")
        ret = checkForUpdates()
        if ret == 0:
            print("API Definition is up to date!")
        else:
            print ("Updating API Definition ....  ")
            update()
            print ("Done!")


    except Exception as e:
        print(e)

if __name__ == '__main__':
    main()
