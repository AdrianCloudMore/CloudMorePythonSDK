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


# Organizations API


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

def GetResellerCustomServiceProductAddon(resellerId,serviceId,productId,addonId):
    api_instance = swagger_client.ResellerServiceProductAddonsApi(api_client=api_client)
    data = api_instance.api_resellers_by_reseller_id_services_by_service_id_products_by_product_id_addons_by_id_get(resellerId,serviceId,productId,addonId)
    print(data)
    return data

def GetAllResellerCustomServiceProductAddons(resellerId,serviceId,productId):
    api_instance = swagger_client.ResellerServiceProductAddonsApi(api_client=api_client)
    data = api_instance.api_resellers_by_reseller_id_services_by_service_id_products_by_product_id_addons_get(resellerId,serviceId,productId)
    print(data)
    return data

def RemoveResellerCustomServiceProductAddon(resellerId,serviceId,productId,addonId):
    api_instance = swagger_client.ResellerServiceProductAddonsApi(api_client=api_client)
    data = api_instance.api_resellers_by_reseller_id_services_by_service_id_products_by_product_id_addons_by_id_delete(resellerId,serviceId,productId,addonId)
    print(data)
    return data

def UpdateResellerCustomServiceProductAddon(resellerId,serviceId,productId,addonId,resellerServiceProductAddonUpdateViewModel):
    api_instance = swagger_client.ResellerServiceProductAddonsApi(api_client=api_client)
    data = api_instance.api_resellers_by_reseller_id_services_by_service_id_products_by_product_id_addons_by_id_put(resellerId,serviceId,productId,addonId,resellerServiceProductAddonUpdateViewModel)
    print(data)
    return data

def CreateResellerCustomServiceProductAddon(resellerId,serviceId,productId,resellerServiceProductAddonCreateViewModel):
    api_instance = swagger_client.ResellerServiceProductAddonsApi(api_client=api_client)
    data = api_instance.api_resellers_by_reseller_id_services_by_service_id_products_by_product_id_addons_post(resellerId,serviceId,productId,resellerServiceProductAddonCreateViewModel)
    print(data)
    return data

# Reseller Service Consumptions API

def GetAllResellerServiceConsumptions(resellerId,resellerServiceConsumptionsFilterViewModel):
    api_instance = swagger_client.ResellerServiceConsumptionsApi(api_client=api_client)
    data = api_instance.api_resellers_by_reseller_id_services_consumptions_post(resellerId,resellerServiceConsumptionsFilterViewModel)
    print(data)
    return data

def CreateResellerServiceConsumption(resellerId,resellerServiceConsumptionsCreateViewModel):
    api_instance = swagger_client.ResellerServiceConsumptionsApi(api_client=api_client)
    data = api_instance.api_resellers_by_reseller_id_services_consumptions_put(resellerId,resellerServiceConsumptionsCreateViewModel)
    print(data)
    return data


# Reseller Roles API


def GetAllResellerAdministratorRoles(resellerId):
    api_instance = swagger_client.ResellerRolesApi(api_client=api_client)
    data = api_instance.api_resellers_by_reseller_id_reseller_roles_get(resellerId)
    print(data)
    return data


# Reseller Price List API

def GetResellerServiceSubscriptionCommitmentPrice(resellerId,serviceId,organizationId,subscriptionId):
    api_instance = swagger_client.ResellerPriceListApi(api_client=api_client)
    data = api_instance.api_resellers_by_reseller_id_services_by_service_id_pricelist_commitment_price_get(resellerId,serviceId,organizationId,subscriptionId)
    print(data)
    return data

def GetAllResellerProductPricesByServiceId(resellerId,serviceId,currencyCode):
    api_instance = swagger_client.ResellerPriceListApi(api_client=api_client)
    data = api_instance.api_resellers_by_reseller_id_services_by_service_id_pricelist_get(resellerId,serviceId,currencyCode)
    print(data)
    return data

def GetResellerServicePostRenewalPriceBySubscriptionId(resellerId,serviceId,organizationId,subscriptionId):
    api_instance = swagger_client.ResellerPriceListApi(api_client=api_client)
    data = api_instance.api_resellers_by_reseller_id_services_by_service_id_pricelist_post_renewal_price_get(resellerId,serviceId,organizationId,subscriptionId)
    print(data)
    return data

def UpdateResellerPriceListByServiceId(resellerId,serviceId,brokerPriceListUpdateViewModel):
    api_instance = swagger_client.ResellerPriceListApi(api_client=api_client)
    data = api_instance.api_resellers_by_reseller_id_services_by_service_id_pricelist_put(resellerId,serviceId,brokerPriceListUpdateViewModel)
    print(data)
    return data

