import logging

ROAM_NAME = 'Roam'
ROAM_HOST = '0.0.0.0'
ROAM_PORT = 8000

# Used Flask's session
SECRET_KEY = 'temp_secret_key'

# Synology shared folder for download.
ROAM_HOME = ''

REGEX = {
    'seasons': '.?(?:s|season|시즌) ?(\d+) ?[- _.:~] ?(?:s|season|시즌)? ?(\d+)\\b|' \
                '[- _.:~]?(?:시즌|\\bseason|\\bs)( ?\d+)(?:[^A-DH-Z]|\\b)|\\b(\d{1,2})x\d+\\b',
    'episodes': '.?(?:e|episode) ?(\d+) ?[-_.:~] ?(?:e|episode)? ?(\d+)|' \
                 '[- _.:~]?(?:episode|e)( ?\d+)(?:[^a-df-z]|\\b)|\\b\d{1,2}x(\d+)\\b|(\d+)[회화]',
    'date': '([0-9]{6})',
    'resolution': '(SD|720p|1080i|1080p|4K|UHD|2160p)',
    'video_codec': '(AVC|x264|H264|h.264|h265|h.265|VC-1|Xvid|DviX|MPEG2|MPEG-2|MP4|TS)',
    'audio_codec': '(AAC|MP3|DTS|DTSHD|FLAC)',
    'source': '(BluRay|Blu-ray|BRRip|DVDRip|HDTV|WEBDL|WEB-DL|Screener)',
}

LOGGING_FORMAT = '[%(asctime)s] %(levelname)s [%(filename)s:%(lineno)s] - %(message)s'
LOGGING_LEVEL = logging.DEBUG