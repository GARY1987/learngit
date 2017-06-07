#!/usr/bin/python
#coding:utf-8
from selenium import webdriver

#下面填入京东的用户名以及密码
jd_up={"ue":"123","pd":"123"}
chrome=webdriver.Chrome(r"C:\Program Files (x86)\Google\Chrome\Application\chromedriver")
chrome.get(url="https://passport.jd.com/new/login.aspx?")
chrome.find_element_by_xpath("//*[@id=\"content\"]/div/div[1]/div/div[2]/a").click()
User=chrome.find_element_by_id("loginname")
User.clear()
User.send_keys(jd_up["ue"])
Passwd=chrome.find_element_by_id("nloginpwd")
Passwd.clear()
Passwd.send_keys(jd_up["pd"])
chrome.find_element_by_id("loginsubmit").click()
while True:
    try:
        chrome.get(url="https://item.jd.com/4099139.html")
        chrome.find_element_by_id("choose-btn-ko").click()
        chrome.find_element_by_id("order-submit").click()
        print("\033[32m抢购成功并且已下单！！\033[0m")
        chrome.quit()
    except Exception:
        print("\033[31m还未开始抢购！！\033[0m")