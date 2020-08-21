import requests
import json


API_KEY = "fL6wNU5ScQ5SDFOPrWt8LEYs"
SECRET_KEY = "BPllXcgRmuSbKUIXd7k44PuPCasI369a"


def get_authorization_code_url(callback_uri, scopes=[]):
    """:return 获取authorization_code的网址"""

    uri = "http://openapi.baidu.com/oauth/2.0/authorize?response_type=code&client_id=%s&redirect_uri=%s" \
          % (API_KEY, callback_uri)
    if scopes:
        uri += "&scope=%s" % ' '.join(scopes)
    return uri


def get_token_dict(authorization_code):
    data = {
        "grant_type": "authorization_code",
        "code": authorization_code,
        "client_id": API_KEY,
        "client_secret": SECRET_KEY,
        "redirect_uri": reverse("callback"),
    }

    response = requests.post("https://openapi.baidu.com/oauth/2.0/token", data=data)
    js = json.loads(response.text)
    return js
