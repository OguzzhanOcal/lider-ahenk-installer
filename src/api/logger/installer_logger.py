#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: Tuncay ÇOLAK <tuncay.colak@tubitak.gov.tr>

import logging
import logging.config
import sys, os
from inspect import getframeinfo, stack

class Logger(object):

    def __init__(self):
        super(Logger, self).__init__()
        # self.logger = logging.getLogger("Lider Ahenk Installer Log")
        if not os.path.exists(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../dist')):
            os.makedirs(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../dist'))

        self.log_out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../dist/installer.log')
        self.log_conf_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../conf/log.conf')


    def info(self, message):
        caller = getframeinfo(stack()[1][0])
        logging.basicConfig(filename=self.log_out_path, filemode='a', level=logging.INFO, format='%(asctime)s %(levelname)s '+str(caller.filename)+': '+str(caller.lineno)+' %(message)s')
        logging.info(message)

    def debug(self, message):
        caller = getframeinfo(stack()[1][0])
        logging.basicConfig(filename=self.log_out_path, filemode='a', level=logging.DEBUG, format='%(asctime)s %(levelname)s '+str(caller.filename)+': '+str(caller.lineno)+' %(message)s')
        logging.debug(message)

    def warning(self, message):
        caller = getframeinfo(stack()[1][0])
        logging.basicConfig(filename=self.log_out_path, filemode='a', level=logging.WARNING, format='%(asctime)s %(levelname)s '+str(caller.filename)+': '+str(caller.lineno)+' %(message)s')
        logging.warning(message)

    def error(self, message):
        caller = getframeinfo(stack()[1][0])
        logging.basicConfig(filename=self.log_out_path, filemode='a', level=logging.ERROR, format='%(asctime)s %(levelname)s '+str(caller.filename)+': '+str(caller.lineno)+' %(message)s')
        logging.error(message)
