while 1:
    import random
    player=input("请输入：")
    computer=['石头','剪刀','布']
    i=random.randint(0,2)
    if player=='退出' or player=='exit':
        exit()
    if player!='石头' and player!='剪刀' and player!='布':
        print('无效操作!!!\n')
    else:
        print('玩家 %s ----- 对方 %s'%(player,computer[i]))
        if (player=='石头' and computer[i]=='剪刀') or (player=='剪刀' and computer[i]=='布') or (player=='布' and computer[i]=='石头'):
            print('玩家胜！\n\n')
        elif player==computer[i]:
            print('平局！\n\n')
        else:
            print('对方胜！\n\n')
