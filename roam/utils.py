import uuid
from datetime import datetime
import hashlib

def create_unique_token():
    random_id = uuid.uuid4()
    time = datetime.now()

    return hashlib.sha256(bytes(str(random_id)+str(time), 'utf-8')).hexdigest()