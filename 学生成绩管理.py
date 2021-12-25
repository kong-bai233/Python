listgd=[]
history=[]
names=[]
help_name=["录入","名字录入","最高分","最低分","所有分数","具体分数","个人","高于","名字高于","清空历史","帮助"]
#11个
help_detail=["仅支持录入分数","需要带有名字或学号录入分数 例如：张三 100","将会输出录入分数中的最高分","将会输出录入分数中的最低分","仅输出上一次录入的所有分数","将会输出上一次录入的所有分数及其对应名字或学号","可以通过输入名字或学号查看对应分数","需要输入一个分数，将会输出高于这个分数的所有分数","需要输入一个分数，将会输出高于这个分数的所有名字或学号","将会删除上一次录入的分数记录","输出所有命令及其用途"]
while 1:
    def best(height):
        if len(height)==0:
            print("还没有录入分数！\n")
        if len(height)!=0:
            height.sort()
            print("最高分：",height[-1],"\n")
    def worst(lgarde):
        if len(lgarde)==0:
            print("还没有录入分数！\n")
        if len(lgarde)!=0:
            lgarde.sort()
            print("最低分：",lgarde[0],"\n")
    user=input("→")
    if user=='退出' or user=='exit':
        exit()
    if user=='录入':
        listgd.clear()
        print("请输入:\n")
        while 1:
            garde=input("")
            if garde=='ok':
                average_garde = sum(listgd)/len(listgd)
                print('平均分：{:.2f}'.format(average_garde))
                history=listgd
                break
            if garde!='ok':
                listgd.append(float(garde))
    if user=='名字录入':
        while 1:
            nam,gard=input("").split()
            if nam=="0" and gard=="0" or nam=="o" and gard=="k":
                print("\n平均分：{:.2f}\n".format(sum(listgd)/len(listgd)))
                history=listgd
                break
            if nam!=0 and gard!=0:
                names.append(nam)
                listgd.append(float(gard))
    if user=='最高分':
        best(history)
    if user=='最低分':
        worst(history)
    if user=='清空历史':
        history.clear()
        print("已清空!\n")
    if user=='所有分数':
        for item in history:
            print(item)
        print("\n")
    if user=='具体分数':
        nam_garde=dict(zip(names,history))
        for name,gd in nam_garde.items():
            print(name,":",gd)
        print("\n")
    if user=='个人':
        print("输入out退出个人成绩查询")
        while 1:
            nam_garde=dict(zip(names,history))
            get_name=input("名字：")
            if get_name!='out':
                print(nam_garde.get(get_name,"查无此人！\n"))
                print("\n")
            if get_name=='out':
                break
    if user=='高于':
        upgarde=int(input("输入分数："))
        ugarde=[x for x in history if x>upgarde]
        print('一共',len(ugarde),'个')
        for item in ugarde:
            print(item)
        print('\n')
    if user=='名字高于':
        garde_nam=dict(zip(history,names))
        get_garde=int(input("输入分数"))
        the_garde=[x for x in history if x>get_garde]
        i=0
        for j in the_garde:
            print(garde_nam.get(the_garde[i]))
            i+=1
        print("\n")
    if user=="help" or user=="帮助":
        the_help=dict(zip(help_name,help_detail))
        for name,detail in the_help.items():
            print(name,"  ",detail,"\n")
