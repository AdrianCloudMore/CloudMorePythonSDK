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

# WebHooks API

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

def CreateSellerSubscription(sellerId, createSellerSubscriptionViewModel):
    api_instance = swagger_client.SellerSubscriptionsApi(api_client=api_client)
    data = api_instance.api_sellers_by_seller_id_subscriptions_by_subscription_id_get(sellerId,createSellerSubscriptionViewModel)
    print(data)
    return data

def GetSellerSubscriptionById(sellerId,subscriptionId):
    api_instance = swagger_client.SellerSubscriptionsApi(api_client=api_client)
    data = api_instance.api_sellers_by_seller_id_subscriptions_by_subscription_id_get(sellerId,subscriptionId)
    print(data)
    return data

def GetAllSellerSubscriptions(sellerId):
    api_instance = swagger_client.SellerSubscriptionsApi(api_client=api_client)
    data = api_instance.api_sellers_by_seller_id_subscriptions_get(sellerId)
    print(data)
    return data

def GetSellerSubscriptionsByServiceId(sellerId,serviceId):
    api_instance = swagger_client.SellerSubscriptionsApi(api_client=api_client)
    data = api_instance.api_sellers_by_seller_id_subscriptions_service_by_service_id_get(sellerId,serviceId)
    print(data)
    return data

def UpdateSellerSubscriptionByIdSetLicenseKey(sellerId, subscriptionId,updateSellerSubscriptionSetLicenseKeyViewModel):
    api_instance = swagger_client.SellerSubscriptionsApi(api_client=api_client)
    data = api_instance.api_sellers_by_seller_id_subscriptions_set_license_key_by_subscription_id_put(sellerId,subscriptionId,updateSellerSubscriptionSetLicenseKeyViewModel)
    print(data)
    return data

def RemoveSellerSubscriptionById(sellerId,subscriptionId,removeAction = "Delete"):
    api_instance = swagger_client.SellerSubscriptionsApi(api_client=api_client)
    data = api_instance.api_sellers_by_seller_id_subscriptions_by_subscription_id_delete(sellerId,subscriptionId,removeAction)
    print(data)
    return data


# Seller Services API

def GetSellerServiceCustomPropertiesById(sellerId,serviceId):
    api_instance = swagger_client.SellerServicesApi(api_client=api_client)
    data = api_instance.api_sellers_by_seller_id_services_by_id_custom_properties_data_get(sellerId,serviceId)
    print(data)
    return data


def CreateSellerServiceBySellerId(sellerId,createSellerServiceViewModel):
    api_instance = swagger_client.SellerServicesApi(api_client=api_client)
    data = api_instance.api_sellers_by_seller_id_services_post(sellerId,createSellerServiceViewModel)
    print(data)
    return data


def RemoveSellerServiceById(sellerId,serviceId):
    api_instance = swagger_client.SellerServicesApi(api_client=api_client)
    data = api_instance.api_sellers_by_seller_id_services_by_id_delete(sellerId,serviceId)
    print(data)
    return data

def GetSellerServiceById(sellerId,serviceId):
    api_instance = swagger_client.SellerServicesApi(api_client=api_client)
    data = api_instance.api_sellers_by_seller_id_services_by_id_get(sellerId,serviceId)
    print(data)
    return data

def UpdateSellerServiceById(sellerId,serviceId,updateSellerServiceViewModel):
    api_instance = swagger_client.SellerServicesApi(api_client=api_client)
    data = api_instance.api_sellers_by_seller_id_services_by_id_put(sellerId,serviceId,updateSellerServiceViewModel)
    print(data)
    return data

def GetSellerServiceResellers(sellerId, serviceId):
    api_instance = swagger_client.SellerServicesApi(api_client=api_client)
    data = api_instance.api_sellers_by_seller_id_services_by_service_id_resellers_get(sellerId,serviceId)
    print(data)
    return data

def GetAllSellerServices(sellerId):
    api_instance = swagger_client.SellerServicesApi(api_client=api_client)
    data = api_instance.api_sellers_by_seller_id_services_get(sellerId)
    print(data)
    return data

