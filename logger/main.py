from logging import getLogger, basicConfig, FileHandler, Formatter, DEBUG, INFO
from mymodule import test_func1, test_func2, culc_div

def main():
    try:
        logger = getLogger(__name__)
        logger.setLevel(DEBUG)
        # basicConfig(filename='./example.log', encoding='utf-8', level=DEBUG)

        fh_formatter = Formatter('[%(asctime)s] [%(levelname)s] [%(filename)s:%(lineno)s] %(message)s')

        # FileHandlerの設定
        fh1 = FileHandler('./main1.log')
        fh1.setLevel(INFO)
        fh1.setFormatter(fh_formatter)
        logger.addHandler(fh1)

        fh2 = FileHandler('./main2.log')
        fh2.setLevel(DEBUG)
        fh2.setFormatter(fh_formatter)
        logger.addHandler(fh2)

        logger.debug('This message should go to the log file')
        logger.info('So should this')
        logger.warning('And this, too')
        logger.error('And non-ASCII stuff, too, like Øresund and Malmö')

        test_func1()
        test_func2()

        result = culc_div(1, 0)
        print(result)

    except ZeroDivisionError as e:
        logger.exception('mainでエラーを捕捉した!')

if __name__ == '__main__':
    main()