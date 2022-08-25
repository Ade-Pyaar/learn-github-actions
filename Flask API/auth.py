from functools import wraps
from re import A
import jwt
from flask import request, abort
from flask import current_app
import models



def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth_token = None
        if "Authorization" in request.headers:
            token = request.headers["Authorization"]
            split_token = token.split()
            if len(split_token) != 2:
                # error
                return {
                    "message": "Invalid Authentication token!",
                    "data": None,
                    "error": "Unauthorized"
                }, 401
            
            if split_token[0] != "Bearer":
                # error
                return {
                    "message": "Invalid Authentication token format!",
                    "data": None,
                    "error": "Unauthorized"
                }, 401

            auth_token = split_token[1]


        if not auth_token:
            return {
                "message": "Authentication Token is missing!",
                "data": None,
                "error": "Unauthorized"
            }, 401

        try:
            data=jwt.decode(auth_token, current_app.config["SECRET_KEY"], algorithms=["HS256"])
            current_user=models.User().get_by_id(data["user_id"])
            if current_user is None:
                return {
                "message": "Invalid Authentication token!",
                "data": None,
                "error": "Unauthorized"
            }, 401

            if not current_user["active"]:
                abort(403)

        except Exception as e:
            return {
                "message": "Something went wrong",
                "data": None,
                "error": str(e)
            }, 500

        return f(current_user, *args, **kwargs)

    return decorated