# Seller Service Publish API

def SellerServicePublishById(sellerId,serviceId,updateSellerServicePublishViewModel):
    api_instance = swagger_client.SellerServicePublishApi(api_client=api_client)
    data = api_instance.api_sellers_by_seller_id_services_by_id_publish_put(sellerId,serviceId,updateSellerServicePublishViewModel)
    print(data)
    return data

# Seller Service Products API


def CreateSellerServiceProductById(sellerId,serviceId,createSellerServiceProductViewModel):
    api_instance = swagger_client.SellerServiceProductsApi(api_client=api_client)
    data = api_instance.api_sellers_by_seller_id_services_by_service_id_products_post(sellerId,serviceId,createSellerServiceProductViewModel)
    print(data)
    return data

def GetSellerServiceProductById(sellerId,serviceId,productId):
    api_instance = swagger_client.SellerServiceProductsApi(api_client=api_client)
    data = api_instance.api_sellers_by_seller_id_services_by_service_id_products_by_id_get(sellerId,serviceId,productId)
    print(data)
    return data

def GetAllSellerServiceProducts(sellerId,serviceId):
    api_instance = swagger_client.SellerServiceProductsApi(api_client=api_client)
    data = api_instance.api_sellers_by_seller_id_services_by_service_id_products_get(sellerId,serviceId)
    print(data)
    return data

def RemoveSellerServiceProductById(sellerId,serviceId,productId):
    api_instance = swagger_client.SellerServiceProductsApi(api_client=api_client)
    data = api_instance.api_sellers_by_seller_id_services_by_service_id_products_by_id_delete(sellerId,serviceId,productId)
    print(data)
    return data


def UpdateSellerServiceProductById(sellerId,serviceId,productId,updateSellerServiceProductViewModel):
    api_instance = swagger_client.SellerServiceProductsApi(api_client=api_client)
    data = api_instance.api_sellers_by_seller_id_services_by_service_id_products_by_id_put(sellerId,serviceId,productId,updateSellerServiceProductViewModel)
    print(data)
    return data


# Seller Service Product Addons API

def CreateSellerServiceProductAddon(sellerId,serviceId,productId, createSellerServiceProductAddonViewModel):
    api_instance = swagger_client.SellerServiceProductAddonsApi(api_client=api_client)
    data = api_instance.api_sellers_by_seller_id_services_by_service_id_products_by_product_id_addons_post(sellerId,serviceId,productId,createSellerServiceProductAddonViewModel)
    print(data)
    return data

def RemoveSellerServiceProductAddonById(sellerId,serviceId,productId,addonId):
    api_instance = swagger_client.SellerServiceProductAddonsApi(api_client=api_client)
    data = api_instance.api_sellers_by_seller_id_services_by_service_id_products_by_product_id_addons_by_id_delete(sellerId,serviceId,productId,addonId)
    print(data)
    return data

def UpdateSellerServiceProductAddon(sellerId,serviceId,productId, addonId,updateSellerServiceProductAddonViewModel):
    api_instance = swagger_client.SellerServiceProductAddonsApi(api_client=api_client)
    data = api_instance.api_sellers_by_seller_id_services_by_service_id_products_by_product_id_addons_by_id_put(sellerId,serviceId,productId,addonId,updateSellerServiceProductAddonViewModel)
    print(data)
    return data

def GetAllSellerServiceProductAddons(sellerId,serviceId):
    api_instance = swagger_client.SellerServiceProductAddonsApi(api_client=api_client)
    data = api_instance.api_sellers_by_seller_id_services_by_service_id_products_by_product_id_addons_get(sellerId,serviceId)
    print(data)
    return data

# Seller Service Consumptions API

def GetAllSellerServiceConsumptionSubscriptions(sellerId, sellerServiceConsumptionsFilterViewModel):
    api_instance = swagger_client.SellerServiceConsumptionsApi(api_client=api_client)
    data = api_instance.api_sellers_by_seller_id_services_consumptions_post(sellerId,sellerServiceConsumptionsFilterViewModel)
    print(data)
    return data

