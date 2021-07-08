import json
from flask import Flask, render_template, jsonify, request, Response, make_response
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
        rewrite_print("日志文档生成时间：" + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + "\n",
                      file=open(filename, "a"))
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


#  插入老人信息,number:1
@app.route('/insert_OldPerson', methods=['GET', 'POST'])
def insert_OldPerson():
    print("正在插入老人信息")
    dbManager.insert_OldPerson(request.args.get('username'), request.args.get('gender'), request.args.get('phone'),
                               request.args.get('id_card'))
    data = {
        'error': "0",  # 0请求成功 1请求失败
        'messages': "插入成功",
    }
    res = make_response(jsonify(data))  # 设置响应体
    res.status = '200'  # 设置状态码
    res.headers['Access-Control-Allow-Origin'] = "*"  # 设置允许跨域
    res.headers['Access-Control-Allow-Methods'] = 'PUT,GET,POST,DELETE'

    return res


#  插入义工信息,number:2
@app.route('/insert_Volunteer', methods=['GET'])
def insert_Volunteer():
    print("正在插入义工信息")
    dbManager.insert_Volunteer(request.args.get('username'), request.args.get('gender'), request.args.get('phone'),
                               request.args.get('id_card'))
    data = {
        'error': "0",  # 0请求成功 1请求失败
        'messages': "插入成功",
    }
    res = make_response(jsonify(data))  # 设置响应体
    res.status = '200'  # 设置状态码
    res.headers['Access-Control-Allow-Origin'] = "*"  # 设置允许跨域
    res.headers['Access-Control-Allow-Methods'] = 'PUT,GET,POST,DELETE'

    return res


#  插入工作人员信息,number:3
@app.route('/insert_Employee', methods=['GET'])
def insert_Employee():
    print("正在插入工作人员信息")
    dbManager.insert_Employee(request.args.get('username'), request.args.get('gender'), request.args.get('phone'),
                               request.args.get('id_card'))
    data = {
        'error': "0",  # 0请求成功 1请求失败
        'messages': "插入成功",
    }
    res = make_response(jsonify(data))  # 设置响应体
    res.status = '200'  # 设置状态码
    res.headers['Access-Control-Allow-Origin'] = "*"  # 设置允许跨域
    res.headers['Access-Control-Allow-Methods'] = 'PUT,GET,POST,DELETE'

    return res


#  插入系统管理员信息,number:4
@app.route('/insert_SysUser', methods=['GET'])
def insert_SysUser():
    print("正在注册管理员信息")
    dbManager.insert_SysUser(request.args.get('email'), request.args.get('password'), request.args.get('sex'),
                             request.args.get('nickname'), request.args.get('phone'))
    data = {
        'error': "0",  # 0请求成功 1请求失败
        'messages': "注册成功",
        'id': "10086",
    }
    res = make_response(jsonify(data))  # 设置响应体
    res.status = '200'  # 设置状态码
    res.headers['Access-Control-Allow-Origin'] = "*"  # 设置允许跨域
    res.headers['Access-Control-Allow-Methods'] = 'PUT,GET,POST,DELETE'

    return res


#  修改老人信息,number:5
@app.route('/update_OldPerson', methods=['GET'])
def update_OldPerson():
    print("正在修改老人信息")
    dbManager.update_OldPerson(request.args.get('id'), request.args.get('update'))
    data = {
        'error': "0",  # 0请求成功 1请求失败
        'messages': "修改成功",
        # 'id': "22"
        # 'update': {'username': "123", 'phone': "18562052031"}
    }
    res = make_response(jsonify(data))  # 设置响应体
    res.status = '200'  # 设置状态码
    res.headers['Access-Control-Allow-Origin'] = "*"  # 设置允许跨域
    res.headers['Access-Control-Allow-Methods'] = 'PUT,GET,POST,DELETE'

    return res


#  修改义工信息,number:6
@app.route('/update_Volunteer', methods=['GET'])
def update_Volunteer():
    print("正在修改义工信息")
    dbManager.update_Volunteer(request.args.get('id'), request.args.get('update'))
    data = {
        'error': "0",  # 0请求成功 1请求失败
        'messages': "修改成功",
    }
    res = make_response(jsonify(data))  # 设置响应体
    res.status = '200'  # 设置状态码
    res.headers['Access-Control-Allow-Origin'] = "*"  # 设置允许跨域
    res.headers['Access-Control-Allow-Methods'] = 'PUT,GET,POST,DELETE'

    return res


#  修改工作人员信息,number:7
@app.route('/update_Employee', methods=['GET'])
def update_Employee():
    print("正在修改工作人员信息")
    dbManager.update_Employee(request.args.get('id'), request.args.get('update'))
    data = {
        'error': "0",  # 0请求成功 1请求失败
        'messages': "修改成功",
    }
    res = make_response(jsonify(data))  # 设置响应体
    res.status = '200'  # 设置状态码
    res.headers['Access-Control-Allow-Origin'] = "*"  # 设置允许跨域
    res.headers['Access-Control-Allow-Methods'] = 'PUT,GET,POST,DELETE'

    return res


#  删除老人信息,number:8
@app.route('/delete_OldPerson', methods=['GET'])
def delete_OldPerson():
    print("正在删除老人信息")
    dbManager.delete_OldPerson(request.args.get('id'))
    data = {
        'error': "1",  # 0请求成功 1请求失败
        'messages': "删除成功"
    }
    res = make_response(jsonify(data))  # 设置响应体
    res.status = '200'  # 设置状态码
    res.headers['Access-Control-Allow-Origin'] = "*"  # 设置允许跨域
    res.headers['Access-Control-Allow-Methods'] = 'PUT,GET,POST,DELETE'

    return res


