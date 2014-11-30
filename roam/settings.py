ROAM_NAME = 'Roam'
ROAM_HOST = '0.0.0.0'
ROAM_PORT = 8000

# Used Flasks' session
SECRET_KEY = 'temp_secret_key'

# Synology shared folder for download.
ROAM_HOME = ''

REGEX_SEASONS = '(?:S|Season|시즌) ?(\d+) ?[- _.:~] ?(?:S|Season|시즌)? ?(\d+)\\b|' \
                '[- _.:~]?(?:시즌|\\bSeason|\\bS)( ?\d+)(?:[^A-DH-Z]|\\b)|\\b(\d{1,2})x\d+\\b'

REGEX_EPISODES = '(?:E|Episode) ?(\d+) ?[- _.:~] ?(?:E|Episode)? ?(\d+)\\b|[- _.:~]?' \
                 '(?:Episode|E)( ?\d+)(?:[^A-DH-Z]|\\b)|\\b\d{1,2}x(\d+)\\b|(\d+)[회화]'

REGEX_DATE = '([0-9]{6})'