import os,sqlite3
CNDL=[]
ENDL=[]
D=[]
#import termios
#检索函数
def find_files(filename, search_path):
   result = []

# Wlaking top-down from the root
   for root, dir, files in os.walk(search_path):
      if filename in files:
         result.append(os.path.join(root, filename))
   return result
#将路径改为可执行路径
def Add(Data):
    Data=list(Data)
    i=0
    while 1:
        if Data[i]==':':
            Data.insert((i+1),'\\')
            Data=''.join(Data)
            return Data
        i+=1
#将路径改为可执行路径
def Change(String):
    String=list(String)
    i=0
    while True:
        if String[i]=='\\':
            String[i]='/'
        i+=1
        if i==len(String):
            break
    Changed=''.join(String)
    return Changed

#通过数据库找文件
def Search(GetFileName,GetDrive='C'):
    file=GetFileName
    PF=GetDrive
    print(file,PF,"检索中...")
    RESULT=find_files(file,PF+':')
    if RESULT==[]:
        print("未找到此文件\n")
    print(RESULT)
    if len(RESULT)>1:
        n=int(input("选择你要打开的路径(从0开始):"))
        while 1:
            try:
                RESULT[n]='\"'+RESULT[n]+'\"'
                RESULT[n]=Add(RESULT[n])
                os.system('start '+'\"\"'+' '+RESULT[n])
                print('start '+RESULT[n])
                print(RESULT[n])
                break
            except:
                n=input("不好啦,报错了!换一个路径吧(输入e退出选择)")
            if n=='e':
                break
    if len(RESULT)==1:
        RESULT[0]='\"'+RESULT[0]+'\"'
        RESULT[0]=Add(RESULT[0])
        os.system('start '+'\"\"'+' '+RESULT[0])
        print('start '+RESULT[0])
        print(RESULT[0])