#  删除义工信息,number:9
@app.route('/delete_Volunteer', methods=['GET'])
def delete_Volunteer():
    print("正在删除义工信息")
    dbManager.delete_Volunteer(request.args.get('id'))
    data = {
        'error': "1",  # 0请求成功 1请求失败
        'messages': "删除成功"
    }
    res = make_response(jsonify(data))  # 设置响应体
    res.status = '200'  # 设置状态码
    res.headers['Access-Control-Allow-Origin'] = "*"  # 设置允许跨域
    res.headers['Access-Control-Allow-Methods'] = 'PUT,GET,POST,DELETE'

    return res


#  删除工作人员信息,number:10
@app.route('/delete_Employee', methods=['GET'])
def delete_Employee():
    print("正在删除工作人员信息")
    dbManager.delete_Employee(request.args.get('id'))
    data = {
        'error': "1",  # 0请求成功 1请求失败
        'messages': "删除成功"
    }
    res = make_response(jsonify(data))  # 设置响应体
    res.status = '200'  # 设置状态码
    res.headers['Access-Control-Allow-Origin'] = "*"  # 设置允许跨域
    res.headers['Access-Control-Allow-Methods'] = 'PUT,GET,POST,DELETE'

    return res


#  查询老人信息,number:11
@app.route('/select_OldPerson', methods=['GET'])
def select_OldPerson():
    #  获取所有老人信息并输出
    print("正在获取老人信息")
    OldPerson = dbManager.select_OldPerson()
    data = {
        'error': "0",  # 0请求成功 1请求失败
        'id': "10086",
        'data': OldPerson
    }
    res = make_response(jsonify(data))  # 设置响应体
    res.status = '200'  # 设置状态码
    res.headers['Access-Control-Allow-Origin'] = "*"  # 设置允许跨域
    res.headers['Access-Control-Allow-Methods'] = 'PUT,GET,POST,DELETE'

    return res


#  查询义工信息,number:12
@app.route('/select_Volunteer', methods=['GET'])
def select_Volunteer():
    #  获取所有义工信息并输出
    print("正在获取义工信息")
    Volunteer = dbManager.select_Volunteer()
    data = {
        'error': "1",  # 0请求成功 1请求失败
        'id': "10086",
        'data': Volunteer
    }
    res = make_response(jsonify(data))  # 设置响应体
    res.status = '200'  # 设置状态码
    res.headers['Access-Control-Allow-Origin'] = "*"  # 设置允许跨域
    res.headers['Access-Control-Allow-Methods'] = 'PUT,GET,POST,DELETE'

    return res


#  查询工作人员信息,number:13
@app.route('/select_Employee', methods=['GET'])
def select_Employee():
    #  获取所有工作人员信息并输出
    print("正在获取工作人员信息")
    Employee = dbManager.select_Employee()
    data = {
        'error': "1",  # 0请求成功 1请求失败
        'id': "10086",
        'data': Employee
    }
    res = make_response(jsonify(data))  # 设置响应体
    res.status = '200'  # 设置状态码
    res.headers['Access-Control-Allow-Origin'] = "*"  # 设置允许跨域
    res.headers['Access-Control-Allow-Methods'] = 'PUT,GET,POST,DELETE'

    return res


#  修改系统管理员信息,number:14
@app.route('/update_SysUser', methods=['GET'])
def update_SysUser():
    print("正在修改系统管理员信息")
    dbManager.update_SysUser(request.args.get('id'), request.args.get('password'), request.args.get('phone'), request.args.get('nickname'))
    data = {
        'error': "0",  # 0请求成功 1请求失败
        'messages': "修改成功",
    }
    res = make_response(jsonify(data))  # 设置响应体
    res.status = '200'  # 设置状态码
    res.headers['Access-Control-Allow-Origin'] = "*"  # 设置允许跨域
    res.headers['Access-Control-Allow-Methods'] = 'PUT,GET,POST,DELETE'

    return res


#  登录验证,number:15
@app.route('/login_SysUser', methods=['GET'])
def login_SysUser():
    print("正在验证用户登录")
    num = dbManager.get_sys_user(request.args.get('email'), request.args.get('password'))
    if num == "0":
        data = {
            'error': "1",  # 0请求成功 1请求失败
            'messages': "邮箱不存在或密码不正确",
        }
    else:
        data = {
            'error': "0",  # 0请求成功 1请求失败
            'messages': "登录成功",
            'id': num,
        }

    res = make_response(jsonify(data))  # 设置响应体
    res.status = '200'  # 设置状态码
    res.headers['Access-Control-Allow-Origin'] = "*"  # 设置允许跨域
    res.headers['Access-Control-Allow-Methods'] = 'PUT,GET,POST,DELETE'

    return res


#  查询管理员信息,number:16
@app.route('/select_SysUser', methods=['GET'])
def select_SysUser():
    print("正在查询管理员信息")
    information = dbManager.select_SysUser(request.args.get('id'))
    data = {
        'error': "0",  # 0请求成功 1请求失败
        'messages': "查询成功",
        'data': information,
    }
    res = make_response(jsonify(data))  # 设置响应体
    res.status = '200'  # 设置状态码
    res.headers['Access-Control-Allow-Origin'] = "*"  # 设置允许跨域
    res.headers['Access-Control-Allow-Methods'] = 'PUT,GET,POST,DELETE'

    # print(data)
    return res


#  网页test
@app.route('/test.html', methods=['GET'])
def test():
    return render_template("test.html")


if __name__ == '__main__':
    app.run()
