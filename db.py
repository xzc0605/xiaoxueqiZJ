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
        rewrite_print("日志文档生成时间：" + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + "\n", file=open(filename, "a"))
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
        print("正在执行语句："+sql)
        self.__cursor.execute(sql)
        self.__connect.commit()
        print("语句执行完毕")
        self._close_db()

    #  插入老人信息,number:1
    def insert_OldPerson(self, username, gender, phone, id_card):
        # 用户传入数据字典列表数据，根据key, value添加进数据库
        # 连接数据库
        self._connect_db()
        try:
            # 构建sql语句
            sql = "INSERT INTO oldperson_info (username,gender,phone,id_card,created,createby) VALUES ('%s', '%s', '%s', '%s', '%s', '%s')""" % (
                username, gender, phone, id_card, datetime.datetime.now().strftime('%Y-%m-%d'), "18301113")
            print("正在执行语句：" + sql)
            self.__cursor.execute(sql)
            self.__connect.commit()
            print("语句执行完毕")
        except Exception:
            print('插入老人信息出错，error')
        finally:
            self._close_db()
            #  自动存储时间
            # self.save_time("1", "oldperson_info", id)

    #  插入义工信息,number:2
    def insert_Volunteer(self, username, gender, phone, id_card):
        # 用户传入数据字典列表数据，根据key, value添加进数据库
        # 连接数据库
        self._connect_db()
        try:
            # 构建sql语句
            sql = "INSERT INTO volunteer_info (username,gender,phone,id_card,created,createby) VALUES ('%s', '%s', '%s', '%s', '%s', '%s')""" % (
                username, gender, phone, id_card, datetime.datetime.now().strftime('%Y-%m-%d'), "18301113")
            print("正在执行语句：" + sql)
            self.__cursor.execute(sql)
            self.__connect.commit()
            # #  创建时间和最后更新时间
            # sql = "INSERT INTO volunteer_info (created, ) VALUES ('%s', '%s', '%s', '%s')""" % (
            #     username, gender, phone, id_card)
            print("正在执行语句：" + sql)
            self.__cursor.execute(sql)
            self.__connect.commit()
            print("语句执行完毕")
        except Exception as error:
            print('插入义工信息出错' + error)
            return error
        finally:
            self._close_db()
            #  自动存储时间
            # self.save_time("1", "volunteer_info", id)

    #  插入工作人员信息,number:3
    def insert_Employee(self, username, gender, phone, id_card):
        # 用户传入数据字典列表数据，根据key, value添加进数据库
        # 连接数据库
        self._connect_db()
        try:
            # 构建sql语句
            sql = "INSERT INTO employee_info (username,gender,phone,id_card,created,createby) VALUES ('%s', '%s', '%s', '%s', '%s', '%s')""" % (
                username, gender, phone, id_card, datetime.datetime.now().strftime('%Y-%m-%d'), "18301113")
            print("正在执行语句：" + sql)
            self.__cursor.execute(sql)
            self.__connect.commit()
            print("语句执行完毕")
        except Exception as error:
            print('插入工作人员信息出错' + error)
            return error
        finally:
            self._close_db()
            #  自动存储时间
            # self.save_time("1", "employee_info", id)

    #  插入系统管理员信息,number:4
    def insert_SysUser(self, username, gender, phone, id_card):
        # 用户传入数据字典列表数据，根据key, value添加进数据库
        # 连接数据库
        self._connect_db()
        try:
            # 构建sql语句
            sql = "INSERT INTO sys_user (username,gender,phone,id_card,created,createby) VALUES ('%s', '%s', '%s', '%s', '%s', '%s')""" % (
                username, gender, phone, id_card, datetime.datetime.now().strftime('%Y-%m-%d'), "18301113")
            print("正在执行语句：" + sql)
            self.__cursor.execute(sql)
            self.__connect.commit()
            print("语句执行完毕")
        except Exception as error:
            print('插入系统管理员信息出错' + error)
            return error
        finally:
            self._close_db()
            #  自动存储时间
            # self.save_time("1", "sys_user", id)

    #  修改老人信息,number:5
    def update_OldPerson(self, id, data):
        self._connect_db()
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

    #  修改义工信息,number:6
    def update_Volunteer(self, id, data):
        self._connect_db()
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

    #  修改工作人员信息,number:7
    def update_Employee(self, id, data):
        self._connect_db()
        # 构建sql语句
        for i in data:
            sql = "UPDATE employee_info SET %s = ('%s') WHERE id = ('%s') """ % (i, data[i], id)
            print("正在执行语句：" + sql)
            self.__cursor.execute(sql)
            self.__connect.commit()
            print("语句执行完毕")
        self._close_db()
        #  自动存储时间
        self.save_time("1", "employee_info", id)

    #  删除老人信息,number:8
    def delete_OldPerson(self, id):
        self._connect_db()
        # # 处理删除的条件
        # condition_list = self._deal_values(id)
        # condition_data = ''.join(condition_list)
        # 构建sql语句
        sql = "DELETE FROM oldperson_info WHERE id=('%s')""" % id
        print("正在执行语句："+sql)
        self.__cursor.execute(sql)
        self.__connect.commit()
        print("语句执行完毕")
        self._close_db()

    #  删除义工信息,number:9
    def delete_Volunteer(self, id):
        self._connect_db()
        # 构建sql语句
        sql = "DELETE FROM volunteer_info WHERE id=('%s')""" % id
        print("正在执行语句："+sql)
        self.__cursor.execute(sql)
        self.__connect.commit()
        print("语句执行完毕")
        self._close_db()

    #  删除工作人员信息,number:10
    def delete_Employee(self, id):
        self._connect_db()
        # 构建sql语句
        sql = "DELETE FROM employee_info WHERE id=('%s')""" % id
        print("正在执行语句："+sql)
        self.__cursor.execute(sql)
        self.__connect.commit()
        print("语句执行完毕")
        self._close_db()

    #  查询老人信息,number:11
    def select_OldPerson(self):
        self._connect_db()
        sql = "SELECT * FROM oldperson_info"
        print("正在执行语句："+sql)
        self.__cursor.execute(sql)
        result = self.__cursor.fetchall()
        print("语句执行完毕")
        self._close_db()
        jsonData = []
        for row in result:
            data = {'uid': row[0], 'username': row[3], 'gender': row[4], 'phone': row[5], 'id_card': row[6],
                    'birthday': row[7], 'checkin_date': row[8], 'checkout_date': row[9], 'imgset_dir': row[10],
                    'profile_photo': row[11], 'room_number': row[12], 'firstguardian_name': row[13], 'firstguardian_relationship': row[14],
                    'firstguardian_phone': row[15], 'firstguardian_wechat': row[16],
                    'secondguardian_name': row[17], 'secondguardian_relationship': row[18],
                    'secondguardian_phone': row[19], 'secondguardian_wechat': row[20], 'health_state': row[21]}
            jsonData.append(data)
        print(data)
        return jsonData

    #  查询义工信息,number:12
    def select_Volunteer(self):
        self._connect_db()
        sql = "SELECT * FROM volunteer_info"
        print("正在执行语句："+sql)
        self.__cursor.execute(sql)
        result = self.__cursor.fetchall()
        print("语句执行完毕")
        self._close_db()
        jsonData = []
        for row in result:
            data = {'uid': row[0], 'username': row[3], 'gender': row[4], 'phone': row[5], 'id_card': row[6],
                    'birthday': row[7], 'checkin_date': row[8], 'checkout_date': row[9], 'imgset_dir': row[10], 'profile_photo': row[11]}
            jsonData.append(data)
        print(data)
        return jsonData

    #  查询工作人员信息,number:13
    def select_Employee(self):
        self._connect_db()
        sql = "SELECT * FROM employee_info"
        print("正在执行语句："+sql)
        self.__cursor.execute(sql)
        result = self.__cursor.fetchall()
        print("语句执行完毕")
        self._close_db()
        jsonData = []
        for row in result:
            data = {'uid': row[0], 'username': row[3], 'gender': row[4], 'phone': row[5], 'id_card': row[6],
                    'birthday': row[7], 'hire_date': row[8], 'resign_date': row[9], 'imgset_dir': row[10], 'profile_photo': row[11]}
            jsonData.append(data)
        print(data)
        return jsonData

    #  修改系统管理员密码,number:14
    def update_SysUser(self, id, password):
        self._connect_db()
        # 构建sql语句
        sql = "UPDATE sys_user SET Password = ('%s') WHERE id = ('%s') """ % (id, password)
        print("正在执行语句："+sql)
        self.__cursor.execute(sql)
        self.__connect.commit()
        print("语句执行完毕")
        self._close_db()
        #  自动存储时间
        self.save_time("1", "sys_user", id)
