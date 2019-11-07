"""
Copyright (c) 2018-2019 Vincenzo Palazzo vicenzopalazzodev@gmail.com
Distributed under the Apache License Version 2.0 software license,
see https://www.apache.org/licenses/LICENSE-2.0.txt
"""
import unittest
from persistence.dao_json import *


class EstimateTypeScriptTest(unittest.TestCase):

    def setUp(self) -> None:
        super().setUp()
        self.dao = DAOJson()

    def test_encoder_json(self):
        value = 23
        self.dao.save("pippo.json", value)


if __name__ == '__main__':
    unittest.main()
