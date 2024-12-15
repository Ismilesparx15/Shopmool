# utils/logger_config.py

import logging
import os

# Create logs directory if it doesn't exist
if not os.path.exists('logs'):
    os.makedirs('logs')

# Configure logging
logging.basicConfig(
    filename='logs/test_execution.log',  # Log file path
    level=logging.DEBUG,  # Log level
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',  # Log format
    datefmt='%Y-%m-%d %H:%M:%S'
)

# Create a logger object
logger = logging.getLogger(__name__)
