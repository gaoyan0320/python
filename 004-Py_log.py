import os
import logging

logging.basicConfig(
    level=logging.DEBUG,
    filename='log.txt',
    filemode='a',
    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
)

logging.info("info")
logging.debug("debug")
logging.error("error")