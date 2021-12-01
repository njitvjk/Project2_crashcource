import logging

logging.basicConfig(level=logging.DEBUG,
format='%(asctime)s %(levelname)s %(message)s',
      filename='myapp.log',
      filemode='w')


logger= logging.getLogger("my_logger")





