import MySQLdb
class MysqlManager(object):
    '''mysql管理器'''

    def __init__(self, db, user, passwd, host='8.131.235.164', port=3306, charset='utf8'):
        '''初始化数据库'''
        self.__db = db
        self.__user = user
        self.__passwd = passwd
        self.__host = host
        self.__port = port
        self.__charset = charset
        self.__connect = None
        self.__cursor = None

    def _connect_db(self):
        """
            dbManager._connect_db()
        连接数据库
        """
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

    def _close_db(self):
        '''
            dbManager._close_db()
        关闭数据库
        '''
        self.__cursor.close()
        self.__connect.close()

    # ------------------------------------------------------------------------------------------------------
    # 管理员登录注册
    # ------------------------------------------------------------------------------------------------------
    def insert_resigter(self,UserName,Password,EMAIL,PHONE):
        # 管理员的注册
        '''
            dbManager.insert(UserName,Password,EMAIL,PHONE)
        添加数据到数据库

        '''
        # 用户传入数据字典列表数据，根据key, value添加进数据库
        # 连接数据库
        self._connect_db()

        try:
            # 构建sql语句
            sql = "insert into sys_user (ORG_ID,CLIENT_ID,UserName,Password,EMAIL,PHONE) values ('1', '1','%s','%s','%s','%s')""" % (UserName,Password,EMAIL,PHONE)

            self.__cursor.execute(sql)
            self.__connect.commit()
        except Exception as error:
            print('error')
            return 0
        finally:
            self._close_db()
            return 1

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
        return jsonData



    def get_sys_user(self, EMAIL,Password):
        # 登录检测并获取ID
        """
            dbManager.get(table, show_list, [condition, get_one]) -> tupe
        获取数据 返回一个元祖
        str -> table 字符串类型
        list -> show_list 列表类型
        dict -> condition 字典类型
        boolean -> get_one 布尔类型

        """
        self._connect_db()

        sql = "select * from sys_user where EMAIL = '%s' and Password = '%s'""" % (EMAIL,Password)
        self.__cursor.execute(sql)


        result = self.__cursor.fetchall()
        self._close_db()
        if (len(result))==1:
            jsonData = []
            for row in result:
                data = {'ID': row[0]}
                jsonData.append(data)
            print(jsonData)
            return jsonData
        else:
            return 0
