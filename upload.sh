aws s3 --region us-west-2 sync --cache-control no-cache --exclude "*" --include "*.html" _site s3://blog.robstenson.com --profile personal
aws s3 --region us-west-2 sync _site s3://blog.robstenson.com --profile personal
