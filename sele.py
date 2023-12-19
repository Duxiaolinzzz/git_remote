#导包
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
#获取浏览器驱动
driver = webdriver.Chrome()
#获取url
url=r'E:\python\test_env\注册A.html'
driver.get(url)
#使用link.text找到新浪网址
driver.find_element(By.LINK_TEXT,'访问 新浪 网站').click()
# driver.find_element('link_text',"访问 新浪 网站").click()
#暂停三秒
sleep(3)
#退出
driver.quit()