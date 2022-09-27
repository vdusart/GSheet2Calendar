import os

from boto.s3.key import Key
from boto.s3.connection import S3Connection
from boto.s3.connection import OrdinaryCallingFormat

apiKey = os.environ.get('CELLAR_ADDON_KEY_ID')
secretKey = os.environ.get('CELLAR_ADDON_KEY_SECRET')
host = os.environ.get('CELLAR_ADDON_HOST')

cf = OrdinaryCallingFormat()  # Can't use uppercase name
conn = S3Connection(aws_access_key_id=apiKey, aws_secret_access_key=secretKey, host=host, calling_format=cf)

bucket = conn.get_bucket(os.environ.get('BUCKET_NAME'))
bucket.set_acl('public-read')

key = Key(bucket)
key.key = "ING3-CS-B.ics"
key.set_contents_from_filename('/home/lucas/Desktop/my.ics')
key.set_acl('public-read')

print(bucket.list())
