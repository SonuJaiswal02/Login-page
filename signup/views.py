from django.shortcuts import render # type: ignore
import mysql.connector as sql  # type: ignore
from django.http import HttpResponse # type: ignore

fn=''
ln=''
s=''
em=''
pwd=''
# Create your views here.
def signaction(request):
    global fn,ln,s,em,pwd
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",passwd="sonu@2002",database='website')
        cursor=m.cursor()
        d=request.POST
        for key,Value in d.items():
            if key=="first_name":
                fn=Value
            if key=="last_name":
                ln=Value
            if key=="sex":
                s=Value        
            if key=="email":
                em=Value
            if key=="password":
                pwd=Value  

        c="insert into users values('{}','{}','{}','{}','{}')".format(fn,ln,s,em,pwd)
        cursor.execute(c)
        m.commit()         
    return render(request,'signup_page.html')


def homepage(request):
    return HttpResponse("Welcome to the Homepage!")