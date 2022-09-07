set -x FLASK_APP __init__
set -x APP_MAIL_USERNAME $1
set -x APP_MAIL_PASSWORD $2
set -x APP_DB $3
set -x FLASK_ENV development 
