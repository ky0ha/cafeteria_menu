from logger.logger import setup_logger

logger = setup_logger("main", "./logger/main.log")
debugger = setup_logger("debug", level="DEBUG")