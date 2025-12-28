import json
#import yaml # Requires pip install pyyaml
import logging
import logging.config
import logging.handlers
import pathlib

logger = logging.getLogger("PJLOG")

def setup_logging():
    # Create logs folder if it doesn't exist
    logs_dir = pathlib.Path("logs")
    logs_dir.mkdir(exist_ok=True)
    
    config_path = pathlib.Path("logging_configs/config.json")
    #config_path = pathlib.Path("logging_configs/config.yml")
    
    with open(config_path, "r") as f:
        config = json.load(f)
        #config = yaml.safe_load(f)
    
    logging.config.dictConfig(config)


if __name__ == "__main__":
    setup_logging()
    logger.info("Logging is configured.")
    logger.debug("Debugging is enabled.")
    logger.warning("This is a warning message.")
    logger.error("This is an error message.")
    logger.critical("This is a critical message.")  

    try:
        1 / 0
    except ZeroDivisionError:
        logger.exception("An exception occurred.")