from flask import Request, Response, make_response


def main(request: Request) -> Response:
    # Extract data from the request
    request_json = request.get_json(silent=True)
    request_args = request.args

    # Process the request data
    name = ""
    if request_json and "name" in request_json:
        name = request_json["name"]
    elif request_args and "name" in request_args:
        name = request_args["name"]
    else:
        name = "World"

    # Create the response
    message: str = f"Hello, {name}!"
    response: Response = make_response(message)
    response.headers["Content-Type"] = "text/plain"

    return response
