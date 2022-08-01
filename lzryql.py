# @Time : 2022/8/1 14:37 
# @Author : yaochengshimao
# @File : lzryql.py 
# @Software: PyCharm
import requests


def login(url, username, password):
    data = {
        "username": username,
        "passowrd": password,
    }
    rep = requests.post(url, data=data)
    return rep.cookies


def delete_resigned_employees(id, cookie, url):
    """
    批量删除离职人员账号
    :param id: 工号
    :param cookie:cookie
    :param url: 域名
    :return:
    """
    url = url + "/v1/api/deleteUser"
    headers = {
        "cookie": cookie,
    }
    data = {
        "userId": id,
    }
    rep = requests.post(url, data=data, headers=headers)
    if rep.json()['result']:
        print("delete user:{id} success".format(id))
    else:
        print(rep)


if __name__ == "__main__":
    url = "http://login.100.me/"
    username = "manager"
    password = "!qaz@wsx#edc"
    cookie = login(url, password, username)
    with open(file="resigned.txt", mode="r", encoding="utf-8") as f_r:
        for userid in f_r.readlines():
            delete_resigned_employees(userid, cookie, url)
