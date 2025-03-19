import argparse
import swagger_client
import api
from auth_config import AuthConfig

args = ""
parser = argparse.ArgumentParser(prog='CloudMoreCLI', description="CloudMore REST API Client CLI")
parser.add_argument("-c","--cmd",metavar="Command (API Function Name)",required=True)
parser.add_argument("-sid","--sid",metavar="Seller ID",required=False)
parser.add_argument("-rid","--rid",metavar="Reseller ID",required=False)
parser.add_argument("-oid","--oid",metavar="Organization ID",required=False)
parser.add_argument("-wid","--wid",metavar="WebHook ID",required=False)
parser.add_argument("-u","--username",metavar="Auth: CloudMore Username",required=True)
parser.add_argument("-p","--password",metavar="Auth: CloudMore Password",required=True)
parser.add_argument("-s","--secret",metavar="Auth: API Secret",required=True)
parser.add_argument("-client","--client-id",metavar="Auth: Client ID",required=False)
parser.add_argument("-g","--grant-type",metavar="Auth: Grant Type",required=False)
parser.add_argument("-scope","--scope",metavar="Auth: Scope",required=False)
parser.add_argument("-j","--data",metavar="API Function Parameters as JSON",required=False)


args = parser.parse_args()




def main():
    try:
        print("CloudMore REST API Client CLI")

        print("")
        auth_config = AuthConfig(username=args.username,password=args.password,client_secret=args.secret)
        api.authenticate(auth_config)

        if args.cmd == 'GetSellerResellerById':
            api.getSellerResellerById(args.sid,args.rid)
        if args.cmd == 'GetSellerWebHookById':
            api.getSellerWebhookById(args.sid, args.wid)
        if args.cmd == 'GetAllSellerWebHooks':
            api.getAllSellerWebHooks(args.sid)
        if args.cmd == 'CreateWebHook':


         #   sellerWebHookCreateViewModel = {
         #       "messageToSendType": "OnlyTriggerAction",
         #       "basicAuthPassword": "string",
         #       "basicAuthUserName": "string",
         #       "httpHeader": "string",
         #       "url": "string",
         #       "serviceId": "string",
         #       "triggerEventType": "BrokerAddService",
         #       "name": "string"
         #   }

            api.createWebHook(args.sid,args.data)
        if args.cmd == 'UpdateWebHook':
            api.updateWebHook(args.sid,args.wid,args.data)
        if args.cmd == 'DeleteWebHook':
            api.deleteWebHook(args.sid, args.wid)

        # Reseller Organizations

        if args.cmd == 'GetAllResellerOrganizations':
            api.getAllResellerOrganizations(args.rid)
        if args.cmd == 'GetResellerOrganizationById':
            api.getResellerOrganizationById(args.rid,args.oid)
        if args.cmd == 'CreateResellerOrganization':
            api.createResellerOrganization(args.rid, args.oid, args.data)
        if args.cmd == 'UpdateResellerOrganizationById':
            api.updateResellerOrganizationById(args.rid,args.oid,args.data)
        if args.cmd == 'DeleteResellerOrganizationById':
            api.deleteResellerOrganizationById(args.rid,args.oid)

    except Exception as e:
        print(e)
        return



if __name__ == '__main__':
    main()