def SubmitSellerServiceConsumption(sellerId, sellerServiceConsumptionsCreateViewModel):
    api_instance = swagger_client.SellerServiceConsumptionsApi(api_client=api_client)
    data = api_instance.api_sellers_by_seller_id_services_consumptions_put(sellerId,sellerServiceConsumptionsCreateViewModel)
    print(data)
    return data


# Seller Service Bulk Consumptions API

def GetStatusOfBulkConsumptionTaskById(sellerId, taskId):
    api_instance = swagger_client.SellerServiceBulkConsumptionsApi(api_client=api_client)
    data = api_instance.api_sellers_by_seller_id_services_bulkconsumptions_by_task_id_get(sellerId,taskId)
    print(data)
    return data

def SubmitBulkConsumptionTaskBySellerId(sellerId, sellerServiceBulkConsumptionViewModel):
    api_instance = swagger_client.SellerServiceBulkConsumptionsApi(api_client=api_client)
    data = api_instance.api_sellers_by_seller_id_services_bulkconsumptions_post(sellerId,sellerServiceBulkConsumptionViewModel)
    print(data)
    return data

# Seller Reseller Manual Billing Line API


def GetManualBillingLineById(sellerId, resellerId,billingLineId):
    api_instance = swagger_client.SellerResellersManualBillingLineApi(api_client=api_client)
    data = api_instance.api_sellers_by_seller_id_resellers_by_reseller_id_manualbilling_by_id_get(sellerId,resellerId,billingLineId)
    print(data)
    return data

def GetAllManualBillingLinesByResellerId(sellerId,resellerId,billingStartDate,billingEndDate):
    api_instance = swagger_client.SellerResellersManualBillingLineApi(api_client=api_client)
    data = api_instance.api_sellers_by_seller_id_resellers_by_reseller_id_manualbilling_get(sellerId,resellerId,billingStartDate,billingEndDate)
    print(data)
    return data

def CreateManualBillingLineByResellerId(sellerId, resellerId,manualBillingLineCreateViewModel):
    api_instance = swagger_client.SellerResellersManualBillingLineApi(api_client=api_client)
    data = api_instance.api_sellers_by_seller_id_resellers_by_reseller_id_manualbilling_post(sellerId,resellerId,manualBillingLineCreateViewModel)
    print(data)
    return data

def RemoveManualBillingLineById(sellerId, resellerId,billingLineId):
    api_instance = swagger_client.SellerResellersManualBillingLineApi(api_client=api_client)
    data = api_instance.api_sellers_by_seller_id_resellers_by_reseller_id_manualbilling_by_billing_line_id_delete(sellerId,resellerId,billingLineId)
    print(data)
    return data


# Seller Price List API


def GetSellerCustomServiceProductPricesById(sellerId, serviceId ,currencyCode):
    api_instance = swagger_client.SellerPriceListApi(api_client=api_client)
    data = api_instance.api_sellers_by_seller_id_services_by_service_id_pricelist_get(sellerId,serviceId,currencyCode)
    print(data)
    return data

def UpdateSellerCustomServiceProductPricesById(sellerId, serviceId ,sellerPriceListUpdateViewModel):
    api_instance = swagger_client.SellerPriceListApi(api_client=api_client)
    data = api_instance.api_sellers_by_seller_id_services_by_service_id_pricelist_put(sellerId,serviceId,sellerPriceListUpdateViewModel)
    print(data)
    return data

# Seller Organizations API


def GetSellerOrganizationById(sellerId, organizationId):
    api_instance = swagger_client.SellerOrganizationsApi(api_client=api_client)
    data = api_instance.api_sellers_by_seller_id_seller_organizations_by_id_get(sellerId,organizationId)
    print(data)
    return data

# Seller Email Templates API

def GetAllSellerEmailTemplates(sellerId):
    api_instance = swagger_client.SellerEmailTemplatesApi(api_client=api_client)
    data = api_instance.api_sellers_by_seller_id_settings_email_templates_get(sellerId)
    print(data)
    return data

# Seller Brokers API

