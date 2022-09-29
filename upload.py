import os
from os.path import isfile, join

from boto.s3.key import Key
from boto.s3.connection import S3Connection
from boto.s3.connection import OrdinaryCallingFormat

api_key = os.environ.get('CELLAR_ADDON_KEY_ID')
secret_key = os.environ.get('CELLAR_ADDON_KEY_SECRET')
host = os.environ.get('CELLAR_ADDON_HOST')

cf = OrdinaryCallingFormat()  # Can't use uppercase name
conn = S3Connection(aws_access_key_id=api_key, aws_secret_access_key=secret_key, host=host, calling_format=cf)

bucket = conn.get_bucket(os.environ.get('BUCKET_NAME'))
bucket.set_acl('public-read')

directory = os.environ.get('ICS_FOLDER_NAME')
calendars = [f for f in os.listdir(directory) if isfile(join(directory, f))]

for calendar in calendars:
    key = Key(bucket)
    key.key = calendar
    key.set_contents_from_filename(f'{directory}/{calendar}')
    key.set_acl('public-read')
