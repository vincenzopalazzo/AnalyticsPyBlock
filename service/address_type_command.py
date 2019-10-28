"""
Copyright (c) 2018-2019 Vincenzo Palazzo vicenzopalazzodev@gmail.com
Distributed under the Apache License Version 2.0 software license,
see https://www.apache.org/licenses/LICENSE-2.0.txt
"""
import logging
import os
from interface import implements
from .command_interface import ICommand
from persistence.dao_json import DAOJson
from model.type_key_bitcoin import TypeKeyBitcoin
from service.plot_analisis import PlotAnalisis


class AddressTypeCommand(implements(ICommand)):
    def __init__(self) -> None:
        super().__init__()
        self.name = 'Analisis address type'

    def do_command(self, data_dir):
        logging.debug('Command %s run with data directory in this path %s', self.name, data_dir)
        files_blk = os.listdir(data_dir)
        i = 0
        dao_json = DAOJson()
        type_bitcoin_key = TypeKeyBitcoin()
        for file_blk in files_blk:
            logging.debug('****** Files BLK.json ******')
            logging.warning(file_blk)
            if os.path.isfile(os.path.join(data_dir, file_blk)):
                path_file = os.path.join(data_dir, file_blk)
                object_json = dao_json.load(path_file)
                logging.debug('***** JSON Object *****')
                logging.debug('Num blocks %i', len(object_json['blocks']))
                for block in object_json['blocks']:
                    for rawTx in block['rawTransactions']:
                        for outTx in rawTx['txOutput']:
                            type_bitcoin_key.add_pubkey_for_year(outTx['script'], block['blockHeader']['time'])

        result_type_key = type_bitcoin_key.get_result()
        for key in result_type_key.keys():
            value_key = result_type_key[key]
            logging.warning('****** Year %s ******', str(key))
            logging.warning('Value: %s', str(value_key))
            plot_graph = PlotAnalisis()
            plot_graph.plot(result_type_key)
