#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/7/6 19:41
# @Author  : yyn
# @FileName: db.py
# @Software: PyCharm

import MySQLdb
import datetime
import os

rewrite_print = print


#  重写print，使其输出后存入文档
def print(*arg):
    rewrite_print(*arg)
    output_dir = "log"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        log_name = 'log.txt'  # 日志文件名称
        filename = os.path.join(output_dir, log_name)
        rewrite_print("日志文档生成时间：" + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + "\n",
                      file=open(filename, "a"))
        # print('新建log文件夹')
    log_name = 'log.txt'  # 日志文件名称
    filename = os.path.join(output_dir, log_name)
    rewrite_print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ": ", end="", file=open(filename, "a"))
    rewrite_print(*arg, file=open(filename, "a"))  # 写入文件


class MysqlManager(object):
    """mysql管理器"""

    def __init__(self, db, user, passwd, host='8.131.235.164', port=3306, charset='utf8'):
        """初始化数据库"""
        self.__db = db
        self.__user = user
        self.__passwd = passwd
        self.__host = host
        self.__port = port
        self.__charset = charset
        self.__connect = None
        self.__cursor = None

    def _connect_db(self):
        """连接数据库"""
        params = {
            "db": self.__db,
            "user": self.__user,
            "passwd": self.__passwd,
            "host": self.__host,
            "port": self.__port,
            "charset": self.__charset
        }
        self.__connect = MySQLdb.connect(**params)
        self.__cursor = self.__connect.cursor()
        print("数据库连接已建立")

    def _close_db(self):
        """关闭数据库连接"""
        self.__cursor.close()
        self.__connect.close()
        print("数据库连接已断开\n")

    #  自动存储信息更新时间update
    def save_time(self, style, cell, id):
        # style中1代表更新时间，2代表创建时间
        self._connect_db()
        now_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        if style == '1':
            sql = "UPDATE %s SET updated= ('%s'), updateby=('18301113') WHERE id = ('%s') """ % (cell, now_time, id)
        if style == '2':
            sql = "UPDATE %s SET created= ('%s'), createby=('18301113') WHERE id = ('%s') """ % (cell, now_time, id)
        # 构建sql语句
        self.__cursor.execute(sql)
        self.__connect.commit()
        print("语句执行完毕")
        print("数据更新时间存储成功\n")
        self._close_db()

    #  插入老人信息,number:1
    def insert_OldPerson(self, username, gender, phone, birthday, checkin_date, checkout_date, id_card):
        # 用户传入数据字典列表数据，根据key, value添加进数据库
        # 连接数据库
        self._connect_db()

        # 验证身份信息是否存在
        sql = "SELECT id_card FROM oldperson_info"
        print("正在执行语句：" + sql)
        self.__cursor.execute(sql)
        id_card_result = self.__cursor.fetchall()
        print("语句执行完毕")
        for i in id_card_result:
            if i[0] == id_card:
                print("身份信息已存在\n")
                self._close_db()
                return "1"
        # 构建sql语句
        sql = "INSERT INTO oldperson_info (username,gender,phone, birthday, checkin_date, checkout_date,id_card,created,createby) VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')""" % (
            username, gender, phone, birthday, checkin_date, checkout_date, id_card,
            datetime.datetime.now().strftime('%Y-%m-%d'), "18301113")
        print("正在执行语句：" + sql)
        self.__cursor.execute(sql)
        self.__connect.commit()
        print("语句执行完毕")
        self._close_db()
        return "0"

    #  插入义工信息,number:2
    def insert_Volunteer(self, username, gender, phone, birthday, checkin_date, checkout_date, id_card):
        # 用户传入数据字典列表数据，根据key, value添加进数据库
        # 连接数据库
        self._connect_db()

        # 验证身份信息是否存在
        sql = "SELECT id_card FROM volunteer_info"
        print("正在执行语句：" + sql)
        self.__cursor.execute(sql)
        id_card_result = self.__cursor.fetchall()
        print("语句执行完毕")
        for i in id_card_result:
            if i[0] == id_card:
                print("身份信息已存在\n")
                self._close_db()
                return "1"
        # 构建sql语句
        sql = "INSERT INTO volunteer_info (username,gender,phone, birthday, checkin_date, checkout_date,id_card,created,createby) VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')""" % (
            username, gender, phone, birthday, checkin_date, checkout_date, id_card,
            datetime.datetime.now().strftime('%Y-%m-%d'), "18301113")
        print("正在执行语句：" + sql)
        self.__cursor.execute(sql)
        self.__connect.commit()
        self._close_db()
        print("语句执行完毕")
        print("插入义工信息成功\n")
        return "0"

    #  插入工作人员信息,number:3
    def insert_Employee(self, username, gender, phone, birthday, hire_date, resign_date, id_card):
        # 用户传入数据字典列表数据，根据key, value添加进数据库
        # 连接数据库
        self._connect_db()

        # 验证身份信息是否存在
        sql = "SELECT id_card FROM employee_info"
        print("正在执行语句：" + sql)
        self.__cursor.execute(sql)
        id_card_result = self.__cursor.fetchall()
        print("语句执行完毕")
        for i in id_card_result:
            if i[0] == id_card:
                print("身份信息已存在\n")
                self._close_db()
                return "1"
        # 构建sql语句
        sql = "INSERT INTO employee_info (username,gender,phone, birthday, hire_date, resign_date,id_card,created,createby) VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')""" % (
            username, gender, phone, birthday, hire_date, resign_date, id_card,
            datetime.datetime.now().strftime('%Y-%m-%d'), "18301113")
        print("正在执行语句：" + sql)
        self.__cursor.execute(sql)
        self.__connect.commit()
        print("语句执行完毕")
        print("插入工作人员信息成功\n")
        self._close_db()
        return "0"

    #  插入系统管理员信息,number:4
    def insert_SysUser(self, email, password, sex, nickname, phone):
        # 用户传入数据字典列表数据，根据key, value添加进数据库
        # 连接数据库
        self._connect_db()

        # 验证邮箱是否存在
        sql = "SELECT email FROM sys_user"
        print("正在执行语句：" + sql)
        self.__cursor.execute(sql)
        email_result = self.__cursor.fetchall()
        print("语句执行完毕")
        # print(email_result)
        for i in email_result:
            # print(i)
            if i[0] == email:
                print("邮箱已存在\n")
                self._close_db()
                return "1"

        # 构建sql语句
        sql = "INSERT INTO sys_user (email,password,sex,username,phone,created,createby) VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s')""" % (
            email, password, sex, nickname, phone, datetime.datetime.now().strftime('%Y-%m-%d'), "18301113")
        print("正在执行语句：" + sql)
        self.__cursor.execute(sql)
        self.__connect.commit()
        print("语句执行完毕")
        print("插入管理员信息成功\n")
        self._close_db()
        return "0"

    #  修改老人信息,number:5
    def update_OldPerson(self, id, update):
        self._connect_db()
        data = {
            'birthday': update['birthday'],
            'gender': update['gender'],
            'checkin_date': update['checkin_date'],
            'id_card': update['id_card'],
            'imgset_dir': update['imgset_dir'],
            'phone': update['phone'],
            'profile_photo': update['profile_photo'],
            'checkout_date': update['checkout_date'],
            'username': update['username']
        }
        # 构建sql语句
        for i in data:
            sql = "UPDATE oldperson_info SET %s = ('%s') WHERE id = ('%s') """ % (i, data[i], id)
            print("正在执行语句：" + sql)
            self.__cursor.execute(sql)
            self.__connect.commit()
            print("语句执行完毕")
        self._close_db()
        #  自动存储时间
        self.save_time("1", "oldperson_info", id)
        return "0"

    #  修改义工信息,number:6
    def update_Volunteer(self, id, update):
        self._connect_db()
        data = {
            'birthday': update['birthday'],
            'gender': update['gender'],
            'checkin_date': update['checkin_date'],
            'id_card': update['id_card'],
            'imgset_dir': update['imgset_dir'],
            'phone': update['phone'],
            'profile_photo': update['profile_photo'],
            'checkout_date': update['checkout_date'],
            'username': update['username']
        }
        # 构建sql语句
        for i in data:
            sql = "UPDATE volunteer_info SET %s = ('%s') WHERE id = ('%s') """ % (i, data[i], id)
            print("正在执行语句：" + sql)
            self.__cursor.execute(sql)
            self.__connect.commit()
            print("语句执行完毕")
        self._close_db()
        #  自动存储时间
        self.save_time("1", "volunteer_info", id)
        return "0"

    #  修改工作人员信息,number:7
    def update_Employee(self, id, update):
        self._connect_db()
        data = {
            'birthday': update['birthday'],
            'gender': update['gender'],
            'hire_date': update['hire_date'],
            'id_card': update['id_card'],
            'imgset_dir': update['imgset_dir'],
            'phone': update['phone'],
            'profile_photo': update['profile_photo'],
            'resign_date': update['resign_date'],
            'username': update['username']
        }
        for i in data:
            # print(data[i])
            sql = "UPDATE employee_info SET %s = ('%s') WHERE id = ('%s') """ % (i, data[i], id)
            print("正在执行语句：" + sql)
            self.__cursor.execute(sql)
            self.__connect.commit()
            print("语句执行完毕")
        self._close_db()
        #  自动存储时间
        self.save_time("1", "employee_info", id)
        return "0"

    #  删除老人信息,number:8
    def delete_OldPerson(self, id):
        self._connect_db()
        # # 处理删除的条件
        # condition_list = self._deal_values(id)
        # condition_data = ''.join(condition_list)
        # 构建sql语句
        sql = "DELETE FROM oldperson_info WHERE id=('%s')""" % id
        print("正在执行语句：" + sql)
        self.__cursor.execute(sql)
        self.__connect.commit()
        print("语句执行完毕")
        self._close_db()
        print("删除老人信息成功\n")
        return "0"

    #  删除义工信息,number:9
    def delete_Volunteer(self, id):
        self._connect_db()
        # 构建sql语句
        sql = "DELETE FROM volunteer_info WHERE id=('%s')""" % id
        print("正在执行语句：" + sql)
        self.__cursor.execute(sql)
        self.__connect.commit()
        print("语句执行完毕")
        self._close_db()
        print("删除义工信息成功\n")
        return "0"

    #  删除工作人员信息,number:10
    def delete_Employee(self, id):
        self._connect_db()
        # 构建sql语句
        sql = "DELETE FROM employee_info WHERE id=('%s')""" % id
        print("正在执行语句：" + sql)
        self.__cursor.execute(sql)
        self.__connect.commit()
        print("语句执行完毕")
        self._close_db()
        print("删除工作人员信息成功\n")
        return "0"

    #  查询老人信息,number:11
    def select_OldPerson(self):
        self._connect_db()
        sql = "SELECT * FROM oldperson_info"
        print("正在执行语句：" + sql)
        self.__cursor.execute(sql)
        result = self.__cursor.fetchall()
        print("语句执行完毕")
        self._close_db()
        jsonData = []
        if result:
            for row in result:
                data = {'id': row[0], 'username': row[3], 'gender': row[4], 'phone': row[5], 'id_card': row[6],
                        'birthday': row[7].strftime('%Y-%m-%d'), 'checkin_date': row[8].strftime('%Y-%m-%d'),
                        'checkout_date': row[9].strftime('%Y-%m-%d'), 'imgset_dir': row[10],
                        'profile_photo': row[11], 'room_number': row[12], 'firstguardian_name': row[13],
                        'firstguardian_relationship': row[14],
                        'firstguardian_phone': row[15], 'firstguardian_wechat': row[16],
                        'secondguardian_name': row[17], 'secondguardian_relationship': row[18],
                        'secondguardian_phone': row[19], 'secondguardian_wechat': row[20], 'health_state': row[21]}
                jsonData.append(data)
            print("老人信息查询成功\n")
            return jsonData
        else:
            print("老人信息查询失败\n")
            return "1"

    #  查询义工信息,number:12
    def select_Volunteer(self):
        self._connect_db()
        sql = "SELECT * FROM volunteer_info"
        print("正在执行语句：" + sql)
        self.__cursor.execute(sql)
        result = self.__cursor.fetchall()
        print("语句执行完毕")
        self._close_db()
        jsonData = []
        if result:
            for row in result:
                data = {'id': row[0], 'username': row[3], 'gender': row[4], 'phone': row[5], 'id_card': row[6],
                        'birthday': row[7].strftime('%Y-%m-%d'), 'checkin_date': row[8].strftime('%Y-%m-%d'),
                        'checkout_date': row[9].strftime('%Y-%m-%d'), 'imgset_dir': row[10],
                        'profile_photo': row[11]}
                jsonData.append(data)
            print("义工信息查询成功\n")
            return jsonData
        else:
            print("义工信息查询失败\n")
            return "1"

    #  查询工作人员信息,number:13
    def select_Employee(self):
        self._connect_db()
        sql = "SELECT * FROM employee_info"
        print("正在执行语句：" + sql)
        self.__cursor.execute(sql)
        result = self.__cursor.fetchall()
        print("语句执行完毕")
        self._close_db()
        jsonData = []
        if result:
            for row in result:
                data = {'id': row[0], 'username': row[3], 'gender': row[4], 'phone': row[5], 'id_card': row[6],
                        'birthday': row[7].strftime('%Y-%m-%d'), 'hire_date': row[8].strftime('%Y-%m-%d'),
                        'resign_date': row[9].strftime('%Y-%m-%d'), 'imgset_dir': row[10],
                        'profile_photo': row[11]}
                jsonData.append(data)
            print("工作人员信息查询成功\n")
            # print(jsonData)
            return jsonData
        else:
            print("工作人员信息查询失败\n")
            return "1"

    #  修改系统管理员信息,number:14
    def update_SysUser(self, id, password, phone, username):
        self._connect_db()
        # 构建sql语句
        sql = "UPDATE sys_user SET Password = ('%s'), phone = ('%s'), username = ('%s') WHERE id = ('%s') """ % (
            password, phone, username, id)
        print("正在执行语句：" + sql)
        self.__cursor.execute(sql)
        self.__connect.commit()
        print("语句执行完毕")
        self._close_db()
        #  自动存储时间
        self.save_time("1", "sys_user", id)
        print("修改管理员信息成功\n")
        return "0"

    def get_resigter_sys_userID(self):
        # 注册时获取管理员的ID

        self._connect_db()

        # 处理显示的数据

        sql = "SELECT AUTO_INCREMENT FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME= 'sys_user'"

        self.__cursor.execute(sql)
        print(sql)
        # 返回一条数据
        result = self.__cursor.fetchone()
        self._close_db()
        jsonData = []
        data = {'ID': result}
        jsonData.append(data)
        print(jsonData)
        print("获取管理员id成功\n")
        return jsonData

    # 登录检测并获取ID,number:15
    def get_sys_user(self, EMAIL, Password):
        self._connect_db()

        sql = "select * from sys_user where EMAIL = '%s' and Password = '%s'""" % (EMAIL, Password)
        print("正在执行语句：" + sql)
        self.__cursor.execute(sql)

        result = self.__cursor.fetchall()
        self._close_db()
        if result:
            for row in result:
                num = row[0]
                print("管理员登录验证成功\n")
                return num
        else:
            print("管理员登录验证失败\n")
            return "1"

    #  查询系统管理人员信息,number:16
    def select_SysUser(self, uid):
        self._connect_db()
        sql = "SELECT * FROM sys_user WHERE id = %s""" % uid
        print("正在执行语句：" + sql)
        self.__cursor.execute(sql)
        result = self.__cursor.fetchall()
        print("语句执行完毕")
        self._close_db()
        information = {}
        if result:
            for row in result:
                data = {'email': row[7], 'username': row[3], 'phone': row[8], 'password': row[4], 'gender': row[6]}
                information = data
                print("管理员信息查询成功\n")
            return information
        else:
            print("管理员信息查询失败\n")
            return "1"

    #  模糊查询通用接口,number:17
    def select_Information(self, form, field, key):
        self._connect_db()
        # sql = "SELECT * FROM %s WHERE username LIKE '%s'  """ % (form, "%"+key+"%")
        sql = "SELECT * FROM %s WHERE %s LIKE '%s'  """ % (form, field, "%"+key+"%")
        print("正在执行语句：" + sql)
        self.__cursor.execute(sql)
        result = self.__cursor.fetchall()
        print("语句执行完毕")
        # print(result)
        self._close_db()

        jsonData = []
        if form == "oldperson_info":
            for row in result:
                data = {'id': row[0], 'username': row[3], 'gender': row[4], 'phone': row[5], 'id_card': row[6],
                        'birthday': row[7].strftime('%Y-%m-%d'), 'checkin_date': row[8].strftime('%Y-%m-%d'),
                        'checkout_date': row[9].strftime('%Y-%m-%d'), 'imgset_dir': row[10],
                        'profile_photo': row[11], 'room_number': row[12], 'firstguardian_name': row[13],
                        'firstguardian_relationship': row[14],
                        'firstguardian_phone': row[15], 'firstguardian_wechat': row[16],
                        'secondguardian_name': row[17], 'secondguardian_relationship': row[18],
                        'secondguardian_phone': row[19], 'secondguardian_wechat': row[20], 'health_state': row[21]}
                jsonData.append(data)
            print("老人信息查询成功\n")
            return jsonData
        elif form == "volunteer_info":
            for row in result:
                data = {'id': row[0], 'username': row[3], 'gender': row[4], 'phone': row[5], 'id_card': row[6],
                        'birthday': row[7].strftime('%Y-%m-%d'), 'checkin_date': row[8].strftime('%Y-%m-%d'),
                        'checkout_date': row[9].strftime('%Y-%m-%d'), 'imgset_dir': row[10],
                        'profile_photo': row[11]}
                jsonData.append(data)
            print("义工信息查询成功\n")
            return jsonData
        elif form == "employee_info":
            for row in result:
                data = {'id': row[0], 'username': row[3], 'gender': row[4], 'phone': row[5], 'id_card': row[6],
                        'birthday': row[7].strftime('%Y-%m-%d'), 'hire_date': row[8].strftime('%Y-%m-%d'),
                        'resign_date': row[9].strftime('%Y-%m-%d'), 'imgset_dir': row[10],
                        'profile_photo': row[11]}
                jsonData.append(data)
            print("工作人员信息查询成功\n")
            return jsonData
        else:
            print("无查询结果\n")
            return "1"

