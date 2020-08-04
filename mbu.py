#!/usr/bin/env python

import hashlib
import base64
import urllib


enums = imp.load_source("lib.core.enums", "/usr/share/sqlmap/lib/core/enums.py")

__priority__ = enums.PRIORITY.NORMAL

def tamper(payload, **kwargs):
    hashed = hashlib.md5(payload.encode())
    payload = payload + ':' + hashed.hexdigest()
    encodedBytes = base64.b64encode(payload.encode("utf-8"))
    payload = str(encodedBytes.encode("utf-8"))
    payload = urllib.quote_plus(payload)
    return payload
