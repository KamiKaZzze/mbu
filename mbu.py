# sqlmap/tamper/mbu.py

import hashlib
import base64
import urllib

from lib.core.enums import PRIORITY

__priority__ = PRIORITY.NORMAL

def tamper(payload, **kwargs):
    hashed = hashlib.md5(payload.encode())
    payload = payload + ':' + hashed.hexdigest()
    encodedBytes = base64.b64encode(payload.encode("utf-8"))
    payload = str(encodedBytes.encode("utf-8"))
    payload = urllib.quote_plus(payload)
    return payload
