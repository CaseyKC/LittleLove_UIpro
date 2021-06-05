#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging, os


def write_log(name):
    logger = logging.getLogger(name)
    logger.setLevel(level=logging.INFO)
    handler = logging.FileHandler("log.txt")
    handler.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger


def res_log():
    filename = os.path.dirname(os.path.abspath(__file__)) + '/res.txt'
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - [%(pathname)s] - [line:%(lineno)d] - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S',
                        handlers=[logging.FileHandler(encoding='utf-8', mode='a', filename=filename)]
                        )
    return logging
