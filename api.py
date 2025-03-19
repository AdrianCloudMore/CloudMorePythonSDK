import swagger_client
from datetime import datetime, timedelta
import requests


config = swagger_client.Configuration()
config.host = "https://api-dev.cloudmore.com"
api_client = swagger_client.ApiClient(configuration=config)


def authenticate(auth_config):
    """Retrieve and store access token for Cloudmore API"""
    url = f"{api_client.configuration.host}/connect/token"
    payload = {
        "client_id": auth_config.client_id,
        "client_secret": auth_config.client_secret,
        "grant_type": auth_config.grant_type,
        "scope": auth_config.scope,
        "username": auth_config.username,
        "password": auth_config.password
    }

    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    response = requests.post(url, payload, headers)
    if response.status_code == 200:
        data = response.json()
        api_client.configuration.access_token = data["access_token"]
        api_client.set_default_header("Authorization", "%s %s" % ("Bearer", data["access_token"]))
        api_client.configuration.token_expiry = datetime.now() + timedelta(seconds=data["expires_in"])
    else:
        print(response)
        raise Exception("Failed to authenticate with CloudMore API")

def getSellerResellerById(sellerId, resellerId):
    api_instance = swagger_client.ResellersApi(api_client=api_client)
    data = api_instance.api_sellers_by_seller_id_resellers_by_id_get(sellerId,resellerId)
    print(data)
    return data


def getSellerWebhookById(sellerId,webhookId):
    api_instance = swagger_client.WebHooksApi(api_client=api_client)
    data = api_instance.api_sellers_by_seller_id_webhooks_by_id_get(sellerId,webhookId)
    print(data)
    return data

def getAllSellerWebHooks(sellerId):
    api_instance = swagger_client.WebHooksApi(api_client=api_client)
    data = api_instance.api_sellers_by_seller_id_webhooks_get(sellerId)
    print(data)
    return data

def updateWebHook(sellerId,webhookId, sellerWebHookUpdateViewModel):
    api_instance = swagger_client.WebHooksApi(api_client=api_client)
    data = api_instance.api_sellers_by_seller_id_webhooks_by_id_put(sellerId,webhookId, sellerWebHookUpdateViewModel)
    print(data)
    return data

def createWebHook(sellerId,sellerWebHookCreateViewModel):
    api_instance = swagger_client.WebHooksApi(api_client=api_client)
    data = api_instance.api_sellers_by_seller_id_webhooks_post(sellerId,sellerWebHookCreateViewModel)
    print(data)
    return data

def deleteWebHook(sellerId,webhookId):
    api_instance = swagger_client.WebHooksApi(api_client=api_client)
    data = api_instance.api_sellers_by_seller_id_webhooks_by_id_delete(sellerId,webhookId)
    print(data)
    return data


# Resellers / :Reseller ID / Organizations


def getAllResellerOrganizations(resellerId, showActive = True):
    api_instance = swagger_client.OrganizationsApi(api_client=api_client)
    data = api_instance.api_resellers_by_reseller_id_organizations_get(resellerId, showActive)
    print(data)
    return data

def getResellerOrganizationById(resellerId, organizationId):
    api_instance = swagger_client.OrganizationsApi(api_client=api_client)
    data = api_instance.api_resellers_by_reseller_id_organizations_by_id_get(resellerId,organizationId)
    print(data)
    return data

def createResellerOrganization(resellerId, organizationCreateViewModel):
    api_instance = swagger_client.OrganizationsApi(api_client=api_client)
    data = api_instance.api_resellers_by_reseller_id_organizations_post(resellerId,organizationCreateViewModel)
    print(data)
    return data

def updateResellerOrganizationById(resellerId, organizationId, organizationUpdateViewModel):
    api_instance = swagger_client.OrganizationsApi(api_client=api_client)
    data = api_instance.api_resellers_by_reseller_id_organizations_by_id_put(resellerId,organizationId,organizationUpdateViewModel)
    print(data)
    return data

def deleteResellerOrganizationById(resellerId, organizationId):
    api_instance = swagger_client.OrganizationsApi(api_client=api_client)
    data = api_instance.api_resellers_by_reseller_id_organizations_by_id_delete(resellerId,organizationId)
    print(data)
    return data


# Users API

def CreateResellerOrganizationUserById(resellerId, organizationId, createResellerOrganizationUserViewModel):
    api_instance = swagger_client.UsersApi(api_client=api_client)
    data = api_instance.api_resellers_by_reseller_id_organizations_by_organization_id_users_post(resellerId,organizationId,createResellerOrganizationUserViewModel)
    print(data)
    return data

def RemoveResellerOrganizationUserById(resellerId, organizationId,userId):
    api_instance = swagger_client.UsersApi(api_client=api_client)
    data = api_instance.api_resellers_by_reseller_id_organizations_by_organization_id_users_by_id_delete(resellerId,organizationId,userId)
    print(data)
    return data

def UpdateResellerOrganizationUserById(resellerId,organizationId,userId,updateResellerOrganizationUserViewModel):
    api_instance = swagger_client.UsersApi(api_client=api_client)
    data = api_instance.api_resellers_by_reseller_id_organizations_by_organization_id_users_by_id_put(resellerId,organizationId,userId,updateResellerOrganizationUserViewModel)
    print(data)
    return data

def GetResellerOrganizationUserById(resellerId,organizationId,userId):
    api_instance = swagger_client.UsersApi(api_client=api_client)
    data = api_instance.api_resellers_by_reseller_id_organizations_by_organization_id_users_by_id_get(resellerId,organizationId,userId)
    print(data)
    return data

def GetAllResellerOrganizationUsers(resellerId, organizationId):
    api_instance = swagger_client.UsersApi(api_client=api_client)
    data = api_instance.api_resellers_by_reseller_id_organizations_by_organization_id_users_get(resellerId,organizationId)
    print(data)
    return data


# Service Categories API


def GetServiceCategories():
    api_instance = swagger_client.ServiceCategoriesApi(api_client=api_client)
    data = api_instance.api_services_categories_get()
    print(data)
    return data

# Seller Subscriptions API

def RemoveSellerSubscriptionById(sellerId,subscriptionId,removeAction = "Delete"):
    api_instance = swagger_client.SellerSubscriptionsApi(api_client=api_client)
    data = api_instance.api_sellers_by_seller_id_subscriptions_by_subscription_id_delete(sellerId,subscriptionId,removeAction)
    print(data)
    return data


# resellers / :reseller ID / services / Azure Subscriptions


def getResellerAzureSubscriptions(resellerId):
    api_instance = swagger_client.ResellerAzureSubscriptionsApi(api_client=api_client)
    data = api_instance.api_resellers_by_reseller_id_services_azure_subscriptions_get(resellerId)
    print(data)
    return data