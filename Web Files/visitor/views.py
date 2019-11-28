from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection
import psycopg2
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
import requests

# Create your views here.
def index(request):
    return render(request,'visitor.html')

def save(request):
    vname = request.GET.get("name1")
    vmail = request.GET.get("mail1")
    vno = request.GET.get("mno1")
    hname = request.GET.get("name2")
    hmail= request.GET.get("mail2")
    hno = request.GET.get("mno2")
    format = '%I:%M %p'
    time = datetime.now()
    time = datetime.strftime(time, format)
    query = "insert into vd values(%s,%s,%s,%s,%s,%s,%s)"
    with connection.cursor() as cursor:
        cursor.execute(query,[vname,vmail,vno,hname,hmail,hno,time])
    smtp_server = "smtp.gmail.com"
    port = 587 
    sender_email = "rajabadhar.vidathusirippu@gmail.com"
    receiver_email = hmail
    password = "crazymohan"

    message = message = MIMEMultipart("alternative")
    message["Subject"] = "Visitor details"
    message["From"] = sender_email
    message["To"] = receiver_email

    text = "PFA new visitor details. This is an automated mail. Please do not reply.\nName: "+str(vname)+"\nEmail: "+str(vmail)+"\nPhone: "+str(vno)+"\nIn Time: "+str(time)
    text2 = "PFA new visitor details. \nName: "+str(vname)+"\nEmail: "+str(vmail)+"\nPhone: "+str(vno)+"\nIn Time: "+str(time)

    part = MIMEText(text, "plain")

    message.attach(part)

    context = ssl.SSLContext()

    with smtplib.SMTP(smtp_server,port) as server:
        server.ehlo()  
        server.starttls(context=context)
        server.ehlo() 
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())

    url = "https://www.fast2sms.com/dev/bulk"
 
    payload = "sender_id=FSTSMS&message="+text2+"&language=english&route=p&numbers="+str(hno)
    headers = {
     'authorization': "p5YMOyf2aR9oUJP7KmXjuLlZQBIFdVcr1g0GnxsHkN6TvhzECiN5HVADIRzvWOpmdbr2YktFZus9Uc7K",
     'Content-Type': "application/x-www-form-urlencoded",
     'Cache-Control': "no-cache",
     }
 
    response = requests.request("POST", url, data=payload, headers=headers)
    
    return render(request,'save.html')

def co(request):
    return render(request,'co.html')

def check0(request):
    mno = request.GET.get("mno")
    query = "select vname,vmail,vno from vd where vno = %s"
    with connection.cursor() as cursor:
       cursor.execute(query,[mno])
       tab = cursor.fetchone()
    context={'tab':tab,}
    return render(request,'co2.html',context=context)

def check(request):
    mno = request.GET.get("mno")
    ct = request.GET.get("ct")
    ap = request.GET.get("ap")
    cho = str(ct)+' '+str(ap)
    query = "update vd set checkout = %s where vno = %s"
    q2 = "select vmail from vd where vno = %s"
    with connection.cursor() as cursor:
        cursor.execute(query,[cho,mno])
    with connection.cursor() as cursor:
        cursor.execute(q2,[mno])
        result = cursor.fetchone()
    vmail = result[0]
    smtp_server = "smtp.gmail.com"
    port = 587 
    sender_email = "rajabadhar.vidathusirippu@gmail.com"
    receiver_email = vmail
    password = "crazymohan"

    message = message = MIMEMultipart("alternative")
    message["Subject"] = "Visitor details"
    message["From"] = sender_email
    message["To"] = receiver_email

    text = "PFA link to form. Fill the details. This is an automated mail. Please do not reply.\nForm Link: http://127.0.1.1:8000/visitor/detail"

    part = MIMEText(text, "plain")

    message.attach(part)

    context = ssl.SSLContext()

    with smtplib.SMTP(smtp_server,port) as server:
        server.ehlo()  
        server.starttls(context=context)
        server.ehlo() 
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())



 
    
    return render(request,'save.html')

def detail(request):
    return render(request,'detail.html')


def submit(request):
    name = request.GET.get("name")
    mno = request.GET.get("mno")
    cit = request.GET.get("cit")
    ap1 = request.GET.get("ap1")
    cot = request.GET.get("cot")
    ap2 = request.GET.get("ap2")
    hname = request.GET.get("hname")
    addr = request.GET.get("addr")
    cit = str(cit)+str(ap1)
    cot = str(cot)+str(ap2)
    query = "insert into vd2 values(%s,%s,%s,%s,%s,%s)"
    with connection.cursor() as cursor:
        cursor.execute(query,[name,mno,cit,cot,hname,addr])
    return render(request,'save.html')

def view(request):
    query = "select * from vd"
    with connection.cursor() as cursor:
       cursor.execute(query,[])
       tab = cursor.fetchall()
    context={'tab':tab,}
    return render(request,'view.html',context=context)













    




