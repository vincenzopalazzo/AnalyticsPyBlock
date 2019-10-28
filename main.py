"""
Copyright (c) 2018-2019 Vincenzo Palazzo vicenzopalazzodev@gmail.com
Distributed under the Apache License Version 2.0 software license,
see https://www.apache.org/licenses/LICENSE-2.0.txt
"""
import sys
import logging

from service import MediatorCommand


class Main:
    def __init__(self) -> None:
        super().__init__()
        self.mediator = MediatorCommand()

    def start_analisis(self, args):
        logging.debug('Args are: %s', args)
        self.mediator.do_command(args[1], args[2])


if __name__ == '__main__':
    if len(sys.argv) <= 2:
        raise Exception('The argument not valid -> I HAVE ADD MORE INFO')
    logging.basicConfig(level=logging.WARNING)
    main = Main()
    main.start_analisis(sys.argv)
