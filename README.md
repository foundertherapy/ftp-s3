Read Only FTP frontend for S3
=============================
This is a proxy service that allow downloading files from FTP protocol through AWS S3.

Usage
-----
Copy `settings.py.template` to `settings.py` and change the configurations.

Execute `run.py [port] [internal]`, where `port` is the port number you want the
server to run on, and `internal` is the literal string you can use to disable
masquerading.

`ftp_s3` is a module with `ftp_s3.main.run()` being the function that puts the
entire thing together and runs the server.

Notes
-----
* Listing is disabled (you can change that by `S3FileSystem` in `main.py`).

* You can only read a specific file, you must have the full path of it, otherwise it will reject the operation with `File not found`.

* It assumes that connection is about reading a file, so it ignore directories and check if the file exist on S3 directly.

* Permissions aren't properly mapped. PR would be appreciated to fix this!

* Only reading works. Writing has not been implemented yet.
