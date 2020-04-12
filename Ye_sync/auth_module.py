# -*- coding: utf-8 -*-
from auth_interface import AuthInterface
from ShareMgnt.ttypes import ncTShareMgntError
import hashlib


class GztzsbAuth(AuthInterface):
    """
        广州特种设备
    """

    def __init__(self, config):
        super(GztzsbAuth, self).__init__(config)

    """账号密码登录接口"""

    def login(self, user_name, passwd, user):
        if passwd == user['f_password']:
            return user['f_user_id']
        md5 = hashlib.md5()

        md5.update(passwd)

        enc_pwd = md5.hexdigest().lower()
        if enc_pwd == user['f_password'].lower():
            return user['f_user_id']
        else:
            raise ValueError(ncTShareMgntError.NCT_INVALID_ACCOUNT_OR_PASSWORD)

    # """单点登录验证接口"""
    #
    # def validate(self, params):
    #     pass
