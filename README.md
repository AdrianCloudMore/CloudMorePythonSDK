# CloudMore SDK

## Description 

The Cloudmore SDK for python is mostly just an auto generated swagger client,
and a few examples of how to make use of the Cloudmore API from python code. 
It also aims to make it easy to install, update and package the API client.

## Install & Update

Run the install script in install.py, it will take the following steps:

    1. Download swagger.json from CloudMore API Swagger page 
    2. Call an online swagger-codegen generator to generate the client code. The files will be placed
        in a folder named "python-client"
    3. Finally, it will note the version of the API definition doument and store it in api_version.txt


If the CloudMore API has been updated, use the update.py script to generate a new
client. It will check the swagger document version against the version in api_version.txt
and update if necessary.

Note that the auto-generated client also comes with API documentation, located in python-client/docs

## Package 

Next you will need to package the swagger client into a python package (.egg),

To package the client, go into the python-client folder and run the following command:

```sh
sudo python3 setup.py install --user
```
(or `python setup.py install` to install the package for all users)
 
there should now be a package mnamed cloudmore_sdk-1.0.0-py3.12.egg in the python-client/dist folder,

Once the package is installed you can import the package, and run the sample cli.py script (see samples below)

```python
import cloudmore_sdk
```

## TO DO

Use the actual models in cloudmore_sdk/models 


## Configure Authentication

You will need to authenticate with the CloudMore API, see api.py for an example
The api.py script, makes use of the AuthConfig class in auth_config.py,
you will need to fill out the missing default values, or set these in code 
before calling any API function. 

You may also need to handle refreshing the access_token, depending on the application.
The authenticate method in api.py will store the value of the expires header 

## Samples 

See 'cli,py' and 'api.py' for examples on how to use the swagger client to 
call different functions.

## CLI

You can use the included CLI client in cli.py to call the CloudMore API. 
The script in cli.py makes use of functions defined in api.py. 
Note that you may need to change the host (base url), configured in api.py, 
by default it's set to: https://api-dev.cloudmore.com

```shell
python3 cli.py -u CloudMoreUser -p CloudMorePassword -s CloudMoreAPISecret -c GetAllManualBillingLinesByResellerId --start-date 03-18-2025 --end-date 03-20-2025 --reseller 3cd64bae-1602-49ce-9d04-d034d4a046ea -seller f28a9284-0ce3-418f-a2f7-f4e3b80c6533
```

Run the following command to display usage instructions

```shell
python3 cli.py -h
```

```shell
usage: CloudMoreCLI [-h] -c Command (API Function Name) [-seller Seller ID] [-reseller Reseller ID] [-organization Organization ID] [-subscription Subscription ID]
                    [-service Service ID] [-webhook WebHook ID] [-user User ID] [-task Task ID] [-product Product ID] [-addon Addon ID] [-billing-line Billing Line ID]
                    [-start-date Start Date] [-end-date End Date] [-show-active Show only active *] [-remove-action Remove subscription action, either delete or cancel]
                    -u Auth: CloudMore Username -p Auth: CloudMore Password -s Auth: API Secret [-client Auth: Client ID] [-g Auth: Grant Type] [-scope Auth: Scope]
                    [-j Request Body as JSON]

CloudMore REST API Client CLI

options:
  -h, --help  show this help message and exit
  -c Command (API Function Name), --cmd Command (API Function Name)
  -seller Seller ID, --seller Seller ID
  -reseller Reseller ID, --reseller Reseller ID
  -organization Organization ID, --organization Organization ID
  -subscription Subscription ID, --subscription Subscription ID
  -service Service ID, --service Service ID
  -webhook WebHook ID, --webhook WebHook ID
  -user User ID, --user User ID
  -task Task ID, --task Task ID
  -product Product ID, --product Product ID
  -addon Addon ID, --addon Addon ID
  -billing-line Billing Line ID, --billing-line Billing Line ID
  -start-date Start Date, --start-date Start Date
  -end-date End Date, --end-date End Date
  -show-active Show only active *, --show-active Show only active *
  -remove-action Remove subscription action, either delete or cancel, --remove-action Remove subscription action, either delete or cancel
  -u Auth: CloudMore Username, --username Auth: CloudMore Username
  -p Auth: CloudMore Password, --password Auth: CloudMore Password
  -s Auth: API Secret, --secret Auth: API Secret
  -client Auth: Client ID, --client-id Auth: Client ID
  -g Auth: Grant Type, --grant-type Auth: Grant Type
  -scope Auth: Scope, --scope Auth: Scope
  -j Request Body as JSON, --data Request Body as JSON
```

# Cloudmore Swagger Client Documentation

