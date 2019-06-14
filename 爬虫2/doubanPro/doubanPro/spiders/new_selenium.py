from selenium import webdriver
from time import sleep

def get_url(bro,path):
    bro.get('https://accounts.douban.com/passport/login')

    first_button = bro.find_element_by_xpath('//*[@id="account"]/div[2]/div[2]/div/div[1]/ul[1]/li[2]')
    first_button.click()
    sleep(2)

    text = bro.find_element_by_id('username')
    text.send_keys('15226208396')

    password = bro.find_element_by_id('password')
    password.send_keys('hao123tanpeng')

    sleep(5)

    button = bro.find_element_by_xpath('//*[@id="account"]/div[2]/div[2]/div/div[2]/div[1]/div[4]/a')
    button.click()

    sleep(5)
    return bro.page_source


