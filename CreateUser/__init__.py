import azure.functions as func
import logging
import uuid
# from app import app
from flask import request, redirect, Blueprint
# from routers.login import login_blueprint

# app.register_blueprint(login_blueprint)
login_blueprint = Blueprint('login', __name__)


# @app.route('/signup', methods=['POST'])
@login_blueprint.route('/signup', methods=['POST'])
def main(req: func.HttpRequest, doc: func.Out[func.Document]) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    email = req.params.get('email')

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


# def main(req: func.HttpRequest, context: func.Context) -> func.HttpResponse:
#     """Each request is redirected to the WSGI handler.
#     """
#     return func.WsgiMiddleware(app.wsgi_app).handle(req, context)
