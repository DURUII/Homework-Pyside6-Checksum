# 流程
1. CHECKSUM
	- [x] 搭建链路-网络-传输层级框架
	-	[x] 确定基于key2bit, key2val, key2dec的模式逐层解析
	- [x] 搭建数据流切分/解读/格式化函数➡️~很笨拙、很繁琐~
		- [x] 支持多进制输入，二进制解析，最后十六进制存储
	- [x] 实现各层key2bit, key2val, key2dec
		- [x] 实现 `Ethernet II` 解析
		- [x] 实现 `IPv4` 解析
		- [x] 实现 `TCP/UDP` 解析
	- [x] 搭建数据流校验函数
		- [x] 支持多进制输入，二进制分组，再用十六进制计算
		- [x] 进位回卷
		- [x] 反攻解析函数，添加checksum置零功能
	- [x] 实现各层 checksum
		- [x] 反攻 `IPv4`，添加伪首部传递功能
		- [x] 实现 `IPv4` 校验
		- [x] 实现 `TCP/UDP` 校验
		- [x] 测试 & Debug

2. UI
	- [ ] 安装 Qt Designer，小打小闹（图标、文字）
	- [ ] 实现`pack&crate.sh`打包脚本
	- [ ] 修改布局，集成文件与字符读入、结果解析、校验和计算过程

# 参考
1. checksum
	- [计算机网络](https://www.bilibili.com/video/BV137411Z7LR)
	- [TCP和UDP校验和](https://www.bilibili.com/video/BV1F3411N7pr)
	- [IP和UDP校验和的计算方法🌟](https://www.bilibili.com/video/BV1fD4y1q7Dj)
	- [WireShark默认不检查校验和的解决办法](https://blog.csdn.net/stephenxu111/article/details/12945893)


2. pyside6
	- [Github - Modern_GUI_PyDracula_PySide6_or_PyQt6🌟](https://github.com/Wanderson-Magalhaes/Modern_GUI_PyDracula_PySide6_or_PyQt6)
	- [Rookie 3.0官方图标库](https://www.iconfont.cn/collections/detail?spm=a313x.7781069.1998910419.dc64b3430&cid=7077)
	- [15分钟快速入门PySide/PyQt](https://www.bilibili.com/video/BV18F411W7y2)
	- [Python+Pyside/PyQt实现的GUI桌面应用](https://www.bilibili.com/video/BV1i24y1X7pV)
	- [实现选择文件界面](https://blog.csdn.net/weixin_42888638/article/details/127186631)


3. Diagram
	- [Python自动绘制UML类图、函数调用图](https://blog.csdn.net/Bit_Coders/article/details/120722430)
	- [error: subprocess-exited-with-error](https://zhuanlan.zhihu.com/p/581112365)





# 实现
🚩闲下来更新README
