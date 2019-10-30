"""
Copyright (c) 2018-2019 Vincenzo Palazzo vicenzopalazzodev@gmail.com
Distributed under the Apache License Version 2.0 software license,
see https://www.apache.org/licenses/LICENSE-2.0.txt
"""
from model.type_script_value import TypescriptValue


class DataTypeScriptAnalisis:

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
        if TypescriptValue.TYPE_P2PK is type:
            self.p2pk += 1
        elif TypescriptValue.TYPE_P2PKH is type:
            self.p2pkh += 1
        elif TypescriptValue.TYPE_NO_STANDARD is type:
            self.not_standard += 1
        elif TypescriptValue.TYPE_OP_RETURN is type:
            self.null_data += 1
        elif TypescriptValue.TYPE_P2MS is type:
            self.p2ms += 1
        elif TypescriptValue.TYPE_P2SH is type:
            self.p2sh += 1
        elif TypescriptValue.TYPE_P2WPKH is type:
            self.p2wpkh += 1
        elif TypescriptValue.TYPE_P2WSH is type:
            self.p2wsh += 1
        else:
            raise Exception('Type not found')

    def get_data(self):
        return {
            TypescriptValue.TYPE_P2PK: self.p2pk,
            TypescriptValue.TYPE_P2PKH: self.p2pkh,
            TypescriptValue.TYPE_NO_STANDARD: self.not_standard,
            TypescriptValue.TYPE_OP_RETURN: self.null_data,
            TypescriptValue.TYPE_P2MS: self.p2ms,
            TypescriptValue.TYPE_P2SH: self.p2sh,
            TypescriptValue.TYPE_P2WSH: self.p2wsh,
            TypescriptValue.TYPE_P2WPKH: self.p2wpkh,
        }

    def __str__(self):
        obj_str = "\n{\n  P2PK: " + str(self.p2pk) + "\n  P2PKH: " + str(self.p2pkh) + "\n  NO_STANDARD: " + \
                  str(self.not_standard) + "\n  P2MS: " + str(self.p2ms) + "\n  P2SH: " + str(self.p2sh) + "\n  P2WSH: "\
                  + str(self.p2wsh) + "\n  P2WPKH: " + str(self.p2wpkh) + "\n}"
        return obj_str
