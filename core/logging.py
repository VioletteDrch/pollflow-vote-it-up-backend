import logging

# Configure logging

def setup_logging():
    logging.basicConfig(
        level=logging.INFO,  # or DEBUG for more detail
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    return logging.getLogger(__name__)