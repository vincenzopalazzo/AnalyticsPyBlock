"""
Copyright (c) 2018-2019 Vincenzo Palazzo vicenzopalazzodev@gmail.com
Distributed under the Apache License Version 2.0 software license,
see https://www.apache.org/licenses/LICENSE-2.0.txt
"""
import logging
import datetime
from model.data_trype_script_analisis import DataTypeScriptAnalisis


class TypeKeyBitcoin:
    TYPE_P2PK = 'P2PK'
    TYPE_P2PKH = 'P2PKH'
    TYPE_P2MS = 'P2PMS'
    TYPE_P2SH = 'P2PSH'
    TYPE_P2WPKH = 'P2WPPKH'
    TYPE_P2WSH = 'P2WPSH'
    TYPE_NO_STANDARD = 'NO_STANDARD'
    TYPE_OP_RETURN = 'OP_RETURN'

    OP_CODE_MAP = {
        int('0x00', 16): 'OP_0',
        int('0x76', 16): 'OP_DUP',
        int('0xac', 16): 'OP_CHECKSIG',
        int('0xae', 16): 'OP_CHECKMULTISIG',
        int('0x6a', 16): 'OP_RETURN',
        int('0xa9', 16): 'OP_HASH160',
    }

    def __init__(self) -> None:
        super().__init__()
        self.result_map = dict()

    def add_pubkey_for_year(self, pub_key_hex, timestamp):
        logging.debug('Hex %s: ', pub_key_hex)
        logging.debug('timespam %d: ', timestamp)
        year = self.from_timestamp_to_year(timestamp)
        type_script = self.check_ty_script(pub_key_hex)
        if year in self.result_map:
            data_type = self.result_map[year]
            data_type.increase_type(type_script)
        else:
            data_type = DataTypeScriptAnalisis()
            data_type.increase_type(type_script)
            self.result_map[year] = data_type

    def get_result(self):
        return self.result_map

    def from_timestamp_to_year(self, timestamp):
        date = datetime.datetime.fromtimestamp(timestamp)
        logging.debug('Date time object: %s', str(date.year))
        return date.year

    def check_ty_script(self, hex_script):
        if len(hex_script) is 0:
            return self.TYPE_NO_STANDARD
        op_code_to_start = int(hex_script[0: 2], 16)
        op_code_end = int(hex_script[len(hex_script) - 2: len(hex_script)], 16)
        op_code_to_start_str = self.OP_CODE_MAP.get(op_code_to_start)
        op_code_end_str = self.OP_CODE_MAP.get(op_code_end)
        logging.debug('OP_CODE -> %s', op_code_to_start_str)
        logging.debug('OP_CODE -> %s', op_code_end_str)
        size_control_program = len(hex_script[2: len(hex_script)])
        logging.debug('Control program size: %i', size_control_program)
        # I dont know the problem on the why this condition op_code_to_start_str is 'OP_0' every false
        if (op_code_to_start_str is 'OP_0' or op_code_end_str is 'OP_CHECKSIG') and \
                (size_control_program is (130 + 2) or size_control_program is (66 + 2)):
            logging.debug('P2PK FOUND')
            return self.TYPE_P2PK
        elif op_code_to_start_str is 'OP_DUP':
            logging.debug('P2PKH FOUND')
            return self.TYPE_P2PKH
        elif op_code_end_str is 'OP_CHECKMULTISIG':
            logging.debug('P2MS FOUND')
            return self.TYPE_P2MS
        elif op_code_to_start_str is 'OP_RETURN':
            logging.debug('OP_RETURN FOUND')
            return self.TYPE_OP_RETURN
        elif op_code_to_start_str is 'OP_HASH160':
            logging.debug('P2SH found')
            return self.TYPE_P2SH
        elif self.is_pay_to_witness_public_key_hash(op_code_to_start_str, hex_script):
            logging.debug('P2WPKH found')
            return self.TYPE_P2WPKH
        elif self.is_pay_to_witness_script_hash(op_code_to_start_str, hex_script):
            logging.debug('P2WSH found')
            return self.TYPE_P2WSH
        else:
            return self.TYPE_NO_STANDARD

    #In the method I used the OP_0 but not is the OP_code but a value for define the script version of the script
    #this is a solution, but mustn't confused with the OP_code start.
    def is_pay_to_witness_public_key_hash(self, op_code_to_start_string, control_program):
        return (op_code_to_start_string is 'OP_0') and (len(control_program) is 22 * 2)

    # In the method I used the OP_0 but not is the OP_code but a value for define the script version of the script
    # this is a solution, but mustn't confused with the OP_code start.
    def is_pay_to_witness_script_hash(self, op_code_to_start_string, control_program):
        return (op_code_to_start_string is 'OP_0') and (len(control_program) is 30 * 2)
