EXIF Cleaner
============

A tool to clean EXIF metadata using Python 3 and exiv2. This tool is a 
wrapper around exiv2 binary, then to use it you must install exiv2 
package before.

Using this tool agains your file will delete EXIF metadata of your 
files keep content (the data) untouched. No more GPS, camera vendor or 
date disclosure anymore. Schedule it in a cron to automate the cleaning 
of your folders.

To install exiv2 in debian/ubuntu systems is so easy as type:

 # apt-get install exiv2


Use
---

To use the tool simply pass a folder list (space separated) to check and 
clean EXIF metadata from your files.

Example:

./exifcleaner.py -v /www/images /www/images2


