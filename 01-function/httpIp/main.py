import logging
import json
import azure.functions as func
import requests


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    logging.info('Getting my public ip from https://icanhazip.com')
    my_ip = "no ip"
    response = requests.get("https://icanhazip.com")
    my_ip = response.text.strip()

    sisid = req.params.get('sisid')
    if not sisid:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            sisid = req_body.get('sisid')

    if sisid:
        return func.HttpResponse(json.dumps({"sisid": f"{sisid}", "ip": f"{my_ip}"}))
    else:
        return func.HttpResponse(
            json.dumps({"sisid": "not supplied", "ip": f"{my_ip}"}),
            status_code=200
        )
