import argparse
import swagger_client
import api
from auth_config import AuthConfig

args = ""
parser = argparse.ArgumentParser(prog='CloudMoreCLI', description="CloudMore REST API Client CLI")
parser.add_argument("-c","--cmd",metavar="Command (API Function Name)",required=True)
parser.add_argument("-seller","--seller",metavar="Seller ID",required=False)
parser.add_argument("-reseller","--reseller",metavar="Reseller ID",required=False)
parser.add_argument("-organization","--organization",metavar="Organization ID",required=False)
parser.add_argument("-subscription","--subscription",metavar="Subscription ID",required=False)
parser.add_argument("-service","--service",metavar="Service ID",required=False)
parser.add_argument("-webhook","--webhook",metavar="WebHook ID",required=False)
parser.add_argument("-user","--user",metavar="User ID",required=False)
parser.add_argument("-task","--task",metavar="Task ID",required=False)
parser.add_argument("-billingline","--billingline",metavar="Billing Line ID",required=False)
parser.add_argument("-startdate","--startdate",metavar="Start Date",required=False)
parser.add_argument("-enddate","--enddate",metavar="End Date",required=False)
parser.add_argument("-active","--active",metavar="Show only active *",required=False)
parser.add_argument("-remove-action","--remove-action",metavar="Remove subscription action, either delete or cancel",required=False)
parser.add_argument("-include-deleted","--include-deleted",metavar="Include Deleted Subscriptions",required=False)
parser.add_argument("-u","--username",metavar="Auth: CloudMore Username",required=True)
parser.add_argument("-p","--password",metavar="Auth: CloudMore Password",required=True)
parser.add_argument("-s","--secret",metavar="Auth: API Secret",required=True)
parser.add_argument("-client","--client-id",metavar="Auth: Client ID",required=False)
parser.add_argument("-g","--grant-type",metavar="Auth: Grant Type",required=False)
parser.add_argument("-scope","--scope",metavar="Auth: Scope",required=False)
parser.add_argument("-j","--data",metavar="Request Body as JSON",required=False)

args = parser.parse_args()




