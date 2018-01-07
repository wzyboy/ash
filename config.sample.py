
class Config:

    # SQLite filename
    T_SQLITE = 'tweets.db'

    # Where to load media files
    # Choices: fs, s3, twitter

    # fs: Media files would be served from local filesystem. Use
    # ./scripts/extract_media_urls.py to extract media files from your Twitter
    # Archive.
    # s3: You could upload the media files to an S3 bucket to serve them from.
    # twitter: The media files will be hot-linked from Twitter.
    T_MEDIA_FROM = 'twitter'

    # S3 bucket name if loading images from S3
    T_MEDIA_S3_BUCKET = 'your-bucket-name'

    # Directory path if loading images from FS
    T_MEDIA_FS_PATH = './media'

    # Uncomment to enable basic auth on search page
    #T_SEARCH_BASIC_AUTH = {'username': 'foo', 'password': 'bar'}
