# author:  freelaeder
# ----
# date:  2022/4/18 16:08


import PySimpleGUI as sg

# 练习python图形化
# 1定义布局
layout = [
    [sg.Text('请输入您的信息')],
    [sg.Text('姓名', enable_events=True), sg.InputText('freelaeder')],
    [sg.Text('性别'), sg.InputText('男')],
    [sg.Text('国籍'), sg.InputText('汉')],
    [sg.Button('确定'), sg.Button('取消')],
    [sg.Button('确定1'), sg.Button('1取消')],
]

# 2创建窗口
# 注意sg 后面的第一个单词都要大写
# 前面是窗口的标题，后面是布局
window = sg.Window('Python GUI', layout)

# 3事件循环
while True:
    # 窗口的读取，有两个返回值，1事件 2 值
    event, values = window.read()

    if event == None:
        # 等于空关闭
        break
    # if event in ('确定', '取消'):
    #     # 两个事件执行一个方法
    #     sg.Popup('您点击了确定或取消')

    if event.startswith('确定'):
        # 以什么开头
        sg.Popup('执行确定')
    if event.endswith('取消'):
        # 以什么结尾
        sg.Popup('取消')
    if event == '姓名':
        sg.Popup('只是一个姓名')
        print(values)

# 窗口关闭
window.close()
