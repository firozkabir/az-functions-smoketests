import logging
import json
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    sisid = req.params.get('sisid')
    if not sisid:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            sisid = req_body.get('sisid')

    if sisid:
        return func.HttpResponse(json.dumps({"sisid": f"{sisid}"}))
    else:
        return func.HttpResponse(
            json.dumps({"sisid": "not supplied"}),
            status_code=200
        )
