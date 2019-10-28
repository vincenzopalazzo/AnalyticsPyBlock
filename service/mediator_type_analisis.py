"""
Copyright (c) 2018-2019 Vincenzo Palazzo vicenzopalazzodev@gmail.com
Distributed under the Apache License Version 2.0 software license,
see https://www.apache.org/licenses/LICENSE-2.0.txt
"""
import logging
from service.address_type_command import AddressTypeCommand


class MediatorCommand:
    def __init__(self) -> None:
        super().__init__()

    def do_command(self, key_command, data_dir):
        logging.debug('Key command is %s', key_command)
        if key_command == 'address_type':
            command = AddressTypeCommand()
            command.do_command(data_dir)
