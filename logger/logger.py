import logging, sys

def setup_logger(name, log_file=sys.stdout, level=logging.INFO):
    # 日志
    logger = logging.getLogger(name)
    logger.setLevel(level)

    if log_file == sys.stdout:
        handler = logging.StreamHandler(sys.stdout)
        formatter = logging.Formatter("\033[36m%(asctime)s\033[0m - \033[1m\033[34m\033[47m%(levelname)s\033[0m - %(message)s")
    else:
        handler = logging.FileHandler(log_file, encoding='utf-8')
        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    
    
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    return logger

if __name__ == "__main__":
    logger = setup_logger("main", "main.log")
    logger.info("Hello World")