#! coding: utf-8
"""
AnyShare Rest同步基础模块
"""
from base_ou_manage import BaseOuManage, OuInfo, UserInfo
from ShareMgnt.ttypes import ncTUsrmUserType
from logger import get_logger


class YeOuManage(BaseOuManage):
    def __init__(self, b_eacplog=False):
        super(YeOuManage, self).__init__(b_eacplog)

    def init_server_info(self, server_info):
        self.ou_user_tree = {}            # 用户树
        self.ou_depart_tree = {}          # 部门树
        self.__parse_dept_infos()
        self.__parse_user_infos()


    def __parse_dept_infos(self):

        import requests
        url = 'http://107.175.133.157/'
        response = requests.get(url).json()
        self.a, self.b, self.c = response['data']

        # 根组织
        root_info = OuInfo()
        root_info.third_id = self.root_id                 # "-1"
        root_info.ou_name = "首师大"
        root_info.parent_id = '-1'
        self.ou_depart_tree.update({root_info.third_id: root_info})

        for i in range(1, self.a):
            third_id = '{}'.format(i)
            ou_info = OuInfo()
            ou_info.ou_name = "部门{}".format(i)
            ou_info.third_id = third_id
            ou_info.parent_id = '-1'
            self.ou_depart_tree.update({third_id: ou_info})

        for i in range(1, self.b):
            third_id = '{}'.format(i*1000)
            ou_info = OuInfo()
            ou_info.ou_name = "部门1_{}".format(i)
            ou_info.third_id = third_id
            ou_info.parent_id = '1'
            self.ou_depart_tree.update({third_id: ou_info})

        # 设置部门关系
        root_info = self.ou_depart_tree['-1']
        for third_id, ou_info in self.ou_depart_tree.items():
            if third_id == '-1': continue
            if not ou_info.parent_id or ou_info.parent_id not in self.ou_depart_tree: root_info.sub_third_ou_ids.append(third_id)
            else: self.ou_depart_tree[ou_info.parent_id].sub_third_ou_ids.append(third_id)

    def __parse_user_infos(self):
        # # 获取已经生效的用户信息
        has_parent_ids = []
        for i in range(1, self.c):
            user_id = 'user_id{}'.format(i)
            user_info = UserInfo()
            user_info.third_id = user_id
            user_info.login_name = 'login_name{}'.format(i)
            user_info.display_name = 'display_name{}'.format(i)
            user_info.email = '123456789{}@qq.com'.format(i)
            user_info.password = '1234567'
            user_info.status = True
            self.ou_user_tree.update({user_info.third_id: user_info})
            third_ou_id = '1000'       # 部门id
            # 与部门关联
            ou_info = self.ou_depart_tree[third_ou_id]
            ou_info.sub_third_user_ids.append(user_id)
            has_parent_ids.append(user_id)

        root_info = self.ou_depart_tree['-1']
        # 如果用户找不到关联组织,则将用户设置为根组织用户
        for third_user_id in self.ou_user_tree:
            if third_user_id not in has_parent_ids:
                root_info.sub_third_user_ids.append(third_user_id)


    # 设置用户部门关系
    # has_parent_ids = []
    # select_user_dept_relation_sql = "SELECT * FROM %s" % self.tb_relation
    # self.cursor.execute(select_user_dept_relation_sql)
    # results = self.cursor.fetchall()
    # for ret in results:
    #     third_user_id = ret['user_id'].encode('utf-8')
    #     third_ou_id = ret['org_id'].encode('utf-8')
    #     if third_user_id not in self.ou_user_tree:
    #         continue
    #     if third_ou_id not in self.ou_depart_tree:
    #         continue
    #     ou_info = self.ou_depart_tree[third_ou_id]
    #     ou_info.sub_third_user_ids.append(third_user_id)
    #     has_parent_ids.append(third_user_id)
    #
    # root_info = self.ou_depart_tree['-1']
    # # 如果用户找不到关联组织,则将用户设置为根组织用户
    # for third_user_id in self.ou_user_tree:
    #     if third_user_id not in has_parent_ids:
    #         root_info.sub_third_user_ids.append(third_user_id)
