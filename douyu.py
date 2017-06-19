#!/usr/bin/env python
# -*- coding:utf-8 -*-
from selenium import webdriver
from lxml import etree
import json
from selenium.webdriver.common.action_chains import ActionChains #引入ActionChains鼠标操作类
from selenium.webdriver.common.keys import Keys #引入keys类操作
import time

def main():
    driver = webdriver.Chrome()
    driver.get("https://www.amazon.cn/")
    etreehtml = etree.HTML(driver.page_source)
    link = etreehtml.xpath('//*[@id="nav-tools"]/a/@href')[0]
    linkurl = 'https://www.amazon.cn/'+link
    driver.get(linkurl)
    driver.save_screenshot('ymx1.png')

    driver.find_element_by_xpath('//*[@id="ap_email"]').send_keys('15302652916')
    driver.find_element_by_xpath('//*[@id="ap_password"]').send_keys('wen951219')
    driver.find_element_by_xpath('//*[@id="a-page"]/div[1]/div[3]/div/div/form/div/div/div/div[3]/div/div/label/div/label/input').click()
    driver.find_element_by_xpath('//*[@id="signInSubmit"]').click()

    time.sleep(3)
    # f = open('爬虫.html','w')
    # f.write(driver.page_source)
    # f.close()
    # driver.find_element_by_xpath('//*[@id="ap_error_return_home"]/p/a/span').click()
    driver.save_screenshot('ymx3.png')





if __name__ == "__main__":
    main()


