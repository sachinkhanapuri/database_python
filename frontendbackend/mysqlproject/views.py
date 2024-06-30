from django.shortcuts import render
import MySQLdb

# Create your views here.
def Homepage(request):
    if request.method=="POST":
        msgg=request.POST.get("msg")
        print("msg:",msgg)
        conn=MySQLdb.connect(host='localhost',user='root',password='root',database='djangodb')
        mycursor=conn.cursor()
        sqlquery="Insert into messagestb(message) values('%s')"
        print(sqlquery)
        args=msgg
        mycursor.execute(sqlquery %args)
        conn.commit()
        mycursor.execute("select * from messagestb")
        datas=mycursor.fetchall()
        for data in datas:
            print(data)
    return render(request,'index.html')