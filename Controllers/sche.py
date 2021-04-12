import sys
import time
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler
from Views.bot import botDo
import logging

if __name__ == "__main__":
    path = sys.argv[0]
    event_handler = LoggingEventHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            botDo()
            time.sleep(1800)
    except Exception as e:
            logging.basicConfig(filename='../static/sche.log', filemode='a+', format='%(name)s - %(levelname)s - %(message)s')
            logging.warning(e)
            print("ske.py expection: ", e)
            observer.stop()
    observer.join()