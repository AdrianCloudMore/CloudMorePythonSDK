import swagger_client
from datetime import datetime, timedelta
import requests


config = swagger_client.Configuration()
api_client = swagger_client.ApiClient(configuration=config)


async def authenticate(auth_config):
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
        raise Exception("Failed to authenticate with Cloudmore API")

async def getSellerResellerById(sellerId, resellerId):
    api_instance = swagger_client.ResellersApi(api_client=api_client)

    data = api_instance.api_sellers_by_seller_id_resellers_by_id_get(sellerId, resellerId)
    print(data)
    print()