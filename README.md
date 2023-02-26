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
	- [ ] 项目结构
		- [ ] 安装 Qt Designer
		- [ ] 实现`pack&crate.sh`打包脚本

	- [ ] 布局改造
		- [ ] 
	- [ ] 功能集成
		- [ ] 

# 参考
1. checksum
	- [计算机网络](https://www.bilibili.com/video/BV137411Z7LR)
	- [TCP和UDP校验和](https://www.bilibili.com/video/BV1F3411N7pr)
	- [IP和UDP校验和的计算方法🌟](https://www.bilibili.com/video/BV1fD4y1q7Dj)
	- [WireShark默认不检查校验和的解决办法](https://blog.csdn.net/stephenxu111/article/details/12945893)


2. pyside6
	- [Github - Modern_GUI_PyDracula_PySide6_or_PyQt6🌟](https://github.com/Wanderson-Magalhaes/Modern_GUI_PyDracula_PySide6_or_PyQt6)
	- [15分钟快速入门PySide/PyQt](https://www.bilibili.com/video/BV18F411W7y2)
	- [Python+Pyside/PyQt实现的GUI桌面应用](https://www.bilibili.com/video/BV1i24y1X7pV)