# Reseller Payment Methods API

def CreateResellerPaymentMethod(resellerId, resellerPaymentMethodCreateViewModel):
    api_instance = swagger_client.ResellerPaymentMethodsApi(api_client=api_client)
    data = api_instance.api_resellers_by_reseller_id_paymentmethods_post(resellerId,resellerPaymentMethodCreateViewModel)
    print(data)
    return data

def DeleteResellerPaymentMethodById(resellerId,paymentMethodId):
    api_instance = swagger_client.ResellerPaymentMethodsApi(api_client=api_client)
    data = api_instance.api_resellers_by_reseller_id_paymentmethods_by_id_delete(resellerId,paymentMethodId)
    print(data)
    return data

def GetResellerPaymentMethodById(resellerId,paymentMethodId):
    api_instance = swagger_client.ResellerPaymentMethodsApi(api_client=api_client)
    data = api_instance.api_resellers_by_reseller_id_paymentmethods_by_id_get(resellerId,paymentMethodId)
    print(data)
    return data

def UpdateResellerPaymentMethodById(resellerId,paymentMethodId,resellerPaymentMethodUpdateViewModel):
    api_instance = swagger_client.ResellerPaymentMethodsApi(api_client=api_client)
    data = api_instance.api_resellers_by_reseller_id_paymentmethods_by_id_put(resellerId,paymentMethodId,resellerPaymentMethodUpdateViewModel)
    print(data)
    return data

def GerAllResellerPaymentMethods(resellerId):
    api_instance = swagger_client.ResellerPaymentMethodsApi(api_client=api_client)
    data = api_instance.api_resellers_by_reseller_id_paymentmethods_get(resellerId)
    print(data)
    return data


# Reseller Organization Groups API


def GetAllResellerOrganizationGroupById(resellerId):
    api_instance = swagger_client.ResellerOrganizationGroupsApi(api_client=api_client)
    data = api_instance.api_resellers_by_reseller_id_organization_groups_get(resellerId)
    print(data)
    return data

def CreateResellerOrganizationGroupById(resellerId,resellerOrganizationGroupCreateViewModel):
    api_instance = swagger_client.ResellerOrganizationGroupsApi(api_client=api_client)
    data = api_instance.api_resellers_by_reseller_id_organization_groups_post(resellerId,resellerOrganizationGroupCreateViewModel)
    print(data)
    return data

def GetResellerOrganizationGroupById(resellerId, groupId):
    api_instance = swagger_client.ResellerOrganizationGroupsApi(api_client=api_client)
    data = api_instance.api_resellers_by_reseller_id_organization_groups_by_id_get(resellerId, groupId)
    print(data)
    return data

def UpdateResellerOrganizationGroupById(resellerId, groupId,resellerOrganizationGroupUpdateViewModel):
    api_instance = swagger_client.ResellerOrganizationGroupsApi(api_client=api_client)
    data = api_instance.api_resellers_by_reseller_id_organization_groups_by_id_put(resellerId, groupId,resellerOrganizationGroupUpdateViewModel)
    print(data)
    return data

def DeleteResellerOrganizationGroupById(resellerId, groupId):
    api_instance = swagger_client.ResellerOrganizationGroupsApi(api_client=api_client)
    data = api_instance.api_resellers_by_reseller_id_organization_groups_by_id_delete(resellerId, groupId)
    print(data)
    return data

# Reseller Organization Group Members API

def AddNewResellerOrganizationGroupMember(resellerId, groupId, resellerOrganizationGroupMemberAddViewModel):
    api_instance = swagger_client.ResellerOrganizationGroupMembersApi(api_client=api_client)
    data = api_instance.api_resellers_by_reseller_id_organization_groups_by_group_id_members_post(resellerId, groupId,resellerOrganizationGroupMemberAddViewModel)
    print(data)
    return data

def GetResellerOrganizationGroupMembersByGroupId(resellerId, groupId):
    api_instance = swagger_client.ResellerOrganizationGroupMembersApi(api_client=api_client)
    data = api_instance.api_resellers_by_reseller_id_organization_groups_by_group_id_members_get(resellerId, groupId)
    print(data)
    return data

def DeleteResellerOrganizationGroupMemberById(resellerId, memberId):
    api_instance = swagger_client.ResellerOrganizationGroupMembersApi(api_client=api_client)
    data = api_instance.api_resellers_by_reseller_id_organization_groups_by_group_id_members_by_id_delete(resellerId, memberId)
    print(data)
    return data

