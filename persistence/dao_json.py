"""
Copyright (c) 2018-2019 Vincenzo Palazzo vicenzopalazzodev@gmail.com
Distributed under the Apache License Version 2.0 software license,
see https://www.apache.org/licenses/LICENSE-2.0.txt
"""
import logging
from interface import implements
from .dao_interface import IDAOFile
from rapidjson import load
from rapidjson import dump


class DAOJson(implements(IDAOFile)):

    def save(self, path_single_file, object):
        logging.debug('The path for save is %s, I\' not enable for run this method sorry')
        file = open(path_single_file, "a")
        dump(object, file)
        file.close()

    def load(self, path_single_file):
        file = open(path_single_file, "r", encoding="utf-8")
        file_blk = load(file)
        file.close()
        return file_blk
