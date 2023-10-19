import time
import requests
import re
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

print("当前程序只针对于【湖南软件职业技术大学】校园网自动化PC端登入操作 -----> IP：10.199.199.199")
header = {
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"
}
try:
    url_get = requests.get("http://10.199.199.199", headers=header)
    get_hunan_soft_campus_network_code = url_get.text
except:
    print("当前接入的WLAN不在校园局域网之内，请连接【湖南软件职业技术大学】校园局域网！")
    time.sleep(5)
    exit()

class Campus_Network():
    def __init__(self):
        # 加载opr_conf配置文件
        print("导导入config配置文件...")
        with open("./apo_config.conf") as open_config_file:
            self.apo_config_data = eval(open_config_file.read())
        self.accounts  = self.apo_config_data["account"]
        self.passwords = self.apo_config_data["password"]
        self.operators = self.apo_config_data["operator"]


        print("[*]正在打开浏览器...")
        self.open_web = webdriver.Chrome()
        time.sleep(1)
        print("[*]正在加载网页...")
        time.sleep(1)
        self.open_web.get("http://10.199.199.199")
    def logout_campus_network_code(self):
        self.open_web.find_element(By.XPATH,'//*[@id="edit_body"]/div[1]/div[1]/form/input').click()
        select_logout = input("[+]请确认是否需要注销（Y/N）：")
        if (select_logout == 'Y') or (select_logout == 'y'):
            print("[*]您已执行注销操作...")
            self.open_web.find_element(By.XPATH,'//*[@id="layui-layer1"]/div[3]/a[1]').click()
            time.sleep(1)
            self.open_web.find_element(By.XPATH,'//*[@id="edit_body"]/div[1]/div[1]/form/input').click()
            time.sleep(1)
            self.login_campus_network()
            self.open_web.quit()
        else:
            print("[*]您已取消注销操作...")
            self.open_web.find_element(By.XPATH,'//*[@id="layui-layer1"]/div[3]/a[2]').click()
            time.sleep(1)
    def login_campus_network(self):
        print("[*]正在输入账号...")
        self.open_web.find_element(By.XPATH,'//*[@id="edit_body"]/div[2]/div[2]/form/input[2]').send_keys(self.accounts) # input account
        time.sleep(1)
        print("[*]正在输入密码...")
        self.open_web.find_element(By.XPATH,'//*[@id="edit_body"]/div[2]/div[2]/form/input[3]').send_keys(self.passwords) # input password
        time.sleep(1)
        print("[*]正在选择通信运营商...")
        # 0：空 1：校园网 2：中国电信 3：中国联通 4：中国移动
        selects = Select(self.open_web.find_element(By.XPATH,'//*[@id="edit_body"]/div[2]/div[2]/select'))
        selects.select_by_index(self.operators) # select operator
        time.sleep(1)
        print("[*]所有选项设置已就绪，正在前往确认...")
        self.open_web.find_element(By.XPATH,'//*[@id="edit_body"]/div[2]/div[2]/form/input[1]').click()
        time.sleep(1)
        login_title = self.open_web.title
        print(login_title)
        if login_title == "登录成功页":
            print("[+]登入成功！")
        else:
            print("[-]登陆失败！请确保apo_config配置文件已正确配置！")
        self.open_web.quit()
def main():
    campus_network = Campus_Network()
    campus_network_title = re.findall("<title>(.*?)</title>",get_hunan_soft_campus_network_code)[0]
    if campus_network_title == "注销页":
        print("[+]检测到页面已登入，执行注销操作...")
        campus_network.logout_campus_network_code()

    elif campus_network_title == "上网登录页":
        print("[+]检测到页面未登入，执行登入操作...")
        campus_network.login_campus_network()
    else:
        print(f"[-]当前页面title：{campus_network_title}，系统暂未添加此页面对应的自动化操作代码，如对此页面的功能有疑问可以联系管理员添加对应的功能操作！")

if __name__ == '__main__':
    main()