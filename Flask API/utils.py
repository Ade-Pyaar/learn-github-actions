import jwt
from datetime import datetime, timedelta









def get_access_token(payload, key, to_expire):
    return jwt.encode(
        {"exp": datetime.now() + timedelta(hours=to_expire), **payload},
        key,
        algorithm='HS256'
    )