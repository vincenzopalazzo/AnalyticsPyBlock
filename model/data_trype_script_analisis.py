"""
Copyright (c) 2018-2019 Vincenzo Palazzo vicenzopalazzodev@gmail.com
Distributed under the Apache License Version 2.0 software license,
see https://www.apache.org/licenses/LICENSE-2.0.txt
"""


class DataTypeScriptAnalisis:
    TYPE_P2PK = 'P2PK'
    TYPE_P2PKH = 'P2PKH'
    TYPE_P2MS = 'P2MS'
    TYPE_P2SH = 'P2SH'
    TYPE_P2WPKH = 'P2WPKH'
    TYPE_P2WSH = 'P2WSH'
    TYPE_NO_STANDARD = 'NO_STANDARD'
    TYPE_OP_RETURN = 'OP_RETURN'

    def __init__(self) -> None:
        super().__init__()
        self.p2pk = 0
        self.p2pkh = 0
        self.p2ms = 0
        self.p2sh = 0
        self.p2wpkh = 0
        self.p2wsh = 0
        self.null_data = 0
        self.not_standard = 0

    def increase_type(self, type):
        if self.TYPE_P2PK is type:
            self.p2pk += 1
        elif self.TYPE_P2PKH is type:
            self.p2pkh += 1
        elif self.TYPE_NO_STANDARD is type:
            self.not_standard += 1
        elif self.TYPE_OP_RETURN is type:
            self.null_data += 1
        elif self.TYPE_P2MS is type:
            self.p2ms += 1
        elif self.TYPE_P2SH is type:
            self.p2sh += 1
        elif self.TYPE_P2WPKH is type:
            self.p2wpkh += 1
        elif self.TYPE_P2WSH is type:
            self.p2wsh += 1

    def get_data(self):
        return {
            self.TYPE_P2PK: self.p2pk,
            self.TYPE_P2PKH: self.p2pkh,
            self.TYPE_NO_STANDARD: self.not_standard,
            self.TYPE_OP_RETURN: self.null_data,
            self.TYPE_P2MS: self.p2ms,
        }

    def __str__(self):
        obj_str = "\n{\n  P2PK: " + str(self.p2pk) + "\n  P2PKH: " + str(self.p2pkh) + "\n  NO_STANDART: " + str(
            self.not_standard) + "\n}"
        return obj_str
