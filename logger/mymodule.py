from logging import getLogger, basicConfig, FileHandler, Formatter, DEBUG, INFO

logger = getLogger(__name__)
logger.setLevel(DEBUG)

fh_formatter = Formatter('[%(asctime)s] [%(levelname)s] [%(filename)s:%(lineno)s] %(message)s')

# FileHandlerの設定
fh1 = FileHandler('./mymodule1.log')
fh1.setLevel(INFO)
fh1.setFormatter(fh_formatter)
logger.addHandler(fh1)

fh2 = FileHandler('./mymodule2.log')
fh2.setLevel(DEBUG)
fh2.setFormatter(fh_formatter)
logger.addHandler(fh2)

def test_func1():
    logger.info('This is test_func1')
    logger.debug('a')

    return None

def test_func2():
    logger.info('This is test_func2')
    logger.debug('a')
    
    return None

def culc_div(num1, num2):
    logger.debug(f'num1:{num1}')
    logger.debug(f'num2:{num2}')
    try:
        result = num1 / num2
        return result
    
    except ZeroDivisionError as e:
        logger.exception('mymodoleでエラーを捕捉した!')
        raise
