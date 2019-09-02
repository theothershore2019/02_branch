# 导入工具包
# 注意：在导入工具包的时候，应该将导入的语句，放在文件的顶部
# 方便下方的代码，在需要时候，使用工具包中的工具
import random

# 从控制台输入要出的拳 —— 石头（1）／剪刀（2）／布（3）
player = int(input("请出拳 石头（1）／剪刀（2）／布（3）："))

# 电脑 随机 出拳 - 假定电脑永远出石头
computer = random.randint(1, 3)

print("玩家出的拳是 %d，电脑出的拳是 %d" % (player, computer))

# 比较胜负
# 如果条件判断的内容太长，可以在最外侧的条件增加一对大括号
# 再在每一个条件之间，使用回车，PyCharm 可以自动增加 8 个空格
if ((player == 1 and computer == 2) or
        (player == 2 and computer == 3) or
        (player == 3 and computer == 1)):

    print("噢耶！！！电脑弱爆了！！！")
elif player == computer:
    print("心有灵犀，再来一盘！")
else:
    print("不行，我要和你决战到天亮！")
