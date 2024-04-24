from dotenv import load_dotenv
import utils.logger as logger
import pyclamd
import os

load_dotenv()

cd = pyclamd.ClamdNetworkSocket(os.getenv("CLAMAV_HOST"), 3310)


def scan_virus(file_stream):
    result = cd.scan_stream(file_stream)

    if result:
        return False

    return True
