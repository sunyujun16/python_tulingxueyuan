import logging

log_fmt = "%(asctime)s === %(levelname)s +++ %(message)s"
time_fmt = "%Y/%m/%d-%A-%H:%M:%S"

logging.basicConfig(filename='sunyujun.log', level=logging.DEBUG, format=log_fmt, datefmt=time_fmt)

# logging.debug("This is a debug log.")
# logging.info("This is a info log.")
# logging.warning("This is a warning log.")
# logging.error("This is a error log.")
# logging.critical("This is a critical log.")

logging.log(logging.DEBUG, "This is a debug log.")
logging.log(logging.INFO, "This is a debug log.")
logging.log(logging.WARNING, "This is a debug log.")
logging.log(logging.ERROR, "This is a debug log.")
logging.log(logging.CRITICAL, "This is a debug log.")
