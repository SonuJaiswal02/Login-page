from django.shortcuts import render # type: ignore
import mysql.connector as sql
em=''
pwd=''
# Create your views here.
def loginaction(request):
    global em,pwd
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",passwd="sonu@2002",database='website')
        cursor=m.cursor()
        d=request.POST
        for key,Value in d.items():    
            if key=="email":
                em=Value
            if key=="password":
                pwd=Value  

        c="select * from users where email='{}' and password='{}'".format(em,pwd)
        cursor.execute(c)
        t=tuple(cursor.fetchall())
        if t==():
            return render(request,'error.html')
        else:
            return render(request,"welcome.html")

    return render(request,'login_page.html')