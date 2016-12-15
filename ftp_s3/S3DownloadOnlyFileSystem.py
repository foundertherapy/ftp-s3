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
        allowed = False

        for allowed_path in settings.ALLOWED_PATHS:
            if filename.startswith(allowed_path):
                allowed = True
                break

        if not allowed and len(settings.ALLOWED_PATHS) > 0:
            raise FilesystemError('File not found')

        return super(S3DownloadOnlyFileSystem, self).open(filename, mode)
