"""
Copyright (c) 2018-2019 Vincenzo Palazzo vicenzopalazzodev@gmail.com
Distributed under the Apache License Version 2.0 software license,
see https://www.apache.org/licenses/LICENSE-2.0.txt
"""
from interface import Interface


class IDAOFile(Interface):

    def save(self, path_single_file):
        pass

    def load(self, path_single_file):
        pass
