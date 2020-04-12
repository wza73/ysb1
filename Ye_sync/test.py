# #!/usr/bin/env python
# # coding=UTF-8
# # @Time    : 2020/4/3 2:14 下午
# # @Author  : Brian
# # @Site    :
# # @File    : test.py
# # @Software: PyCharm
#
# root_info = '风控公司'
# data_attr = {
#             "技术部": {'third_id': 'jsb', 'parent_id': '-1'},
#             "运营部": {'third_id': 'yyb', 'parent_id': '-1'},
#             "技术A": {'third_id': 'jsb_A', 'parent_id': 'jsb'},
#             "技术B": {'third_id': 'jsb_B', 'parent_id': 'jsb'},
#             "技术C": {'third_id': 'jsb_C', 'parent_id': 'jsb'},
#             "技术D": {'third_id': 'jsb_D', 'parent_id': 'jsb'},
#             "技术E": {'third_id': 'jsb_E', 'parent_id': 'jsb'},
#             "技术F": {'third_id': 'jsb_F', 'parent_id': 'jsb'},
#             "技术G": {'third_id': 'jsb_G', 'parent_id': 'jsb'},
#             "运营A": {'third_id': 'yyb_A', 'parent_id': 'yyb'},
#             "运营B": {'third_id': 'yyb_B', 'parent_id': 'yyb'},
#             "运营C": {'third_id': 'yyb_C', 'parent_id': 'yyb'},
#         }
# data = {"风控公司": {"技术部": {"技术A": {"丁丁": "", "明明": "", "花花": "", "绿绿": "", "憨憨": ""}, "技术B": {"小米": "", "小美": "", "小新": ""}, "技术C": {}, "技术D": {}, "技术E": {}, "技术F": {}, "技术G": {}}, "运营部": {"运营A": {"朱书军": "", "朱书君": "", "朱梦露": "", "朱庆晋": "", "朱玉东": "", "朱方杰": ""}, "运营B": {}, "运营C": {}}}}
# dp = data[root_info]
#
# # for key, value in data_attr.items():
# #     ou_info = OuInfo()
# #     ou_info.ou_name = key
# #     ou_info.third_id = value['third_id']
# #     ou_info.parent_id = value['parent_id']
# #     self.ou_depart_tree[ou_info.third_id] = ou_info
#
#
# for key, value in dp.items():
#     for _key, _value in value.items():
#         if not _value: continue
#         for __key, __value in _value.items():
#             print key, _key, __key, data_attr[_key]['third_id'],data_attr[_key]['parent_id']
#
#
# # {
# #     "syncModule": "BaseSyncer",
# #     "authModule": "GztzsbAuth",
# #     "ouModule": "YeOuManage",
# #     "authServer": "http://172.17.107.83/sso?auth=pc",
# #     "hideThirdLogin": false,
# #     "mainUnit": "1",
# #      "userCreateStatus": true,
# #      "matchUrl": "http://172.17.107.83/#/sso"
# # }


print 123



