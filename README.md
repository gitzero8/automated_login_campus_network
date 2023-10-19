# automated_login_campus_network
针对校园网的自动化登录
==================================================================
本脚本使用开源开放
==================================================================
1.当前程序只针对于【湖南软件职业技术大学】校园网自动化PC端登入操作
	操作IP：10.199.199.199
2.在使用之前请确保有python运行环境，以及程序所使用的模块（包含：selenium,requests,re,time）。
3.请确保在安装了selenium之后已经将对应的浏览器驱动配置文件放在在python安装目录下,这里我已提供了【chromedriver.exe】该版本是（谷歌浏览器118.0.5993.70/79）版本驱动，只需将此驱动放置python安装根目录下即可，自己相对应的浏览器自行下载对应版本的driver驱动程序
	提供chrome对应的驱动版本下载地址：
					114及之前的版本下载地址：https://chromedriver.storage.googleapis.com/index.html
					117/118/119版本下载地址：https://googlechromelabs.github.io/chrome-for-testing/#stable
4.在使用本程序之前请确保apo【apo_config.conf】文件已正确配置！
	apo_config.conf文件内容的配置格式：
	{
		"account" : "【这里填写校园网账号】",
		"password" : "【这里填写校园网登录密码】",
		"operator" : 【这里填写校园网运营商的下拉select选择序号】 
		注：下拉菜单select选择序号对应内容：# 0：空 1：校园网 2：中国电信 3：中国联通 4：中国移动
	}
5.所有配置完成之后，双击【automated_login_campus_network.py】启动脚本。
