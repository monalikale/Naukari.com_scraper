#!/usr/bin/env python
# coding: utf-8

# In[5]:


import requests
import pandas as pd


# In[1]:


import requests

cookies = {
    'test': 'naukri.com',
    '_t_ds': '2e3f93451688479986-92e3f9345-02e3f9345',
    '_fbp': 'fb.1.1688479994823.1704441326',
    'PS': 'eec1aa57213371b929bc8b74f237f8d9c3708d0fb6e8cd92060a8622dbd7e476237376ccad94d1f7',
    'PS': 'eec1aa57213371b929bc8b74f237f8d9c3708d0fb6e8cd92060a8622dbd7e476237376ccad94d1f7',
    '__utmz': '266160400.1688481281.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)',
    'jd': '170723903896',
    '_cc_id': '77191440ff33875ae8b4880b385d6f97',
    '_ff_ds': '0038971001691477473-10AA42A2B357-C839CC915C94',
    'G_ENABLED_IDPS': 'google',
    '_ga_WV3ER2B7CG': 'GS1.1.1693071449.3.0.1693071453.56.0.0',
    '_ga_89XHHLE6WS': 'GS1.1.1696316580.1.0.1696316580.0.0.0',
    'cto_bundle': 'C7Zx1l9RTzJja2FHWnZJZ2IxbW8zN04yNElpY1EwQjFlNXN3Vm5RVmhzU3BmbXZPJTJCdktnRkJiRUpnOFRReGclMkZyZXAwaWRPJTJCc0lOZkNGUXozSWtuNDhjY2s3ck9nOSUyQk1OaDNnMXZyMlRqamt1ZnlQJTJGNyUyRk5kMGVLOWtHS3ZETG9DTkVTMXZLRWNScSUyRkFmOWVLJTJGNlVpMGdhR2hURmF6aHprYzZFdWEzS3pMMnVQNmhNJTJCSXJQU3I3SHJob3R4ZkpTQnpRQlBuUjBhM2FFNGQxRCUyRk1iTVVEdDk1ZlgyRmNHZXRiSVNjcGcxcW1WdWJscFFPUVVjSkV0R3FyRFZDVW5tWTlmRmk',
    '_uetvid': '1d56f4c061ba11ee8e73b33ddd41d774',
    '__utma': '266160400.1428175496.1688479989.1696341690.1696654854.6',
    '_ga': 'GA1.1.1428175496.1688479989',
    '_clck': '16fh0f3%7C2%7Cfh0%7C0%7C1371',
    '_abck': '8B561D4174E11159C098E06F623D65BB~0~YAAQJ1M2F0S382KMAQAAybU2oQsnU46V40ul92854Io/4rf+Y8StPO6yxmvlWDkoMyB4jchZK+4VLQBlh4NIye6a+UUpczuwmt/Kak86aZUH71nsKpv0KKrkIZjhfe5Mlhy1bflaPydu/6/JknCmsx3dTwcvTBu36LVbULwEyYFKsdzuxhMZxjpbpVVOoK3kUt8FA109AlDaBgwaNis7SCyk07B/ovYB4ndb6+t2+Wg1gzG7kjIHhUvYoreLxjbZsfmCPfo6ykVuWTtI5Yc0EJfgP2AX3WPnifmbp2CO2LnpouiRuzxwZwnr97ahhbIMtwbMXXMsbn3DvM0wZsf5j5gS1F8fq3ywTViIjC7lwejQ7UDm5kIgIVhXlq+JHNJ6KFxcZFc9byDer2U/jVN43DHrKQS+nisb~-1~-1~-1',
    '_gcl_au': '1.1.1625231530.1707018908.1404684136.1707025002.1707025002',
    '__gpi': 'UID=00000c1db7436cf4:T=1688481168:RT=1707027914:S=ALNI_MbkWn1mdIXQfAfVDtQ2AowxgPEbUQ',
    'bm_mi': '55D3A2787C387C33220EECEAAAAA3185~YAAQH/3UF9OlGYqNAQAAZfAhkxY/gZfezp8exHTdA9KDjO6slmZAKbffQLiMqqJ8p8xO8LSuI4Vt3+3y6Sd1NGeJFGtNDfekS7rm/fw5qBQ4HDasmR7033cTii1db0gUoj+VVm0vlBQIIUwhHN1JguhBwcozyx/xXNLkBtdl0TWjzNb07ibaO0nxRh+x5uDQ7mPLYCHmJJP/D57Kqto6es5Gu1yzmIgBV2MqTKtG99iBZFAGmkIXlB5CDxW/kDDvauP8TUfxgG7T7hK3hZNRUaryCeLYZoJrnM9bxb0/ciWgeLYzuPCZIQNOeChWTpJaoJ/kDVErrS5C5eaqtQ==~1',
    'ak_bmsc': '06E6F89854BEBA3E0FE7EFE93B99F94F~000000000000000000000000000000~YAAQH/3UF+WlGYqNAQAAdPYhkxbD9bNMdsUraO3ZCIPkP/wk+K6/4Dblp6IYcP+i/iHRMFe5kdgKUvHBSvFILEx+JsF+cCiz0RPomjGiiEbGXQAmfCLscZ5OA6fwGqSE2krvUMR5xRDh1KbHWJ7C31Z66KgyP2HgYJ78ebK4oLwTIQPGZ/g7v8jO6gZ+rQ0Dng35wPVl/YjM6il1yN0Mdxt4HpLzcCQ4JyVH6M7VFOYfFsQzVIsxy7uShK36dMEyiHeSZNJd5kZ2yipcgUzZJUOCSxkXR/9iIStrBtAVfNeeRCgxIGkEMNxG2dosy25G0BsSZrqKW/qqk1N+SORWTqmhe4uWQvyYqOJ+RaawpIqCZFOCgpl9OLfXpw4vlEvnl240Ns+p8vHo3xwOGdWoHOdiRyvCNFOaypuxm+THYDXu9kdFO/2eqMT5jS9qNQTimHaMvVL1R7IJWmskQsMlb5BMuWY2+2pz0hNRICDLkabX5eKLCcsaA8aw2ERfwIRoFsHXveSjXU0Y3w4zXfuQLeuwYdjBcrqUQEba6b2mUatnuHAcS8xlGUiAi/NNp5NAMQv2GFHKpGXo5Fqi',
    '_t_us': '65C77560',
    '_t_s': 'direct',
    '_t_r': '1030%2F%2F',
    'persona': 'default',
    'PHPSESSID': 'a5jjik15rrrb798jcvajc0uoqo',
    'nauk_at': 'eyJraWQiOiIxIiwidHlwIjoiSldUIiwiYWxnIjoiUlM1MTIifQ.eyJ1ZF9yZXNJZCI6MTU2NzQ3Mjk3LCJzdWIiOiIxNjcxMzc3NjUiLCJ1ZF91c2VybmFtZSI6Im1vbmFsaWthbGU5MkBnbWFpbC5jb20iLCJ1ZF9pc0VtYWlsIjp0cnVlLCJpc3MiOiJJbmZvRWRnZSBJbmRpYSBQdnQuIEx0ZC4iLCJ1c2VyQWdlbnQiOiJNb3ppbGxhLzUuMCAoV2luZG93cyBOVCAxMC4wOyBXaW42NDsgeDY0KSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBDaHJvbWUvMTIxLjAuMC4wIFNhZmFyaS81MzcuMzYiLCJpcEFkcmVzcyI6IjI0MDE6NDkwMDoxYzJkOjhkN2M6OWMzZTo5MDUyOjlhNjU6Mzg2YiIsInVkX2lzVGVjaE9wc0xvZ2luIjpmYWxzZSwidXNlcklkIjoxNjcxMzc3NjUsInN1YlVzZXJUeXBlIjoiam9ic2Vla2VyIiwidXNlclN0YXRlIjoiQVVUSEVOVElDQVRFRCIsInVkX2lzUGFpZENsaWVudCI6ZmFsc2UsInVkX2VtYWlsVmVyaWZpZWQiOnRydWUsInVzZXJUeXBlIjoiam9ic2Vla2VyIiwic2Vzc2lvblN0YXRUaW1lIjoiMjAyNC0wMi0xMFQxODozOToxNyIsInVkX2VtYWlsIjoiZHMubW9uYWxpa2FsZUBnbWFpbC5jb20iLCJ1c2VyUm9sZSI6InVzZXIiLCJleHAiOjE3MDc1NzQxNTcsInRva2VuVHlwZSI6ImFjY2Vzc1Rva2VuIiwiaWF0IjoxNzA3NTcwNTU3LCJqdGkiOiIzNmIwMGQ0MGQ2ZGU0OWNjOWU0ZGYwZDA4N2Q1ZDVkMCJ9.dg9dVkoFfPGkAfCcZqIJxFE6qt7ax86CJLOsZCScvNDx-RF9XS5mEs3uqb92l7LyYSX-yTBiPpG__pR6W_2ZExTaVSgKMc2VM5R_m4_PBcSAWse-0JOImDeeUVwKDNAixBmiLRsyPeULx78xPOLEL0Udm-E8R_9RjH0Ivg2jxO5sG4Uact1gm1qzTLqyba1JCAbYaczZ0bW4EWdvrdepvMrQWZ3D02Hn1XZR3EgFPURq50bMXpTOwQACLxpueY9M96Yi3GOUAJ49Fp7izPR40MI3av6LVXZOfED1Sg00pCduh4mKbB5SaP2FLBS3iq7qFuIqJ8A6mXGd4K_RzQ4wog',
    'nauk_rt': 'eyJraWQiOiIxIiwidHlwIjoiSldUIiwiYWxnIjoiUlM1MTIifQ.eyJ1ZF9yZXNJZCI6MTU2NzQ3Mjk3LCJzdWIiOiIxNjcxMzc3NjUiLCJ1ZF91c2VybmFtZSI6Im1vbmFsaWthbGU5MkBnbWFpbC5jb20iLCJ1ZF9pc0VtYWlsIjp0cnVlLCJpc3MiOiJJbmZvRWRnZSBJbmRpYSBQdnQuIEx0ZC4iLCJ1c2VyQWdlbnQiOiJNb3ppbGxhLzUuMCAoV2luZG93cyBOVCAxMC4wOyBXaW42NDsgeDY0KSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBDaHJvbWUvMTIxLjAuMC4wIFNhZmFyaS81MzcuMzYiLCJpcEFkcmVzcyI6IjI0MDE6NDkwMDoxYzJkOjhkN2M6OWMzZTo5MDUyOjlhNjU6Mzg2YiIsInVkX2lzVGVjaE9wc0xvZ2luIjpmYWxzZSwidXNlcklkIjoxNjcxMzc3NjUsInN1YlVzZXJUeXBlIjoiam9ic2Vla2VyIiwidXNlclN0YXRlIjoiQVVUSEVOVElDQVRFRCIsInVkX2lzUGFpZENsaWVudCI6ZmFsc2UsInVkX2VtYWlsVmVyaWZpZWQiOnRydWUsInVzZXJUeXBlIjoiam9ic2Vla2VyIiwic2Vzc2lvblN0YXRUaW1lIjoiMjAyNC0wMi0xMFQxODozOToxNyIsInVkX2VtYWlsIjoiZHMubW9uYWxpa2FsZUBnbWFpbC5jb20iLCJ1c2VyUm9sZSI6InVzZXIiLCJleHAiOjE3MzkxMDY1NTcsInRva2VuVHlwZSI6InJlZnJlc2hUb2tlbiIsImlhdCI6MTcwNzU3MDU1NywianRpIjoiMzZiMDBkNDBkNmRlNDljYzllNGRmMGQwODdkNWQ1ZDAifQ.dzniHY73GvgvuYd2-Sqm4Srh36Oq9FPZcQ4UsiciU475U_YCSN7md7jP95xvZcEjk7__hM06iDVoORLd6YywrWrhmA75Hc9u1UocBif3z3A1sugRt6h1xRE_TGZoiJVOBs53eYB74JJfN0el5W9WNlMVurVuqJ6Kiuj8mz-GV-s-QIjINZtqvq6MvZ16Zbg7JBfnm9rcbrouvjwRq6iG8f7NGjzVwqRUMcPaXQ5dh7hSyL_iqbPGEc_k3g7LXpiFZGHZJs-xUtuIvdSPFK5ZvZoJWfGHnGPjmBuxZUaaK-PV5hZJb-SBO2OkR1x_Wx_JN10O71x3Qt76bF4CfqXf3g',
    'is_login': '1',
    'nauk_sid': '36b00d40d6de49cc9e4df0d087d5d5d0',
    'nauk_otl': '36b00d40d6de49cc9e4df0d087d5d5d0',
    'NKWAP': '80933b16b154daca3581ff0e81ae9fe6d9b73ba36245e4bc5fd57a53a9c4a3361edd7a843282321a~eec1aa57213371b929bc8b74f237f8d9c3708d0fb6e8cd92060a8622dbd7e476237376ccad94d1f7~1~0',
    'MYNAUKRI[UNID]': 'da30422f490a477cbcc9511bd544885b',
    '_ga_T749QGK6MQ': 'GS1.1.1707570529.2.0.1707570559.0.0.0',
    'nauk_ps': 'default',
    'ACTIVE': '1707570560',
    '__gads': 'ID=7cb064b2a4c9aed9:T=1688481168:RT=1707571113:S=ALNI_MZ3Mv2ztKDgRHw3AsXEUgJx09Mvfg',
    '__eoi': 'ID=398d0e73f2d6560a:T=1707024133:RT=1707571113:S=AA-AfjZmpgTp4SNvG9Ee4_pb5wU5',
    'bm_sv': '56485D02E30616EDAB9EE5CD59D7EA76~YAAQP/3UF1o+IImNAQAAHu8zkxZQ9tTJJJohxWtkuM4Tg44YPQFm+N9hg9eiDiTSIeBgnbR5DSshGGE7K6L/gs44BPIPBoHdK5ZvtYLpzFNtYADPgqlwKZ120vL40+ii9cgTzNTN+S0IQH/XRJGlsUJASa6CDglW0otWVZ/bXiOOTNBH3juE4h3R71vHjT11szFXiCgyMIu858ye9g2S2HyS1F/qwP+4GU+f+/3j162vIV1lXpaMZX1pLZg/dgd61xY=~1',
    'HOWTORT': 'ul=1707571671362&r=https%3A%2F%2Fwww.naukri.com%2Fpython-development-jobs-in-pune%3Fk%3Dpython%2520development%26l%3Dpune%26experience%3D3%26nignbevent_src%3DjobsearchDeskGNB&hd=1707571671556',
    '_ga_K2YBNZVRLL': 'GS1.1.1707570494.68.1.1707571671.60.0.0',
}

