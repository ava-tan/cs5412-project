import logging
import json

import azure.functions as func


def main(req: func.HttpRequest, doc: func.DocumentList) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    products_json = []

    for product in doc:
        product_json = {
            "product_id": product['product_id'],
            "product_variant_id": product['product_variant_id'],
            "title": product['title'],
            "handle": product['handle'],
            "price": product['price'],
            "vendor": product['vendor'],
            "created_at": product['created_at'],
            "image_source": product['image_source'],
            "product_type": product['product_type'],
            "published_at": product['published_at'],
            "tags": product['tags'],
            "id": product['id'],
        }
        products_json.append(product_json)

    return func.HttpResponse(
        json.dumps(products_json),
        status_code=200,
        mimetype="application/json"
    )
