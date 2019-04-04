# -*- coding:utf-8 -*-
# author: lyl

menu_dict = {
    "主菜单1": {
        "son1": "菜单1",
        "son2": "菜单2",
        "son3": "菜单3"
    },
    "主菜单2": {
        "son1": "菜单1",
        "son2": "菜单2",
        "son3": "菜单3"
    },
    "主菜单3": {
        "son1": "菜单1",
        "son2": "菜单2",
        "son3": "菜单3"
    }
}


for i in menu_dict:
    print(i)
    for n in menu_dict[i]:
        print(menu_dict[i][n])