headers = {
    'authority': 'www.naukri.com',
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9',
    'appid': '109',
    'authorization': 'Bearer eyJraWQiOiIxIiwidHlwIjoiSldUIiwiYWxnIjoiUlM1MTIifQ.eyJ1ZF9yZXNJZCI6MTU2NzQ3Mjk3LCJzdWIiOiIxNjcxMzc3NjUiLCJ1ZF91c2VybmFtZSI6Im1vbmFsaWthbGU5MkBnbWFpbC5jb20iLCJ1ZF9pc0VtYWlsIjp0cnVlLCJpc3MiOiJJbmZvRWRnZSBJbmRpYSBQdnQuIEx0ZC4iLCJ1c2VyQWdlbnQiOiJNb3ppbGxhLzUuMCAoV2luZG93cyBOVCAxMC4wOyBXaW42NDsgeDY0KSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBDaHJvbWUvMTIxLjAuMC4wIFNhZmFyaS81MzcuMzYiLCJpcEFkcmVzcyI6IjI0MDE6NDkwMDoxYzJkOjhkN2M6OWMzZTo5MDUyOjlhNjU6Mzg2YiIsInVkX2lzVGVjaE9wc0xvZ2luIjpmYWxzZSwidXNlcklkIjoxNjcxMzc3NjUsInN1YlVzZXJUeXBlIjoiam9ic2Vla2VyIiwidXNlclN0YXRlIjoiQVVUSEVOVElDQVRFRCIsInVkX2lzUGFpZENsaWVudCI6ZmFsc2UsInVkX2VtYWlsVmVyaWZpZWQiOnRydWUsInVzZXJUeXBlIjoiam9ic2Vla2VyIiwic2Vzc2lvblN0YXRUaW1lIjoiMjAyNC0wMi0xMFQxODozOToxNyIsInVkX2VtYWlsIjoiZHMubW9uYWxpa2FsZUBnbWFpbC5jb20iLCJ1c2VyUm9sZSI6InVzZXIiLCJleHAiOjE3MDc1NzQxNTcsInRva2VuVHlwZSI6ImFjY2Vzc1Rva2VuIiwiaWF0IjoxNzA3NTcwNTU3LCJqdGkiOiIzNmIwMGQ0MGQ2ZGU0OWNjOWU0ZGYwZDA4N2Q1ZDVkMCJ9.dg9dVkoFfPGkAfCcZqIJxFE6qt7ax86CJLOsZCScvNDx-RF9XS5mEs3uqb92l7LyYSX-yTBiPpG__pR6W_2ZExTaVSgKMc2VM5R_m4_PBcSAWse-0JOImDeeUVwKDNAixBmiLRsyPeULx78xPOLEL0Udm-E8R_9RjH0Ivg2jxO5sG4Uact1gm1qzTLqyba1JCAbYaczZ0bW4EWdvrdepvMrQWZ3D02Hn1XZR3EgFPURq50bMXpTOwQACLxpueY9M96Yi3GOUAJ49Fp7izPR40MI3av6LVXZOfED1Sg00pCduh4mKbB5SaP2FLBS3iq7qFuIqJ8A6mXGd4K_RzQ4wog',
    'clientid': 'd3skt0p',
    'content-type': 'application/json',
    # 'cookie': 'test=naukri.com; _t_ds=2e3f93451688479986-92e3f9345-02e3f9345; _fbp=fb.1.1688479994823.1704441326; PS=eec1aa57213371b929bc8b74f237f8d9c3708d0fb6e8cd92060a8622dbd7e476237376ccad94d1f7; PS=eec1aa57213371b929bc8b74f237f8d9c3708d0fb6e8cd92060a8622dbd7e476237376ccad94d1f7; __utmz=266160400.1688481281.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); jd=170723903896; _cc_id=77191440ff33875ae8b4880b385d6f97; _ff_ds=0038971001691477473-10AA42A2B357-C839CC915C94; G_ENABLED_IDPS=google; _ga_WV3ER2B7CG=GS1.1.1693071449.3.0.1693071453.56.0.0; _ga_89XHHLE6WS=GS1.1.1696316580.1.0.1696316580.0.0.0; cto_bundle=C7Zx1l9RTzJja2FHWnZJZ2IxbW8zN04yNElpY1EwQjFlNXN3Vm5RVmhzU3BmbXZPJTJCdktnRkJiRUpnOFRReGclMkZyZXAwaWRPJTJCc0lOZkNGUXozSWtuNDhjY2s3ck9nOSUyQk1OaDNnMXZyMlRqamt1ZnlQJTJGNyUyRk5kMGVLOWtHS3ZETG9DTkVTMXZLRWNScSUyRkFmOWVLJTJGNlVpMGdhR2hURmF6aHprYzZFdWEzS3pMMnVQNmhNJTJCSXJQU3I3SHJob3R4ZkpTQnpRQlBuUjBhM2FFNGQxRCUyRk1iTVVEdDk1ZlgyRmNHZXRiSVNjcGcxcW1WdWJscFFPUVVjSkV0R3FyRFZDVW5tWTlmRmk; _uetvid=1d56f4c061ba11ee8e73b33ddd41d774; __utma=266160400.1428175496.1688479989.1696341690.1696654854.6; _ga=GA1.1.1428175496.1688479989; _clck=16fh0f3%7C2%7Cfh0%7C0%7C1371; _abck=8B561D4174E11159C098E06F623D65BB~0~YAAQJ1M2F0S382KMAQAAybU2oQsnU46V40ul92854Io/4rf+Y8StPO6yxmvlWDkoMyB4jchZK+4VLQBlh4NIye6a+UUpczuwmt/Kak86aZUH71nsKpv0KKrkIZjhfe5Mlhy1bflaPydu/6/JknCmsx3dTwcvTBu36LVbULwEyYFKsdzuxhMZxjpbpVVOoK3kUt8FA109AlDaBgwaNis7SCyk07B/ovYB4ndb6+t2+Wg1gzG7kjIHhUvYoreLxjbZsfmCPfo6ykVuWTtI5Yc0EJfgP2AX3WPnifmbp2CO2LnpouiRuzxwZwnr97ahhbIMtwbMXXMsbn3DvM0wZsf5j5gS1F8fq3ywTViIjC7lwejQ7UDm5kIgIVhXlq+JHNJ6KFxcZFc9byDer2U/jVN43DHrKQS+nisb~-1~-1~-1; _gcl_au=1.1.1625231530.1707018908.1404684136.1707025002.1707025002; __gpi=UID=00000c1db7436cf4:T=1688481168:RT=1707027914:S=ALNI_MbkWn1mdIXQfAfVDtQ2AowxgPEbUQ; bm_mi=55D3A2787C387C33220EECEAAAAA3185~YAAQH/3UF9OlGYqNAQAAZfAhkxY/gZfezp8exHTdA9KDjO6slmZAKbffQLiMqqJ8p8xO8LSuI4Vt3+3y6Sd1NGeJFGtNDfekS7rm/fw5qBQ4HDasmR7033cTii1db0gUoj+VVm0vlBQIIUwhHN1JguhBwcozyx/xXNLkBtdl0TWjzNb07ibaO0nxRh+x5uDQ7mPLYCHmJJP/D57Kqto6es5Gu1yzmIgBV2MqTKtG99iBZFAGmkIXlB5CDxW/kDDvauP8TUfxgG7T7hK3hZNRUaryCeLYZoJrnM9bxb0/ciWgeLYzuPCZIQNOeChWTpJaoJ/kDVErrS5C5eaqtQ==~1; ak_bmsc=06E6F89854BEBA3E0FE7EFE93B99F94F~000000000000000000000000000000~YAAQH/3UF+WlGYqNAQAAdPYhkxbD9bNMdsUraO3ZCIPkP/wk+K6/4Dblp6IYcP+i/iHRMFe5kdgKUvHBSvFILEx+JsF+cCiz0RPomjGiiEbGXQAmfCLscZ5OA6fwGqSE2krvUMR5xRDh1KbHWJ7C31Z66KgyP2HgYJ78ebK4oLwTIQPGZ/g7v8jO6gZ+rQ0Dng35wPVl/YjM6il1yN0Mdxt4HpLzcCQ4JyVH6M7VFOYfFsQzVIsxy7uShK36dMEyiHeSZNJd5kZ2yipcgUzZJUOCSxkXR/9iIStrBtAVfNeeRCgxIGkEMNxG2dosy25G0BsSZrqKW/qqk1N+SORWTqmhe4uWQvyYqOJ+RaawpIqCZFOCgpl9OLfXpw4vlEvnl240Ns+p8vHo3xwOGdWoHOdiRyvCNFOaypuxm+THYDXu9kdFO/2eqMT5jS9qNQTimHaMvVL1R7IJWmskQsMlb5BMuWY2+2pz0hNRICDLkabX5eKLCcsaA8aw2ERfwIRoFsHXveSjXU0Y3w4zXfuQLeuwYdjBcrqUQEba6b2mUatnuHAcS8xlGUiAi/NNp5NAMQv2GFHKpGXo5Fqi; _t_us=65C77560; _t_s=direct; _t_r=1030%2F%2F; persona=default; PHPSESSID=a5jjik15rrrb798jcvajc0uoqo; nauk_at=eyJraWQiOiIxIiwidHlwIjoiSldUIiwiYWxnIjoiUlM1MTIifQ.eyJ1ZF9yZXNJZCI6MTU2NzQ3Mjk3LCJzdWIiOiIxNjcxMzc3NjUiLCJ1ZF91c2VybmFtZSI6Im1vbmFsaWthbGU5MkBnbWFpbC5jb20iLCJ1ZF9pc0VtYWlsIjp0cnVlLCJpc3MiOiJJbmZvRWRnZSBJbmRpYSBQdnQuIEx0ZC4iLCJ1c2VyQWdlbnQiOiJNb3ppbGxhLzUuMCAoV2luZG93cyBOVCAxMC4wOyBXaW42NDsgeDY0KSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBDaHJvbWUvMTIxLjAuMC4wIFNhZmFyaS81MzcuMzYiLCJpcEFkcmVzcyI6IjI0MDE6NDkwMDoxYzJkOjhkN2M6OWMzZTo5MDUyOjlhNjU6Mzg2YiIsInVkX2lzVGVjaE9wc0xvZ2luIjpmYWxzZSwidXNlcklkIjoxNjcxMzc3NjUsInN1YlVzZXJUeXBlIjoiam9ic2Vla2VyIiwidXNlclN0YXRlIjoiQVVUSEVOVElDQVRFRCIsInVkX2lzUGFpZENsaWVudCI6ZmFsc2UsInVkX2VtYWlsVmVyaWZpZWQiOnRydWUsInVzZXJUeXBlIjoiam9ic2Vla2VyIiwic2Vzc2lvblN0YXRUaW1lIjoiMjAyNC0wMi0xMFQxODozOToxNyIsInVkX2VtYWlsIjoiZHMubW9uYWxpa2FsZUBnbWFpbC5jb20iLCJ1c2VyUm9sZSI6InVzZXIiLCJleHAiOjE3MDc1NzQxNTcsInRva2VuVHlwZSI6ImFjY2Vzc1Rva2VuIiwiaWF0IjoxNzA3NTcwNTU3LCJqdGkiOiIzNmIwMGQ0MGQ2ZGU0OWNjOWU0ZGYwZDA4N2Q1ZDVkMCJ9.dg9dVkoFfPGkAfCcZqIJxFE6qt7ax86CJLOsZCScvNDx-RF9XS5mEs3uqb92l7LyYSX-yTBiPpG__pR6W_2ZExTaVSgKMc2VM5R_m4_PBcSAWse-0JOImDeeUVwKDNAixBmiLRsyPeULx78xPOLEL0Udm-E8R_9RjH0Ivg2jxO5sG4Uact1gm1qzTLqyba1JCAbYaczZ0bW4EWdvrdepvMrQWZ3D02Hn1XZR3EgFPURq50bMXpTOwQACLxpueY9M96Yi3GOUAJ49Fp7izPR40MI3av6LVXZOfED1Sg00pCduh4mKbB5SaP2FLBS3iq7qFuIqJ8A6mXGd4K_RzQ4wog; nauk_rt=eyJraWQiOiIxIiwidHlwIjoiSldUIiwiYWxnIjoiUlM1MTIifQ.eyJ1ZF9yZXNJZCI6MTU2NzQ3Mjk3LCJzdWIiOiIxNjcxMzc3NjUiLCJ1ZF91c2VybmFtZSI6Im1vbmFsaWthbGU5MkBnbWFpbC5jb20iLCJ1ZF9pc0VtYWlsIjp0cnVlLCJpc3MiOiJJbmZvRWRnZSBJbmRpYSBQdnQuIEx0ZC4iLCJ1c2VyQWdlbnQiOiJNb3ppbGxhLzUuMCAoV2luZG93cyBOVCAxMC4wOyBXaW42NDsgeDY0KSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBDaHJvbWUvMTIxLjAuMC4wIFNhZmFyaS81MzcuMzYiLCJpcEFkcmVzcyI6IjI0MDE6NDkwMDoxYzJkOjhkN2M6OWMzZTo5MDUyOjlhNjU6Mzg2YiIsInVkX2lzVGVjaE9wc0xvZ2luIjpmYWxzZSwidXNlcklkIjoxNjcxMzc3NjUsInN1YlVzZXJUeXBlIjoiam9ic2Vla2VyIiwidXNlclN0YXRlIjoiQVVUSEVOVElDQVRFRCIsInVkX2lzUGFpZENsaWVudCI6ZmFsc2UsInVkX2VtYWlsVmVyaWZpZWQiOnRydWUsInVzZXJUeXBlIjoiam9ic2Vla2VyIiwic2Vzc2lvblN0YXRUaW1lIjoiMjAyNC0wMi0xMFQxODozOToxNyIsInVkX2VtYWlsIjoiZHMubW9uYWxpa2FsZUBnbWFpbC5jb20iLCJ1c2VyUm9sZSI6InVzZXIiLCJleHAiOjE3MzkxMDY1NTcsInRva2VuVHlwZSI6InJlZnJlc2hUb2tlbiIsImlhdCI6MTcwNzU3MDU1NywianRpIjoiMzZiMDBkNDBkNmRlNDljYzllNGRmMGQwODdkNWQ1ZDAifQ.dzniHY73GvgvuYd2-Sqm4Srh36Oq9FPZcQ4UsiciU475U_YCSN7md7jP95xvZcEjk7__hM06iDVoORLd6YywrWrhmA75Hc9u1UocBif3z3A1sugRt6h1xRE_TGZoiJVOBs53eYB74JJfN0el5W9WNlMVurVuqJ6Kiuj8mz-GV-s-QIjINZtqvq6MvZ16Zbg7JBfnm9rcbrouvjwRq6iG8f7NGjzVwqRUMcPaXQ5dh7hSyL_iqbPGEc_k3g7LXpiFZGHZJs-xUtuIvdSPFK5ZvZoJWfGHnGPjmBuxZUaaK-PV5hZJb-SBO2OkR1x_Wx_JN10O71x3Qt76bF4CfqXf3g; is_login=1; nauk_sid=36b00d40d6de49cc9e4df0d087d5d5d0; nauk_otl=36b00d40d6de49cc9e4df0d087d5d5d0; NKWAP=80933b16b154daca3581ff0e81ae9fe6d9b73ba36245e4bc5fd57a53a9c4a3361edd7a843282321a~eec1aa57213371b929bc8b74f237f8d9c3708d0fb6e8cd92060a8622dbd7e476237376ccad94d1f7~1~0; MYNAUKRI[UNID]=da30422f490a477cbcc9511bd544885b; _ga_T749QGK6MQ=GS1.1.1707570529.2.0.1707570559.0.0.0; nauk_ps=default; ACTIVE=1707570560; __gads=ID=7cb064b2a4c9aed9:T=1688481168:RT=1707571113:S=ALNI_MZ3Mv2ztKDgRHw3AsXEUgJx09Mvfg; __eoi=ID=398d0e73f2d6560a:T=1707024133:RT=1707571113:S=AA-AfjZmpgTp4SNvG9Ee4_pb5wU5; bm_sv=56485D02E30616EDAB9EE5CD59D7EA76~YAAQP/3UF1o+IImNAQAAHu8zkxZQ9tTJJJohxWtkuM4Tg44YPQFm+N9hg9eiDiTSIeBgnbR5DSshGGE7K6L/gs44BPIPBoHdK5ZvtYLpzFNtYADPgqlwKZ120vL40+ii9cgTzNTN+S0IQH/XRJGlsUJASa6CDglW0otWVZ/bXiOOTNBH3juE4h3R71vHjT11szFXiCgyMIu858ye9g2S2HyS1F/qwP+4GU+f+/3j162vIV1lXpaMZX1pLZg/dgd61xY=~1; HOWTORT=ul=1707571671362&r=https%3A%2F%2Fwww.naukri.com%2Fpython-development-jobs-in-pune%3Fk%3Dpython%2520development%26l%3Dpune%26experience%3D3%26nignbevent_src%3DjobsearchDeskGNB&hd=1707571671556; _ga_K2YBNZVRLL=GS1.1.1707570494.68.1.1707571671.60.0.0',
    'gid': 'LOCATION,INDUSTRY,EDUCATION,FAREA_ROLE',
    'referer': 'https://www.naukri.com/python-development-jobs-in-pune?k=python%20development&l=pune&experience=3&nignbevent_src=jobsearchDeskGNB',
    'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'systemid': 'Naukri',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
}

