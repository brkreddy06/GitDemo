import logging

def test_loggingName():
    logger = logging.getLogger(__name__)

    fileHandler = logging.FileHandler("logfile.log")  # this will be file location
#Formatter method will print the format, variable'%(asctime)s' prints date & if you give
# levelName '%(levelname)s' at runtime python will see what kind of error or debug or warning message I'm getting in what level
# s means string. %(name)s - this will print the name of the test where it got error or debug or warning message
# %(message)s - it will print the message for ex. in debug method have one msg that will store in message variable and prints on run time
# now we have to form a connection to logger object then only it will consider the format defined below
    formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s : %(message)s")  #2020-07-22 15:15:54,549 :INFO : PytestsConcept.test_loggingConcept : Information Statement
    fileHandler.setFormatter(formatter)  # this will form the connection to fileHandler object, anyway this obj used in addHandler

    logger.addHandler(fileHandler)  # this will store all the loges in logfile.log

#finally set the level this is core objective of this one
#hierarchy: 1.debug, 2.info, 3.warning, 4.error, 5.critical
# Q1 - Can i see only error logs instead of all logs? yes by setting the levels
    #logger.setLevel(logging.INFO)  # this will print from level 2(info) 3(error,&4 and skip level 1 (debug) while run time
    #logger.setLevel(logging.DEBUG)  # prints from debug level
    logger.setLevel(logging.CRITICAL)  # prints only critical
    logger.debug("A debug statement is executed")
    logger.info("Information Statement")
    logger.warning("Something is in warning mode")
    logger.error("A major error is happened")
    logger.critical("Critical issue")