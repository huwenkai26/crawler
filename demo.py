#!/usr/bin/env python
# -*- coding:utf-8 -*-
import selenium.webdriver.common.keys
from selenium import webdriver
from lxml import etree
import time
def sun():
    driver = webdriver.Chrome()
    driver.get("https://www.amazon.cn/")
    etreehtml = etree.HTML(driver.page_source)
    link = etreehtml.xpath('//*[@id="nav-tools"]/a/@href')[0]
    link3 = etreehtml.xpath('//*[@id="nav-tools"]/a/@href')[2]
    linkurl = 'https://www.amazon.cn/'+link
    linkurl3 = 'https://www.amazon.cn/'+link3
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
    driver.find_element_by_xpath('//*[@id="twotabsearchtextbox"]').send_keys('手套')
    driver.find_element_by_xpath('//*[@id="twotabsearchtextbox"]').send_keys(selenium.webdriver.common.keys.Keys.ENTER)

    time.sleep(3)
    if driver.current_url != homeUrl:
        GotosearchPage(driver, handles,linkurl3)
    else:
        time.sleep(3)
        GotosearchPage(driver, handles,linkurl3)


def GotosearchPage(driver, handles,linkurl3):
    ssurl = driver.current_url
    print(ssurl)
    try:
        driver.find_element_by_xpath('//*[@id="result_0"]/div/div[2]/div/div/a/img').click()
    except :
        time.sleep(3)
        driver.find_element_by_class_name('a-link-normal a-text-normal').click()
    if len(driver.window_handles) > 1:
        browseGoods(driver, handles,linkurl3)
        driver.quit()
    else:
        try:
            driver.find_element_by_xpath('//*[@id="result_0"]/div/div[2]/div/div/a/img').click()
        except :
            driver.find_element_by_xpath('//*[@id="result_0"]/div/div[2]/div/div/a/img').click()
            print('haha')
        if len(driver.window_handles) > 1:
            browseGoods(driver, handles,linkurl3)
            driver.quit()
def browseGoods(driver, handles,linkurl3):
    time.sleep(3)
    driver.switch_to_window(handles[-1])
    time.sleep(3)
    driver.switch_to_window(handles[0])
    time.sleep(3)
    try:
        driver.find_element_by_xpath('//*[@id="result_1"]/div/div[2]').click()
    except:
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="result_1"]/div/div[2]').click()
    js = "var q=document.body.scrollTop=100000"
    driver.execute_script(js)
    time.sleep(5)
    # driver.switch_to_window(handles[-2])
    # time.sleep(3)

    driver.find_element_by_class_name('a-button-input').click()
    time.sleep(10)
    # driver.find_element_by_xpath('//*[@id="hlb-ptc-btn-native"]').click()

    f = open('爬虫.html', 'wb')
    f.write(driver.page_source.encode('utf-8'))
    f.close()

    # try:
    #     driver.find_element_by_partial_link_text('https://www.amazon.cn/gp/cart/view.html/ref=lh_co_dup?ie=UTF8&proceedToCheckout').click()
    #     print('1')
    # except:
    #     try:
    #         driver.find_element_by_xpath('//*[@id="a-page"]/div/div[2]/div[2]')
    #         print('2')
    #     except:
    #         driver.find_element_by_partial_link_text()
    #         print('3')
    driver.switch_to_window(handles[0])
    driver.implicitly_wait(30)
    driver.get(linkurl3)
    driver.implicitly_wait(30)
    driver.find_element_by_xpath('//*[@id="sc-buy-box-ptc-button"]/span/input').click()
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="address-book-entry-0"]/div[2]/span').click()
    time.sleep(3)
    # 继续
    driver.find_element_by_xpath('//*[@id="shippingOptionFormId"]/div[1]/div[2]/div/span[1]/span/input').click()
#     输入持卡人姓名
    driver.find_element_by_xpath('//*[@id="ccName"]').send_keys("huwenkai")
    driver.find_element_by_xpath('//*[@id="addCreditCardNumber"]').send_keys('123456789')


sun()


