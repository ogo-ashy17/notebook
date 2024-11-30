# 設定ファイルを使用してLogger, Handler, Formatterを制御する
from logging import getLogger, config
from mymodule import test_func1, test_func2, culc_div
import yaml

def main():
    try:
        config.dictConfig(yaml.safe_load(open('./config.yml').read()))
        logger = getLogger(__name__)

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