#主体#
while 1:
    choose=input("        1:检索FileName.txt内的文件\n        2:输入目标文件及盘符\n        3:查找数据库内文件\n        4:向数据库内加入新数据\n        5:查看数据库内所有内容\n        6:删除数据库中某个内容\n        del:删除数据库\n\n选择:")
    
    #检索FileName.txt内的文件#
    try:
        if choose=='1':
            Path=os.getcwd()
            Path=Change(Path)
            with open(Path+'/FileName.txt','r+') as f:
                datas=f.readlines()
            print(datas)
            file=datas[0][0:-1]
            print(file)
            PF=datas[1]
            with open(Path+'/FileName.txt','r+') as f:
                f.truncate()
            print("检索中...")
            RESULT=find_files(file,PF+':')
            if RESULT==[]:
                print("未找到此文件\n")
            print(RESULT)
            if len(RESULT)>1:
                n=int(input("选择你要打开的路径(从0开始):"))
                while 1:
                    try:
                        RESULT[n]='\"'+RESULT[n]+'\"'
                        RESULT[n]=Add(RESULT[n])
                        os.system('start '+'\"\"'+' '+RESULT[n])
                        print('start '+RESULT[n])
                        print(RESULT[n])
                        break
                    except:
                        n=input("不好啦,报错了!换一个路径吧(输入e退出选择)")
                    if n=='e':
                        break
            if len(RESULT)==1:
                RESULT[0]='\"'+RESULT[0]+'\"'
                RESULT[0]=Add(RESULT[0])
                os.system('start '+'\"\"'+' '+RESULT[0])
                print('start '+RESULT[0])
                print(RESULT[0])
    except:
        print('文件内不能为空，请在FileName.txt中输入文件名以及搜索盘符\n')

    #输入目标文件及盘符#
    if choose=='2':
        file=input('输入文件名(示例:devcpp.exe):')
        PF=input("输入盘符(示例:C):")
        print("检索中...")
        RESULT=find_files(file,PF+':')
        if RESULT==[]:
            print("未找到此文件\n您可以输入 4 来添加，输入 5 可以查看数据库中所有内容\n")
        print(RESULT)
        if len(RESULT)>1:
            n=int(input("选择你要打开的路径(从0开始):"))
            while 1:
                try:
                    RESULT[n]='\"'+RESULT[n]+'\"'
                    RESULT[n]=Add(RESULT[n])
                    os.system('start '+'\"\"'+' '+RESULT[n])
                    print('start '+RESULT[n])
                    print(RESULT[n])
                    break
                except:
                    n=input("不好啦,报错了!换一个路径吧(输入e退出选择)")
                if n=='e':
                    break
        if len(RESULT)==1:
            RESULT[0]='\"'+RESULT[0]+'\"'
            RESULT[0]=Add(RESULT[0])
            os.system('start '+'\"\"'+' '+RESULT[0])
            print('start '+RESULT[0])
            print(RESULT[0]) 
    
    
    if choose=='3':
        FIND=input('输入文件名:')
        FIND=(FIND,)
        SqlPath=os.getcwd()
        SqlPath=Change(SqlPath)
        SqlPath=SqlPath+'/FileNamesData.db'
        FileNameData=sqlite3.connect(SqlPath)
        #SqlOperate=FileNameData.cursor()
        SqlOperate = FileNameData.execute('SELECT ChineseName,EnglishName,DRIVE FROM FileNamesDatas WHERE ChineseName == ?',FIND)
        Result=SqlOperate.fetchall()
        try:
            print(Result)
            Search(Result[0][1],Result[0][2])
            FileNameData.close()
        except:
            print('\n抱歉，并未在数据库中找到此文件，您可以输入 4 来添加，输入 5 可以查看数据库中所有内容\n')

    if choose=='4':
        SqlPath=os.getcwd()
        SqlPath=Change(SqlPath)
        SqlPath=SqlPath+'/FileNamesData.db'
        FileNameData=sqlite3.connect(SqlPath)
        SqlOperate=FileNameData.cursor()
        try:
            SqlOperate.execute('create table FileNamesDatas (ChineseName varchar(30),EnglishName varchar(30) UNIQUE,DRIVE varchar(30))')
        except:
            pass
        while 1:
            try:
                ChineseNameData,EnglishNameData,Drive=input("分别输入中文名与文件中的英文名及盘符(例如:网易云音乐 cloudmusic.exe C)(输入0 0 0停止输入):").split(' ')
            except:
                break
            if ChineseNameData=='0' and EnglishNameData=='0' and Drive=='0' or ChineseNameData=='' and EnglishNameData=='' and Drive=='':
                break
            #ChineseNameData='\''+ChineseNameData+'\''
            #EnglishNameData='\''+EnglishNameData+'\''
            CNDL.append(ChineseNameData)
            ENDL.append(EnglishNameData)
            D.append(Drive)
        TotalData=list(zip(CNDL,ENDL,D))
        CNDL.clear()
        ENDL.clear()
        D.clear()
        print(TotalData)
        i=0
        for j in TotalData:
            try:
                SqlOperate.execute('insert into FileNamesDatas(ChineseName,EnglishName,DRIVE) values(?,?,?)',TotalData[i])
            except:
                SqlOperate.execute('replace into FileNamesDatas(ChineseName,EnglishName,DRIVE) values(?,?,?)',TotalData[i])
            FileNameData.commit()
            i+=1
        #SqlOperate.executemany('insert into FileNamesDatas(ChineseName,EnglishName,DRIVE) values(?,?,?)',TotalData)
        FileNameData.commit()
        TotalData.clear()
        #FileNameData.commit()
        SqlOperate=FileNameData.execute('select * from FileNamesDatas')
        print(SqlOperate.fetchall())
        FileNameData.close()

    if choose=='5':
        try:
            SqlPath=os.getcwd()
            SqlPath=Change(SqlPath)
            SqlPath=SqlPath+'/FileNamesData.db'
            FileNameData=sqlite3.connect(SqlPath)
            SqlOperate=FileNameData.cursor()
            SqlOperate=FileNameData.execute('select * from FileNamesDatas')
            print('\n',SqlOperate.fetchall(),'\n\n')
            FileNameData.close()
        except sqlite3.OperationalError:
            print("未找到数据库或数据库为空！！！\n")

    if choose=='6':
        Del=input('输入要删除的文件名（例如：网易云音乐）：')
        Del=(Del,)
        SqlPath=os.getcwd()
        SqlPath=Change(SqlPath)
        SqlPath=SqlPath+'/FileNamesData.db'
        FileNameData=sqlite3.connect(SqlPath)
        SqlOperate=FileNameData.cursor()
        SqlOperate=FileNameData.execute('DELETE from FileNamesDatas WHERE ChineseName == ?',Del)
        FileNameData.commit()
        print('\n删除成功\n')
        FileNameData.close()
    
    if choose=='del':
        SqlPath=os.getcwd()
        SqlPath=Change(SqlPath)
        SqlPath=SqlPath+'/FileNamesData.db'
        os.remove(SqlPath)
    else:
        print('功能还未开发~')