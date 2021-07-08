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
            print("用户名不存在")
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
            sql ="Select gender," \
                 "Sum(Case When age <=50 Then 1 Else 0 End) As '[0-50]'," \
                 "Sum(Case When age Between 51 And 60 Then 1 Else 0 End) As '[51-60]'," \
                 "Sum(Case When age Between 61 And 70 Then 1 Else 0 End) As '[61-70]'," \
                 "Sum(Case When age Between 71 And 80 Then 1 Else 0 End) As '[71-80]'," \
                 "Sum(Case When age >=81 Then 1 Else 0 End) As '[80-90]' " \
                 "From" \
                 "(SELECT *, ROUND(DATEDIFF(CURDATE(), birthday)/365.2422)  AS 'age' FROM oldperson_info) s " \
                 "GROUP BY gender"

            self.__cursor.execute(sql)
            self.__connect.commit()
        except Exception as error:
            print('error')
            return 0
        finally:
            result = self.__cursor.fetchall()
            jsonData = []
            for row in result:
                data = {'[0-50岁(人)]': row[1],'[50-60岁(人)]': row[2],'[60-70岁(人)]': row[3]}
                jsonData.append(data)
            print(jsonData)
            return jsonData
            self._close_db()
            return 1