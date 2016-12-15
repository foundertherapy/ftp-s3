import boto

from pyftpdlib.authorizers import DummyAuthorizer, AuthenticationFailed
from . import settings

class S3Authorizer(DummyAuthorizer):
    def __init__(self, *args, **kwargs):
        DummyAuthorizer.__init__(self, *args, **kwargs)
        self.conn = None

    def validate_authentication(self, username, password, handler):
        if username == settings.FTP_USERNAME and password == settings.FTP_PASSWORD:
            if not self.has_user(settings.FTP_USERNAME):
                self.add_user(settings.FTP_USERNAME, u'', u'/', perm="elr")
                self.conn = boto.connect_s3(settings.AWS_ACCESS_KEY_ID, settings.AWS_SECRET_ACCESS_KEY)
            return True
        else:
            self.conn = None
            raise AuthenticationFailed
