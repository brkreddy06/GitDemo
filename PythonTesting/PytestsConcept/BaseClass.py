import inspect
import logging


class BaseClass:
    def getLogger(self):
        loggerName = inspect.stack()[1][3]  # in python loggerName obj will store when getLogger method called from various tests
        #test_editProfile (test_usingLoggersInTestCase file) calling test_getLogger() method so in the log file test_editProfile
        # name displays actually which is stored in loggerName obj
        #logger = logging.getLogger(__name__) # __name__ this will print BaseClass name
        logger = logging.getLogger(loggerName)  # provide loggerName obj to getLogger method

        fileHandler = logging.FileHandler("logfile.log")  # this will be file location
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s : %(message)s")
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)
        # logger.setLevel(logging.INFO)  # this will print from level 2(info) 3(error,&4 and skip level 1 (debug) while run time
        logger.setLevel(logging.DEBUG)  # prints from debug level
        #logger.setLevel(logging.CRITICAL)  # prints only critical
        return logger   # it will return the loggers object flow stated above to any of our test case
