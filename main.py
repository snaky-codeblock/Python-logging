import logging

logging.basicConfig (filename='example.log', encoding='utf-8', level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s', datefmt='%d/%m/%Y %H:%M:%S')

logging.info('Подтверждение того, что все работает так, как ожидалось.')
logging.debug('Подробная информация, обычно представляющая интерес только при диагностике проблем.')
logging.warning('Указание на то, что произошло что-то неожиданное, или указание на какую-то проблему в ближайшем будущем (например, «недостаточно места на диске»). Программное обеспечение по-прежнему работает, как ожидалось.')
logging.error('Из-за более серьезной проблемы программное обеспечение не может выполнять некоторые функции.')
logging.critical('Серьезная ошибка, указывающая на то, что сама программа не может продолжать работу.')