params = [
    ('noOfResults', '100'),
    ('urlType', 'search_by_key_loc'),
    ('searchType', 'adv'),
    ('location', 'pune'),
    ('keyword', 'python development'),
    ('pageNo', '1'),
    ('experience', '3'),
    ('k', 'python development'),
    ('l', 'pune'),
    ('experience', '3'),
    ('nignbevent_src', 'jobsearchDeskGNB'),
    ('seoKey', 'python-development-jobs-in-pune'),
    ('src', 'directSearch'),
    ('latLong', '21.1124224_79.0986752'),
]

response = requests.get('https://www.naukri.com/jobapi/v3/search', params=params, cookies=cookies, headers=headers)
j2data=response.json()
print(j2data)


# In[7]:


peint(len(j2data['jobDetails']))
job_list=[]
for i in range(100):
    print(i)
    params = [
        ('noOfResults', '100'),
        ('urlType', 'search_by_key_loc'),
        ('searchType', 'adv'),
        ('location', 'pune'),
        ('keyword', 'Web scraping'),
        ('pageNo', i),
        ('experience', '3'),
        ('k', 'Web scraping'),
        ('l', 'pune'),
        ('experience', '3'),
        ('nignbevent_src', 'jobsearchDeskGNB'),
        ('seoKey', 'webscraping-jobs-in-pune'),
        ('src', 'directSearch'),
        ('latLong', '21.1124224_79.0986752'),
        
    ]

    response2 = requests.get('https://www.naukri.com/jobapi/v3/search', params=params, cookies=cookies, headers=headers)
    
    j2data=response2.json()
    #print(j2data)
    joblen=len(j2data['jobDetails'])
    #joblen=2
    try:
        for i in range(joblen):
                job_list=[]
                Title= j2data['jobDetails'][i]['title']
                Age = j2data['jobDetails'][i]['footerPlaceholderLabel']
                companyName = j2data['jobDetails'][i]['companyName']
                experience= j2data['jobDetails'][i]['placeholders'][0]['label']
                salary= j2data['jobDetails'][i]['placeholders'][1]['label']
                location= j2data['jobDetails'][i]['placeholders'][2]['label']
                job_path= j2data['jobDetails'][i]['jdURL']
                joburl="https://www.naukri.com"+str(job_path)
                jobDescription=j2data['jobDetails'][i]['jobDescription']
                jobdict={"Title":Title,"Age":Age,"companyName":companyName,"experience":experience,
                      "salary":salary,"location":location,"joburl":joburl,"jobDescription":jobDescription}
                job_list.append(jobdict)
                Job_df=pd.DataFrame(job_list)
                Job_df.to_csv("Naukri_Job_deatsil_webscrapn_10feb.csv",mode ='a')
    except Exception as e:
        print(e)
        print("Error")

