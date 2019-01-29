#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: Tuncay ÇOLAK <tuncay.colak@tubitak.gov.tr>

from api.logger.installer_logger import Logger
from ui.log.watch_log_page import WacthLog

class Test(object):

    def __init__(self):
        super(Test, self).__init__()
        self.logger = WacthLog()


    def deneme(self):
        self.logger.watch_log("denemeeee")
        # self.logger.info("tuncay colak")
        # self.logger.info("hasta kara")
        # self.logger.info("edip yıldız")

if __name__ == '__main__':
    app = Test()
    app.deneme()