from logging import getLogger, config
import yaml

config.dictConfig(yaml.safe_load(open('./config.yml').read()))
logger = getLogger(__name__)

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
