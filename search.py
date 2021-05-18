#!/usr/bin/env python3
# ПОИСЕ КЛИЕНТА (ФИЗ ЛИЦО) ПО НОМЕРУ ТЕЛЕФОНА
import requests # ТРЕБУЕТ УСТАНОВКИ МОДУЛЯ requests (pip install requests)

URL_TOKEN = "https://login.intradesk.ru/connect/token"

USERNAME = "test@nashadmin.ru"
PASSWORD = "nhjgbyrf1917"
CLIENT_ID = "resourceowner"
GRANT_TYPE = "password"
SCOPE = "openid profile email custom.profile api offline_access"
ACR_VALUES = "https://itr.intradesk.ru"


payload = {
	"grant_type": GRANT_TYPE,
	"scope": SCOPE,
	"username": USERNAME,
	"password": PASSWORD,
	"client_id": CLIENT_ID,
	"acr_values": ACR_VALUES
}

CONTENT_TYPE = "application/x-www-form-urlencoded"

headers = {
	"Content-Type": "application/x-www-form-urlencoded",
}

response = requests.request("POST", URL_TOKEN, headers=headers, data = payload)

print(response.json())

token = response.json().get("access_token")


URL_CLIENTS = "https://apigw.intradesk.ru/settings/odata/v1/Clients"



input_phone  = input("PHONE: ")

PHONE_NUMBER = input_phone # Номер телефона

params = {
	"$filter": "contains(searchField, '{0}')".format(PHONE_NUMBER)
}

payload = {}

headers = {
	"Content-Type": "application/json",
	"Authorization": "Bearer {0}".format(token),
}

response = requests.request("GET", URL_CLIENTS, headers=headers, params=params)

print(response.json())
