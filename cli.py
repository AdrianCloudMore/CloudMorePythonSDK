import argparse
import asyncio
import swagger_client
import api
from auth_config import AuthConfig

args = ""
parser = argparse.ArgumentParser(prog='CloudMoreCLI', description="CloudMore REST API Client CLI")
parser.add_argument("-c","--cmd",metavar="Command (API Function Name)",required=True)
parser.add_argument("-sid","--sid",metavar="Seller ID",required=False)
parser.add_argument("-rid","--rid",metavar="Reseller ID",required=False)
parser.add_argument("-u","--username",metavar="Auth: CloudMore Username",required=True)
parser.add_argument("-p","--password",metavar="Auth: CloudMore Password",required=True)
parser.add_argument("-s","--secret",metavar="Auth: API Secret",required=True)
parser.add_argument("-client","--client-id",metavar="Auth: Client ID",required=False)
parser.add_argument("-g","--grant-type",metavar="Auth: Grant Type",required=False)
parser.add_argument("-scope","--scope",metavar="Auth: Scope",required=False)


args = parser.parse_args()




async def main():
    try:
        print("CloudMore REST API Client")

        print("")
        auth_config = AuthConfig(username=args.username,password=args.password,client_secret=args.secret)
        await api.authenticate(auth_config)

        if args.cmd == 'GetSellerResellerById':
            await api.getSellerResellerById(args.sid,args.rid)

    except Exception as e:
        print(e)
        return



if __name__ == '__main__':
    asyncio.run(main())