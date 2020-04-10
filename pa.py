#-*-  coding:utf-8 -*-
import tkinter as tk
from tkinter import ttk
from selenium import webdriver
import time
import pyperclip
import os
import threading
from tkinter.messagebox import askyesno
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException




def thread_it(func, *args):
    '''将函数打包进线程'''
    # 创建
    t = threading.Thread(target=func, args=args)
    # 守护 !!!
    t.setDaemon(True)
    # 启动
    t.start()
    # 阻塞--卡死界面！



# 封装一个函数，用来判断属性值是否存在
def isElementPresent(by, value):
        """
        用来判断元素标签是否存在，
        """
        try:
            element = driver.find_element(by=by, value=value)
        # 原文是except NoSuchElementException, e:
        except NoSuchElementException as e:
            # 发生了NoSuchElementException异常，说明页面中未找到该元素，返回False
            return False
        else:
            # 没有发生异常，表示在页面中找到了该元素，返回True
            return True


# 复制
def copy(i):
    '''
    复制boss的马
    :param i: boss的ID 具体看boss顺序.txt文件
    :return:
    '''
    global t
    global pre_boss


    if isElementPresent(By.XPATH, "/html/body/div/div[2]/div[3]/div[1]/div/div[2]/ul"):
        # 打开选择界面
        js = 'document.querySelector("body > div > div.gbfrf-main-content > div.gbfrf-settings-fab__container > button").click();'
        driver.execute_script(js)
        time.sleep(1.5)

        # 选择Boss
        js = 'document.querySelector("#gbfrf-dialog__follow > ul > li:nth-child(%s)").click();' % pre_boss
        driver.execute_script(js)
        time.sleep(1.5)

        # 关闭选择界面
        js = 'document.querySelector("body > div > dialog:nth-child(2) > div > div > div > button:nth-child(1)").click();'
        driver.execute_script(js)
        time.sleep(1.5)


    # 打开选择界面
    js = 'document.querySelector("body > div > div.gbfrf-main-content > div.gbfrf-settings-fab__container > button").click();'
    driver.execute_script(js)
    time.sleep(1.5)

    # 选择Boss
    js = 'document.querySelector("#gbfrf-dialog__follow > ul > li:nth-child(%s)").click();' %i
    driver.execute_script(js)
    time.sleep(1.5)

    pre_boss = i

    # 关闭选择界面
    js = 'document.querySelector("body > div > dialog:nth-child(2) > div > div > div > button:nth-child(1)").click();'
    driver.execute_script(js)
    time.sleep(1.5)

    ul = driver.find_element_by_xpath('/html/body/div/div[2]/div[3]/div[1]/div/div[2]/ul')
    lis = ul.find_elements_by_xpath('li')
    while(flag):
        lis = ul.find_elements_by_xpath('li')
        t0 = (lis[0].text)[-8:]
        if(t == t0):
            time.sleep(0.5)
            continue
        if(t!=t0):
            t = t0
            var1.set("已复制:"+t)
            pyperclip.copy(t)
            continue
    return


# 得到Boss的ID并保存至boss顺序.txt
def get_boss_name():
    if os.path.exists("boss顺序.txt"):
        os.remove("boss顺序.txt")

    # 打开boss选择
    js = 'document.querySelector("body > div > div.gbfrf-main-content > div.gbfrf-settings-fab__container > button").click();'
    driver.execute_script(js)
    time.sleep(1.5)

    while not isElementPresent(By.XPATH,'/html/body/div/dialog[1]/div/div/section[1]/ul'):
        # 关闭选择界面
        js = 'document.querySelector("body > div > dialog:nth-child(2) > div > div > div > button:nth-child(1)").click();'
        driver.execute_script(js)
        time.sleep(1.5)

        # 打开boss选择
        js = 'document.querySelector("body > div > div.gbfrf-main-content > div.gbfrf-settings-fab__container > button").click();'
        driver.execute_script(js)
        time.sleep(1.5)

    ul = driver.find_element_by_xpath('/html/body/div/dialog[1]/div/div/section[1]/ul')
    lis = ul.find_elements_by_xpath('li')
    lisl = len(lis)  # boss数量
    for i in range(1, lisl + 1):
        f = open('boss顺序.txt', 'a', encoding='utf-8')
        name = driver.find_element_by_xpath('/html/body/div/dialog[1]/div/div/section[1]/ul/li[%s]/span/span[1]' % i)
        f.write(str(i) + ":" + name.text + "\n")
    f.close()

def btn1():
    var1.set('正在获取')
    time.sleep(0.5)
    get_boss_name()
    fo = open('boss顺序.txt', 'r', encoding='utf-8')
    for line in fo.readlines():
        line = line.strip()
        if line !='\n':
            boss_lis.append(line)
    fo.close()
    lb['value'] = boss_lis
    var1.set('获取完成')

def btn2():
    global flag
    flag = True
    var1.set("正在复制")
    copy(boss)

def btn3():
    global flag
    flag = False


def lbb(event): # 下拉事件
    global boss
    global flag
    flag = False
    boss = lb.current() + 1
    var1.set(lb.get())


# 退出事件
def close():
    ans = askyesno(title='警告', message='确定退出?')
    if ans:
        driver.quit()
        window.destroy()
    else:
        return


if __name__ == '__main__':
    window = tk.Tk()
    window.title('舔舔表网')
    window.geometry('500x300')
    canvas = tk.Canvas(window, bg='LightCyan', height=3000, width=5000)
    canvas.pack()
    var1 = tk.StringVar()  # 将label标签的内容设置为字符类型，用var来接收hit_me函数的传出内容用以显示在标签上
    l1 = tk.Label(window, textvariable=var1, bg='LightYellow', fg='DarkSeaGreen', font=('microsoft yahei', 11), width=30, height=2)
    l1.place(relx=0.35, rely=0.8)
    l2 = tk.Label(window, text='状态:', bg='LightYellow', fg='DarkGreen', font=('microsoft yahei', 11), width=10, height=2)
    l2.place(relx=0.1, rely=0.8)
    b1 = tk.Button(window, text='获取boss列表', bg='LightYellow', fg='DarkGreen', font=('microsoft yahei', 11), width=10, height=2, command=lambda :thread_it(btn1))
    b1.place(relx=0.1, rely=0.1)
    b2 = tk.Button(window, text='开始复制', bg='LightYellow', fg='DarkGreen', font=('microsoft yahei', 11), width=10, height=2, command=lambda :thread_it(btn2))
    b2.place(relx=0.1, rely=0.5)
    b3 = tk.Button(window, text='停止', bg='LightYellow', fg='DarkGreen', font=('microsoft yahei', 11), width=10,
                   height=2, command=lambda: thread_it(btn3))
    b3.place(relx=0.4, rely=0.5)
    lb = ttk.Combobox(window, font=('microsoft yahei', 11))
    lb.place(relx=0.4,rely=0.1)
    lb.bind("<<ComboboxSelected>>", lbb)

    flag = True
    boss_lis = []
    boss = 1
    pre_boss = 1
    t = ''

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(executable_path='./chromedriver.exe', options=chrome_options)
    driver.get("https://gbf-tbw.tk/")

    try:
        WebDriverWait(driver, 10, 0.5).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div/div[2]/div[2]/button")))
    except Exception as e:
        var1.set("无法连接到网站，请重试")

    time.sleep(1)

    window.protocol('WM_DELETE_WINDOW', close)
    window.mainloop()
