from pyftpdlib.servers import FTPServer

from .S3Authorizer import S3Authorizer
from .S3FTPHandler import S3FTPHandler
from .S3DownloadOnlyFileSystem import S3DownloadOnlyFileSystem

def run(port=21, passive_ports=range(60000,65535), masquerade_address=None):
    authorizer = S3Authorizer()

    handler = S3FTPHandler
    handler.authorizer = authorizer
    handler.abstracted_fs = S3DownloadOnlyFileSystem

    if masquerade_address is not None:
        handler.masquerade_address = masquerade_address

    handler.permit_foreign_addresses = True
    handler.passive_ports = passive_ports

    server = FTPServer(('', port), handler)
    server.serve_forever()

if __name__ == "__main__":
    run()
