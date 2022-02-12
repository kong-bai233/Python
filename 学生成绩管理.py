listgd=[]
history=[]
names=[]
nam=None
gard=None
help_name=["录入","名字录入","最高分","最低分","所有分数","具体分数","个人","高于","名字高于","清空历史","帮助"]
#11个
help_detail=["仅支持录入分数","需要带有名字或学号录入分数 例如:张三 100","将会输出录入分数中的最高分","将会输出录入分数中的最低分","仅输出上一次录入的所有分数","将会输出上一次录入的所有分数及其对应名字或学号","可以通过输入名字或学号查看对应分数","需要输入一个分数，将会输出高于这个分数的所有分数","需要输入一个分数，将会输出高于这个分数的所有名字或学号","将会删除上一次录入的分数记录","输出所有命令及其用途"]
while 1:
    def best(height):
            a=sorted(height)
            print("最高分:",a[-1],"\n")
    def worst(lgarde):
            b=sorted(lgarde)
            print("最低分:",b[0],"\n")
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
                print('平均分:{:.2f}'.format(average_garde))
                history=listgd
                break
            if garde!='ok':
                listgd.append(float(garde))
    if user=='名字录入':
        listgd.clear()
        while 1:
            try:
                nam,gard=input("").split()
            except:
                print("输入方式有误\n")
            if nam=="0" and gard=="0" or nam=="o" and gard=="k" or nam=='' and gard=='':
                try:
                    print("\n平均分:{:.2f}\n".format(sum(listgd)/len(listgd)))
                    history=listgd
                    nam_garde=dict(zip(names,history))
                    break
                except ZeroDivisionError:
                    print("还没有录入任何数据!\n")
                    break
            if nam!=0 and gard!=0:
                try:
                    names.append(nam)
                    listgd.append(float(gard))
                except ValueError:
                    pass
    if user=='最高分':
        try:
            best(history)
        except:
            print("还没有录入分数\n")
    if user=='最低分':
        try:
            worst(history)
        except:
             print("还没有录入分数\n")
    if user=='清空历史':
        history.clear()
        print("已清空!\n")
    if user=='所有分数':
        print("一共",len(history),"人")
        for item in history:
            print(item)
        print("\n")
    if user=='具体分数':
        for name,gd in nam_garde.items():
            print(name,":",gd)
        print("\n")
    if user=='个人':
        print("输入out退出个人成绩查询")
        while 1:
            nam_garde=dict(zip(names,history))
            get_name=input("名字:")
            if get_name!='out':
                print(nam_garde.get(get_name,"查无此人!\n"))
                print("\n")
            if get_name=='out':
                break
    if user=='高于':
        upgarde=int(input("输入分数:"))
        ugarde=[x for x in history if x>upgarde]
        print('一共',len(ugarde),'个')
        for item in ugarde:
            print(item)
        print('\n')
    if user=='名字高于':
        garde_nam=dict(zip(names,history))
        get_garde=float(input("输入分数"))
        for key,valu in garde_nam.items():
            if valu>get_garde:
                print(key,":",valu)
        print("\n")
    if user=="help" or user=="帮助":
        the_help=dict(zip(help_name,help_detail))
        for name,detail in the_help.items():
            print(name,"  ",detail,"\n")
    if user=='低于':
        get_garde=int(input("输入分数:"))
        the_garde=[x for x in history if x<get_garde]
        print('一共',len(the_garde),'个')
        for item in the_garde:
            print(item)
        print('\n')