def main():
    try:
        print("CloudMore REST API Client CLI")

        print("")
        auth_config = AuthConfig(username=args.username,password=args.password,client_secret=args.secret)
        api.authenticate(auth_config)

        if args.cmd == 'GetSellerResellerById':
            api.getSellerResellerById(args.seller,args.reseller)

        # WebHooks API
        if args.cmd == 'GetSellerWebHookById':
            api.getSellerWebhookById(args.seller, args.webhook)
        if args.cmd == 'GetAllSellerWebHooks':
            api.getAllSellerWebHooks(args.seller)
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

            api.createWebHook(args.seller,args.data)
        if args.cmd == 'UpdateWebHook':
            api.updateWebHook(args.seller,args.webhook,args.data)
        if args.cmd == 'DeleteWebHook':
            api.deleteWebHook(args.seller, args.webhook)

        # Reseller Organizations

        if args.cmd == 'GetAllResellerOrganizations':
            api.getAllResellerOrganizations(args.reseller,args.active)
        if args.cmd == 'GetResellerOrganizationById':
            api.getResellerOrganizationById(args.reseller,args.organization)
        if args.cmd == 'CreateResellerOrganization':
            api.createResellerOrganization(args.reseller, args.data)
        if args.cmd == 'UpdateResellerOrganizationById':
            api.updateResellerOrganizationById(args.reseller,args.organization,args.data)
        if args.cmd == 'DeleteResellerOrganizationById':
            api.deleteResellerOrganizationById(args.reseller,args.organization)

        # Reseller Organization Users

        if args.cmd == 'CreateResellerOrganizationUser':
            api.CreateResellerOrganizationUserById(args.reseller,args.organization,args.data)
        if args.cmd == 'GetResellerOrganizationUserById':
            api.GetResellerOrganizationUserById(args.reseller,args.organization,args.user)
        if args.cmd == 'GetAllResellerOrganizationUsers':
                api.GetAllResellerOrganizationUsers(args.reseller, args.organization)
        if args.cmd == 'RemoveResellerOrganizationUserById':
            api.RemoveResellerOrganizationUserById(args.reseller, args.organization, args.user)
        if args.cmd == 'UpdateResellerOrganizationUserById':
            api.UpdateResellerOrganizationUserById(args.reseller, args.organization, args.user,args.data)

        # Service Categories API

        if args.cmd == 'GetServiceCategories':
            api.GetServiceCategories()

        # Seller Subscription API

        if args.cmd == 'CreateSellerSubscription':
            api.CreateSellerSubscription(args.seller,args.data)
        if args.cmd == 'RemoveSellerSubscriptionById':
            api.RemoveSellerSubscriptionById(args.seller,args.subscription,args.removeaction)
        if args.cmd == 'GetAllSellerSubscriptions':
            api.GetAllSellerSubscriptions(args.seller)
        if args.cmd == 'GetSellerSubscriptionById':
            api.GetSellerSubscriptionById(args.seller,args.subscription)
        if args.cmd == 'GetSellerSubscriptionByServiceId':
            api.GetSellerSubscriptionsByServiceId(args.seller,args.service)
        if args.cmd == 'UpdateSellerSubscriptionByIdSetLicenseKey':
            api.UpdateSellerSubscriptionByIdSetLicenseKey(args.seller, args.subscription, args.data)

        # Seller Services API

        if args.cmd == 'GetSellerServiceById':
            api.GetSellerServiceById(args.seller,args.service)
        if args.cmd == 'GetAllSellerServices':
            api.GetAllSellerServices(args.seller)
        if args.cmd == 'GetSellerServiceCustomPropertiesById':
            api.GetSellerServiceCustomPropertiesById(args.seller,args.service)
        if args.cmd == 'CreateSellerServiceBySellerId':
            api.CreateSellerServiceBySellerId(args.seller,args.data)
        if args.cmd == 'RemoveSellerServiceById':
            api.RemoveSellerServiceById(args.seller,args.service)
        if args.cmd == 'UpdateSellerServiceById':
            api.UpdateSellerServiceById(args.seller, args.service, args.data)
        if args.cmd == 'GetSellerServiceResellers':
            api.GetSellerServiceResellers(args.seller)

        # Seller Service Publish API

        if args.cmd == 'SellerServicePublishById':
            api.SellerServicePublishById(args.seller,args.service,args.data)

        # Seller Service Products API

        if args.cmd == 'CreateSellerServiceProductById':
            api.CreateSellerServiceProductById(args.seller,args.service,args.data)
        if args.cmd == 'GetSellerServiceProductById':
            api.GetSellerServiceProductById(args.seller,args.service,args.product)
        if args.cmd == 'GetAllSellerServiceProducts':
            api.GetAllSellerServiceProducts(args.seller,args.service)
        if args.cmd == 'RemoveSellerServiceProductById':
            api.RemoveSellerServiceProductById(args.seller,args.service,args.product)
        if args.cmd == 'UpdateSellerServiceProductById':
            api.UpdateSellerServiceProductById(args.seller, args.service,args.product,args.data)

        # Seller Service Product Addons API

        if args.cmd == 'CreateSellerServiceProductAddon':
            api.CreateSellerServiceProductAddon(args.seller,args.service,args.product,args.data)
        if args.cmd == 'RemoveSellerServiceProductAddonById':
            api.RemoveSellerServiceProductAddonById(args.seller,args.service,args.product,args.addon)
        if args.cmd == 'UpdateSellerServiceProductAddon':
            api.UpdateSellerServiceProductAddon(args.seller,args.service,args.product,args.addon,args.data)
        if args.cmd == 'GetAllSellerServiceProductAddons':
            api.GetAllSellerServiceProductAddons(args.seller, args.service)

        # Seller Service Consumptions API

        if args.cmd == 'GetAllSellerServiceConsumptionSubscriptions':
            api.GetAllSellerServiceConsumptionSubscriptions(args.seller,args.data)
        if args.cmd == 'SubmitSellerServiceConsumption':
            api.SubmitSellerServiceConsumption(args.seller,args.data)

        # Seller Service Bulk Consumptions API

        if args.cmd == 'GetStatusOfBulkConsumptionTaskById':
            api.GetStatusOfBulkConsumptionTaskById(args.seller,args.task)
        if args.cmd == 'SubmitBulkConsumptionTaskBySellerId':
            api.SubmitBulkConsumptionTaskBySellerId(args.seller,args.data)

        # Seller Reseller Manual Billing Line API

        if args.cmd == 'GetManualBillingLineById':
            api.GetManualBillingLineById(args.seller,args.reseller,args.billingline)
        if args.cmd == 'GetAllManualBillingLinesByResellerId':
            api.GetAllManualBillingLinesByResellerId(args.seller,args.reseller,args.startdate,args.enddate)
        if args.cmd == 'CreateManualBillingLineByResellerId':
            api.CreateManualBillingLineByResellerId(args.seller,args.reseller,args.data)
        if args.cmd == 'RemoveManualBillingLineById':
            api.RemoveManualBillingLineById(args.seller, args.reseller,args.billingline)


        # Seller Price List API


    except Exception as e:
        print(e)
        return



if __name__ == '__main__':
    main()