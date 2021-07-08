import json
from flask import Flask, render_template, jsonify, request, Response
import db
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


#  将datetime格式的时间转化为可以被json使用的字符
class DateTimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, datetime.date):
            return obj.strftime('%Y-%m-%d')
        return json.JSONEncoder.default(self, obj)


app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

# 通过用户名和密码连接数据库old_care
dbManager = db.MysqlManager("old_care", 'yyn', '13141516')


#  初始界面
@app.route('/', methods=['GET'])
def index():
    # print("正在删除老人信息")
    # dbManager.delete_OldPerson("2")

    # print("正在查询老人信息")
    # user = dbManager.select_OldPerson()

    # print("正在插入工作人员信息")
    # dbManager.insert_Employee("王永健", "男", "19652520962", "18301107")

    print("正在插入老人信息")
    dbManager.insert_OldPerson("王永健", "男", "19652520962", "18301107")

    # print("正在修改老人信息")
    # data = {'id': "23", 'gender': "中性", 'id_card': "16301109", 'birthday': "1970-1-1",
    #         'checkin_date': "2000-3-3", 'checkout_date': "2030-5-5", 'description': "吃喝玩乐，当房东的日子太无聊了"}
    # dbManager.update_OldPerson(data['id'], data)

    return json.dumps({"error_code": "0", "id": ""})


#  插入老人信息,number:1
@app.route('/insert_OldPerson', methods=['GET', 'POST'])
def insert_OldPerson():
    print("正在插入老人信息")
    data = request.data
    OldPerson = json.loads(data)
    print(OldPerson)
    dbManager.insert_OldPerson(OldPerson['username'], OldPerson['gender'], OldPerson['phone'], OldPerson['id_card'])
    return json.dumps({"error_code": "0", "id": ""})


#  插入义工信息,number:2
@app.route('/insert_Volunteer', methods=['GET'])
def insert_Volunteer():
    print("正在插入义工信息")
    data = request.data
    Volunteer = json.loads(data)
    print(Volunteer)
    dbManager.insert_Volunteer(Volunteer['username'], Volunteer['gender'], Volunteer['phone'], Volunteer['id_card'])
    return json.dumps({"error_code": "0", "id": ""})


#  插入工作人员信息,number:3
@app.route('/insert_Employee', methods=['GET'])
def insert_Employee():
    print("正在插入工作人员信息")
    data = request.data
    Employee = json.loads(data)
    print(Employee)
    dbManager.insert_Employee(Employee['username'], Employee['gender'], Employee['phone'], Employee['id_card'])
    return json.dumps({"error_code": "0", "id": ""})


#  插入系统管理员信息,number:4
@app.route('/insert_SysUser', methods=['GET'])
def insert_SysUser():
    print("正在注册管理员信息")
    data = request.data
    sys_data = json.loads(data)
    print(sys_data)
    dbManager.insert_SysUser(sys_data['username'], sys_data['password'])
    return json.dumps({"error_code": "0", "id": ""})


#  修改老人信息,number:5
@app.route('/update_OldPerson', methods=['GET'])
def update_OldPerson():
    print("正在修改老人信息")
    data = request.data
    OldPerson = json.loads(data)
    print(OldPerson)
    dbManager.update_OldPerson(OldPerson['id'], OldPerson)
    return json.dumps({"error_code": "0", "id": ""})


#  修改义工信息,number:6
@app.route('/update_Volunteer', methods=['GET'])
def update_Volunteer():
    print("正在修改义工信息")
    data = request.data
    Volunteer = json.loads(data)
    print(Volunteer)
    dbManager.update_Volunteer(Volunteer['id'], Volunteer)
    return json.dumps({"error_code": "0", "id": ""})


#  修改工作人员信息,number:7
@app.route('/update_Employee', methods=['GET'])
def update_Employee():
    print("正在修改工作人员信息")
    data = request.data
    Employee = json.loads(data)
    print(Employee)
    dbManager.update_Employee(Employee['id'], Employee)
    return json.dumps({"error_code": "0", "id": ""})


#  删除老人信息,number:8
@app.route('/delete_OldPerson', methods=['GET'])
def delete_OldPerson():
    print("正在删除老人信息")
    data = request.data
    OldPerson = json.loads(data)
    print(OldPerson)
    dbManager.delete_OldPerson(OldPerson['id'])
    return json.dumps({"error_code": "0", "id": ""})


#  删除义工信息,number:9
@app.route('/delete_Volunteer', methods=['GET'])
def delete_Volunteer():
    print("正在删除义工信息")
    data = request.data
    Volunteer = json.loads(data)
    print(Volunteer)
    dbManager.insert_SysUser(Volunteer['id'])
    return json.dumps({"error_code": "0", "id": ""})


#  删除工作人员信息,number:10
@app.route('/delete_Employee', methods=['GET'])
def delete_Employee():
    print("正在删除工作人员信息")
    data = request.data
    Employee = json.loads(data)
    print(Employee)
    dbManager.insert_SysUser(Employee['id'])
    return json.dumps({"error_code": "0", "id": ""})


#  查询老人信息,number:11
@app.route('/select_OldPerson', methods=['GET'])
def select_OldPerson():
    #  获取所有老人信息并输出
    print("正在获取老人信息")
    user = dbManager.select_OldPerson()
    return json.dumps(user, cls=DateTimeEncoder)


#  查询义工信息,number:12
@app.route('/select_Volunteer', methods=['GET'])
def select_Volunteer():
    #  获取所有义工信息并输出
    print("正在获取义工信息")
    user = dbManager.select_Volunteer()
    return json.dumps(user, cls=DateTimeEncoder)


#  查询工作人员信息,number:13
@app.route('/select_Employee', methods=['GET'])
def select_Employee():
    #  获取所有工作人员信息并输出
    print("正在获取工作人员信息")
    user = dbManager.select_Employee()
    return json.dumps(user, cls=DateTimeEncoder)


#  修改系统管理员密码,number:14
@app.route('/update_SysUser', methods=['GET'])
def update_SysUser():
    print("正在修改系统管理员密码")
    data = request.data
    sys_data = json.loads(data)
    print(sys_data)
    dbManager.update_SysUser(sys_data['id'], sys_data['password'])
    return json.dumps({"error_code": "0", "id": ""})


#  网页test
@app.route('/test.html', methods=['GET'])
def test():
    return render_template("test.html")


if __name__ == '__main__':
    app.run()
