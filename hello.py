#!/usr/bin/env python3

# 2. print(f"<p>HTTP_USER_AGENT = (os.environ['HTTP_USER_AGENT']),</p>")
# 3. print(json.dumps(dict(os.environ), indent = 2))
# 4. the field storage creates a username and password fields, and the getfirst methods are used to retrieve the username and password
# 5. The syntax header is print(f"Set-Cookie: usernam)
# 6. HTTP_COOKIE is the header
# 7. Cookies are used for storing user data

import os
import json
print("Content-Type: text/html)
print()
print(f"<p>HTTP_USER_AGENT = (os.environ['HTTP_USER_AGENT']),</p>")
