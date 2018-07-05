#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: İsmail BAŞARAN <ismail.basaran@tubitak.gov.tr> <basaran.ismaill@gmail.com>
# Author: Tuncay ÇOLAK <tuncay.colak@tubitak.gov.tr>

import os
from api.config.config_manager import ConfigManager
from api.logger.installer_logger import Logger


class EjabberInstaller(object):

    def __init__(self, ssh_api, ssh_status):
        self.ssh_api = ssh_api
        self.ssh_status = ssh_status
        self.logger = Logger()
        self.config_manager = ConfigManager()
        self.jabberd_template_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../conf/ejabberd_temp.yml')
        self.jabberd_out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../dist/ejabberd.yml')

    def install(self, data):
        config_manager = ConfigManager()
        # configuration ejabberd.yml
        base_dn = self.base_dn_parse(data)
        ldap_root_dn = "cn=admin,"+str(base_dn) #cn=admnin,dc=liderahenk,dc=org
        cfg_data = config_manager.read()
        conf_data = {
            "#HOST": data['e_hosts'],
            "#LDAP_SERVER": data['ldap_servers'],
            "#LDAP_ROOT_DN": ldap_root_dn,
            "#LDAP_ROOT_PWD": data['l_admin_pwd'],
            "#LDAP_BASE_DN": base_dn,
            "#SERVICE_NAME": data['e_service_name']
        }
        self.f_ejabberd_yml = open(self.jabberd_template_path, 'r+')
        jabber_data = self.f_ejabberd_yml.read()
        self.logger.info("Ejabberd sunucu kurulumu için veriler okundu")

        txt = self.config_manager.replace_all(jabber_data, conf_data)
        self.f_ejabberd_yml_out = open(self.jabberd_out_path, 'w+')
        self.f_ejabberd_yml_out.write(txt)
        self.f_ejabberd_yml.close()
        self.f_ejabberd_yml_out.close()
        self.logger.info("ejabberd.yml dosyası oluşturuldu")

        #run commands of ejabberd
        if self.ssh_status == 1 or data['location'] == 'local':

            self.ssh_api.run_command(cfg_data["cmd_ejabberd_install"])
            self.logger.info("Ejabberd paketi kuruldu")
            self.ssh_api.scp_file(self.jabberd_out_path, cfg_data["jabberd_des_path"])
            self.logger.info("Ejabberd konfigürasyon dosyası sunucuya kopyalandı")
            self.ssh_api.run_command(cfg_data["cmd_cp_conf"].format(cfg_data["jabberd_des_path"], cfg_data["jabberd_conf_path"]))
            self.ssh_api.run_command(cfg_data["cmd_register"].format(cfg_data["jabberd_conf_path"], data["e_username"], data["e_service_name"], data["e_user_pwd"]))
            self.logger.info("{0} kullanıcısı kaydedildi".format(data["e_username"]))
            self.ssh_api.run_command(cfg_data["cmd_register"].format(cfg_data["jabberd_conf_path"], data["lider_username"], data["e_service_name"], data["lider_user_pwd"]))
            self.logger.info("{0} kullanıcısı kaydedildi".format(data["lider_username"]))
            self.ssh_api.run_command(cfg_data["cmd_jabberd_start"].format(cfg_data["jabberd_conf_path"]))
            self.logger.info("Ejabberd servisi başlatıldı")
            self.ssh_api.run_command(cfg_data["cmd_jabberd_status"].format(cfg_data["jabberd_conf_path"]))
        else:
            # print("bağlantı sağlanamadığı için kurulum yapılamadı..")
            self.logger.error("XMPP sunucusuna bağlantı sağlanamadığı için kurulum yapılamadı. Lütfen bağlantı ayarlarını kotrol ediniz!")

    def base_dn_parse(self, data):
        ### split for get data['base_dn']: liderahenk.org #BASECN and #BASEDN
        parse_dn = data["l_base_dn"].split('.')
        dn_list = []
        for dn in parse_dn:
            message = 'dc=' + str(dn) + ','
            dn_list.append(message)
        base_dn = ''.join(str(x) for x in dn_list)
        base_dn = base_dn.strip(',')
        return base_dn