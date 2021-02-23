# copy-translate


## 功能

实现能在电脑上读取复制到剪切板的内容并翻译后弹窗的Python语言的脚本


## 获取

[到该页面下载或直接克隆本仓库](https://github.com/sposer/copy-translate/releases/tag/1.0)


## 使用

1. 第一次运行`exe`文件或入口脚本`Start.py`会在当前目录生成一个`config.txt`配置文件，删除该文件下次运行会重新生成
2. 在窗口上鼠标右键长按可以拖动窗口，松开后会记录位置，分别是`win_x`和`win_y`
3. 鼠标左键可以选择文字后复制（显示时间内），双击左键可以提前关闭悬浮窗
4. 显示时间默认为`3s`，可以通过修改`win_showTime`来设置
5. `time_interval`决定读取剪切板的间隔，默认`0.2s`一次
6. `win_alpha`为窗口透明度，范围`0~1`