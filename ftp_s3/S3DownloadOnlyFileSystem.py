from .S3FileSystem import S3FileSystem
from . import settings
from pyftpdlib.filesystems import FilesystemError

class S3DownloadOnlyFileSystem(S3FileSystem):
    def listdir(self, path):
        return []

    def isfile(self, path):
        return True

    def islink(self, path):
        return False

    def isdir(self, path):
        return False

    def open(self, filename, mode):
        # block access to any file out side ALLOWED_PATH
        if not filename.startswith(settings.ALLOWED_PATH):
            raise FilesystemError('File not found')

        return super(S3DownloadOnlyFileSystem, self).open(filename, mode)
