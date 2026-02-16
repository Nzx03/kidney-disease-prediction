import os
import sys
import logging   #as it is already  treated as package so it is in there

logging_str="[%(asctime)s: %(levelname)s : %(module)s:%(message)s]"

log_dir="logs"
log_filepath=os.path.join(log_dir,"running_logs.log")
os.makedirs(log_dir, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format= logging_str,

    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout) #will get the msg in terminal too
    ]
)


logger=logging.getLogger("cnnClassifier")