# ---------------------------------------------------------------------------------------------------------------
# 老人信息处理
# ---------------------------------------------------------------------------------------------------------------
    def analysis_oldpeolpe(self):
        # 统计分析老人的年龄结构
        '''
                    dbManager.analysis_oldpeolpe()

        '''
        # 连接数据库
        self._connect_db()

        try:
            # 构建sql语句
            sql ="Select " \
                 "Sum(1), " \
                 "Sum(Case When age <=50 Then 1 Else 0 End) As '[0-50]'," \
                 "Sum(Case When age Between 51 And 60 Then 1 Else 0 End) As '[51-60]'," \
                 "Sum(Case When age Between 61 And 70 Then 1 Else 0 End) As '[61-70]'," \
                 "Sum(Case When age Between 71 And 80 Then 1 Else 0 End) As '[71-80]'," \
                 "Sum(Case When age >=81 Then 1 Else 0 End) As '[80-90]' " \
                 "From" \
                 "(SELECT *, ROUND(DATEDIFF(CURDATE(), birthday)/365.2422)  AS 'age' FROM oldperson_info) s "


            self.__cursor.execute(sql)
            self.__connect.commit()
        except Exception as error:
            print('error')
            return 0
        finally:
            result = self.__cursor.fetchall()
            print(result)
            jsonData = []
            for row in result:
                data = {'[总人数(人)]': int(row[0]),'[0-50岁(人)]': int(row[1]),'[50-60岁(人)]': int(row[2]),'[60-70岁(人)]': int(row[3]),'[70-80岁(人)]': int(row[4]),'[80-90岁(人)]': int(row[5])}
                jsonData.append(data)
            print(jsonData)
            return jsonData
            self._close_db()
            return 1

        # ---------------------------------------------------------------------------------------------------------------
        # 工作人员信息处理
        # ---------------------------------------------------------------------------------------------------------------
    def analysis_employee(self):
        # 统计分析工作人员的年龄结构
        '''
                    dbManager.analysis_employee()

        '''
        # 连接数据库
        self._connect_db()

        try:
            # 构建sql语句
            sql = "Select " \
                  "Sum(1), " \
                  "Sum(Case When age <=20 Then 1 Else 0 End) As '[0-20]'," \
                  "Sum(Case When age Between 21 And 30 Then 1 Else 0 End) As '[21-30]'," \
                  "Sum(Case When age Between 31 And 40 Then 1 Else 0 End) As '[31-40]'," \
                  "Sum(Case When age Between 41 And 50 Then 1 Else 0 End) As '[41-50]'" \
                  "From" \
                  "(SELECT *, ROUND(DATEDIFF(CURDATE(), birthday)/365.2422)  AS 'age' FROM employee_info) s "

            self.__cursor.execute(sql)
            self.__connect.commit()
        except Exception as error:
            print('error')
            return 0
        finally:
            result = self.__cursor.fetchall()
            print(result)
            jsonData = []
            for row in result:
                data = {'[总人数(人)]': int(row[0]), '[0-20岁(人)]': int(row[1]), '[20-30岁(人)]': int(row[2]),
                        '[30-40岁(人)]': int(row[3]), '[40-50岁(人)]': int(row[4])}
                jsonData.append(data)
            print(jsonData)
            return jsonData
            self._close_db()
            return 1

        # ---------------------------------------------------------------------------------------------------------------
        # 义工信息处理
        # ---------------------------------------------------------------------------------------------------------------

    def analysis_volunteer(self):
        # 统计分析工作人员的年龄结构
        '''
                    dbManager.analysis_volunteer()

        '''
        # 连接数据库
        self._connect_db()

        try:
            # 构建sql语句
            sql = "Select " \
                  "Sum(1), " \
                  "Sum(Case When age <=20 Then 1 Else 0 End) As '[0-20]'," \
                  "Sum(Case When age Between 21 And 30 Then 1 Else 0 End) As '[21-30]'," \
                  "Sum(Case When age Between 31 And 40 Then 1 Else 0 End) As '[31-40]'," \
                  "Sum(Case When age Between 41 And 50 Then 1 Else 0 End) As '[41-50]'" \
                  "From" \
                  "(SELECT *, ROUND(DATEDIFF(CURDATE(), birthday)/365.2422)  AS 'age' FROM volunteer_info) s "

            self.__cursor.execute(sql)
            self.__connect.commit()
        except Exception as error:
            print('error')
            return 0
        finally:
            result = self.__cursor.fetchall()
            print(result)
            jsonData = []
            for row in result:
                data = {'[总人数(人)]': int(row[0]), '[0-20岁(人)]': int(row[1]), '[20-30岁(人)]': int(row[2]),
                        '[30-40岁(人)]': int(row[3]), '[40-50岁(人)]': int(row[4])}
                jsonData.append(data)
            print(jsonData)
            return jsonData
            self._close_db()
            return 1

    # ----------------------------------------------------------------------------------------------------------------------
# 与计算机视觉的对接
# ----------------------------------------------------------------------------------------------------------------------
#     分析老人的情感
    def insert_event1(self,event_type,event_date,event_location,event_desc,oldperson_id):
        # 管理员的注册
        '''
            dbManager.insert(UserName,Password,EMAIL,PHONE)
        添加数据到数据库

        '''
        # 用户传入数据字典列表数据，根据key, value添加进数据库
        # 连接数据库
        self._connect_db()

        try:
            # 构建sql语句
            sql = "insert into event_info (event_type,event_date,event_location,event_desc,oldperson_id) values ('%s','%s','%s','%s','%s')""" % (event_type,event_date,event_location,event_desc,oldperson_id)
            print(sql)
            self.__cursor.execute(sql)
            self.__connect.commit()
        except Exception as error:
            print('error')
            return 0
        finally:
            self._close_db()
            print('插入成功')
            return 1

    #分析是否有人摔倒、分析是否有人闯入禁止区域、分析老人是否与义工互动、分析是否有陌生人出现
    def insert_event2(self,event_type,event_date,event_location,event_desc):
        # 管理员的注册
        '''
            dbManager.insert(UserName,Password,EMAIL,PHONE)
        添加数据到数据库

        '''
        # 用户传入数据字典列表数据，根据key, value添加进数据库
        # 连接数据库
        self._connect_db()

        try:
            # 构建sql语句
            sql = "insert into event_info (event_type,event_date,event_location,event_desc) values ('%s','%s','%s','%s')""" % (event_type,event_date,event_location,event_desc)
            print(sql)
            self.__cursor.execute(sql)
            self.__connect.commit()
        except Exception as error:
            print('error')
            return 0
        finally:
            self._close_db()
            print('插入成功')
            return 1