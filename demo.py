#!/usr/bin/env python
# -*- coding:utf-8 -*-
import selenium.webdriver.common.keys
from selenium import webdriver
from lxml import etree
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
    # driver.save_screenshot('ymx3.png')
    # sleep
    handles = driver.window_handles
    homeUrl = driver.current_url
    driver.find_element_by_xpath('//*[@id="twotabsearchtextbox"]').send_keys('背包')
    driver.find_element_by_xpath('//*[@id="twotabsearchtextbox"]').send_keys(selenium.webdriver.common.keys.Keys.ENTER)

    time.sleep(3)
    if driver.current_url != homeUrl:
        GotosearchPage(driver, handles)
    else:
        time.sleep(3)
        GotosearchPage(driver, handles)


def GotosearchPage(driver, handles):
    ssurl = driver.current_url
    print(ssurl)
    try:
        driver.find_element_by_xpath('//*[@id="result_0"]/div/div[3]').click()
    except :
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="result_0"]/div/div[3]').click()
    if len(driver.window_handles) > 1:
        browseGoods(driver, handles)
        driver.quit()
    else:
        try:
            driver.find_element_by_xpath('//*[@id="result_0"]/div/div[3]/div[1]/a/h2').click()
        except :
            print('被网站劫持')
            f = open('爬虫.html', 'wb')
            f.write(driver.page_source.encode('utf-8').decode('utf-8'))
            f.close()
        if len(driver.window_handles) > 1:
            browseGoods(driver, handles)
            driver.quit()
def browseGoods(driver, handles):
    time.sleep(3)
    driver.switch_to_window(handles[-1])
    time.sleep(3)
    driver.switch_to_window(handles[0])
    time.sleep(3)
    try:
        driver.find_element_by_xpath('//*[@id="result_1"]/div/div[3]').click()
    except:
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="result_1"]/div/div[3]').click()
    js = "var q=document.body.scrollTop=100000"
    driver.execute_script(js)
    time.sleep(5)
    # driver.switch_to_window(handles[-2])
    # time.sleep(3)
    f = open('爬虫.html','wb')
    f.write(driver.page_source.encode('utf-8').decode('utf-8'))
    f.close()
    driver.find_element_by_class_name('a-button-input').click()
    # time.sleep(3)
    # driver.find_element_by_xpath('//*[@id="hlb-ptc-btn-native"]').click()



if __name__ == "__main__":
    main()


