import logging

# Configure logging to write to a file
logging.basicConfig(
    level=logging.INFO,  # Set the desired log level
    filename='log_file.log',  # Specify the file path
    filemode='w',  # Choose the file mode ('w' for write, 'a' for append)
    format='%(message)s'  # Set the log message format
)


