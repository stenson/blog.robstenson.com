aws s3 --region us-west-2 sync --cache-control no-cache --exclude "*" --include "*.html" . s3://blog.robstenson.com --profile personal
aws s3 --region us-west-2 sync . s3://blog.robstenson.com --profile personal