# Reseller EMail Templates API

def GetAllResellerEmailTemplates(resellerId):
    api_instance = swagger_client.ResellerEmailTemplatesApi(api_client=api_client)
    data = api_instance.api_resellers_by_reseller_id_settings_email_templates_get(resellerId)
    print(data)
    return data

# Reseller CSP Subscriptions API

def GetAllResellerCSPSubscriptions(resellerId):
    api_instance = swagger_client.ResellerCspSubscriptionsApi(api_client=api_client)
    data = api_instance.api_resellers_by_reseller_id_services_csp_subscriptions_get(resellerId)
    print(data)
    return data

# Reseller CSP NCE Subscriptions API

def GetAllResellerCSPNCESubscriptions(resellerId):
    api_instance = swagger_client.ResellerCspNceSubscriptionsApi(api_client=api_client)
    data = api_instance.api_resellers_by_reseller_id_services_csp_nce_subscriptions_get(resellerId)
    print(data)
    return data


# Reseller Azure Subscriptions API

def GetAllResellerAzureSubscriptions(resellerId):
    api_instance = swagger_client.ResellerAzureSubscriptionsApi(api_client=api_client)
    data = api_instance.api_resellers_by_reseller_id_services_azure_subscriptions_get(resellerId)
    print(data)
    return data

# Reseller Administrators API

def GetAllResellerAdministrators(resellerId):
    api_instance = swagger_client.ResellerAdministratorsApi(api_client=api_client)
    data = api_instance.api_resellers_by_reseller_id_reseller_administrators_get(resellerId)
    print(data)
    return data

def GetResellerAdministratorById(resellerId,userId):
    api_instance = swagger_client.ResellerAdministratorsApi(api_client=api_client)
    data = api_instance.api_resellers_by_reseller_id_reseller_administrators_by_id_get(resellerId,userId)
    print(data)
    return data

def CreateResellerAdministratorById(resellerId,administratorCreateViewModel):
    api_instance = swagger_client.ResellerAdministratorsApi(api_client=api_client)
    data = api_instance.api_resellers_by_reseller_id_reseller_administrators_post(resellerId,administratorCreateViewModel)
    print(data)
    return data

def UpdateResellerAdministratorById(resellerId,userId,administratorUpdateViewModel):
    api_instance = swagger_client.ResellerAdministratorsApi(api_client=api_client)
    data = api_instance.api_resellers_by_reseller_id_reseller_administrators_by_id_put(resellerId,userId,administratorUpdateViewModel)
    print(data)
    return data

def DeleteResellerAdministratorById(resellerId,userId):
    api_instance = swagger_client.ResellerAdministratorsApi(api_client=api_client)
    data = api_instance.api_resellers_by_reseller_id_reseller_administrators_by_id_delete(resellerId,userId)
    print(data)
    return data

# Organization User Groups API

def GetAllOrganizationUserGroups(resellerId,organizationId):
    api_instance = swagger_client.OrganizationUserGroupsApi(api_client=api_client)
    data = api_instance.api_resellers_by_reseller_id_organizations_by_organization_id_user_groups_get(resellerId,organizationId)
    print(data)
    return data

def CreateOrganizationUserGroup(resellerId,organizationId,organizationUserGroupCreateViewModel):
    api_instance = swagger_client.OrganizationUserGroupsApi(api_client=api_client)
    data = api_instance.api_resellers_by_reseller_id_organizations_by_organization_id_user_groups_post(resellerId,organizationId, organizationUserGroupCreateViewModel)
    print(data)
    return data

def GetOrganizationUserGroupById(resellerId,organizationId):
    api_instance = swagger_client.OrganizationUserGroupsApi(api_client=api_client)
    data = api_instance.api_resellers_by_reseller_id_organizations_by_organization_id_user_groups_by_id_get(resellerId,organizationId)
    print(data)
    return data

def UpdateOrganizationUserGroupById(resellerId,organizationId, groupId,organizationUserGroupUpdateViewModel):
    api_instance = swagger_client.OrganizationUserGroupsApi(api_client=api_client)
    data = api_instance.api_resellers_by_reseller_id_organizations_by_organization_id_user_groups_by_id_put(resellerId,organizationId,groupId, organizationUserGroupUpdateViewModel)
    print(data)
    return data

def DeleteOrganizationUserGroupById(resellerId,organizationId):
    api_instance = swagger_client.OrganizationUserGroupsApi(api_client=api_client)
    data = api_instance.api_resellers_by_reseller_id_organizations_by_organization_id_user_groups_by_id_delete(resellerId,organizationId)
    print(data)
    return data