Is 64-bit process: True  REST API for managing the Cloudmore platform. NOTE: use this page only for viewing the API documentation, submitting actual requests is disabled.

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: v1.07.0
- Package version: 1.0.0
- Build package: io.swagger.codegen.languages.PythonClientCodegen
For more information, please visit [https://support.cloudmore.com](https://support.cloudmore.com)

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com//.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com//.git`)

Then import the package:
```python
import swagger_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python3 setup.py install --user
```
(or `sudo python3 setup.py install` to install the package for all users)

Then import the package:
```python
import swagger_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AzureBillingReportsApi(swagger_client.ApiClient(configuration))
reseller_id = 'reseller_id_example' # str | Guid of the reseller(required)
task_id = 'task_id_example' # str | Id of the data generation task returned in the response header \"Location\" of a call to POST AzureOneTimeBillingAsync.

try:
    # Returns asynchronosly generated azure onetime billing report
    api_response = api_instance.api_resellers_by_reseller_id_billing_azurereports_azure_one_time_invoice_by_task_id_get(reseller_id, task_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AzureBillingReportsApi->api_resellers_by_reseller_id_billing_azurereports_azure_one_time_invoice_by_task_id_get: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://localhost*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AzureBillingReportsApi* | [**api_resellers_by_reseller_id_billing_azurereports_azure_one_time_invoice_by_task_id_get**](docs/AzureBillingReportsApi.md#api_resellers_by_reseller_id_billing_azurereports_azure_one_time_invoice_by_task_id_get) | **GET** /api/resellers/{resellerId}/billing/azurereports/AzureOneTimeInvoice/{taskId} | Returns asynchronosly generated azure onetime billing report
*AzureBillingReportsApi* | [**api_resellers_by_reseller_id_billing_azurereports_azure_one_time_invoice_generate_report_post**](docs/AzureBillingReportsApi.md#api_resellers_by_reseller_id_billing_azurereports_azure_one_time_invoice_generate_report_post) | **POST** /api/resellers/{resellerId}/billing/azurereports/AzureOneTimeInvoice/generateReport | starts asynchronous generation of azure onetime billing report.
*AzureBillingReportsApi* | [**api_resellers_by_reseller_id_billing_azurereports_azure_one_time_invoice_list_get**](docs/AzureBillingReportsApi.md#api_resellers_by_reseller_id_billing_azurereports_azure_one_time_invoice_list_get) | **GET** /api/resellers/{resellerId}/billing/azurereports/AzureOneTimeInvoiceList | Returns list of Azure one time invoice Ids and corresponding dates
*AzureBillingReportsApi* | [**api_resellers_by_reseller_id_billing_azurereports_invoice_get**](docs/AzureBillingReportsApi.md#api_resellers_by_reseller_id_billing_azurereports_invoice_get) | **GET** /api/resellers/{resellerId}/billing/azurereports/Invoice | Returns detailed Azure invoice
*AzureBillingReportsApi* | [**api_resellers_by_reseller_id_billing_azurereports_invoice_list_get**](docs/AzureBillingReportsApi.md#api_resellers_by_reseller_id_billing_azurereports_invoice_list_get) | **GET** /api/resellers/{resellerId}/billing/azurereports/InvoiceList | Returns list of Azure invoice Ids and corresponding dates
*AzureBillingReportsApi* | [**api_resellers_by_reseller_id_billing_azurereports_invoice_overview_get**](docs/AzureBillingReportsApi.md#api_resellers_by_reseller_id_billing_azurereports_invoice_overview_get) | **GET** /api/resellers/{resellerId}/billing/azurereports/InvoiceOverview | Returns Microsoft Azure invoice overview report
*AzureBillingReportsApi* | [**api_resellers_by_reseller_id_billing_azurereports_invoices_by_custom_dates_get**](docs/AzureBillingReportsApi.md#api_resellers_by_reseller_id_billing_azurereports_invoices_by_custom_dates_get) | **GET** /api/resellers/{resellerId}/billing/azurereports/InvoicesByCustomDates | Returns Microsoft Azure utilization data by invoice periods.
*AzureBillingReportsApi* | [**api_resellers_by_reseller_id_billing_azurereports_monthly_billing_per_organization_get**](docs/AzureBillingReportsApi.md#api_resellers_by_reseller_id_billing_azurereports_monthly_billing_per_organization_get) | **GET** /api/resellers/{resellerId}/billing/azurereports/MonthlyBillingPerOrganization | Returns reseller invoice based Microsoft Azure billing report per organization
*AzureBillingReportsApi* | [**api_resellers_by_reseller_id_billing_azurereports_ongoing_period_get**](docs/AzureBillingReportsApi.md#api_resellers_by_reseller_id_billing_azurereports_ongoing_period_get) | **GET** /api/resellers/{resellerId}/billing/azurereports/OngoingPeriod | Returns reseller ongoing period Microsoft Azure billing report per organization
*AzureOneTimeUsageApi* | [**api_resellers_by_reseller_id_billing_azureonetimeusage_azure_one_time_invoice_get**](docs/AzureOneTimeUsageApi.md#api_resellers_by_reseller_id_billing_azureonetimeusage_azure_one_time_invoice_get) | **GET** /api/resellers/{resellerId}/billing/azureonetimeusage/AzureOneTimeInvoice | Returns azure onetime usage invoice report
*AzureOneTimeUsageApi* | [**api_resellers_by_reseller_id_billing_azureonetimeusage_azure_one_time_ongoing_period_get**](docs/AzureOneTimeUsageApi.md#api_resellers_by_reseller_id_billing_azureonetimeusage_azure_one_time_ongoing_period_get) | **GET** /api/resellers/{resellerId}/billing/azureonetimeusage/AzureOneTimeOngoingPeriod | Returns Azure One Time usage report for ongoing period
*AzureOnetimeUsageReportApiApi* | [**api_resellers_by_reseller_id_billing_azureonetimeusage_report_billed_invoice_by_invoice_id_get**](docs/AzureOnetimeUsageReportApiApi.md#api_resellers_by_reseller_id_billing_azureonetimeusage_report_billed_invoice_by_invoice_id_get) | **GET** /api/resellers/{resellerId}/billing/azureonetimeusage/report/billed/invoice/{invoiceId} | Returns azure onetime billed usage invoice report
*AzureOnetimeUsageReportApiApi* | [**api_resellers_by_reseller_id_billing_azureonetimeusage_report_unbilled_period_by_period_export_post**](docs/AzureOnetimeUsageReportApiApi.md#api_resellers_by_reseller_id_billing_azureonetimeusage_report_unbilled_period_by_period_export_post) | **POST** /api/resellers/{resellerId}/billing/azureonetimeusage/report/unbilled/period/{period}/export | Request azure onetime unbilled usage invoice report
*AzureOnetimeUsageReportApiApi* | [**api_resellers_by_reseller_id_billing_azureonetimeusage_report_unbilled_period_by_period_operation_by_operation_id_result_get**](docs/AzureOnetimeUsageReportApiApi.md#api_resellers_by_reseller_id_billing_azureonetimeusage_report_unbilled_period_by_period_operation_by_operation_id_result_get) | **GET** /api/resellers/{resellerId}/billing/azureonetimeusage/report/unbilled/period/{period}/operation/{operationId}/result | Returns azure onetime unbilled usage period report
*AzureOnetimeUsageReportApiApi* | [**api_resellers_by_reseller_id_billing_azureonetimeusage_report_unbilled_period_by_period_operation_by_operation_id_status_get**](docs/AzureOnetimeUsageReportApiApi.md#api_resellers_by_reseller_id_billing_azureonetimeusage_report_unbilled_period_by_period_operation_by_operation_id_status_get) | **GET** /api/resellers/{resellerId}/billing/azureonetimeusage/report/unbilled/period/{period}/operation/{operationId}/status | Request azure onetime unbilled usage invoice report
*BillingReportsApi* | [**api_resellers_by_reseller_id_billing_reports_monthly_billing_per_organization_get**](docs/BillingReportsApi.md#api_resellers_by_reseller_id_billing_reports_monthly_billing_per_organization_get) | **GET** /api/resellers/{resellerId}/billing/reports/MonthlyBillingPerOrganization | 
*BillingReportsApi* | [**api_resellers_by_reseller_id_billing_reports_monthly_billing_per_service_get**](docs/BillingReportsApi.md#api_resellers_by_reseller_id_billing_reports_monthly_billing_per_service_get) | **GET** /api/resellers/{resellerId}/billing/reports/MonthlyBillingPerService | 
*BillingReportsAsyncApi* | [**api_resellers_by_reseller_id_billing_reports_monthly_billing_per_organization_async_by_task_id_get**](docs/BillingReportsAsyncApi.md#api_resellers_by_reseller_id_billing_reports_monthly_billing_per_organization_async_by_task_id_get) | **GET** /api/resellers/{resellerId}/billing/reports/MonthlyBillingPerOrganizationAsync/{taskId} | Returns asynchronosly generated reseller monthly billing report per organization
*BillingReportsAsyncApi* | [**api_resellers_by_reseller_id_billing_reports_monthly_billing_per_organization_async_post**](docs/BillingReportsAsyncApi.md#api_resellers_by_reseller_id_billing_reports_monthly_billing_per_organization_async_post) | **POST** /api/resellers/{resellerId}/billing/reports/MonthlyBillingPerOrganizationAsync | Starts asynchronous generation of reseller monthly billing report per organization
*CspBillingReportsApi* | [**api_resellers_by_reseller_id_billing_cspreports_monthly_billing_per_organization_get**](docs/CspBillingReportsApi.md#api_resellers_by_reseller_id_billing_cspreports_monthly_billing_per_organization_get) | **GET** /api/resellers/{resellerId}/billing/cspreports/MonthlyBillingPerOrganization | Returns reseller monthly Microsoft CSP billing report per organization
*CspDomainValidationApi* | [**api_resellers_by_reseller_id_services_csp_domainvalidation_get**](docs/CspDomainValidationApi.md#api_resellers_by_reseller_id_services_csp_domainvalidation_get) | **GET** /api/resellers/{resellerId}/services/csp/domainvalidation | Validates customer&#39;s desired Microsoft CSP domain prefix
*CspTenantsApi* | [**api_resellers_by_reseller_id_services_csp_csp_tenants_link_post**](docs/CspTenantsApi.md#api_resellers_by_reseller_id_services_csp_csp_tenants_link_post) | **POST** /api/resellers/{resellerId}/services/csp/CspTenants/Link | Links Microsoft Csp tenant and reseller&#39;s organization together
*CspTenantsApi* | [**api_resellers_by_reseller_id_services_csp_csp_tenants_list_get**](docs/CspTenantsApi.md#api_resellers_by_reseller_id_services_csp_csp_tenants_list_get) | **GET** /api/resellers/{resellerId}/services/csp/CspTenants/List | Returns all reseller Microsoft Csp tenants and corresponding linked organizations
*CustomPropertiesApi* | [**api_resellers_by_reseller_id_settings_custom_properties_get**](docs/CustomPropertiesApi.md#api_resellers_by_reseller_id_settings_custom_properties_get) | **GET** /api/resellers/{resellerId}/settings/CustomProperties | Returns all custom properties defined by broker for the organization.
*CustomPropertiesApi* | [**api_sellers_by_seller_id_settings_custom_properties_get**](docs/CustomPropertiesApi.md#api_sellers_by_seller_id_settings_custom_properties_get) | **GET** /api/sellers/{sellerId}/settings/CustomProperties | Returns all custom properties defined by the seller for the brokers.
*EstoreApi* | [**api_resellers_by_reseller_id_organizations_by_organization_id_estore_by_service_id_get**](docs/EstoreApi.md#api_resellers_by_reseller_id_organizations_by_organization_id_estore_by_service_id_get) | **GET** /api/resellers/{resellerId}/organizations/{organizationId}/Estore/{serviceId} | Returns details for service that can be added to organization
*EstoreApi* | [**api_resellers_by_reseller_id_organizations_by_organization_id_estore_get**](docs/EstoreApi.md#api_resellers_by_reseller_id_organizations_by_organization_id_estore_get) | **GET** /api/resellers/{resellerId}/organizations/{organizationId}/Estore | Returns all services available for adding to organization
*ExternalInvoiceApi* | [**api_resellers_by_reseller_id_organizations_by_organization_id_external_invoice_by_id_delete**](docs/ExternalInvoiceApi.md#api_resellers_by_reseller_id_organizations_by_organization_id_external_invoice_by_id_delete) | **DELETE** /api/resellers/{resellerId}/organizations/{organizationId}/ExternalInvoice/{id} | Deletes external invoice.
*ExternalInvoiceApi* | [**api_resellers_by_reseller_id_organizations_by_organization_id_external_invoice_by_id_get**](docs/ExternalInvoiceApi.md#api_resellers_by_reseller_id_organizations_by_organization_id_external_invoice_by_id_get) | **GET** /api/resellers/{resellerId}/organizations/{organizationId}/ExternalInvoice/{id} | Returns external invoice.
*ExternalInvoiceApi* | [**api_resellers_by_reseller_id_organizations_by_organization_id_external_invoice_by_id_put**](docs/ExternalInvoiceApi.md#api_resellers_by_reseller_id_organizations_by_organization_id_external_invoice_by_id_put) | **PUT** /api/resellers/{resellerId}/organizations/{organizationId}/ExternalInvoice/{id} | Updates external invoice.
*ExternalInvoiceApi* | [**api_resellers_by_reseller_id_organizations_by_organization_id_external_invoice_get**](docs/ExternalInvoiceApi.md#api_resellers_by_reseller_id_organizations_by_organization_id_external_invoice_get) | **GET** /api/resellers/{resellerId}/organizations/{organizationId}/ExternalInvoice | Returns all external invoices for the orgnization.
*ExternalInvoiceApi* | [**api_resellers_by_reseller_id_organizations_by_organization_id_external_invoice_post**](docs/ExternalInvoiceApi.md#api_resellers_by_reseller_id_organizations_by_organization_id_external_invoice_post) | **POST** /api/resellers/{resellerId}/organizations/{organizationId}/ExternalInvoice | Creates new external invoice for the organization.
*HealthCheckApi* | [**api_healthcheck_get**](docs/HealthCheckApi.md#api_healthcheck_get) | **GET** /api/healthcheck | Can be used to verify that Cloudmore API is responding
*MarketCountriesApi* | [**api_services_market_countries_get**](docs/MarketCountriesApi.md#api_services_market_countries_get) | **GET** /api/services/marketCountries | Retrieve market countries
*MarketRegionApi* | [**api_services_market_regions_get**](docs/MarketRegionApi.md#api_services_market_regions_get) | **GET** /api/services/marketRegions | Retrieve market regions
*OrganizationAzureApi* | [**api_resellers_by_reseller_id_organizations_by_organization_id_services_azure_delete**](docs/OrganizationAzureApi.md#api_resellers_by_reseller_id_organizations_by_organization_id_services_azure_delete) | **DELETE** /api/resellers/{resellerId}/organizations/{organizationId}/services/Azure | Removes Microsoft Azure service from organization.
*OrganizationAzureApi* | [**api_resellers_by_reseller_id_organizations_by_organization_id_services_azure_get**](docs/OrganizationAzureApi.md#api_resellers_by_reseller_id_organizations_by_organization_id_services_azure_get) | **GET** /api/resellers/{resellerId}/organizations/{organizationId}/services/Azure | Returns organization Microsoft Azure service details
*OrganizationAzureApi* | [**api_resellers_by_reseller_id_organizations_by_organization_id_services_azure_post**](docs/OrganizationAzureApi.md#api_resellers_by_reseller_id_organizations_by_organization_id_services_azure_post) | **POST** /api/resellers/{resellerId}/organizations/{organizationId}/services/Azure | Adds available Microsoft Azure service from Estore to organization
*OrganizationAzurePlanSubscriptionsApi* | [**api_resellers_by_reseller_id_organizations_by_organization_id_services_azureplan_subscriptions_by_id_get**](docs/OrganizationAzurePlanSubscriptionsApi.md#api_resellers_by_reseller_id_organizations_by_organization_id_services_azureplan_subscriptions_by_id_get) | **GET** /api/resellers/{resellerId}/organizations/{organizationId}/services/azureplan/subscriptions/{id} | Returns organization&#39;s Azure plan subscription.
*OrganizationAzurePlanSubscriptionsApi* | [**api_resellers_by_reseller_id_organizations_by_organization_id_services_azureplan_subscriptions_by_id_put**](docs/OrganizationAzurePlanSubscriptionsApi.md#api_resellers_by_reseller_id_organizations_by_organization_id_services_azureplan_subscriptions_by_id_put) | **PUT** /api/resellers/{resellerId}/organizations/{organizationId}/services/azureplan/subscriptions/{id} | Update Azure Plan subscription or entitlement.
*OrganizationAzurePlanSubscriptionsApi* | [**api_resellers_by_reseller_id_organizations_by_organization_id_services_azureplan_subscriptions_create_entitlement_post**](docs/OrganizationAzurePlanSubscriptionsApi.md#api_resellers_by_reseller_id_organizations_by_organization_id_services_azureplan_subscriptions_create_entitlement_post) | **POST** /api/resellers/{resellerId}/organizations/{organizationId}/services/azureplan/subscriptions/CreateEntitlement | Creates entitlement for organization&#39;s Microsoft Azure Plan without assigning it to user.
*OrganizationAzurePlanSubscriptionsApi* | [**api_resellers_by_reseller_id_organizations_by_organization_id_services_azureplan_subscriptions_get**](docs/OrganizationAzurePlanSubscriptionsApi.md#api_resellers_by_reseller_id_organizations_by_organization_id_services_azureplan_subscriptions_get) | **GET** /api/resellers/{resellerId}/organizations/{organizationId}/services/azureplan/subscriptions | Returns organization Azure plan subscription and its entitlements.
*OrganizationAzurePlanSubscriptionsApi* | [**api_resellers_by_reseller_id_organizations_by_organization_id_services_azureplan_subscriptions_post**](docs/OrganizationAzurePlanSubscriptionsApi.md#api_resellers_by_reseller_id_organizations_by_organization_id_services_azureplan_subscriptions_post) | **POST** /api/resellers/{resellerId}/organizations/{organizationId}/services/azureplan/subscriptions | Creates subscription and first entitlement for organization&#39;s Microsoft Azure Plan without assigning it to user.
*OrganizationAzureSubscriptionsApi* | [**api_resellers_by_reseller_id_organizations_by_organization_id_services_azure_subscriptions_by_subscription_id_delete**](docs/OrganizationAzureSubscriptionsApi.md#api_resellers_by_reseller_id_organizations_by_organization_id_services_azure_subscriptions_by_subscription_id_delete) | **DELETE** /api/resellers/{resellerId}/organizations/{organizationId}/services/azure/subscriptions/{subscriptionId} | Suspends Microsoft Azure service subscription for organization.
*OrganizationAzureSubscriptionsApi* | [**api_resellers_by_reseller_id_organizations_by_organization_id_services_azure_subscriptions_get**](docs/OrganizationAzureSubscriptionsApi.md#api_resellers_by_reseller_id_organizations_by_organization_id_services_azure_subscriptions_get) | **GET** /api/resellers/{resellerId}/organizations/{organizationId}/services/azure/subscriptions | Returns all organization Azure subscriptions.
*OrganizationAzureUserSubscriptionsApi* | [**api_resellers_by_reseller_id_organizations_by_organization_id_services_azure_users_by_user_id_subscriptions_by_id_delete**](docs/OrganizationAzureUserSubscriptionsApi.md#api_resellers_by_reseller_id_organizations_by_organization_id_services_azure_users_by_user_id_subscriptions_by_id_delete) | **DELETE** /api/resellers/{resellerId}/organizations/{organizationId}/services/azure/users/{userId}/subscriptions/{id} | Removes Owner and/or Contributor role from user in subscription.
*OrganizationAzureUserSubscriptionsApi* | [**api_resellers_by_reseller_id_organizations_by_organization_id_services_azure_users_by_user_id_subscriptions_get**](docs/OrganizationAzureUserSubscriptionsApi.md#api_resellers_by_reseller_id_organizations_by_organization_id_services_azure_users_by_user_id_subscriptions_get) | **GET** /api/resellers/{resellerId}/organizations/{organizationId}/services/azure/users/{userId}/subscriptions | Returns all Azure user subscriptions with assigned role.
*OrganizationAzureUserSubscriptionsApi* | [**api_resellers_by_reseller_id_organizations_by_organization_id_services_azure_users_by_user_id_subscriptions_post**](docs/OrganizationAzureUserSubscriptionsApi.md#api_resellers_by_reseller_id_organizations_by_organization_id_services_azure_users_by_user_id_subscriptions_post) | **POST** /api/resellers/{resellerId}/organizations/{organizationId}/services/azure/users/{userId}/subscriptions | Assigns role to user in active Azure subscription.
*OrganizationAzureUserSubscriptionsApi* | [**api_resellers_by_reseller_id_organizations_by_organization_id_services_azure_users_by_user_id_subscriptions_put**](docs/OrganizationAzureUserSubscriptionsApi.md#api_resellers_by_reseller_id_organizations_by_organization_id_services_azure_users_by_user_id_subscriptions_put) | **PUT** /api/resellers/{resellerId}/organizations/{organizationId}/services/azure/users/{userId}/subscriptions | Updates role assignment in active subscription.
*OrganizationAzureUsersApi* | [**api_resellers_by_reseller_id_organizations_by_organization_id_services_azure_users_get**](docs/OrganizationAzureUsersApi.md#api_resellers_by_reseller_id_organizations_by_organization_id_services_azure_users_get) | **GET** /api/resellers/{resellerId}/organizations/{organizationId}/services/azure/users | Returns all organization Azure users for which a subscription can be added.
*OrganizationCostCenterReportsApi* | [**api_resellers_by_reseller_id_organizations_by_organization_id_costcenters_reports_by_year_by_month_get**](docs/OrganizationCostCenterReportsApi.md#api_resellers_by_reseller_id_organizations_by_organization_id_costcenters_reports_by_year_by_month_get) | **GET** /api/resellers/{resellerId}/organizations/{organizationId}/costcenters/reports/{year}/{month} | Get organization cost centers report
*OrganizationCspApi* | [**api_resellers_by_reseller_id_organizations_by_organization_id_services_csp_delete**](docs/OrganizationCspApi.md#api_resellers_by_reseller_id_organizations_by_organization_id_services_csp_delete) | **DELETE** /api/resellers/{resellerId}/organizations/{organizationId}/services/Csp | Removes Microsoft CSP service from organization.
*OrganizationCspApi* | [**api_resellers_by_reseller_id_organizations_by_organization_id_services_csp_get**](docs/OrganizationCspApi.md#api_resellers_by_reseller_id_organizations_by_organization_id_services_csp_get) | **GET** /api/resellers/{resellerId}/organizations/{organizationId}/services/Csp | Returns organization Microsoft CSP service details
*OrganizationCspApi* | [**api_resellers_by_reseller_id_organizations_by_organization_id_services_csp_post**](docs/OrganizationCspApi.md#api_resellers_by_reseller_id_organizations_by_organization_id_services_csp_post) | **POST** /api/resellers/{resellerId}/organizations/{organizationId}/services/Csp | Adds available Microsoft CSP service from Estore to organization
*OrganizationCspProductLicensesApi* | [**api_resellers_by_reseller_id_organizations_by_organization_id_services_csp_productlicenses_get**](docs/OrganizationCspProductLicensesApi.md#api_resellers_by_reseller_id_organizations_by_organization_id_services_csp_productlicenses_get) | **GET** /api/resellers/{resellerId}/organizations/{organizationId}/services/Csp/productlicenses | Returns all organization O365 product licenses.
*OrganizationCspProductsApi* | [**api_resellers_by_reseller_id_organizations_by_organization_id_services_csp_products_get**](docs/OrganizationCspProductsApi.md#api_resellers_by_reseller_id_organizations_by_organization_id_services_csp_products_get) | **GET** /api/resellers/{resellerId}/organizations/{organizationId}/services/Csp/products | Returns all organization CSP service products in reseller currency
*OrganizationCspProductsNceApi* | [**api_resellers_by_reseller_id_organizations_by_organization_id_services_csp_nce_products_get**](docs/OrganizationCspProductsNceApi.md#api_resellers_by_reseller_id_organizations_by_organization_id_services_csp_nce_products_get) | **GET** /api/resellers/{resellerId}/organizations/{organizationId}/services/csp/nce/products | Returns all organization CSP service new commerce products
*OrganizationCspSubscriptionsApi* | [**api_resellers_by_reseller_id_organizations_by_organization_id_services_csp_subscriptions_by_id_get**](docs/OrganizationCspSubscriptionsApi.md#api_resellers_by_reseller_id_organizations_by_organization_id_services_csp_subscriptions_by_id_get) | **GET** /api/resellers/{resellerId}/organizations/{organizationId}/services/csp/subscriptions/{id} | Returns organization CSP subscription details
*OrganizationCspSubscriptionsApi* | [**api_resellers_by_reseller_id_organizations_by_organization_id_services_csp_subscriptions_by_subscription_id_delete**](docs/OrganizationCspSubscriptionsApi.md#api_resellers_by_reseller_id_organizations_by_organization_id_services_csp_subscriptions_by_subscription_id_delete) | **DELETE** /api/resellers/{resellerId}/organizations/{organizationId}/services/csp/subscriptions/{subscriptionId} | Suspends Microsoft CSP service subscription for organization.
*OrganizationCspSubscriptionsApi* | [**api_resellers_by_reseller_id_organizations_by_organization_id_services_csp_subscriptions_by_subscription_id_put**](docs/OrganizationCspSubscriptionsApi.md#api_resellers_by_reseller_id_organizations_by_organization_id_services_csp_subscriptions_by_subscription_id_put) | **PUT** /api/resellers/{resellerId}/organizations/{organizationId}/services/csp/subscriptions/{subscriptionId} | Updates Microsoft 365 CSP service subscription.
*OrganizationCspSubscriptionsApi* | [**api_resellers_by_reseller_id_organizations_by_organization_id_services_csp_subscriptions_get**](docs/OrganizationCspSubscriptionsApi.md#api_resellers_by_reseller_id_organizations_by_organization_id_services_csp_subscriptions_get) | **GET** /api/resellers/{resellerId}/organizations/{organizationId}/services/csp/subscriptions | Returns all organization CSP subscriptions
*OrganizationCspSubscriptionsApi* | [**api_resellers_by_reseller_id_organizations_by_organization_id_services_csp_subscriptions_post**](docs/OrganizationCspSubscriptionsApi.md#api_resellers_by_reseller_id_organizations_by_organization_id_services_csp_subscriptions_post) | **POST** /api/resellers/{resellerId}/organizations/{organizationId}/services/csp/subscriptions | Creates subscription for organization Microsoft CSP service
*OrganizationCspSubscriptionsNceApi* | [**api_resellers_by_reseller_id_organizations_by_organization_id_services_csp_nce_subscriptions_alignmentdates_get**](docs/OrganizationCspSubscriptionsNceApi.md#api_resellers_by_reseller_id_organizations_by_organization_id_services_csp_nce_subscriptions_alignmentdates_get) | **GET** /api/resellers/{resellerId}/organizations/{organizationId}/services/csp/nce/subscriptions/alignmentdates | Get a list of possible organization alignment dates with list of subscripitonIds per term duration
*OrganizationCspSubscriptionsNceApi* | [**api_resellers_by_reseller_id_organizations_by_organization_id_services_csp_nce_subscriptions_by_id_get**](docs/OrganizationCspSubscriptionsNceApi.md#api_resellers_by_reseller_id_organizations_by_organization_id_services_csp_nce_subscriptions_by_id_get) | **GET** /api/resellers/{resellerId}/organizations/{organizationId}/services/csp/nce/subscriptions/{id} | Returns organization new commerce subscription details
*OrganizationCspSubscriptionsNceApi* | [**api_resellers_by_reseller_id_organizations_by_organization_id_services_csp_nce_subscriptions_by_subscription_id_delete**](docs/OrganizationCspSubscriptionsNceApi.md#api_resellers_by_reseller_id_organizations_by_organization_id_services_csp_nce_subscriptions_by_subscription_id_delete) | **DELETE** /api/resellers/{resellerId}/organizations/{organizationId}/services/csp/nce/subscriptions/{subscriptionId} | Delete Microsoft CSP service new commerce subscription for organization.
*OrganizationCspSubscriptionsNceApi* | [**api_resellers_by_reseller_id_organizations_by_organization_id_services_csp_nce_subscriptions_by_subscription_id_existing_subscription_eligiblities_get**](docs/OrganizationCspSubscriptionsNceApi.md#api_resellers_by_reseller_id_organizations_by_organization_id_services_csp_nce_subscriptions_by_subscription_id_existing_subscription_eligiblities_get) | **GET** /api/resellers/{resellerId}/organizations/{organizationId}/services/csp/nce/subscriptions/{subscriptionId}/existingSubscriptionEligiblities | Returns all available upgradable subscriptions to an existing subscription
*OrganizationCspSubscriptionsNceApi* | [**api_resellers_by_reseller_id_organizations_by_organization_id_services_csp_nce_subscriptions_by_subscription_id_new_subscription_eligibilities_get**](docs/OrganizationCspSubscriptionsNceApi.md#api_resellers_by_reseller_id_organizations_by_organization_id_services_csp_nce_subscriptions_by_subscription_id_new_subscription_eligibilities_get) | **GET** /api/resellers/{resellerId}/organizations/{organizationId}/services/csp/nce/subscriptions/{subscriptionId}/newSubscriptionEligibilities | Returns all available products to upgrade as new subscription
*OrganizationCspSubscriptionsNceApi* | [**api_resellers_by_reseller_id_organizations_by_organization_id_services_csp_nce_subscriptions_by_subscription_id_put**](docs/OrganizationCspSubscriptionsNceApi.md#api_resellers_by_reseller_id_organizations_by_organization_id_services_csp_nce_subscriptions_by_subscription_id_put) | **PUT** /api/resellers/{resellerId}/organizations/{organizationId}/services/csp/nce/subscriptions/{subscriptionId} | Updates Microsoft O365 CSP service new commerce subscription.
*OrganizationCspSubscriptionsNceApi* | [**api_resellers_by_reseller_id_organizations_by_organization_id_services_csp_nce_subscriptions_by_subscription_id_upgrade_status_get**](docs/OrganizationCspSubscriptionsNceApi.md#api_resellers_by_reseller_id_organizations_by_organization_id_services_csp_nce_subscriptions_by_subscription_id_upgrade_status_get) | **GET** /api/resellers/{resellerId}/organizations/{organizationId}/services/csp/nce/subscriptions/{subscriptionId}/upgradeStatus | Returns organization new commerce subscription upgrade status
*OrganizationCspSubscriptionsNceApi* | [**api_resellers_by_reseller_id_organizations_by_organization_id_services_csp_nce_subscriptions_by_subscription_id_upgrade_to_existing_subscription_post**](docs/OrganizationCspSubscriptionsNceApi.md#api_resellers_by_reseller_id_organizations_by_organization_id_services_csp_nce_subscriptions_by_subscription_id_upgrade_to_existing_subscription_post) | **POST** /api/resellers/{resellerId}/organizations/{organizationId}/services/csp/nce/subscriptions/{subscriptionId}/upgradeToExistingSubscription | Upgrade subscription to an existing subscription
*OrganizationCspSubscriptionsNceApi* | [**api_resellers_by_reseller_id_organizations_by_organization_id_services_csp_nce_subscriptions_by_subscription_id_upgrade_to_new_subscription_post**](docs/OrganizationCspSubscriptionsNceApi.md#api_resellers_by_reseller_id_organizations_by_organization_id_services_csp_nce_subscriptions_by_subscription_id_upgrade_to_new_subscription_post) | **POST** /api/resellers/{resellerId}/organizations/{organizationId}/services/csp/nce/subscriptions/{subscriptionId}/upgradeToNewSubscription | Upgrade subscription to new subscripiton
*OrganizationCspSubscriptionsNceApi* | [**api_resellers_by_reseller_id_organizations_by_organization_id_services_csp_nce_subscriptions_get**](docs/OrganizationCspSubscriptionsNceApi.md#api_resellers_by_reseller_id_organizations_by_organization_id_services_csp_nce_subscriptions_get) | **GET** /api/resellers/{resellerId}/organizations/{organizationId}/services/csp/nce/subscriptions | Returns all organization new commerce subscriptions
*OrganizationCspSubscriptionsNceApi* | [**api_resellers_by_reseller_id_organizations_by_organization_id_services_csp_nce_subscriptions_post**](docs/OrganizationCspSubscriptionsNceApi.md#api_resellers_by_reseller_id_organizations_by_organization_id_services_csp_nce_subscriptions_post) | **POST** /api/resellers/{resellerId}/organizations/{organizationId}/services/csp/nce/subscriptions | Creates new commerce subscription for organization Microsoft CSP service
*OrganizationCspUserProductLicensesApi* | [**api_resellers_by_reseller_id_organizations_by_organization_id_services_csp_users_by_user_id_productlicenses_by_id_delete**](docs/OrganizationCspUserProductLicensesApi.md#api_resellers_by_reseller_id_organizations_by_organization_id_services_csp_users_by_user_id_productlicenses_by_id_delete) | **DELETE** /api/resellers/{resellerId}/organizations/{organizationId}/services/csp/users/{userId}/productlicenses/{id} | Removes Office 365 product license from user.
*OrganizationCspUserProductLicensesApi* | [**api_resellers_by_reseller_id_organizations_by_organization_id_services_csp_users_by_user_id_productlicenses_post**](docs/OrganizationCspUserProductLicensesApi.md#api_resellers_by_reseller_id_organizations_by_organization_id_services_csp_users_by_user_id_productlicenses_post) | **POST** /api/resellers/{resellerId}/organizations/{organizationId}/services/csp/users/{userId}/productlicenses | Adds Office 365 product license to user.
*OrganizationCspUsersApi* | [**api_resellers_by_reseller_id_organizations_by_organization_id_services_csp_users_by_id_get**](docs/OrganizationCspUsersApi.md#api_resellers_by_reseller_id_organizations_by_organization_id_services_csp_users_by_id_get) | **GET** /api/resellers/{resellerId}/organizations/{organizationId}/services/csp/users/{id} | Returns organization Microsoft 365 user details.
*OrganizationCspUsersApi* | [**api_resellers_by_reseller_id_organizations_by_organization_id_services_csp_users_by_user_id_delete**](docs/OrganizationCspUsersApi.md#api_resellers_by_reseller_id_organizations_by_organization_id_services_csp_users_by_user_id_delete) | **DELETE** /api/resellers/{resellerId}/organizations/{organizationId}/services/csp/users/{userId} | Delete a Microsoft 365 user.
*OrganizationCspUsersApi* | [**api_resellers_by_reseller_id_organizations_by_organization_id_services_csp_users_by_user_id_put**](docs/OrganizationCspUsersApi.md#api_resellers_by_reseller_id_organizations_by_organization_id_services_csp_users_by_user_id_put) | **PUT** /api/resellers/{resellerId}/organizations/{organizationId}/services/csp/users/{userId} | Update a Microsoft 365 user.
*OrganizationCspUsersApi* | [**api_resellers_by_reseller_id_organizations_by_organization_id_services_csp_users_get**](docs/OrganizationCspUsersApi.md#api_resellers_by_reseller_id_organizations_by_organization_id_services_csp_users_get) | **GET** /api/resellers/{resellerId}/organizations/{organizationId}/services/csp/users | Returns all organization Microsoft 365 users for which a product license can be added.
*OrganizationCspUsersApi* | [**api_resellers_by_reseller_id_organizations_by_organization_id_services_csp_users_post**](docs/OrganizationCspUsersApi.md#api_resellers_by_reseller_id_organizations_by_organization_id_services_csp_users_post) | **POST** /api/resellers/{resellerId}/organizations/{organizationId}/services/csp/users | Creates new Microsoft 365 user.
*OrganizationCspUsersAsyncApi* | [**api_resellers_by_reseller_id_organizations_by_organization_id_services_csp_users_async_by_task_id_get**](docs/OrganizationCspUsersAsyncApi.md#api_resellers_by_reseller_id_organizations_by_organization_id_services_csp_users_async_by_task_id_get) | **GET** /api/resellers/{resellerId}/organizations/{organizationId}/services/csp/usersAsync/{taskId} | Returns asynchronosly generated Csp user list
*OrganizationCspUsersAsyncApi* | [**api_resellers_by_reseller_id_organizations_by_organization_id_services_csp_users_async_post**](docs/OrganizationCspUsersAsyncApi.md#api_resellers_by_reseller_id_organizations_by_organization_id_services_csp_users_async_post) | **POST** /api/resellers/{resellerId}/organizations/{organizationId}/services/csp/usersAsync | starts Asynchronous generation of all organization Microsoft 365 users  for which a product license can be added.
*OrganizationManualBillingLineApi* | [**api_resellers_by_reseller_id_organizations_by_organization_id_manualbilling_by_billing_line_id_put**](docs/OrganizationManualBillingLineApi.md#api_resellers_by_reseller_id_organizations_by_organization_id_manualbilling_by_billing_line_id_put) | **PUT** /api/resellers/{resellerId}/organizations/{organizationId}/manualbilling/{billingLineId} | Updates manual billing line for organization&#39;s service.
*OrganizationManualBillingLineApi* | [**api_resellers_by_reseller_id_organizations_by_organization_id_manualbilling_by_id_delete**](docs/OrganizationManualBillingLineApi.md#api_resellers_by_reseller_id_organizations_by_organization_id_manualbilling_by_id_delete) | **DELETE** /api/resellers/{resellerId}/organizations/{organizationId}/manualbilling/{id} | Deletes manual billing line for organization&#39;s service.
*OrganizationManualBillingLineApi* | [**api_resellers_by_reseller_id_organizations_by_organization_id_manualbilling_by_id_get**](docs/OrganizationManualBillingLineApi.md#api_resellers_by_reseller_id_organizations_by_organization_id_manualbilling_by_id_get) | **GET** /api/resellers/{resellerId}/organizations/{organizationId}/manualbilling/{id} | Returns organization manual billing line details
*OrganizationManualBillingLineApi* | [**api_resellers_by_reseller_id_organizations_by_organization_id_manualbilling_get**](docs/OrganizationManualBillingLineApi.md#api_resellers_by_reseller_id_organizations_by_organization_id_manualbilling_get) | **GET** /api/resellers/{resellerId}/organizations/{organizationId}/manualbilling | Returns all organization manual billing lines for all organization services
*OrganizationManualBillingLineApi* | [**api_resellers_by_reseller_id_organizations_by_organization_id_manualbilling_post**](docs/OrganizationManualBillingLineApi.md#api_resellers_by_reseller_id_organizations_by_organization_id_manualbilling_post) | **POST** /api/resellers/{resellerId}/organizations/{organizationId}/manualbilling | Creates manual billing line for organization&#39;s service
*OrganizationPaymentMethodsApi* | [**api_resellers_by_reseller_id_organizations_by_organization_id_paymentmethods_get**](docs/OrganizationPaymentMethodsApi.md#api_resellers_by_reseller_id_organizations_by_organization_id_paymentmethods_get) | **GET** /api/resellers/{resellerId}/organizations/{organizationId}/paymentmethods | Returns organization payment method.
*OrganizationPaymentMethodsApi* | [**api_resellers_by_reseller_id_organizations_by_organization_id_paymentmethods_put**](docs/OrganizationPaymentMethodsApi.md#api_resellers_by_reseller_id_organizations_by_organization_id_paymentmethods_put) | **PUT** /api/resellers/{resellerId}/organizations/{organizationId}/paymentmethods | Updates organization payment method.
*OrganizationPriceListApi* | [**api_resellers_by_reseller_id_organizations_by_organization_id_services_by_service_id_pricelist_get**](docs/OrganizationPriceListApi.md#api_resellers_by_reseller_id_organizations_by_organization_id_services_by_service_id_pricelist_get) | **GET** /api/resellers/{resellerId}/organizations/{organizationId}/services/{serviceId}/pricelist | Returns all organization products for a service
*OrganizationPriceListApi* | [**api_resellers_by_reseller_id_organizations_by_organization_id_services_by_service_id_pricelist_put**](docs/OrganizationPriceListApi.md#api_resellers_by_reseller_id_organizations_by_organization_id_services_by_service_id_pricelist_put) | **PUT** /api/resellers/{resellerId}/organizations/{organizationId}/services/{serviceId}/pricelist | Updates product or addon price for organization.
*OrganizationRolesApi* | [**api_resellers_by_reseller_id_organizations_by_organization_id_organization_roles_get**](docs/OrganizationRolesApi.md#api_resellers_by_reseller_id_organizations_by_organization_id_organization_roles_get) | **GET** /api/resellers/{resellerId}/organizations/{organizationId}/OrganizationRoles | Returns all organization user roles
*OrganizationServiceProductsApi* | [**api_resellers_by_reseller_id_organizations_by_organization_id_services_by_service_id_products_get**](docs/OrganizationServiceProductsApi.md#api_resellers_by_reseller_id_organizations_by_organization_id_services_by_service_id_products_get) | **GET** /api/resellers/{resellerId}/organizations/{organizationId}/services/{serviceId}/products | Returns all organization service products
*OrganizationServiceSubscriptionsApi* | [**api_resellers_by_reseller_id_organizations_by_organization_id_services_by_service_id_subscriptions_by_subscription_id_delete**](docs/OrganizationServiceSubscriptionsApi.md#api_resellers_by_reseller_id_organizations_by_organization_id_services_by_service_id_subscriptions_by_subscription_id_delete) | **DELETE** /api/resellers/{resellerId}/organizations/{organizationId}/services/{serviceId}/subscriptions/{subscriptionId} | Cancels custom service subscription for organization.
*OrganizationServiceSubscriptionsApi* | [**api_resellers_by_reseller_id_organizations_by_organization_id_services_by_service_id_subscriptions_by_subscription_id_get**](docs/OrganizationServiceSubscriptionsApi.md#api_resellers_by_reseller_id_organizations_by_organization_id_services_by_service_id_subscriptions_by_subscription_id_get) | **GET** /api/resellers/{resellerId}/organizations/{organizationId}/services/{serviceId}/subscriptions/{subscriptionId} | Returns organization custom service subscription
*OrganizationServiceSubscriptionsApi* | [**api_resellers_by_reseller_id_organizations_by_organization_id_services_by_service_id_subscriptions_by_subscription_id_put**](docs/OrganizationServiceSubscriptionsApi.md#api_resellers_by_reseller_id_organizations_by_organization_id_services_by_service_id_subscriptions_by_subscription_id_put) | **PUT** /api/resellers/{resellerId}/organizations/{organizationId}/services/{serviceId}/subscriptions/{subscriptionId} | Update subscription for organization custom service
*OrganizationServiceSubscriptionsApi* | [**api_resellers_by_reseller_id_organizations_by_organization_id_services_by_service_id_subscriptions_get**](docs/OrganizationServiceSubscriptionsApi.md#api_resellers_by_reseller_id_organizations_by_organization_id_services_by_service_id_subscriptions_get) | **GET** /api/resellers/{resellerId}/organizations/{organizationId}/services/{serviceId}/subscriptions | Returns all organization custom service subscriptions, including cancelled
*OrganizationServiceSubscriptionsApi* | [**api_resellers_by_reseller_id_organizations_by_organization_id_services_by_service_id_subscriptions_post**](docs/OrganizationServiceSubscriptionsApi.md#api_resellers_by_reseller_id_organizations_by_organization_id_services_by_service_id_subscriptions_post) | **POST** /api/resellers/{resellerId}/organizations/{organizationId}/services/{serviceId}/subscriptions | Creates subscription for organization custom service
*OrganizationServicesApi* | [**api_resellers_by_reseller_id_organizations_by_organization_id_services_by_service_id_delete**](docs/OrganizationServicesApi.md#api_resellers_by_reseller_id_organizations_by_organization_id_services_by_service_id_delete) | **DELETE** /api/resellers/{resellerId}/organizations/{organizationId}/services/{serviceId} | Removes custom service from organization.
*OrganizationServicesApi* | [**api_resellers_by_reseller_id_organizations_by_organization_id_services_by_service_id_get**](docs/OrganizationServicesApi.md#api_resellers_by_reseller_id_organizations_by_organization_id_services_by_service_id_get) | **GET** /api/resellers/{resellerId}/organizations/{organizationId}/services/{serviceId} | Returns organization service details
*OrganizationServicesApi* | [**api_resellers_by_reseller_id_organizations_by_organization_id_services_by_service_id_patch**](docs/OrganizationServicesApi.md#api_resellers_by_reseller_id_organizations_by_organization_id_services_by_service_id_patch) | **PATCH** /api/resellers/{resellerId}/organizations/{organizationId}/services/{serviceId} | Updates organization service custom property data
*OrganizationServicesApi* | [**api_resellers_by_reseller_id_organizations_by_organization_id_services_by_service_id_put**](docs/OrganizationServicesApi.md#api_resellers_by_reseller_id_organizations_by_organization_id_services_by_service_id_put) | **PUT** /api/resellers/{resellerId}/organizations/{organizationId}/services/{serviceId} | Updates organizations services data.
*OrganizationServicesApi* | [**api_resellers_by_reseller_id_organizations_by_organization_id_services_get**](docs/OrganizationServicesApi.md#api_resellers_by_reseller_id_organizations_by_organization_id_services_get) | **GET** /api/resellers/{resellerId}/organizations/{organizationId}/services | Returns all organization services
*OrganizationServicesApi* | [**api_resellers_by_reseller_id_organizations_by_organization_id_services_post**](docs/OrganizationServicesApi.md#api_resellers_by_reseller_id_organizations_by_organization_id_services_post) | **POST** /api/resellers/{resellerId}/organizations/{organizationId}/services | Adds available custom service from Estore to organization
*OrganizationSubscriptionHistoryApi* | [**api_resellers_by_reseller_id_organizations_by_organization_id_services_by_service_id_subscriptions_history_by_subscription_id_get**](docs/OrganizationSubscriptionHistoryApi.md#api_resellers_by_reseller_id_organizations_by_organization_id_services_by_service_id_subscriptions_history_by_subscription_id_get) | **GET** /api/resellers/{resellerId}/organizations/{organizationId}/services/{serviceId}/Subscriptions/history/{subscriptionId} | Returns organization subscription history
*OrganizationSubscriptionUsersApi* | [**api_resellers_by_reseller_id_organizations_by_organization_id_services_by_service_id_subscriptions_by_subscription_id_users_by_user_id_delete**](docs/OrganizationSubscriptionUsersApi.md#api_resellers_by_reseller_id_organizations_by_organization_id_services_by_service_id_subscriptions_by_subscription_id_users_by_user_id_delete) | **DELETE** /api/resellers/{resellerId}/organizations/{organizationId}/services/{serviceId}/subscriptions/{subscriptionId}/users/{userId} | Removes an user from subscription.
*OrganizationSubscriptionUsersApi* | [**api_resellers_by_reseller_id_organizations_by_organization_id_services_by_service_id_subscriptions_by_subscription_id_users_get**](docs/OrganizationSubscriptionUsersApi.md#api_resellers_by_reseller_id_organizations_by_organization_id_services_by_service_id_subscriptions_by_subscription_id_users_get) | **GET** /api/resellers/{resellerId}/organizations/{organizationId}/services/{serviceId}/subscriptions/{subscriptionId}/users | Returns all organization users assigned to subscription.
*OrganizationSubscriptionUsersApi* | [**api_resellers_by_reseller_id_organizations_by_organization_id_services_by_service_id_subscriptions_by_subscription_id_users_post**](docs/OrganizationSubscriptionUsersApi.md#api_resellers_by_reseller_id_organizations_by_organization_id_services_by_service_id_subscriptions_by_subscription_id_users_post) | **POST** /api/resellers/{resellerId}/organizations/{organizationId}/services/{serviceId}/subscriptions/{subscriptionId}/users | Assign an user to a subscription.
*OrganizationSubscriptionUsersApi* | [**api_resellers_by_reseller_id_organizations_by_organization_id_services_by_service_id_subscriptions_by_subscription_id_users_put**](docs/OrganizationSubscriptionUsersApi.md#api_resellers_by_reseller_id_organizations_by_organization_id_services_by_service_id_subscriptions_by_subscription_id_users_put) | **PUT** /api/resellers/{resellerId}/organizations/{organizationId}/services/{serviceId}/subscriptions/{subscriptionId}/users | Updates subscription external user id.
*OrganizationUserGroupMembersApi* | [**api_resellers_by_reseller_id_organizations_by_organization_id_user_groups_by_group_id_members_by_id_delete**](docs/OrganizationUserGroupMembersApi.md#api_resellers_by_reseller_id_organizations_by_organization_id_user_groups_by_group_id_members_by_id_delete) | **DELETE** /api/resellers/{resellerId}/organizations/{organizationId}/UserGroups/{groupId}/members/{id} | Removes member from user group.
*OrganizationUserGroupMembersApi* | [**api_resellers_by_reseller_id_organizations_by_organization_id_user_groups_by_group_id_members_get**](docs/OrganizationUserGroupMembersApi.md#api_resellers_by_reseller_id_organizations_by_organization_id_user_groups_by_group_id_members_get) | **GET** /api/resellers/{resellerId}/organizations/{organizationId}/UserGroups/{groupId}/members | Returns all organization user group members.
*OrganizationUserGroupMembersApi* | [**api_resellers_by_reseller_id_organizations_by_organization_id_user_groups_by_group_id_members_post**](docs/OrganizationUserGroupMembersApi.md#api_resellers_by_reseller_id_organizations_by_organization_id_user_groups_by_group_id_members_post) | **POST** /api/resellers/{resellerId}/organizations/{organizationId}/UserGroups/{groupId}/members | Adds new member to user group.
*OrganizationUserGroupsApi* | [**api_resellers_by_reseller_id_organizations_by_organization_id_user_groups_by_id_delete**](docs/OrganizationUserGroupsApi.md#api_resellers_by_reseller_id_organizations_by_organization_id_user_groups_by_id_delete) | **DELETE** /api/resellers/{resellerId}/organizations/{organizationId}/UserGroups/{id} | Deletes organization user group.
*OrganizationUserGroupsApi* | [**api_resellers_by_reseller_id_organizations_by_organization_id_user_groups_by_id_get**](docs/OrganizationUserGroupsApi.md#api_resellers_by_reseller_id_organizations_by_organization_id_user_groups_by_id_get) | **GET** /api/resellers/{resellerId}/organizations/{organizationId}/UserGroups/{id} | Returns organization user group details.
*OrganizationUserGroupsApi* | [**api_resellers_by_reseller_id_organizations_by_organization_id_user_groups_by_id_put**](docs/OrganizationUserGroupsApi.md#api_resellers_by_reseller_id_organizations_by_organization_id_user_groups_by_id_put) | **PUT** /api/resellers/{resellerId}/organizations/{organizationId}/UserGroups/{id} | Updates organization user group.
*OrganizationUserGroupsApi* | [**api_resellers_by_reseller_id_organizations_by_organization_id_user_groups_get**](docs/OrganizationUserGroupsApi.md#api_resellers_by_reseller_id_organizations_by_organization_id_user_groups_get) | **GET** /api/resellers/{resellerId}/organizations/{organizationId}/UserGroups | Returns all organization user groups.
*OrganizationUserGroupsApi* | [**api_resellers_by_reseller_id_organizations_by_organization_id_user_groups_post**](docs/OrganizationUserGroupsApi.md#api_resellers_by_reseller_id_organizations_by_organization_id_user_groups_post) | **POST** /api/resellers/{resellerId}/organizations/{organizationId}/UserGroups | Creates new user group for the organization.
*OrganizationsApi* | [**api_resellers_by_reseller_id_organizations_by_id_delete**](docs/OrganizationsApi.md#api_resellers_by_reseller_id_organizations_by_id_delete) | **DELETE** /api/resellers/{resellerId}/Organizations/{id} | Deletes reseller organization.
*OrganizationsApi* | [**api_resellers_by_reseller_id_organizations_by_id_get**](docs/OrganizationsApi.md#api_resellers_by_reseller_id_organizations_by_id_get) | **GET** /api/resellers/{resellerId}/Organizations/{id} | Returns organization details.
*OrganizationsApi* | [**api_resellers_by_reseller_id_organizations_by_id_put**](docs/OrganizationsApi.md#api_resellers_by_reseller_id_organizations_by_id_put) | **PUT** /api/resellers/{resellerId}/Organizations/{id} | Updates reseller organization.
*OrganizationsApi* | [**api_resellers_by_reseller_id_organizations_get**](docs/OrganizationsApi.md#api_resellers_by_reseller_id_organizations_get) | **GET** /api/resellers/{resellerId}/Organizations | Returns all reseller organizations.
*OrganizationsApi* | [**api_resellers_by_reseller_id_organizations_post**](docs/OrganizationsApi.md#api_resellers_by_reseller_id_organizations_post) | **POST** /api/resellers/{resellerId}/Organizations | Creates new organization for the reseller.
*ResellerAdministratorsApi* | [**api_resellers_by_reseller_id_reseller_administrators_by_id_delete**](docs/ResellerAdministratorsApi.md#api_resellers_by_reseller_id_reseller_administrators_by_id_delete) | **DELETE** /api/resellers/{resellerId}/ResellerAdministrators/{id} | Deletes reseller administrator.
*ResellerAdministratorsApi* | [**api_resellers_by_reseller_id_reseller_administrators_by_id_get**](docs/ResellerAdministratorsApi.md#api_resellers_by_reseller_id_reseller_administrators_by_id_get) | **GET** /api/resellers/{resellerId}/ResellerAdministrators/{id} | Returns reseller administrator details.
*ResellerAdministratorsApi* | [**api_resellers_by_reseller_id_reseller_administrators_by_id_put**](docs/ResellerAdministratorsApi.md#api_resellers_by_reseller_id_reseller_administrators_by_id_put) | **PUT** /api/resellers/{resellerId}/ResellerAdministrators/{id} | Updates reseller administrator.
*ResellerAdministratorsApi* | [**api_resellers_by_reseller_id_reseller_administrators_get**](docs/ResellerAdministratorsApi.md#api_resellers_by_reseller_id_reseller_administrators_get) | **GET** /api/resellers/{resellerId}/ResellerAdministrators | Returns all reseller administrators.
*ResellerAdministratorsApi* | [**api_resellers_by_reseller_id_reseller_administrators_post**](docs/ResellerAdministratorsApi.md#api_resellers_by_reseller_id_reseller_administrators_post) | **POST** /api/resellers/{resellerId}/ResellerAdministrators | Creates new administrator for the reseller.
*ResellerAzureSubscriptionsApi* | [**api_resellers_by_reseller_id_services_azure_subscriptions_get**](docs/ResellerAzureSubscriptionsApi.md#api_resellers_by_reseller_id_services_azure_subscriptions_get) | **GET** /api/resellers/{resellerId}/services/azure/Subscriptions | Returns all reseller Azure subscriptions.
*ResellerCspNceSubscriptionsApi* | [**api_resellers_by_reseller_id_services_csp_nce_subscriptions_get**](docs/ResellerCspNceSubscriptionsApi.md#api_resellers_by_reseller_id_services_csp_nce_subscriptions_get) | **GET** /api/resellers/{resellerId}/services/csp/nce/subscriptions | Returns all reseller NCE CSP subscriptions
*ResellerCspSubscriptionsApi* | [**api_resellers_by_reseller_id_services_csp_subscriptions_get**](docs/ResellerCspSubscriptionsApi.md#api_resellers_by_reseller_id_services_csp_subscriptions_get) | **GET** /api/resellers/{resellerId}/services/csp/Subscriptions | Returns all reseller legacy CSP subscriptions
*ResellerEmailTemplatesApi* | [**api_resellers_by_reseller_id_settings_email_templates_get**](docs/ResellerEmailTemplatesApi.md#api_resellers_by_reseller_id_settings_email_templates_get) | **GET** /api/resellers/{resellerId}/settings/EmailTemplates | Returns all reseller email templates
*ResellerOrganizationGroupMembersApi* | [**api_resellers_by_reseller_id_organization_groups_by_group_id_members_by_id_delete**](docs/ResellerOrganizationGroupMembersApi.md#api_resellers_by_reseller_id_organization_groups_by_group_id_members_by_id_delete) | **DELETE** /api/resellers/{resellerId}/OrganizationGroups/{groupId}/Members/{id} | Removes member from organization group.
*ResellerOrganizationGroupMembersApi* | [**api_resellers_by_reseller_id_organization_groups_by_group_id_members_get**](docs/ResellerOrganizationGroupMembersApi.md#api_resellers_by_reseller_id_organization_groups_by_group_id_members_get) | **GET** /api/resellers/{resellerId}/OrganizationGroups/{groupId}/Members | Returns all reseller organization group members.
*ResellerOrganizationGroupMembersApi* | [**api_resellers_by_reseller_id_organization_groups_by_group_id_members_post**](docs/ResellerOrganizationGroupMembersApi.md#api_resellers_by_reseller_id_organization_groups_by_group_id_members_post) | **POST** /api/resellers/{resellerId}/OrganizationGroups/{groupId}/Members | Adds new member to organization group.
*ResellerOrganizationGroupsApi* | [**api_resellers_by_reseller_id_organization_groups_by_id_delete**](docs/ResellerOrganizationGroupsApi.md#api_resellers_by_reseller_id_organization_groups_by_id_delete) | **DELETE** /api/resellers/{resellerId}/OrganizationGroups/{id} | Deletes reseller organization group.
*ResellerOrganizationGroupsApi* | [**api_resellers_by_reseller_id_organization_groups_by_id_get**](docs/ResellerOrganizationGroupsApi.md#api_resellers_by_reseller_id_organization_groups_by_id_get) | **GET** /api/resellers/{resellerId}/OrganizationGroups/{id} | Returns reseller organization group details.
*ResellerOrganizationGroupsApi* | [**api_resellers_by_reseller_id_organization_groups_by_id_put**](docs/ResellerOrganizationGroupsApi.md#api_resellers_by_reseller_id_organization_groups_by_id_put) | **PUT** /api/resellers/{resellerId}/OrganizationGroups/{id} | Updates reseller organization group.
*ResellerOrganizationGroupsApi* | [**api_resellers_by_reseller_id_organization_groups_get**](docs/ResellerOrganizationGroupsApi.md#api_resellers_by_reseller_id_organization_groups_get) | **GET** /api/resellers/{resellerId}/OrganizationGroups | Returns all reseller organization groups.
*ResellerOrganizationGroupsApi* | [**api_resellers_by_reseller_id_organization_groups_post**](docs/ResellerOrganizationGroupsApi.md#api_resellers_by_reseller_id_organization_groups_post) | **POST** /api/resellers/{resellerId}/OrganizationGroups | Creates new organization group for the reseller.
*ResellerPaymentMethodsApi* | [**api_resellers_by_reseller_id_paymentmethods_by_id_delete**](docs/ResellerPaymentMethodsApi.md#api_resellers_by_reseller_id_paymentmethods_by_id_delete) | **DELETE** /api/resellers/{resellerId}/paymentmethods/{id} | Deletes reseller payment method.
*ResellerPaymentMethodsApi* | [**api_resellers_by_reseller_id_paymentmethods_by_id_get**](docs/ResellerPaymentMethodsApi.md#api_resellers_by_reseller_id_paymentmethods_by_id_get) | **GET** /api/resellers/{resellerId}/paymentmethods/{id} | Returns reseller payment method details.
*ResellerPaymentMethodsApi* | [**api_resellers_by_reseller_id_paymentmethods_by_id_put**](docs/ResellerPaymentMethodsApi.md#api_resellers_by_reseller_id_paymentmethods_by_id_put) | **PUT** /api/resellers/{resellerId}/paymentmethods/{id} | Updates reseller payment method.
*ResellerPaymentMethodsApi* | [**api_resellers_by_reseller_id_paymentmethods_get**](docs/ResellerPaymentMethodsApi.md#api_resellers_by_reseller_id_paymentmethods_get) | **GET** /api/resellers/{resellerId}/paymentmethods | Returns all reseller payment methods.
*ResellerPaymentMethodsApi* | [**api_resellers_by_reseller_id_paymentmethods_post**](docs/ResellerPaymentMethodsApi.md#api_resellers_by_reseller_id_paymentmethods_post) | **POST** /api/resellers/{resellerId}/paymentmethods | Creates new payment method for reseller.
*ResellerPriceListApi* | [**api_resellers_by_reseller_id_services_by_service_id_pricelist_commitment_price_get**](docs/ResellerPriceListApi.md#api_resellers_by_reseller_id_services_by_service_id_pricelist_commitment_price_get) | **GET** /api/resellers/{resellerId}/services/{serviceId}/pricelist/CommitmentPrice | Returns the commitment price for a specific subscription of the reseller service
*ResellerPriceListApi* | [**api_resellers_by_reseller_id_services_by_service_id_pricelist_get**](docs/ResellerPriceListApi.md#api_resellers_by_reseller_id_services_by_service_id_pricelist_get) | **GET** /api/resellers/{resellerId}/services/{serviceId}/pricelist | Returns all reseller products for a service
*ResellerPriceListApi* | [**api_resellers_by_reseller_id_services_by_service_id_pricelist_post_renewal_price_get**](docs/ResellerPriceListApi.md#api_resellers_by_reseller_id_services_by_service_id_pricelist_post_renewal_price_get) | **GET** /api/resellers/{resellerId}/services/{serviceId}/pricelist/PostRenewalPrice | Returns the post-renewal price for a specific subscription of the reseller service
*ResellerPriceListApi* | [**api_resellers_by_reseller_id_services_by_service_id_pricelist_put**](docs/ResellerPriceListApi.md#api_resellers_by_reseller_id_services_by_service_id_pricelist_put) | **PUT** /api/resellers/{resellerId}/services/{serviceId}/pricelist | Updates product or addon prices for broker.  For custom services ProductId should be passed as ItemId.  For Microsoft CSP services ItemCode should be passed as ItemId.
*ResellerRolesApi* | [**api_resellers_by_reseller_id_reseller_roles_get**](docs/ResellerRolesApi.md#api_resellers_by_reseller_id_reseller_roles_get) | **GET** /api/resellers/{resellerId}/ResellerRoles | Returns all reseller administrator roles
*ResellerServiceConsumptionsApi* | [**api_resellers_by_reseller_id_services_consumptions_post**](docs/ResellerServiceConsumptionsApi.md#api_resellers_by_reseller_id_services_consumptions_post) | **POST** /api/resellers/{resellerId}/services/consumptions | Returns all reseller service consumption subscriptions
*ResellerServiceConsumptionsApi* | [**api_resellers_by_reseller_id_services_consumptions_put**](docs/ResellerServiceConsumptionsApi.md#api_resellers_by_reseller_id_services_consumptions_put) | **PUT** /api/resellers/{resellerId}/services/consumptions | 
*ResellerServiceProductAddonsApi* | [**api_resellers_by_reseller_id_services_by_service_id_products_by_product_id_addons_by_id_delete**](docs/ResellerServiceProductAddonsApi.md#api_resellers_by_reseller_id_services_by_service_id_products_by_product_id_addons_by_id_delete) | **DELETE** /api/resellers/{resellerId}/services/{serviceId}/products/{productId}/addons/{id} | Deletes Reseller service product addon.
*ResellerServiceProductAddonsApi* | [**api_resellers_by_reseller_id_services_by_service_id_products_by_product_id_addons_by_id_get**](docs/ResellerServiceProductAddonsApi.md#api_resellers_by_reseller_id_services_by_service_id_products_by_product_id_addons_by_id_get) | **GET** /api/resellers/{resellerId}/services/{serviceId}/products/{productId}/addons/{id} | Returns reseller service product addon
*ResellerServiceProductAddonsApi* | [**api_resellers_by_reseller_id_services_by_service_id_products_by_product_id_addons_by_id_put**](docs/ResellerServiceProductAddonsApi.md#api_resellers_by_reseller_id_services_by_service_id_products_by_product_id_addons_by_id_put) | **PUT** /api/resellers/{resellerId}/services/{serviceId}/products/{productId}/addons/{id} | Updates Reseller service product addon.
*ResellerServiceProductAddonsApi* | [**api_resellers_by_reseller_id_services_by_service_id_products_by_product_id_addons_get**](docs/ResellerServiceProductAddonsApi.md#api_resellers_by_reseller_id_services_by_service_id_products_by_product_id_addons_get) | **GET** /api/resellers/{resellerId}/services/{serviceId}/products/{productId}/addons | Returns all reseller service product addons
*ResellerServiceProductAddonsApi* | [**api_resellers_by_reseller_id_services_by_service_id_products_by_product_id_addons_post**](docs/ResellerServiceProductAddonsApi.md#api_resellers_by_reseller_id_services_by_service_id_products_by_product_id_addons_post) | **POST** /api/resellers/{resellerId}/services/{serviceId}/products/{productId}/addons | Creates new product addon for Reseller service.
*ResellerServiceProductsApi* | [**api_resellers_by_reseller_id_services_by_service_id_products_by_id_delete**](docs/ResellerServiceProductsApi.md#api_resellers_by_reseller_id_services_by_service_id_products_by_id_delete) | **DELETE** /api/resellers/{resellerId}/services/{serviceId}/products/{id} | Deletes reseller custom service product.
*ResellerServiceProductsApi* | [**api_resellers_by_reseller_id_services_by_service_id_products_by_id_get**](docs/ResellerServiceProductsApi.md#api_resellers_by_reseller_id_services_by_service_id_products_by_id_get) | **GET** /api/resellers/{resellerId}/services/{serviceId}/products/{id} | Returns reseller custom service details
*ResellerServiceProductsApi* | [**api_resellers_by_reseller_id_services_by_service_id_products_by_id_put**](docs/ResellerServiceProductsApi.md#api_resellers_by_reseller_id_services_by_service_id_products_by_id_put) | **PUT** /api/resellers/{resellerId}/services/{serviceId}/products/{id} | Updates reseller custom service product.
*ResellerServiceProductsApi* | [**api_resellers_by_reseller_id_services_by_service_id_products_get**](docs/ResellerServiceProductsApi.md#api_resellers_by_reseller_id_services_by_service_id_products_get) | **GET** /api/resellers/{resellerId}/services/{serviceId}/products | Returns all reseller custom service products
*ResellerServiceProductsApi* | [**api_resellers_by_reseller_id_services_by_service_id_products_post**](docs/ResellerServiceProductsApi.md#api_resellers_by_reseller_id_services_by_service_id_products_post) | **POST** /api/resellers/{resellerId}/services/{serviceId}/products | Creates new product for reseller custom service.
*ResellerServicesApi* | [**api_resellers_by_reseller_id_services_by_id_delete**](docs/ResellerServicesApi.md#api_resellers_by_reseller_id_services_by_id_delete) | **DELETE** /api/resellers/{resellerId}/services/{id} | Disables service for the broker.
*ResellerServicesApi* | [**api_resellers_by_reseller_id_services_by_id_get**](docs/ResellerServicesApi.md#api_resellers_by_reseller_id_services_by_id_get) | **GET** /api/resellers/{resellerId}/services/{id} | Returns reseller service by identifier
*ResellerServicesApi* | [**api_resellers_by_reseller_id_services_by_id_put**](docs/ResellerServicesApi.md#api_resellers_by_reseller_id_services_by_id_put) | **PUT** /api/resellers/{resellerId}/services/{id} | Updates service for the broker.
*ResellerServicesApi* | [**api_resellers_by_reseller_id_services_by_service_id_patch**](docs/ResellerServicesApi.md#api_resellers_by_reseller_id_services_by_service_id_patch) | **PATCH** /api/resellers/{resellerId}/services/{serviceId} | Updates seller service custom property data for broker.
*ResellerServicesApi* | [**api_resellers_by_reseller_id_services_by_service_id_subscriptions_get**](docs/ResellerServicesApi.md#api_resellers_by_reseller_id_services_by_service_id_subscriptions_get) | **GET** /api/resellers/{resellerId}/services/{serviceId}/subscriptions | Returns reseller subscriptions
*ResellerServicesApi* | [**api_resellers_by_reseller_id_services_get**](docs/ResellerServicesApi.md#api_resellers_by_reseller_id_services_get) | **GET** /api/resellers/{resellerId}/services | Returns all reseller services.
*ResellerServicesApi* | [**api_resellers_by_reseller_id_services_post**](docs/ResellerServicesApi.md#api_resellers_by_reseller_id_services_post) | **POST** /api/resellers/{resellerId}/services | Creates new service for the reseller.
*ResellersApi* | [**api_sellers_by_seller_id_resellers_by_id_get**](docs/ResellersApi.md#api_sellers_by_seller_id_resellers_by_id_get) | **GET** /api/sellers/{sellerId}/resellers/{id} | Returns seller reseller information by id
*ResellersApi* | [**api_sellers_by_seller_id_resellers_get**](docs/ResellersApi.md#api_sellers_by_seller_id_resellers_get) | **GET** /api/sellers/{sellerId}/resellers | This API call will return all Brokers (resellers) that have activated services from the seller.
*SellerAdministratorsApi* | [**api_sellers_by_seller_id_seller_administrators_by_id_delete**](docs/SellerAdministratorsApi.md#api_sellers_by_seller_id_seller_administrators_by_id_delete) | **DELETE** /api/sellers/{sellerId}/SellerAdministrators/{id} | Deletes seller administrator.
*SellerAdministratorsApi* | [**api_sellers_by_seller_id_seller_administrators_by_id_get**](docs/SellerAdministratorsApi.md#api_sellers_by_seller_id_seller_administrators_by_id_get) | **GET** /api/sellers/{sellerId}/SellerAdministrators/{id} | Returns seller administrator details.
*SellerAdministratorsApi* | [**api_sellers_by_seller_id_seller_administrators_by_id_put**](docs/SellerAdministratorsApi.md#api_sellers_by_seller_id_seller_administrators_by_id_put) | **PUT** /api/sellers/{sellerId}/SellerAdministrators/{id} | Updates seller administrator.
*SellerAdministratorsApi* | [**api_sellers_by_seller_id_seller_administrators_get**](docs/SellerAdministratorsApi.md#api_sellers_by_seller_id_seller_administrators_get) | **GET** /api/sellers/{sellerId}/SellerAdministrators | Returns all seller administrators.
*SellerAdministratorsApi* | [**api_sellers_by_seller_id_seller_administrators_post**](docs/SellerAdministratorsApi.md#api_sellers_by_seller_id_seller_administrators_post) | **POST** /api/sellers/{sellerId}/SellerAdministrators | Creates new administrator for the seller.
*SellerBillingReportsApi* | [**api_sellers_by_seller_id_billing_monthly_billing_per_reseller_get**](docs/SellerBillingReportsApi.md#api_sellers_by_seller_id_billing_monthly_billing_per_reseller_get) | **GET** /api/sellers/{sellerId}/billing/MonthlyBillingPerReseller | Returns seller monthly billing report per Broker (reseller)
*SellerBrokersApi* | [**api_sellers_by_seller_id_brokers_by_id_delete**](docs/SellerBrokersApi.md#api_sellers_by_seller_id_brokers_by_id_delete) | **DELETE** /api/sellers/{sellerId}/brokers/{id} | Deletes seller broker.
*SellerBrokersApi* | [**api_sellers_by_seller_id_brokers_by_id_get**](docs/SellerBrokersApi.md#api_sellers_by_seller_id_brokers_by_id_get) | **GET** /api/sellers/{sellerId}/brokers/{id} | Returns seller broker details.
*SellerBrokersApi* | [**api_sellers_by_seller_id_brokers_by_id_put**](docs/SellerBrokersApi.md#api_sellers_by_seller_id_brokers_by_id_put) | **PUT** /api/sellers/{sellerId}/brokers/{id} | Updates seller broker.
*SellerBrokersApi* | [**api_sellers_by_seller_id_brokers_get**](docs/SellerBrokersApi.md#api_sellers_by_seller_id_brokers_get) | **GET** /api/sellers/{sellerId}/brokers | Returns all Seller&#39;s associated Brokers and ServiceBrokers who have added any Seller&#39;s service.
*SellerBrokersApi* | [**api_sellers_by_seller_id_brokers_post**](docs/SellerBrokersApi.md#api_sellers_by_seller_id_brokers_post) | **POST** /api/sellers/{sellerId}/brokers | Creates new broker for the seller.
*SellerEmailTemplatesApi* | [**api_sellers_by_seller_id_settings_email_templates_get**](docs/SellerEmailTemplatesApi.md#api_sellers_by_seller_id_settings_email_templates_get) | **GET** /api/sellers/{sellerId}/settings/EmailTemplates | Returns all seller email templates
*SellerOrganizationsApi* | [**api_sellers_by_seller_id_seller_organizations_by_id_get**](docs/SellerOrganizationsApi.md#api_sellers_by_seller_id_seller_organizations_by_id_get) | **GET** /api/sellers/{sellerId}/SellerOrganizations/{id} | Returns seller organization details.
*SellerPriceListApi* | [**api_sellers_by_seller_id_services_by_service_id_pricelist_get**](docs/SellerPriceListApi.md#api_sellers_by_seller_id_services_by_service_id_pricelist_get) | **GET** /api/sellers/{sellerId}/services/{serviceId}/pricelist | 
*SellerPriceListApi* | [**api_sellers_by_seller_id_services_by_service_id_pricelist_put**](docs/SellerPriceListApi.md#api_sellers_by_seller_id_services_by_service_id_pricelist_put) | **PUT** /api/sellers/{sellerId}/services/{serviceId}/pricelist | Updates product or addon prices for seller custom service.  For custom services ProductId should be passed as ItemId.
*SellerResellersManualBillingLineApi* | [**api_sellers_by_seller_id_resellers_by_reseller_id_manualbilling_by_billing_line_id_delete**](docs/SellerResellersManualBillingLineApi.md#api_sellers_by_seller_id_resellers_by_reseller_id_manualbilling_by_billing_line_id_delete) | **DELETE** /api/sellers/{sellerId}/resellers/{resellerId}/manualbilling/{billingLineId} | Delete a manual billing line for a Broker
*SellerResellersManualBillingLineApi* | [**api_sellers_by_seller_id_resellers_by_reseller_id_manualbilling_by_id_get**](docs/SellerResellersManualBillingLineApi.md#api_sellers_by_seller_id_resellers_by_reseller_id_manualbilling_by_id_get) | **GET** /api/sellers/{sellerId}/resellers/{resellerId}/manualbilling/{id} | Get a reseller&#39;s manual billing line by Id
*SellerResellersManualBillingLineApi* | [**api_sellers_by_seller_id_resellers_by_reseller_id_manualbilling_get**](docs/SellerResellersManualBillingLineApi.md#api_sellers_by_seller_id_resellers_by_reseller_id_manualbilling_get) | **GET** /api/sellers/{sellerId}/resellers/{resellerId}/manualbilling | Returns all manual billing lines for a Broker.
*SellerResellersManualBillingLineApi* | [**api_sellers_by_seller_id_resellers_by_reseller_id_manualbilling_post**](docs/SellerResellersManualBillingLineApi.md#api_sellers_by_seller_id_resellers_by_reseller_id_manualbilling_post) | **POST** /api/sellers/{sellerId}/resellers/{resellerId}/manualbilling | Adds a manual billing line for a Broker
*SellerServiceBulkConsumptionsApi* | [**api_sellers_by_seller_id_services_bulkconsumptions_by_task_id_get**](docs/SellerServiceBulkConsumptionsApi.md#api_sellers_by_seller_id_services_bulkconsumptions_by_task_id_get) | **GET** /api/sellers/{sellerId}/services/bulkconsumptions/{taskId} | Query status of the bulk submitted consumptions
*SellerServiceBulkConsumptionsApi* | [**api_sellers_by_seller_id_services_bulkconsumptions_post**](docs/SellerServiceBulkConsumptionsApi.md#api_sellers_by_seller_id_services_bulkconsumptions_post) | **POST** /api/sellers/{sellerId}/services/bulkconsumptions | Submit seller service consumptions in bulk
*SellerServiceConsumptionsApi* | [**api_sellers_by_seller_id_services_consumptions_post**](docs/SellerServiceConsumptionsApi.md#api_sellers_by_seller_id_services_consumptions_post) | **POST** /api/sellers/{sellerId}/services/consumptions | Returns all seller service consumption subscriptions
*SellerServiceConsumptionsApi* | [**api_sellers_by_seller_id_services_consumptions_put**](docs/SellerServiceConsumptionsApi.md#api_sellers_by_seller_id_services_consumptions_put) | **PUT** /api/sellers/{sellerId}/services/consumptions | Submit seller service consumptions
*SellerServiceProductAddonsApi* | [**api_sellers_by_seller_id_services_by_service_id_products_by_product_id_addons_by_id_delete**](docs/SellerServiceProductAddonsApi.md#api_sellers_by_seller_id_services_by_service_id_products_by_product_id_addons_by_id_delete) | **DELETE** /api/sellers/{sellerId}/services/{serviceId}/products/{productId}/addons/{id} | Deletes Seller service product addon.
*SellerServiceProductAddonsApi* | [**api_sellers_by_seller_id_services_by_service_id_products_by_product_id_addons_by_id_get**](docs/SellerServiceProductAddonsApi.md#api_sellers_by_seller_id_services_by_service_id_products_by_product_id_addons_by_id_get) | **GET** /api/sellers/{sellerId}/services/{serviceId}/products/{productId}/addons/{id} | Returns seller service product addon
*SellerServiceProductAddonsApi* | [**api_sellers_by_seller_id_services_by_service_id_products_by_product_id_addons_by_id_put**](docs/SellerServiceProductAddonsApi.md#api_sellers_by_seller_id_services_by_service_id_products_by_product_id_addons_by_id_put) | **PUT** /api/sellers/{sellerId}/services/{serviceId}/products/{productId}/addons/{id} | Updates Seller service product addon.
*SellerServiceProductAddonsApi* | [**api_sellers_by_seller_id_services_by_service_id_products_by_product_id_addons_get**](docs/SellerServiceProductAddonsApi.md#api_sellers_by_seller_id_services_by_service_id_products_by_product_id_addons_get) | **GET** /api/sellers/{sellerId}/services/{serviceId}/products/{productId}/addons | Returns all seller service product addons
*SellerServiceProductAddonsApi* | [**api_sellers_by_seller_id_services_by_service_id_products_by_product_id_addons_post**](docs/SellerServiceProductAddonsApi.md#api_sellers_by_seller_id_services_by_service_id_products_by_product_id_addons_post) | **POST** /api/sellers/{sellerId}/services/{serviceId}/products/{productId}/addons | Creates new product addon for Seller service.
*SellerServiceProductsApi* | [**api_sellers_by_seller_id_services_by_service_id_products_by_id_delete**](docs/SellerServiceProductsApi.md#api_sellers_by_seller_id_services_by_service_id_products_by_id_delete) | **DELETE** /api/sellers/{sellerId}/services/{serviceId}/products/{id} | Deletes Seller service product.
*SellerServiceProductsApi* | [**api_sellers_by_seller_id_services_by_service_id_products_by_id_get**](docs/SellerServiceProductsApi.md#api_sellers_by_seller_id_services_by_service_id_products_by_id_get) | **GET** /api/sellers/{sellerId}/services/{serviceId}/products/{id} | Returns seller service product details
*SellerServiceProductsApi* | [**api_sellers_by_seller_id_services_by_service_id_products_by_id_put**](docs/SellerServiceProductsApi.md#api_sellers_by_seller_id_services_by_service_id_products_by_id_put) | **PUT** /api/sellers/{sellerId}/services/{serviceId}/products/{id} | Updates Seller service product.
*SellerServiceProductsApi* | [**api_sellers_by_seller_id_services_by_service_id_products_get**](docs/SellerServiceProductsApi.md#api_sellers_by_seller_id_services_by_service_id_products_get) | **GET** /api/sellers/{sellerId}/services/{serviceId}/products | Returns all seller service products
*SellerServiceProductsApi* | [**api_sellers_by_seller_id_services_by_service_id_products_post**](docs/SellerServiceProductsApi.md#api_sellers_by_seller_id_services_by_service_id_products_post) | **POST** /api/sellers/{sellerId}/services/{serviceId}/products | Creates new product for Seller service.
*SellerServicePublishApi* | [**api_sellers_by_seller_id_services_by_id_publish_put**](docs/SellerServicePublishApi.md#api_sellers_by_seller_id_services_by_id_publish_put) | **PUT** /api/sellers/{sellerId}/services/{id}/publish | Publishes service.
*SellerServicesApi* | [**api_sellers_by_seller_id_services_by_id_custom_properties_data_get**](docs/SellerServicesApi.md#api_sellers_by_seller_id_services_by_id_custom_properties_data_get) | **GET** /api/sellers/{sellerId}/services/{id}/custom-properties-data | Returns seller service custom property data
*SellerServicesApi* | [**api_sellers_by_seller_id_services_by_id_delete**](docs/SellerServicesApi.md#api_sellers_by_seller_id_services_by_id_delete) | **DELETE** /api/sellers/{sellerId}/services/{id} | Disables service for the seller
*SellerServicesApi* | [**api_sellers_by_seller_id_services_by_id_get**](docs/SellerServicesApi.md#api_sellers_by_seller_id_services_by_id_get) | **GET** /api/sellers/{sellerId}/services/{id} | Returns seller service by identifier
*SellerServicesApi* | [**api_sellers_by_seller_id_services_by_id_put**](docs/SellerServicesApi.md#api_sellers_by_seller_id_services_by_id_put) | **PUT** /api/sellers/{sellerId}/services/{id} | Updates service for the seller.
*SellerServicesApi* | [**api_sellers_by_seller_id_services_by_service_id_resellers_get**](docs/SellerServicesApi.md#api_sellers_by_seller_id_services_by_service_id_resellers_get) | **GET** /api/sellers/{sellerId}/services/{serviceId}/resellers | Returns the list of resellers who has signed seller&#39;s services
*SellerServicesApi* | [**api_sellers_by_seller_id_services_get**](docs/SellerServicesApi.md#api_sellers_by_seller_id_services_get) | **GET** /api/sellers/{sellerId}/services | Returns all seller services
*SellerServicesApi* | [**api_sellers_by_seller_id_services_post**](docs/SellerServicesApi.md#api_sellers_by_seller_id_services_post) | **POST** /api/sellers/{sellerId}/services | Creates new service for the seller.
*SellerSubscriptionsApi* | [**api_sellers_by_seller_id_subscriptions_by_subscription_id_delete**](docs/SellerSubscriptionsApi.md#api_sellers_by_seller_id_subscriptions_by_subscription_id_delete) | **DELETE** /api/sellers/{sellerId}/subscriptions/{subscriptionId} | Cancels/deletes custom service subscription.
*SellerSubscriptionsApi* | [**api_sellers_by_seller_id_subscriptions_by_subscription_id_get**](docs/SellerSubscriptionsApi.md#api_sellers_by_seller_id_subscriptions_by_subscription_id_get) | **GET** /api/sellers/{sellerId}/subscriptions/{subscriptionId} | Returns seller subscription details
*SellerSubscriptionsApi* | [**api_sellers_by_seller_id_subscriptions_get**](docs/SellerSubscriptionsApi.md#api_sellers_by_seller_id_subscriptions_get) | **GET** /api/sellers/{sellerId}/subscriptions | Returns all seller subscriptions, including cancelled
*SellerSubscriptionsApi* | [**api_sellers_by_seller_id_subscriptions_service_by_service_id_get**](docs/SellerSubscriptionsApi.md#api_sellers_by_seller_id_subscriptions_service_by_service_id_get) | **GET** /api/sellers/{sellerId}/subscriptions/service/{serviceId} | Returns seller subscriptions by service identifier
*SellerSubscriptionsApi* | [**api_sellers_by_seller_id_subscriptions_set_license_key_by_subscription_id_put**](docs/SellerSubscriptionsApi.md#api_sellers_by_seller_id_subscriptions_set_license_key_by_subscription_id_put) | **PUT** /api/sellers/{sellerId}/subscriptions/SetLicenseKey/{subscriptionId} | Set license key for subscription. License keys must be enabled for service.
*ServiceCategoriesApi* | [**api_services_categories_get**](docs/ServiceCategoriesApi.md#api_services_categories_get) | **GET** /api/services/categories | Retrieve service categories
*UsersApi* | [**api_resellers_by_reseller_id_organizations_by_organization_id_users_by_id_delete**](docs/UsersApi.md#api_resellers_by_reseller_id_organizations_by_organization_id_users_by_id_delete) | **DELETE** /api/resellers/{resellerId}/organizations/{organizationId}/Users/{id} | Deletes organization user.
*UsersApi* | [**api_resellers_by_reseller_id_organizations_by_organization_id_users_by_id_get**](docs/UsersApi.md#api_resellers_by_reseller_id_organizations_by_organization_id_users_by_id_get) | **GET** /api/resellers/{resellerId}/organizations/{organizationId}/Users/{id} | Returns user details.
*UsersApi* | [**api_resellers_by_reseller_id_organizations_by_organization_id_users_by_id_put**](docs/UsersApi.md#api_resellers_by_reseller_id_organizations_by_organization_id_users_by_id_put) | **PUT** /api/resellers/{resellerId}/organizations/{organizationId}/Users/{id} | Updates organizarion user.
*UsersApi* | [**api_resellers_by_reseller_id_organizations_by_organization_id_users_get**](docs/UsersApi.md#api_resellers_by_reseller_id_organizations_by_organization_id_users_get) | **GET** /api/resellers/{resellerId}/organizations/{organizationId}/Users | Returns all organization users.
*UsersApi* | [**api_resellers_by_reseller_id_organizations_by_organization_id_users_post**](docs/UsersApi.md#api_resellers_by_reseller_id_organizations_by_organization_id_users_post) | **POST** /api/resellers/{resellerId}/organizations/{organizationId}/Users | Creates new user for the organization.
*WebHooksApi* | [**api_sellers_by_seller_id_webhooks_by_id_delete**](docs/WebHooksApi.md#api_sellers_by_seller_id_webhooks_by_id_delete) | **DELETE** /api/sellers/{sellerId}/webhooks/{id} | Deletes webhook.
*WebHooksApi* | [**api_sellers_by_seller_id_webhooks_by_id_get**](docs/WebHooksApi.md#api_sellers_by_seller_id_webhooks_by_id_get) | **GET** /api/sellers/{sellerId}/webhooks/{id} | Returns seller webhook by identifier
*WebHooksApi* | [**api_sellers_by_seller_id_webhooks_by_id_put**](docs/WebHooksApi.md#api_sellers_by_seller_id_webhooks_by_id_put) | **PUT** /api/sellers/{sellerId}/webhooks/{id} | Updates webhook.
*WebHooksApi* | [**api_sellers_by_seller_id_webhooks_get**](docs/WebHooksApi.md#api_sellers_by_seller_id_webhooks_get) | **GET** /api/sellers/{sellerId}/webhooks | Returns all seller webhooks
*WebHooksApi* | [**api_sellers_by_seller_id_webhooks_post**](docs/WebHooksApi.md#api_sellers_by_seller_id_webhooks_post) | **POST** /api/sellers/{sellerId}/webhooks | Creates new webhook for the seller service.


## Documentation For Models

 - [AddonGetViewModel](docs/AddonGetViewModel.md)
 - [AddonSetViewModel](docs/AddonSetViewModel.md)
 - [AdministratorAddressCreateViewModel](docs/AdministratorAddressCreateViewModel.md)
 - [AdministratorAddressDetailViewModel](docs/AdministratorAddressDetailViewModel.md)
 - [AdministratorAddressUpdateViewModel](docs/AdministratorAddressUpdateViewModel.md)
 - [AdministratorCreateViewModel](docs/AdministratorCreateViewModel.md)
 - [AdministratorDetailViewModel](docs/AdministratorDetailViewModel.md)
 - [AdministratorUpdateViewModel](docs/AdministratorUpdateViewModel.md)
 - [AdministratorViewModel](docs/AdministratorViewModel.md)
 - [ApiError](docs/ApiError.md)
 - [AzureCategoryBillingViewModel](docs/AzureCategoryBillingViewModel.md)
 - [AzureCustomInvoiceBillingReportViewModel](docs/AzureCustomInvoiceBillingReportViewModel.md)
 - [AzureDetailBillingViewModel](docs/AzureDetailBillingViewModel.md)
 - [AzureInvoiceOverviewOrganizationViewModel](docs/AzureInvoiceOverviewOrganizationViewModel.md)
 - [AzureInvoiceOverviewViewModel](docs/AzureInvoiceOverviewViewModel.md)
 - [AzureOneTimeBilledUsageReportLineItemViewModel](docs/AzureOneTimeBilledUsageReportLineItemViewModel.md)
 - [AzureOneTimeBilledUsageReportViewModel](docs/AzureOneTimeBilledUsageReportViewModel.md)
 - [AzureOneTimeBillingAsyncViewModel](docs/AzureOneTimeBillingAsyncViewModel.md)
 - [AzureOneTimeBillingReportAsyncViewModel](docs/AzureOneTimeBillingReportAsyncViewModel.md)
 - [AzureOneTimeInvoiceListVeiwModel](docs/AzureOneTimeInvoiceListVeiwModel.md)
 - [AzureOneTimeUnBilledUsageReportLineItemViewModel](docs/AzureOneTimeUnBilledUsageReportLineItemViewModel.md)
 - [AzureOneTimeUnbilledUsageReportViewModel](docs/AzureOneTimeUnbilledUsageReportViewModel.md)
 - [AzureOneTimeUnbilledUsageRequestStatusViewModel](docs/AzureOneTimeUnbilledUsageRequestStatusViewModel.md)
 - [AzureOneTimeUnbilledUsageRequestViewModel](docs/AzureOneTimeUnbilledUsageRequestViewModel.md)
 - [AzureOneTimeUsageReportViewModel](docs/AzureOneTimeUsageReportViewModel.md)
 - [AzureOngoingPeriodBillingReportViewModel](docs/AzureOngoingPeriodBillingReportViewModel.md)
 - [AzureOrganizationBillingViewModel](docs/AzureOrganizationBillingViewModel.md)
 - [AzurePartnerInvoiceBaseViewModel](docs/AzurePartnerInvoiceBaseViewModel.md)
 - [AzurePartnerInvoiceItemViewModel](docs/AzurePartnerInvoiceItemViewModel.md)
 - [AzureServiceCategoryViewModel](docs/AzureServiceCategoryViewModel.md)
 - [AzureSubscriptionBillingViewModel](docs/AzureSubscriptionBillingViewModel.md)
 - [AzureSubscriptionViewModel](docs/AzureSubscriptionViewModel.md)
 - [BrokerCustomPropertyViewModel](docs/BrokerCustomPropertyViewModel.md)
 - [BrokerPriceListUpdateViewModel](docs/BrokerPriceListUpdateViewModel.md)
 - [CommitmentPriceViewModel](docs/CommitmentPriceViewModel.md)
 - [CoterminousDate](docs/CoterminousDate.md)
 - [CspCloudAgreement](docs/CspCloudAgreement.md)
 - [CspCloudAgreementContact](docs/CspCloudAgreementContact.md)
 - [CspDomainValidationViewModel](docs/CspDomainValidationViewModel.md)
 - [CspLinkedTenantViewModel](docs/CspLinkedTenantViewModel.md)
 - [CspNceEligibleProductViewModel](docs/CspNceEligibleProductViewModel.md)
 - [CspNceSubscriptionViewModel](docs/CspNceSubscriptionViewModel.md)
 - [CspOrganizationBillingCycleFeeViewModel](docs/CspOrganizationBillingCycleFeeViewModel.md)
 - [CspOrganizationBillingOtherItemViewModel](docs/CspOrganizationBillingOtherItemViewModel.md)
 - [CspOrganizationBillingOtherViewModel](docs/CspOrganizationBillingOtherViewModel.md)
 - [CspOrganizationBillingProRateItemViewModel](docs/CspOrganizationBillingProRateItemViewModel.md)
 - [CspOrganizationBillingProRateViewModel](docs/CspOrganizationBillingProRateViewModel.md)
 - [CspOrganizationBillingSubscription](docs/CspOrganizationBillingSubscription.md)
 - [CspOrganizationBillingViewModel](docs/CspOrganizationBillingViewModel.md)
 - [CspOrganizationViewModel](docs/CspOrganizationViewModel.md)
 - [CspProductsLicense](docs/CspProductsLicense.md)
 - [CspServiceCategoryViewModel](docs/CspServiceCategoryViewModel.md)
 - [CspSubscriptionViewModel](docs/CspSubscriptionViewModel.md)
 - [CspTenantLinkViewModel](docs/CspTenantLinkViewModel.md)
 - [CspTenantViewModel](docs/CspTenantViewModel.md)
 - [CustomPropertyDataGetViewModel](docs/CustomPropertyDataGetViewModel.md)
 - [CustomPropertyDataSetViewModel](docs/CustomPropertyDataSetViewModel.md)
 - [CustomServiceCustomPropertyViewModel](docs/CustomServiceCustomPropertyViewModel.md)
 - [DetailViewCustomProperty](docs/DetailViewCustomProperty.md)
 - [EstoreDetailViewModel](docs/EstoreDetailViewModel.md)
 - [EstoreServiceCategoryViewModel](docs/EstoreServiceCategoryViewModel.md)
 - [EstoreViewModel](docs/EstoreViewModel.md)
 - [ExternalInvoiceCreateViewModel](docs/ExternalInvoiceCreateViewModel.md)
 - [ExternalInvoiceUpdateViewModel](docs/ExternalInvoiceUpdateViewModel.md)
 - [ExternalInvoiceViewModel](docs/ExternalInvoiceViewModel.md)
 - [ManualBillingLineCreateViewModel](docs/ManualBillingLineCreateViewModel.md)
 - [ManualBillingLineViewModel](docs/ManualBillingLineViewModel.md)
 - [MarketCountryViewModel](docs/MarketCountryViewModel.md)
 - [MarketRegionViewModel](docs/MarketRegionViewModel.md)
 - [MbpoOrganizationViewModel](docs/MbpoOrganizationViewModel.md)
 - [MbpoProductViewModel](docs/MbpoProductViewModel.md)
 - [MbpoServiceItemViewModel](docs/MbpoServiceItemViewModel.md)
 - [MbpoServiceViewModel](docs/MbpoServiceViewModel.md)
 - [MbprResellerViewModel](docs/MbprResellerViewModel.md)
 - [MbprServiceProductViewModel](docs/MbprServiceProductViewModel.md)
 - [MbprServiceSubscriptionViewModel](docs/MbprServiceSubscriptionViewModel.md)
 - [MbprServiceViewModel](docs/MbprServiceViewModel.md)
 - [MbpsOrganizationViewModel](docs/MbpsOrganizationViewModel.md)
 - [MbpsProductViewModel](docs/MbpsProductViewModel.md)
 - [MbpsServiceItemViewModel](docs/MbpsServiceItemViewModel.md)
 - [MbpsServiceViewModel](docs/MbpsServiceViewModel.md)
 - [MonthlyAzureBillingPerOrganizationViewModel](docs/MonthlyAzureBillingPerOrganizationViewModel.md)
 - [MonthlyBillingPerOrganizationAsyncViewModel](docs/MonthlyBillingPerOrganizationAsyncViewModel.md)
 - [MonthlyBillingPerOrganizationCreateAsyncViewModel](docs/MonthlyBillingPerOrganizationCreateAsyncViewModel.md)
 - [MonthlyBillingPerOrganizationViewModel](docs/MonthlyBillingPerOrganizationViewModel.md)
 - [MonthlyBillingPerResellerViewModel](docs/MonthlyBillingPerResellerViewModel.md)
 - [MonthlyBillingPerServiceViewModel](docs/MonthlyBillingPerServiceViewModel.md)
 - [MonthlyCspBillingPerOrganizationViewModel](docs/MonthlyCspBillingPerOrganizationViewModel.md)
 - [OrganizationAddressCreateViewModel](docs/OrganizationAddressCreateViewModel.md)
 - [OrganizationAddressDetailViewModel](docs/OrganizationAddressDetailViewModel.md)
 - [OrganizationAddressUpdateViewModel](docs/OrganizationAddressUpdateViewModel.md)
 - [OrganizationAzureAddViewModel](docs/OrganizationAzureAddViewModel.md)
 - [OrganizationAzureDetailViewModel](docs/OrganizationAzureDetailViewModel.md)
 - [OrganizationAzurePlanSubscriptionUpdateViewModel](docs/OrganizationAzurePlanSubscriptionUpdateViewModel.md)
 - [OrganizationAzureSubscriptionCreateViewModel](docs/OrganizationAzureSubscriptionCreateViewModel.md)
 - [OrganizationAzureSubscriptionViewModel](docs/OrganizationAzureSubscriptionViewModel.md)
 - [OrganizationAzureUserRoleSubscriptionUpdateViewModel](docs/OrganizationAzureUserRoleSubscriptionUpdateViewModel.md)
 - [OrganizationAzureUserSubscriptionAddViewModel](docs/OrganizationAzureUserSubscriptionAddViewModel.md)
 - [OrganizationAzureUserSubscriptionViewModel](docs/OrganizationAzureUserSubscriptionViewModel.md)
 - [OrganizationAzureUserViewModel](docs/OrganizationAzureUserViewModel.md)
 - [OrganizationContactCreateViewModel](docs/OrganizationContactCreateViewModel.md)
 - [OrganizationContactDetailViewModel](docs/OrganizationContactDetailViewModel.md)
 - [OrganizationContactUpdateViewModel](docs/OrganizationContactUpdateViewModel.md)
 - [OrganizationCostCenterReportModel](docs/OrganizationCostCenterReportModel.md)
 - [OrganizationCreateCustomProperty](docs/OrganizationCreateCustomProperty.md)
 - [OrganizationCreateViewModel](docs/OrganizationCreateViewModel.md)
 - [OrganizationCspAddViewModel](docs/OrganizationCspAddViewModel.md)
 - [OrganizationCspDetailViewModel](docs/OrganizationCspDetailViewModel.md)
 - [OrganizationCspNceSkuViewModel](docs/OrganizationCspNceSkuViewModel.md)
 - [OrganizationCspNceSubscriptionCreateViewModel](docs/OrganizationCspNceSubscriptionCreateViewModel.md)
 - [OrganizationCspNceSubscriptionEditViewModel](docs/OrganizationCspNceSubscriptionEditViewModel.md)
 - [OrganizationCspNceSubscriptionExistingSubscriptionEligibilityViewModel](docs/OrganizationCspNceSubscriptionExistingSubscriptionEligibilityViewModel.md)
 - [OrganizationCspNceSubscriptionNewSubscriptionEligibilityViewModel](docs/OrganizationCspNceSubscriptionNewSubscriptionEligibilityViewModel.md)
 - [OrganizationCspNceSubscriptionTransitionStatusViewModel](docs/OrganizationCspNceSubscriptionTransitionStatusViewModel.md)
 - [OrganizationCspNceSubscriptionUpgradeToExistingSubscriptionViewModel](docs/OrganizationCspNceSubscriptionUpgradeToExistingSubscriptionViewModel.md)
 - [OrganizationCspNceSubscriptionUpgradeToNewSubscriptionViewModel](docs/OrganizationCspNceSubscriptionUpgradeToNewSubscriptionViewModel.md)
 - [OrganizationCspNceSubscriptionViewModel](docs/OrganizationCspNceSubscriptionViewModel.md)
 - [OrganizationCspNceSubscriptionsAlignmentDatesViewModel](docs/OrganizationCspNceSubscriptionsAlignmentDatesViewModel.md)
 - [OrganizationCspProductLicenseViewModel](docs/OrganizationCspProductLicenseViewModel.md)
 - [OrganizationCspProductViewModel](docs/OrganizationCspProductViewModel.md)
 - [OrganizationCspSubscriptionCreateViewModel](docs/OrganizationCspSubscriptionCreateViewModel.md)
 - [OrganizationCspSubscriptionEditViewModel](docs/OrganizationCspSubscriptionEditViewModel.md)
 - [OrganizationCspSubscriptionViewModel](docs/OrganizationCspSubscriptionViewModel.md)
 - [OrganizationCspUserAsyncViewModel](docs/OrganizationCspUserAsyncViewModel.md)
 - [OrganizationCspUserCreateViewModel](docs/OrganizationCspUserCreateViewModel.md)
 - [OrganizationCspUserProductLicenseAddViewModel](docs/OrganizationCspUserProductLicenseAddViewModel.md)
 - [OrganizationCspUserUpdateViewModel](docs/OrganizationCspUserUpdateViewModel.md)
 - [OrganizationCspUsersViewModel](docs/OrganizationCspUsersViewModel.md)
 - [OrganizationDetailViewModel](docs/OrganizationDetailViewModel.md)
 - [OrganizationManualBillingLineCreateViewModel](docs/OrganizationManualBillingLineCreateViewModel.md)
 - [OrganizationManualBillingLineUpdateViewModel](docs/OrganizationManualBillingLineUpdateViewModel.md)
 - [OrganizationManualBillingLineViewModel](docs/OrganizationManualBillingLineViewModel.md)
 - [OrganizationPaymentMethodUpdateViewModel](docs/OrganizationPaymentMethodUpdateViewModel.md)
 - [OrganizationPaymentMethodViewModel](docs/OrganizationPaymentMethodViewModel.md)
 - [OrganizationPriceListUpdateViewModel](docs/OrganizationPriceListUpdateViewModel.md)
 - [OrganizationPriceListViewModel](docs/OrganizationPriceListViewModel.md)
 - [OrganizationProductAddon](docs/OrganizationProductAddon.md)
 - [OrganizationServiceAddViewModel](docs/OrganizationServiceAddViewModel.md)
 - [OrganizationServiceDetailViewModel](docs/OrganizationServiceDetailViewModel.md)
 - [OrganizationServiceProductAddonViewModel](docs/OrganizationServiceProductAddonViewModel.md)
 - [OrganizationServiceProductViewModel](docs/OrganizationServiceProductViewModel.md)
 - [OrganizationServiceSubscriptionCreateViewModel](docs/OrganizationServiceSubscriptionCreateViewModel.md)
 - [OrganizationServiceSubscriptionUpdateViewModel](docs/OrganizationServiceSubscriptionUpdateViewModel.md)
 - [OrganizationServiceSubscriptionUserCreateViewModel](docs/OrganizationServiceSubscriptionUserCreateViewModel.md)
 - [OrganizationServiceSubscriptionUserUpdateViewModel](docs/OrganizationServiceSubscriptionUserUpdateViewModel.md)
 - [OrganizationServiceSubscriptionUserViewModel](docs/OrganizationServiceSubscriptionUserViewModel.md)
 - [OrganizationServiceSubscriptionViewModel](docs/OrganizationServiceSubscriptionViewModel.md)
 - [OrganizationServiceUpdateViewModel](docs/OrganizationServiceUpdateViewModel.md)
 - [OrganizationServiceViewModel](docs/OrganizationServiceViewModel.md)
 - [OrganizationSubscriptionHistoryViewModel](docs/OrganizationSubscriptionHistoryViewModel.md)
 - [OrganizationUpdateCustomProperty](docs/OrganizationUpdateCustomProperty.md)
 - [OrganizationUpdateViewModel](docs/OrganizationUpdateViewModel.md)
 - [OrganizationUserGroupCreateViewModel](docs/OrganizationUserGroupCreateViewModel.md)
 - [OrganizationUserGroupMemberAddViewModel](docs/OrganizationUserGroupMemberAddViewModel.md)
 - [OrganizationUserGroupMemberViewModel](docs/OrganizationUserGroupMemberViewModel.md)
 - [OrganizationUserGroupUpdateViewModel](docs/OrganizationUserGroupUpdateViewModel.md)
 - [OrganizationUserGroupViewModel](docs/OrganizationUserGroupViewModel.md)
 - [OrganizationViewModel](docs/OrganizationViewModel.md)
 - [PostRenewalPriceContext](docs/PostRenewalPriceContext.md)
 - [PostRenewalPriceViewModel](docs/PostRenewalPriceViewModel.md)
 - [Price](docs/Price.md)
 - [ProductCustomProperty](docs/ProductCustomProperty.md)
 - [ResellerEmailTemplateViewModel](docs/ResellerEmailTemplateViewModel.md)
 - [ResellerOrganizationGroupCreateViewModel](docs/ResellerOrganizationGroupCreateViewModel.md)
 - [ResellerOrganizationGroupMemberAddViewModel](docs/ResellerOrganizationGroupMemberAddViewModel.md)
 - [ResellerOrganizationGroupMemberViewModel](docs/ResellerOrganizationGroupMemberViewModel.md)
 - [ResellerOrganizationGroupUpdateViewModel](docs/ResellerOrganizationGroupUpdateViewModel.md)
 - [ResellerOrganizationGroupViewModel](docs/ResellerOrganizationGroupViewModel.md)
 - [ResellerPaymentMethodCreateViewModel](docs/ResellerPaymentMethodCreateViewModel.md)
 - [ResellerPaymentMethodUpdateViewModel](docs/ResellerPaymentMethodUpdateViewModel.md)
 - [ResellerPaymentMethodViewModel](docs/ResellerPaymentMethodViewModel.md)
 - [ResellerPriceListViewModel](docs/ResellerPriceListViewModel.md)
 - [ResellerProductAddon](docs/ResellerProductAddon.md)
 - [ResellerServiceConsumptionsAddonViewModel](docs/ResellerServiceConsumptionsAddonViewModel.md)
 - [ResellerServiceConsumptionsCreateViewModel](docs/ResellerServiceConsumptionsCreateViewModel.md)
 - [ResellerServiceConsumptionsFilterViewModel](docs/ResellerServiceConsumptionsFilterViewModel.md)
 - [ResellerServiceConsumptionsProductViewModel](docs/ResellerServiceConsumptionsProductViewModel.md)
 - [ResellerServiceConsumptionsServiceViewModel](docs/ResellerServiceConsumptionsServiceViewModel.md)
 - [ResellerServiceConsumptionsSubscriptionViewModel](docs/ResellerServiceConsumptionsSubscriptionViewModel.md)
 - [ResellerServiceConsumptionsViewModel](docs/ResellerServiceConsumptionsViewModel.md)
 - [ResellerServiceCreateViewModel](docs/ResellerServiceCreateViewModel.md)
 - [ResellerServiceCustomPropertyDataUpdateViewModel](docs/ResellerServiceCustomPropertyDataUpdateViewModel.md)
 - [ResellerServiceDetailViewModel](docs/ResellerServiceDetailViewModel.md)
 - [ResellerServiceProductAddonCreateViewModel](docs/ResellerServiceProductAddonCreateViewModel.md)
 - [ResellerServiceProductAddonUpdateViewModel](docs/ResellerServiceProductAddonUpdateViewModel.md)
 - [ResellerServiceProductAddonViewModel](docs/ResellerServiceProductAddonViewModel.md)
 - [ResellerServiceProductCreateViewModel](docs/ResellerServiceProductCreateViewModel.md)
 - [ResellerServiceProductDetailViewModel](docs/ResellerServiceProductDetailViewModel.md)
 - [ResellerServiceProductUpdateViewModel](docs/ResellerServiceProductUpdateViewModel.md)
 - [ResellerServiceProductViewModel](docs/ResellerServiceProductViewModel.md)
 - [ResellerServiceSubscriptionViewModel](docs/ResellerServiceSubscriptionViewModel.md)
 - [ResellerServiceUpdateViewModel](docs/ResellerServiceUpdateViewModel.md)
 - [ResellerServiceViewModel](docs/ResellerServiceViewModel.md)
 - [ResourceAttributes](docs/ResourceAttributes.md)
 - [RoleViewModel](docs/RoleViewModel.md)
 - [SellerAdministratorCreateViewModel](docs/SellerAdministratorCreateViewModel.md)
 - [SellerAdministratorDetailViewModel](docs/SellerAdministratorDetailViewModel.md)
 - [SellerAdministratorUpdateViewModel](docs/SellerAdministratorUpdateViewModel.md)
 - [SellerAdministratorViewModel](docs/SellerAdministratorViewModel.md)
 - [SellerBrokerAddressCreateViewModel](docs/SellerBrokerAddressCreateViewModel.md)
 - [SellerBrokerAddressDetailViewModel](docs/SellerBrokerAddressDetailViewModel.md)
 - [SellerBrokerAddressUpdateViewModel](docs/SellerBrokerAddressUpdateViewModel.md)
 - [SellerBrokerContactCreateViewModel](docs/SellerBrokerContactCreateViewModel.md)
 - [SellerBrokerContactDetailViewModel](docs/SellerBrokerContactDetailViewModel.md)
 - [SellerBrokerContactUpdateViewModel](docs/SellerBrokerContactUpdateViewModel.md)
 - [SellerBrokerCreateViewModel](docs/SellerBrokerCreateViewModel.md)
 - [SellerBrokerDetailViewModel](docs/SellerBrokerDetailViewModel.md)
 - [SellerBrokerInvoiceContactCreateViewModel](docs/SellerBrokerInvoiceContactCreateViewModel.md)
 - [SellerBrokerInvoiceContactDetailViewModel](docs/SellerBrokerInvoiceContactDetailViewModel.md)
 - [SellerBrokerInvoiceContactUpdateViewModel](docs/SellerBrokerInvoiceContactUpdateViewModel.md)
 - [SellerBrokerUpdateViewModel](docs/SellerBrokerUpdateViewModel.md)
 - [SellerBrokerViewModel](docs/SellerBrokerViewModel.md)
 - [SellerCustomPropertyViewModel](docs/SellerCustomPropertyViewModel.md)
 - [SellerEmailTemplateViewModel](docs/SellerEmailTemplateViewModel.md)
 - [SellerPriceListUpdateViewModel](docs/SellerPriceListUpdateViewModel.md)
 - [SellerProductAddon](docs/SellerProductAddon.md)
 - [SellerProductPriceListModel](docs/SellerProductPriceListModel.md)
 - [SellerResellerViewModel](docs/SellerResellerViewModel.md)
 - [SellerServiceBulkConsumptionAcceptedViewModel](docs/SellerServiceBulkConsumptionAcceptedViewModel.md)
 - [SellerServiceBulkConsumptionFailedRecord](docs/SellerServiceBulkConsumptionFailedRecord.md)
 - [SellerServiceBulkConsumptionRecord](docs/SellerServiceBulkConsumptionRecord.md)
 - [SellerServiceBulkConsumptionStatusViewModel](docs/SellerServiceBulkConsumptionStatusViewModel.md)
 - [SellerServiceBulkConsumptionViewModel](docs/SellerServiceBulkConsumptionViewModel.md)
 - [SellerServiceConsumptionsAddonViewModel](docs/SellerServiceConsumptionsAddonViewModel.md)
 - [SellerServiceConsumptionsCreateViewModel](docs/SellerServiceConsumptionsCreateViewModel.md)
 - [SellerServiceConsumptionsFilterViewModel](docs/SellerServiceConsumptionsFilterViewModel.md)
 - [SellerServiceConsumptionsOrganizationViewModel](docs/SellerServiceConsumptionsOrganizationViewModel.md)
 - [SellerServiceConsumptionsProductViewModel](docs/SellerServiceConsumptionsProductViewModel.md)
 - [SellerServiceConsumptionsServiceViewModel](docs/SellerServiceConsumptionsServiceViewModel.md)
 - [SellerServiceConsumptionsSubscriptionViewModel](docs/SellerServiceConsumptionsSubscriptionViewModel.md)
 - [SellerServiceConsumptionsViewModel](docs/SellerServiceConsumptionsViewModel.md)
 - [SellerServiceCreateViewModel](docs/SellerServiceCreateViewModel.md)
 - [SellerServiceProductAddonCreateViewModel](docs/SellerServiceProductAddonCreateViewModel.md)
 - [SellerServiceProductAddonUpdateViewModel](docs/SellerServiceProductAddonUpdateViewModel.md)
 - [SellerServiceProductAddonViewModel](docs/SellerServiceProductAddonViewModel.md)
 - [SellerServiceProductCreateViewModel](docs/SellerServiceProductCreateViewModel.md)
 - [SellerServiceProductDetailViewModel](docs/SellerServiceProductDetailViewModel.md)
 - [SellerServiceProductUpdateViewModel](docs/SellerServiceProductUpdateViewModel.md)
 - [SellerServiceProductViewModel](docs/SellerServiceProductViewModel.md)
 - [SellerServicePublishViewModel](docs/SellerServicePublishViewModel.md)
 - [SellerServiceResellerViewModel](docs/SellerServiceResellerViewModel.md)
 - [SellerServiceSubscriptionViewModel](docs/SellerServiceSubscriptionViewModel.md)
 - [SellerServiceUpdateViewModel](docs/SellerServiceUpdateViewModel.md)
 - [SellerServiceViewModel](docs/SellerServiceViewModel.md)
 - [SellerWebHookCreateViewModel](docs/SellerWebHookCreateViewModel.md)
 - [SellerWebHookUpdateViewModel](docs/SellerWebHookUpdateViewModel.md)
 - [SellerWebHookViewModel](docs/SellerWebHookViewModel.md)
 - [ServiceCategoryGetViewModel](docs/ServiceCategoryGetViewModel.md)
 - [ServiceCategoryViewModel](docs/ServiceCategoryViewModel.md)
 - [ServiceProductCustomProperty](docs/ServiceProductCustomProperty.md)
 - [StatusViewModel](docs/StatusViewModel.md)
 - [UserAddressCreateViewModel](docs/UserAddressCreateViewModel.md)
 - [UserAddressDetailViewModel](docs/UserAddressDetailViewModel.md)
 - [UserAddressUpdateViewModel](docs/UserAddressUpdateViewModel.md)
 - [UserCreateCustomProperty](docs/UserCreateCustomProperty.md)
 - [UserCreateViewModel](docs/UserCreateViewModel.md)
 - [UserDetailViewCustomProperty](docs/UserDetailViewCustomProperty.md)
 - [UserDetailViewModel](docs/UserDetailViewModel.md)
 - [UserUpdateCustomProperty](docs/UserUpdateCustomProperty.md)
 - [UserUpdateViewModel](docs/UserUpdateViewModel.md)
 - [UserViewModel](docs/UserViewModel.md)


## Documentation For Authorization


## oauth2

- **Type**: OAuth
- **Flow**: password
- **Authorization URL**: ../connect/authorize
- **Scopes**: N/A


## Author

support@cloudmore.com

