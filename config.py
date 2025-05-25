# config.py
import os
import logging

# --- General Application Settings ---
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# --- Flask Application Specific Configuration ---
# Debug Mode: Set to True for development, False for production.
DEBUG = False  # Set to False for production, True for development

# Leaderboard Configuration
DATA_DIR_NAME = "data"
LEADERBOARD_FILENAME = "leaderboard.json"
MAX_LEADERBOARD_ENTRIES_DISPLAY = 10

# Maze Configuration
VALID_DIMENSIONS = {3, 5, 7, 10, 15, 20, 100}

# Logging Configuration
LOG_LEVEL_DEBUG = logging.DEBUG
LOG_LEVEL_PRODUCTION = logging.INFO

# --- Archive Script Specific Configuration ---
ARCHIVE_DIR_NAME = "leaderboard_archives"
RESET_LEADERBOARD_AFTER_ARCHIVE = False
ARCHIVE_SCRIPT_LOG_LEVEL = logging.INFO
