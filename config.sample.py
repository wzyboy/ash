
class Config:

    # SQLite filename
    T_SQLITE = 'tweets.db'

    # Where to load images
    # Choices: fs, s3, twitter
    T_MEDIA_FROM = 's3'

    # S3 bucket name if loading images from S3
    T_MEDIA_S3_BUCKET = 'your-bucket-name'

    # Directory path if loading images from FS
    T_MEDIA_FS_PATH = './media'