def RemoveSellerResellerById(sellerId,resellerId):
    api_instance = swagger_client.SellerBrokersApi(api_client=api_client)
    data = api_instance.api_sellers_by_seller_id_brokers_by_id_delete(sellerId, resellerId)
    print(data)
    return data

def GetSellerResellerById(sellerId,resellerId):
    api_instance = swagger_client.SellerBrokersApi(api_client=api_client)
    data = api_instance.api_sellers_by_seller_id_brokers_by_id_get(sellerId, resellerId)
    print(data)
    return data

def UpdateSellerResellerById(sellerId,resellerId,sellerBrokerUpdateViewModel):
    api_instance = swagger_client.SellerBrokersApi(api_client=api_client)
    data = api_instance.api_sellers_by_seller_id_brokers_by_id_put(sellerId, resellerId,sellerBrokerUpdateViewModel)
    print(data)
    return data

def GetAllSellerAssociatedResellers(sellerId):
    api_instance = swagger_client.SellerBrokersApi(api_client=api_client)
    data = api_instance.api_sellers_by_seller_id_brokers_get(sellerId)
    print(data)
    return data

def CreateSellerReseller(sellerId,sellerBrokerCreateViewModel):
    api_instance = swagger_client.SellerBrokersApi(api_client=api_client)
    data = api_instance.api_sellers_by_seller_id_brokers_post(sellerId,sellerBrokerCreateViewModel)
    print(data)
    return data

# Seller Billing Reports API

def GetSellerResellerMonthlyBillingReportByResellerId(sellerId,sellerBrokerCreateViewModel):
    api_instance = swagger_client.SellerBillingReportsApi(api_client=api_client)
    data = api_instance.api_sellers_by_seller_id_billing_monthly_billing_per_reseller_get(sellerId,sellerBrokerCreateViewModel)
    print(data)
    return data

# Seller Administrator API

def GetSellerAdministratorById(sellerId,userId):
    api_instance = swagger_client.SellerAdministratorsApi(api_client=api_client)
    data = api_instance.api_sellers_by_seller_id_seller_administrators_by_id_get(sellerId,userId)
    print(data)
    return data

def GetAllSellerAdministrators(sellerId):
    api_instance = swagger_client.SellerAdministratorsApi(api_client=api_client)
    data = api_instance.api_sellers_by_seller_id_seller_administrators_get(sellerId)
    print(data)
    return data

def RemoveSellerAdministratorById(sellerId,userId):
    api_instance = swagger_client.SellerAdministratorsApi(api_client=api_client)
    data = api_instance.api_sellers_by_seller_id_seller_administrators_by_id_delete(sellerId,userId)
    print(data)
    return data

def UpdateSellerAdministratorById(sellerId,userId,sellerAdministratorUpdateViewModel):
    api_instance = swagger_client.SellerAdministratorsApi(api_client=api_client)
    data = api_instance.api_sellers_by_seller_id_seller_administrators_by_id_put(sellerId,userId,sellerAdministratorUpdateViewModel)
    print(data)
    return data

def CreateSellerAdministrator(sellerId,sellerAdministratorCreateViewModel):
    api_instance = swagger_client.SellerAdministratorsApi(api_client=api_client)
    data = api_instance.api_sellers_by_seller_id_seller_administrators_post(sellerId,sellerAdministratorCreateViewModel)
    print(data)
    return data

# Resellers API

def GetSellerResellerById(sellerId, resellerId):
    api_instance = swagger_client.ResellersApi(api_client=api_client)
    data = api_instance.api_sellers_by_seller_id_resellers_by_id_get(sellerId,resellerId)
    print(data)
    return data

def GetAllSellerResellers(sellerId):
    api_instance = swagger_client.ResellersApi(api_client=api_client)
    data = api_instance.api_sellers_by_seller_id_resellers_get(sellerId)
    print(data)
    return data

# Reseller Services API

def GetResellerServiceById(resellerId, serviceId):
    api_instance = swagger_client.ResellerServicesApi(api_client=api_client)
    data = api_instance.api_resellers_by_reseller_id_services_by_id_get(resellerId, serviceId)
    print(data)
    return data

