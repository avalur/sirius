#! /usr/bin/env python
# -*- coding: utf-8 -*-

# pip install --upgrade transliterate pwgen

import os
import yaml
import subprocess
import traceback
import smtplib
from email.mime.text import MIMEText
import pwgen
import socket
from transliterate import translit
import pandas as pd

GROUP_NAME = 'students'
CONFIG = yaml.load(open('conf_sirius.yml'))
ROOT_QUOTA_USER = CONFIG.get('root_quota_user')

class Action:
    DONE = "Done"
    ERROR = "Error"
    DELETE = "delete"
    EMPTY = ''

    @staticmethod
    def make_action(row_num, username, action):
        action_column_num = CONFIG.get('column_num')
        # users_sheet.update_cell(row_num + 2, action_column_num, action)
        print "{} {}!".format(username, action if action != Action.EMPTY else "Deleted")


# def make_username(user_cred, name_affect=1):
#     parsed_cred = [translit(user_cred.get(i), 'ru', True).lower() for i in (u'Имя', u'Отчество', u'Фамилия')]
#     return "{}{}{}".format(parsed_cred[0][0:name_affect], parsed_cred[1][0:name_affect], parsed_cred[2]).replace('\'', '')


def send_mail(to, subj, body):
    msg = MIMEText(body, "plain", "utf-8")
    msg['Subject'] = subj
    msg['From'] = 'sirius.cluster.help@gmail.com'
    msg['To'] = to
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('sirius.cluster.help@gmail.com', 'zv2ei2BSVjKEfTn')
    server.sendmail('sirius.cluster.help@gmail.com', [to], msg.as_string())
    server.quit()


def _write_ssh_key(ssh_pub, home):
    """
    :type ssh_pub: str
    """
    ssh_path = os.path.join(home, '.ssh')
    auth_file = os.path.join(ssh_path, 'authorized_keys')
    os.makedirs(ssh_path, mode=0o700)
    with open(auth_file, 'w') as keyfile:
        keyfile.write(ssh_pub)
    os.chmod(auth_file, 0o600)

ssh_key=True

creds = pd.read_csv('users.csv')
for row_num, cred in creds.iterrows():
    username = cred['login']
    email = cred['Email']
    if True: #not cred.get(CONFIG.get('column_name')) or cred.get(CONFIG.get('column_name')) == Action.ERROR:
        password = pwgen.pwgen()
        userhome = os.path.join('/home', username)
        try:
            # GROUP_NAME = 'curators'
            subprocess.check_call(['groupadd', '-f', GROUP_NAME])
            subprocess.check_call(['useradd', '-m', '-d', userhome, username, '-c', GROUP_NAME])
            if ssh_key:
                ssh_pub = cred['ssh_pub']
                _write_ssh_key(ssh_pub, userhome)
            else:
                subprocess.check_call('echo {}:{} | chpasswd'.format(username, password), shell=True)
            subprocess.check_call('chown -R {}:{} {}'.format(username, GROUP_NAME, userhome), shell=True)
            subprocess.check_call(['chmod', '700', userhome])
            subprocess.check_call(['chsh', '-s', '/bin/bash', username])
            # subprocess.check_call(['edquota', '-p', ROOT_QUOTA_USER, '-u', username], stderr=subprocess.PIPE)
            # _process_hdfs_userdir(username)
        except subprocess.CalledProcessError:
            traceback.print_exc()
            Action.make_action(row_num, username, Action.ERROR)
            continue
        send_mail(email, u'Регистрация на сервере {}'.format(CONFIG.get('hostname')),
                  u'Пользователь создан. \n\nДоступ: ssh -p {} {}@{}'.format(
            CONFIG.get('port'), username, CONFIG.get('global_hostname')))
        Action.make_action(row_num, username, Action.DONE)
    # elif cred.get(CONFIG.get('column_name')) == Action.DELETE:
    #     try:
    #         subprocess.check_call(['userdel', '-r', '-f', username], stderr=subprocess.PIPE)
    #         Action.make_action(row_num, username, Action.EMPTY)
    #         _process_hdfs_userdir(username, False)
    #     except subprocess.CalledProcessError:
    #         traceback.print_exc()
