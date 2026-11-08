# pylearn

Python 学习练习仓库，记录学习过程中的练习代码与小案例。

## 目录结构

```
test1/
├── day1/    # Python 基础：流程控制、数据结构、文件操作、小案例
└── day2/    # 进阶主题：JSON 序列化、生成器、并发
```

## Day 1 · Python 基础

| 文件 | 内容 |
| --- | --- |
| while.py | while 循环 |
| list.py | 列表操作 |
| dictionary.py | 字典操作 |
| 索引.py | 序列的索引与切片 |
| binary.py | 二进制转换 |
| file_op.py | 文件读写（open / read / readline） |
| getpass1.py | getpass 模块：隐藏式密码输入 |
| login.py | 简单登录验证 |
| guess.py | 猜数字小游戏（if / elif / else） |
| shoppingcart.py | 购物车小程序 |
| 3level_menus.py | 三级菜单（多级字典 + 循环） |
| sys_mod.py | import 自定义模块的初步使用 |

## Day 2 · 进阶主题

| 文件 | 内容 |
| --- | --- |
| json序列化.py | 使用 json.dump 写入 JSON 文件 |
| json反序列化.py | 读取并还原 JSON 数据 |
| 生成器.py | 生成器：yield、`__next__()`、斐波那契数列 |
| 并发.py | 并发编程入门 |

## 使用方法

```bash
# 直接运行任意一个练习
python test1/day1/guess.py
```

> 注意：部分练习依赖同目录下的数据文件（如 `file.txt`）。

## 环境

- Python 3.6+
- 开发工具：PyCharm
