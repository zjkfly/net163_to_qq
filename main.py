# -*- coding: UTF-8 -*-

import json
import requests
import time

# 请修改成为自己的请求头中的信息
g_tk = "863981763"
uin = "995700257"
cookie = ""


def get_id_qq(music_name):
    url = 'https://c.y.qq.com/splcloud/fcgi-bin/smartbox_new.fcg?is_xml=0&format=jsonp&key=' + music_name + '&g_tk=' + g_tk + '&jsonpCallback=SmartboxKeysCallbackmod_top_search4053&loginUin='+ uin + '&hostUin=0&format=jsonp&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq&needNewCode=0'
    r = requests.get(url)
    rr = r.text.replace('(', '')
    rr = rr.replace(')', '')
    r_1 = rr.split('search4053')
    if len(r_1) == 0:
        r_4 = json.loads(rr)
        return r_4

    str1 = str(r_1[1])
    r_2 = str1
    print(r_2)
    r_3 = json.loads(r_2)
    return r_3


def music_add(midlist):
    url = 'https://c.y.qq.com/splcloud/fcgi-bin/fcg_music_add2songdir.fcg?g_tk=' + g_tk
    headers = {'cookie': cookie}
    post_data = {'loginUin': uin,
                 'hostUin': '0',
                 'format': 'json',
                 'inCharset': 'utf8',
                 'outCharset': 'utf-8',
                 'notice': '0',
                 'platform': 'yqq.post',
                 'needNewCode': '0',
                 'uin': uin,
                 'midlist': midlist,
                 'typelist': '13',
                 'dirid': '201',
                 'addtype': '',
                 'formsender': '4',
                 'source': '153',
                 'r2': '0',
                 'r3': '1',
                 'utf8': '1',
                 'g_tk': g_tk
                 }
    r = requests.post(url, data=post_data, headers=headers)
    print(r.text)


def transfer_music(json_url):
    # 从网易云音乐返回的json格式中获取我喜欢的音乐
    filename = json_url
    f = open(filename, 'r', encoding="utf-8")
    fp = f.read()
    f.close()
    json_list = json.loads(fp)

    # 获取我喜欢歌曲的名称和作者名
    my_love_music_name = []
    my_love_music_author = []

    for i in range(len(json_list['playlist']['tracks'])):
        my_love_music_name.append(json_list['playlist']['tracks'][i]['name'])
        my_love_music_author.append(json_list['playlist']['tracks'][i]['ar'][0]['name'])

    for j in range(0, len(my_love_music_name)):
        print(j)
        time.sleep(5)
        print("正在添加歌曲：" + my_love_music_name[j])
        count = 0
        # 将获取到的歌曲名放到qq音乐里面进行搜索（双重匹配搜索）
        music = get_id_qq(my_love_music_name[j])
        print(music)
        music_1 = []
        try:
            music_1 = music["data"]["song"]["itemlist"]
            for i in range(len(music_1)):
                print(music_1[i]['mid'], music_1[i]['name'], music_1[i]['singer'])

                if my_love_music_author[j] == music_1[i]['singer']:
                    music_add(music_1[i]['mid'])
                    count = 1

            if count == 0:
                music_add(music_1[0]['mid'])
        except:
            f1 = open('test.txt', 'a', encoding="utf-8")
            name1 = str(my_love_music_name[j]) + '\n编号为：' + str(j)
            f1.write(name1)
            f1.close()


if __name__ == "__main__":
    # 此处为你抓取的网易云喜欢的歌曲列表json
    transfer_music("json.txt")
