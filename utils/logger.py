# utils/logger.py
# This module sets up logging for the application.

import logging
from pathlib import Path


def setup_logger(name: str = "network_toolkit") -> logging.Logger:
    """
    Set up a logger that logs messages to both console and a file.

    Args:
        name (str): The name of the logger.
    
    Returns:
        logging.Logger: Configured logger instance.
    """
    # Create logs directory if it doesn't exist
    log_dir =  Path("logs")
    log_dir.mkdir(exist_ok=True)

    # Configure logger
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    # Formatter
    formatter = logging.Formatter("%(asctime)s | %(levelname)s | %(message)s")

    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    # File handler
    file_handler = logging.FileHandler(log_dir / "app.log")
    file_handler.setFormatter(formatter)

    # Add handlers to logger
    if not logger.handlers:
        logger.addHandler(console_handler)
        logger.addHandler(file_handler)

    return logger