import logging
import json
import azure.functions as func
from azure.keyvault.secrets import SecretClient
from azure.identity import ClientSecretCredential
import cx_Oracle
import os
import atexit


def get_from_keyvault(secret_name):

    CLIENT_ID = os.getenv('CLIENT_ID')
    TENANT_ID = os.getenv('TENANT_ID')
    CLIENT_SECRET = os.getenv('CLIENT_SECRET')
    KEYVAULT_NAME = os.getenv('KEYVAULT_NAME')
    keyvault_uri = f"https://{KEYVAULT_NAME}.vault.azure.net"

    _client_credential = ClientSecretCredential(
        tenant_id=TENANT_ID, client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
    _secret_client = SecretClient(
        vault_url=keyvault_uri, credential=_client_credential)

    return _secret_client.get_secret(secret_name).value


# init credentials
DB_USERNAME = get_from_keyvault(secret_name='func-db-username')
DB_PASSWORD = get_from_keyvault(secret_name='func-db-password')
DB_HOST = get_from_keyvault(secret_name='func-db-host')
DB_PORT = get_from_keyvault(secret_name='func-db-port')
DB_SID = get_from_keyvault(secret_name='func-db-sid')

db_connection_string = f"{DB_HOST}:{DB_PORT}/{DB_SID}"

orcl = cx_Oracle.connect(
    DB_USERNAME,
    DB_PASSWORD,
    db_connection_string)


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('httpOracle.main() started')

    sisid = req.params.get('sisid')
    if not sisid:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            sisid = req_body.get('sisid')

    if sisid:
        return func.HttpResponse(json.dumps({"sisid": f"{sisid}", "version": f"{orcl.version}"}))
    else:
        return func.HttpResponse(
            json.dumps({"sisid": "not supplied"}),
            status_code=200
        )
