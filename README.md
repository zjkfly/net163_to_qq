# net163_to_qq
由于网易云听不到大木老师的歌了，所以我只好转移动qq音乐了。
半自动将网易云音乐的收藏的歌单导入到qq音乐

PS:需要自己抓包找到下列数据：

1.自己的QQ音乐登陆cookie
2.网易云音乐的歌单json数据
所以说是半自动化

TODO：自动化将歌单直接导入
TODO：使用代理，防止ip被封，或者多线程

## 1、如何获取歌单json数据
也可以直接通过api直接请求，不过需要构造一下请求头。
response中即为歌单的json数据
![image](https://user-images.githubusercontent.com/42086593/164384031-e579b2f5-87e0-44a0-97f9-ebd61f2a0fba.png)
## 2、qq音乐登录cookie
登录qq音乐后，打开浏览器抓包工具，查看cookie和
在请求头中也可以获取到，保存一下。
![image](https://user-images.githubusercontent.com/42086593/164384944-a7cfe8b1-da3c-4ab1-b2da-6a1c53ce5a40.png)
随便点击一首歌，抓取收藏的请求，保存字段gtk与uin(应该是qq号)，最后在代码中修改对应字段即可
![image](https://user-images.githubusercontent.com/42086593/164385095-35ad0d6c-dd41-4a1c-b0a9-acaf200d5f6c.png)