# Organization User Group Members API

def GetOrganizationUserGroupMemberById(resellerId,organizationId,groupId, memberId):
    api_instance = swagger_client.OrganizationUserGroupMembersApi(api_client=api_client)
    data = api_instance.api_resellers_by_reseller_id_organizations_by_organization_id_user_groups_by_group_id_members_get(resellerId,organizationId,groupId,memberId)
    print(data)
    return data


def AddOrganizationUserGroupMember(resellerId,organizationId,groupId, organizationUserGroupMemberAddViewModel):
    api_instance = swagger_client.OrganizationUserGroupMembersApi(api_client=api_client)
    data = api_instance.api_resellers_by_reseller_id_organizations_by_organization_id_user_groups_by_group_id_members_post(resellerId,organizationId,groupId,organizationUserGroupMemberAddViewModel)
    print(data)
    return data

def GetAllOrganizationUserGroupMembers(resellerId,organizationId,groupId):
    api_instance = swagger_client.OrganizationUserGroupMembersApi(api_client=api_client)
    data = api_instance.api_resellers_by_reseller_id_organizations_by_organization_id_user_groups_by_group_id_members_get(resellerId,organizationId,groupId)
    print(data)
    return data

def DeleteOrganizationUserGroupMemberById(resellerId,organizationId,groupId,memberId):
    api_instance = swagger_client.OrganizationUserGroupMembersApi(api_client=api_client)
    data = api_instance.api_resellers_by_reseller_id_organizations_by_organization_id_user_groups_by_group_id_members_by_id_delete(resellerId,organizationId,groupId,memberId)
    print(data)
    return data


# Organization Subscription Users API

def RemoveOrganizationUserFromSubscription(resellerId,organizationId,serviceId,subscriptionId,userId):
    api_instance = swagger_client.OrganizationSubscriptionUsersApi(api_client=api_client)
    data = api_instance.api_resellers_by_reseller_id_organizations_by_organization_id_services_by_service_id_subscriptions_by_subscription_id_users_by_user_id_delete(resellerId,organizationId,serviceId,subscriptionId,userId)
    print(data)
    return data

def GetAllOrganizationUsersAssignedToSubscription(resellerId,organizationId,serviceId,subscriptionId):
    api_instance = swagger_client.OrganizationSubscriptionUsersApi(api_client=api_client)
    data = api_instance.api_resellers_by_reseller_id_organizations_by_organization_id_services_by_service_id_subscriptions_by_subscription_id_users_get(resellerId,organizationId,serviceId,subscriptionId)
    print(data)
    return data

def UpdateOrganizationUserAssignedToSubscription(resellerId,organizationId,serviceId,subscriptionId,organizationServiceSubscriptionUserUpdateViewModel):
    api_instance = swagger_client.OrganizationSubscriptionUsersApi(api_client=api_client)
    data = api_instance.api_resellers_by_reseller_id_organizations_by_organization_id_services_by_service_id_subscriptions_by_subscription_id_users_put(resellerId,organizationId,serviceId,subscriptionId,organizationServiceSubscriptionUserUpdateViewModel)
    print(data)
    return data

def AssignOrganizationUserToSubscription(resellerId,organizationId,serviceId,subscriptionId,organizationServiceSubscriptionUserCreateViewModel):
    api_instance = swagger_client.OrganizationSubscriptionUsersApi(api_client=api_client)
    data = api_instance.api_resellers_by_reseller_id_organizations_by_organization_id_services_by_service_id_subscriptions_by_subscription_id_users_post(resellerId,organizationId,serviceId,subscriptionId,organizationServiceSubscriptionUserCreateViewModel)
    print(data)
    return data

# Organization Subscription History API

def GetOrganizationSubscriptionHistoryById(resellerId,organizationId,serviceId,subscriptionId):
    api_instance = swagger_client.OrganizationSubscriptionHistoryApi(api_client=api_client)
    data = api_instance.api_resellers_by_reseller_id_organizations_by_organization_id_services_by_service_id_subscriptions_history_by_subscription_id_get(resellerId,organizationId,serviceId,subscriptionId)
    print(data)
    return data

# Organization Custom Services API

def GetOrganizationCustomServiceById(resellerId,organizationId,serviceId):
    api_instance = swagger_client.OrganizationServicesApi(api_client=api_client)
    data = api_instance.api_resellers_by_reseller_id_organizations_by_organization_id_services_by_service_id_get(resellerId,organizationId,serviceId)
    print(data)
    return data


