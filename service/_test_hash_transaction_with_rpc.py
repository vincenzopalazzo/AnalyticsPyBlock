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
from .bitcoincore.rpc_command_bitcoincore import RPCBitcoinCoreCommand

class HashTransactionTestWithBitcoinCore(implements(ICommand)):
    def __init__(self) -> None:
        super().__init__()
        self.name = 'Test hash transaction with Bitcoin core RPC'
        self.rpcCommand = RPCBitcoinCoreCommand('vincent', 'vincent', 8332)

    def do_command(self, data_dir):
        logging.debug('Command %s run with data directory in this path %s', self.name, data_dir)
        files_blk = os.listdir(data_dir)
        dao_json = DAOJson()

        lenght = len([iq for iq in os.scandir(data_dir)])
        start = 0
        self.printProgressBar(start, lenght, length=50)
        for file_blk in files_blk:
            logging.debug('****** Files BLK.json ******')
            logging.debug(file_blk)
            if os.path.isfile(os.path.join(data_dir, file_blk)):
                path_file = os.path.join(data_dir, file_blk)
                object_json = dao_json.load(path_file)
                logging.debug('***** JSON Object *****')
                logging.debug('Num blocks %i', len(object_json['blocks']))
                blockCount = 0
                for block in object_json['blocks']:
                    indexTx = 0
                    for rawTx in block['rawTransactions']:

                       result = self.rpcCommand.callCommand('TODO', rawTx['hashRawTransaction'])
                       if result != "OK":
                           logging.warning('At the file %s inside the the block %s the hash %s is not valid for indextx %s', file_blk,
                                           block['hashBlock'], rawTx['hashRawTransaction'], indexTx)
                           logging.warning(blockCount)
                       else:
                           logging.warning(rawTx['hashRawTransaction'])
                       indexTx += 1
                    blockCount += 1

            start += 1
            self.printProgressBar(start, lenght, length=50)


        # Print iterations progress

    # Print iterations progress create an submodule separate
    def printProgressBar(self, iteration, total, prefix='Progress', suffix='Complete', decimals=1, length=100, fill='█', printEnd="\r"):
        """
        Call in a loop to create terminal progress bar
        @params:
            iteration   - Required  : current iteration (Int)
            total       - Required  : total iterations (Int)
            prefix      - Optional  : prefix string (Str)
            suffix      - Optional  : suffix string (Str)
            decimals    - Optional  : positive number of decimals in percent complete (Int)
            bar_length  - Optional  : character length of bar (Int)
        """
        percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
        filledLength = int(length * iteration // total)
        bar = fill * filledLength + '-' * (length - filledLength)
        print('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), end=printEnd)
        # Print New Line on Complete
        if iteration == total:
            print()
