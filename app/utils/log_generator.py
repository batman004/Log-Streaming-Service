import datetime
import logging
import os
import time

# create logger with log app


def log_generator():

    os.chdir("logs/")
    dir_path = os.getcwd()

    print(dir_path)

    LOGFILE = f"{dir_path}/test.log"
    logger = logging.getLogger("log_app")

    logger.setLevel(logging.DEBUG)
    fh = logging.FileHandler(LOGFILE)
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    fh.setFormatter(formatter)
    logger.addHandler(fh)

    # writing to logging file to simulate real-time log updates

    while True:
        logger.info(f"log message sent at {datetime.datetime.now().time()}")
        time.sleep(0.5)


if __name__ == "__main__":
    log_generator()