def GetAllOrganizationCustomServices(resellerId,organizationId):
    api_instance = swagger_client.OrganizationServicesApi(api_client=api_client)
    data = api_instance.api_resellers_by_reseller_id_organizations_by_organization_id_services_get(resellerId,organizationId)
    print(data)
    return data

def AddOrganizationCustomServiceById(resellerId,organizationId, organizationServiceAddViewModel):
    api_instance = swagger_client.OrganizationServicesApi(api_client=api_client)
    data = api_instance.api_resellers_by_reseller_id_organizations_by_organization_id_services_post(resellerId,organizationId,organizationServiceAddViewModel)
    print(data)
    return data

def UpdateOrganizationCustomServiceCustomPropertyData(resellerId,organizationId,serviceId, organizationServiceUpdateViewModel):
    api_instance = swagger_client.OrganizationServicesApi(api_client=api_client)
    data = api_instance.api_resellers_by_reseller_id_organizations_by_organization_id_services_by_service_id_patch(resellerId,organizationId,serviceId,organizationServiceUpdateViewModel)
    print(data)
    return data

def UpdateOrganizationCustomServiceById(resellerId,organizationId,serviceId, organizationServiceUpdateViewModel):
    api_instance = swagger_client.OrganizationServicesApi(api_client=api_client)
    data = api_instance.api_resellers_by_reseller_id_organizations_by_organization_id_services_by_service_id_put(resellerId,organizationId,serviceId,organizationServiceUpdateViewModel)
    print(data)
    return data

def RemoveOrganizationCustomServiceById(resellerId,organizationId,serviceId):
    api_instance = swagger_client.OrganizationServicesApi(api_client=api_client)
    data = api_instance.api_resellers_by_reseller_id_organizations_by_organization_id_services_by_service_id_delete(resellerId,organizationId,serviceId)
    print(data)
    return data

# Organization Service Subscriptions API

def GetOrganizationCustomServiceSubscriptionById(resellerId,organizationId,serviceId,subscriptionId):
    api_instance = swagger_client.OrganizationServiceSubscriptionsApi(api_client=api_client)
    data = api_instance.api_resellers_by_reseller_id_organizations_by_organization_id_services_by_service_id_subscriptions_by_subscription_id_get(resellerId,organizationId,serviceId,subscriptionId)
    print(data)
    return data

def GetAllOrganizationCustomServiceSubscriptions(resellerId,organizationId,serviceId):
    api_instance = swagger_client.OrganizationServiceSubscriptionsApi(api_client=api_client)
    data = api_instance.api_resellers_by_reseller_id_organizations_by_organization_id_services_by_service_id_subscriptions_get(resellerId,organizationId,serviceId)
    print(data)
    return data

def CreateOrganizationCustomServiceSubscription(resellerId,organizationId,serviceId,organizationServiceSubscriptionCreateViewModel):
    api_instance = swagger_client.OrganizationServiceSubscriptionsApi(api_client=api_client)
    data = api_instance.api_resellers_by_reseller_id_organizations_by_organization_id_services_by_service_id_subscriptions_post(resellerId,organizationId,serviceId,organizationServiceSubscriptionCreateViewModel)
    print(data)
    return data

def CancelOrganizationCustomServiceSubscriptionById(resellerId,organizationId,serviceId,subscriptionId):
    api_instance = swagger_client.OrganizationServiceSubscriptionsApi(api_client=api_client)
    data = api_instance.api_resellers_by_reseller_id_organizations_by_organization_id_services_by_service_id_subscriptions_by_subscription_id_delete(resellerId,organizationId,serviceId,subscriptionId)
    print(data)
    return data

def UpdateOrganizationCustomServiceSubscriptionById(resellerId,organizationId,serviceId,subscriptionId,organizationServiceSubscriptionUpdateViewModel):
    api_instance = swagger_client.OrganizationServiceSubscriptionsApi(api_client=api_client)
    data = api_instance.api_resellers_by_reseller_id_organizations_by_organization_id_services_by_service_id_subscriptions_by_subscription_id_put(resellerId,organizationId,serviceId,subscriptionId,organizationServiceSubscriptionUpdateViewModel)
    print(data)
    return data

# Organization Service Products API

def GetAllOrganizationCustomServiceProducts(resellerId,organizationId,serviceId):
    api_instance = swagger_client.OrganizationServiceProductsApi(api_client=api_client)
    data = api_instance.api_resellers_by_reseller_id_organizations_by_organization_id_services_by_service_id_products_get(resellerId,organizationId,serviceId)
    print(data)
    return data



