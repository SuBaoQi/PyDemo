import logging


# 打印日志级别
def test_logging():
    logging.debug('Python debug')
    logging.info('Python info')
    logging.warning('Python warning')
    logging.error('Python Error')
    logging.critical('Python critical')


def test_logging_2():
    # 设置日志
    logger = logging.getLogger('test')
    # 设置日志级别
    logger.setLevel(logging.INFO)
    # 输出渠道
    handler = logging.StreamHandler()
    fmt = '%(asctime)s  %(name)s %(levelname)s %(filename)s-%(lineno)d行：%(message)s'
    formatter = logging.Formatter(fmt)
    handler.setFormatter(formatter)
    file_handler = logging.FileHandler(filename="test.log", encoding="utf-8")
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    logger.addHandler(handler)
    logger.info("dsadsdsa")
    logger.error("sasas")


if __name__ == '__main__':
    test_logging_2()
