import azure.functions as func
import logging
import uuid


def main(req: func.HttpRequest, doc: func.Out[func.Document]) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    # name = req.params.get('name')

    email = req.params.get('email')
    # if not name:
    #     try:
    #         req_body = req.get_json()
    #     except ValueError:
    #         pass
    #     else:
    #         name = req_body.get('name')

    if not email:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            email = req_body.get('email')

    if email:
        newdocs = func.DocumentList()
        newproduct_dict = {
            "id": str(uuid.uuid4()),
            "email": email
        }
        newdocs.append(func.Document.from_dict(newproduct_dict))
        doc.set(newdocs)
        return func.HttpResponse(f"User {email} created successfully.")
    else:
        return func.HttpResponse(
            "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
            status_code=200
        )