def CreateResellerServiceById(resellerId, resellerServiceCreateViewModel):
    api_instance = swagger_client.ResellerServicesApi(api_client=api_client)
    data = api_instance.api_resellers_by_reseller_id_services_post(resellerId, resellerServiceCreateViewModel)
    print(data)
    return data

def RemoveResellerServiceById(resellerId, serviceId):
    api_instance = swagger_client.ResellerServicesApi(api_client=api_client)
    data = api_instance.api_resellers_by_reseller_id_services_by_id_delete(resellerId, serviceId)
    print(data)
    return data

def UpdateResellerServiceById(resellerId, serviceId, resellerServiceUpdateViewModel):
    api_instance = swagger_client.ResellerServicesApi(api_client=api_client)
    data = api_instance.api_resellers_by_reseller_id_services_by_id_put(resellerId, serviceId, resellerServiceUpdateViewModel)
    print(data)
    return data

def UpdateResellerServiceCustomPropertyDataById(resellerId, serviceId, resellerServiceCustomPropertyDataUpdateViewModel):
    api_instance = swagger_client.ResellerServicesApi(api_client=api_client)
    data = api_instance.api_resellers_by_reseller_id_services_by_service_id_patch(resellerId, serviceId, resellerServiceCustomPropertyDataUpdateViewModel)
    print(data)
    return data

def GetAllResellerSubscriptionsByServiceId(resellerId, serviceId):
    api_instance = swagger_client.ResellerServicesApi(api_client=api_client)
    data = api_instance.api_resellers_by_reseller_id_services_by_service_id_subscriptions_get(resellerId, serviceId)
    print(data)
    return data

def GetAllResellerServices(resellerId):
    api_instance = swagger_client.ResellerServicesApi(api_client=api_client)
    data = api_instance.api_resellers_by_reseller_id_services_get(resellerId)
    print(data)
    return data

# Reseller Service Products API

def GetResellerCustomServiceProduct(resellerId,serviceId,productId):
    api_instance = swagger_client.ResellerServiceProductsApi(api_client=api_client)
    data = api_instance.api_resellers_by_reseller_id_services_by_service_id_products_by_id_get(resellerId,serviceId,productId)
    print(data)
    return data

def GetAllResellerCustomServiceProducts(resellerId,serviceId):
    api_instance = swagger_client.ResellerServiceProductsApi(api_client=api_client)
    data = api_instance.api_resellers_by_reseller_id_services_by_service_id_products_get(resellerId,serviceId)
    print(data)
    return data

def CreateResellerCustomServiceProduct(resellerId,serviceId,resellerServiceProductCreateViewModel):
    api_instance = swagger_client.ResellerServiceProductsApi(api_client=api_client)
    data = api_instance.api_resellers_by_reseller_id_services_by_service_id_products_post(resellerId,serviceId,resellerServiceProductCreateViewModel )
    print(data)
    return data

def UpdateResellerCustomServiceProduct(resellerId,serviceId,productId,resellerServiceProductUpdateViewModel):
    api_instance = swagger_client.ResellerServiceProductsApi(api_client=api_client)
    data = api_instance.api_resellers_by_reseller_id_services_by_service_id_products_by_id_put(resellerId,serviceId,productId,resellerServiceProductUpdateViewModel )
    print(data)
    return data

def RemoveResellerCustomServiceProduct(resellerId,serviceId,productId):
    api_instance = swagger_client.ResellerServiceProductsApi(api_client=api_client)
    data = api_instance.api_resellers_by_reseller_id_services_by_service_id_products_by_id_delete(resellerId,serviceId,productId)
    print(data)
    return data


# Reseller Service Product Addons API



# resellers / :reseller ID / services / Azure Subscriptions


def getResellerAzureSubscriptions(resellerId):
    api_instance = swagger_client.ResellerAzureSubscriptionsApi(api_client=api_client)
    data = api_instance.api_resellers_by_reseller_id_services_azure_subscriptions_get(resellerId)
    print(data)
    return data