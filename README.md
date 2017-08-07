# ReSpeaker-Switcher

ReSpeaker 2-Mic Pi HAT 的麦克风开关。使用开发板上的按钮开关麦克风。

## 安装

``` sh
pip install -r requirements.txt
```

## 使用

``` sh
python switcher.py
```

## 与叮当一同开机启动

要与叮当一同开机启动，可以参考叮当 [设置开机启动](https://github.com/wzpan/dingdang-robot/wiki/configuration#设置开机启动) ，在 dingdang.sh 中添加如下命令：

``` sh
python respeaker-switcher/switcher.py &
``` 
