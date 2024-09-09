import logging
import logging.handlers
import time
import os


class LoggerSetup:

    def __init__(self) -> None:
        self.logger = logging.getLogger("")
        self.setup_logging()

    def setup_logging(self):
        # define log format
        LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

        # logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)

        self.logger.setLevel(logging.INFO)

        # configuring logger formatter
        formatter = logging.Formatter(LOG_FORMAT)

        # configure console handler
        console = logging.StreamHandler()
        console.setFormatter(formatter)

        # ensure log directory exists
        log_directory = "logs"
        if not os.path.exists(log_directory):
            os.makedirs(log_directory)

        # configure TimeRotatingFileHandler
        log_file = os.path.join(log_directory, "fastapi_todo_with_efk.log")

        file = logging.handlers.TimedRotatingFileHandler(
            filename=log_file, when="midnight", backupCount=5
        )

        file.setFormatter(formatter)

        self.logger.addHandler(console)
        self.logger.addHandler(file)
