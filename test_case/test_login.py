#import Actions as Actions
from smtpd import Options
from telnetlib import EC
from tkinter import Image

from selenium import webdriver
import  unittest,time
from time import sleep
import os
import time
from selenium.webdriver.common import action_chains
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class Test_login(unittest.TestCase):
    u"""登录"""
    driver = webdriver.Chrome()
    #driver = webdriver.Firefox()



    def setUp(self):
        dr = self.driver
        dr.get("http://t.yqboom.com")
        dr.maximize_window()

    def test_regis(self):
        u"""使用账号密码登录查看能否正常登录"""
        dr = self.driver
        # 点击登录试用
        dr.find_element_by_xpath('/html/body/div/div/button').click()
        sleep(2)
        # 点击账号登录
        dr.find_element_by_xpath('/html/body/div/div/div[1]/div/ul/li[4]').click()
        sleep(2)
        # 输入账号名称
        dr.find_element_by_xpath('//*[@id="normal_login_account"]').send_keys('test')
        sleep(1)
        # 输入密码
        dr.find_element_by_xpath('//*[@id="normal_login_password"]').send_keys('123456')
        sleep(1)
        # 点击登录提交
        dr.find_element_by_xpath('/html/body/div/div/div[1]/div/div[2]/form/div[3]/button').click()
        sleep(10)
            #点击数据大屏，使用鼠标键盘事件
        cs = dr.find_element_by_class_name('menu_span')
        ActionChains(dr).move_to_element(cs).perform()
            #点击自建方案,使用了父级定位和鼠标键盘事件
        sleep(20)
        temp = dr.find_element_by_xpath("//ul[@class='programme_list programme_list_dom']/li")
        action = action_chains.ActionChains(dr)
        action.move_to_element(temp)
        action.click()
        action.perform()
        sleep(15)
        # #点击方案
        tmp = dr.find_element_by_xpath('/html/body/div[1]/div[2]/div[3]/span[1]/ul/li[1]/ul/div[1]/li[2]/div/span[1]')
        action = action_chains.ActionChains(dr)
        action.move_to_element(tmp)
        action.click()
        action.perform()
        sleep(10)

        dr.save_screenshot('D:\zhangtest_framework\screenshot/pri1ntq.png')
    #     #dr.get_screenshot_as_file('D:\zhangtest_framework\screenshot/wcc.png')
    #
    #     # 通过try抛出异常进行断言判断
    #     #生成年月日时分秒时间
    #     # picture_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    #     # print(picture_time)
    #     # try:
    #     #     url = dr.save_screenshot('D:\\Test_framework\\screenshot\\' + picture_time + '.png')
    #     #     print("%s ：截图成功！！！" % url)
    #     #
    #     # except BaseException as pic_msg:
    #     #     print("截图失败：%s" % pic_msg)

    def tearDown(self):
         self.driver.quit()


if __name__ == "__main__":
    unittest.main()