# -*- coding: UTF-8 -*-

import json
import requests
import time

def get_id_qq(music_name):
    url = 'https://c.y.qq.com/splcloud/fcgi-bin/smartbox_new.fcg?is_xml=0&format=jsonp&key='+music_name+'&g_tk=936441715&jsonpCallback=SmartboxKeysCallbackmod_top_search4053&loginUin=1562597324&hostUin=0&format=jsonp&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq&needNewCode=0'
    r = requests.get(url)
    rr = r.text.replace('(','')
    rr = rr.replace(')', '')
    r_1 = rr.split('search4053')
    if len(r_1) ==0:
        r_4 = json.loads(rr)
        return r_4

    str1 = str(r_1[1])
    r_2 = str1
    print(r_2)
    r_3 = json.loads(r_2)
    return r_3

def music_add(midlist):
    url = 'https://c.y.qq.com/splcloud/fcgi-bin/fcg_music_add2songdir.fcg?g_tk=936441715'
    headers = {'cookie':'pvid=9564822718; __v3_c_review_10685=0; __v3_c_last_10685=1459745716973; __v3_c_visitor=1459745716973534; pac_uid=1_1562597324; has_show_ilike=1; tvfe_boss_uuid=38e25911faf4a558; 3g_guest_id=-8978160799759388672; mobileUV=1_158188b7162_1a81b; RK=CyMLDiFqVf; ue_uid=14cf68ddb38005fe02324c30622b2133; ue_ts=1494133034; ue_uk=511b1152477bffccb3e236f1c4293532; ue_skey=acec8cf35d30c11038a931b52ef84ee3; LW_pid=0edb7fa02714a643cf62a4cf5ce73198; pgv_pvi=7176894464; AMCV_248F210755B762187F000101%40AdobeOrg=-1891778711%7CMCIDTS%7C17539%7CMCMID%7C37857052962717579937408224126560698741%7CMCAID%7CNONE%7CMCAAMLH-1515940194%7C11%7CMCAAMB-1515940194%7Cj8Odv6LonN4r3an7LhD3WZrU1bUpAkFkkiY1ncBR96t2PTI%7CMCOPTOUT-1515342594s%7CNONE%7CMCSYNCSOP%7C411-17546%7CvVersion%7C2.4.0; eas_sid=61N5a1p9p9v1P2X9e9K6C0q6o0; LW_uid=01D5R2T38061S6G4P2T2N0d5D8; yq_index=0; pgv_pvid_new=1562597324_66213c9d44; ts_uid=3193114520; ptui_loginuin=1442444640; o_cookie=1562597324; pgv_pvid=415086728; ptcz=c46738997a735227c3082985b597ef36710504decd7d109efb70eb107dc96150; pt2gguin=o1562597324; LW_sid=R115s2D5c107H037R0O5e1d3r8; pgv_info=ssid=s3715153302; uid=248716326; _qpsvr_localtk=0.7684892966204999; ptisp=cnc; pgv_si=s4844869632; uin=o1562597324; skey=@22VL5yCzl; luin=o1562597324; lskey=0001000019054592a3c987cda569fd7ca07e1f79fc7a63112b0fcb01c3dd59f7d68be0e683c045b0f6d4f79e; p_uin=o1562597324; pt4_token=cn4oBP-yfJcPEzK-8Ov6cQo4IBIgq-COGJObCZUgQDk_; p_skey=8dpAOtfsAKBhQcS5*0iqcfdiUFxnf2YGVYJNzti5Dok_; p_luin=o1562597324; p_lskey=000400002580651ba13725fef92c549a69176a2f2f66c95730f23959ea83cca240682bc65a67147a500182ee; SL_GWPT_Show_Hide_tmp=1; SL_wptGlobTipTmp=1; ts_refer=www.baidu.com/link; yplayer_open=1; yq_playschange=1; yq_playdata=s_0_1_; player_exist=0; yqq_stat=0; ts_last=y.qq.com/n/yqq/song/00467LeA1TSU69.html'}
    post_data = {'loginUin': '1562597324',
'hostUin': '0',
'format': 'json',
'inCharset': 'utf8',
'outCharset': 'utf-8',
'notice': '0',
'platform': 'yqq.post',
'needNewCode': '0',
'uin': '1562597324',
'midlist': midlist,
'typelist': '13',
'dirid': '201',
'addtype':'' ,
'formsender': '4',
'source': '153',
'r2': '0',
'r3': '1',
'utf8': '1',
'g_tk': '936441715'}
    r =requests.post(url,data=post_data,headers = headers)
    print(r.text)







#从网易云音乐返回的json格式中获取我喜欢的音乐
filename= '1.txt'
f = open(filename,'r')
fp = f.read()
f.close()
json_list=json.loads(fp)

#获取我喜欢歌曲的名称和作者名
my_love_music_name = []
my_love_music_author = []

for i in range(len(json_list['playlist']['tracks'])):
    my_love_music_name.append(json_list['playlist']['tracks'][i]['name'])
    my_love_music_author.append(json_list['playlist']['tracks'][i]['ar'][0]['name'])





for j in range(271,len(my_love_music_name)):
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
            print(music_1[i]['mid'],music_1[i]['name'],music_1[i]['singer'])

            if my_love_music_author[j] == music_1[i]['singer']:
                music_add(music_1[i]['mid'])
                count = 1

        if count == 0:
            music_add(music_1[0]['mid'])

    except:
        f1 = open('test.txt','a')
        name1 = str(my_love_music_name[j])+'\n编号为：'+str(j)
        f1.write(name1)
        f1.close()
