print('石头(1) 剪刀(2) 布(3)\n')
while 1:
    import random
    player=int(input("请输入："))
    computer=random.randint(1,3)
    if player>3 or player<1:
        print('无效操作!!!\n')
    else:
        print('玩家 %d ----- 对方 %d'%(player,computer))
        if (player==1 and computer==2) or (player==2 and computer==3) or (player==3 and computer==1):
            print('玩家胜！\n\n')
        elif player==computer:
            print('平局！\n\n')
        else:
            print('对方胜！\n\n')
