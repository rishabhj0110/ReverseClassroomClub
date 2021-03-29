from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.core.exceptions import ObjectDoesNotExist
import datetime
import os
from django.conf import settings 
from django.core.mail import send_mail 
import numpy as np
from django.contrib import messages
from subprocess import check_output, CalledProcessError,STDOUT
from django.contrib.auth.models import User, auth
from django.http import HttpResponse, request
from .models import SignUp,UserProfile,Newsletter,Contact,Instructor,Workshop,Courses,Ngo,Emailsystem
def home(request):
    return render(request,"home.html")
def contact(request):
    if request.method=='POST':
        g=0
        name=request.POST.get("name")
        email=request.POST.get("email")
        subject=request.POST.get("subject")
        message=request.POST.get("message")
        c=Contact(name=name,email=email,sub=subject,msg=message)
        c.save()
        try:
            subject = 'Query/Suggestion Received'   
            message = f'Hi{name}--{email},Your response is received by reverse classroom club.We will reply as soon as possible.'
            email_from = settings.EMAIL_HOST_USER 
            recipient_list = [email] 
            send_mail( subject, message, email_from, recipient_list ,fail_silently=False)
            messages.info(request,'Query/Feedback Submitted.we will reply you soon.')
        except:
            messages.info(request,'Query/Feedback Submitted.we will reply you soon.')
        return render(request,"contact.html",{"g":g})    
    return render(request,"contact.html")
def about(request):
    return render(request,"about.html")
def signuplogin(request):
    return render(request,"signuplogin.html") 
def signup(request):
    if request.method=='POST':
        first_name=request.POST.get("fname")
        last_name=request.POST.get("lname")
        email=request.POST.get("email")
        username=email
        mobno=request.POST.get("phoneno")
        password=request.POST.get("pass")
        password1=request.POST.get("pass1")
        def password_check(password):
            SpecialSym =['$', '@', '#', '%'] 
            val = True
            if len(password) < 8:
                print('length should be at least 6') 
                val = False
            if len(password) > 20: 
                print('length should be not be greater than 8') 
                val = False
            if not any(char.isdigit() for char in password): 
                print('Password should have at least one numeral') 
                val = False
            if not any(char.isupper() for char in password): 
                print('Password should have at least one uppercase letter') 
                val = False
            if not any(char.islower() for char in password): 
                print('Password should have at least one lowercase letter') 
                val = False
            if not any(char in SpecialSym for char in password): 
                print('Password should have at least one of the symbols $@#') 
                val = False
            if val == False: 
                val=True
                return val
                print(val)
        if (password_check(password)): 
            print("y")
        else: 
            print("x")                 
        if password==password1:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username taken')
                return redirect('signup')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email taken')
                return redirect('signup')
            elif (password_check(password)):
                messages.info(request,'password is not valid(must be combination of (A-Z,a-z,@,1-9))')
                return redirect('signup')
            else:
                user=User.objects.create_user(username=username,password=password,email=email,first_name=first_name,last_name=last_name)
                user.save()
                work=SignUp(username=username,password=password,email=email,first_name=first_name,last_name=last_name,pemail="none",year="none",degree="none",phoneno=mobno,college="none",address="none",descr="none",link="none",utype="normal")
                work.save()
                messages.info(request,"user created succesfully")
                user=auth.authenticate(username=username,password=password)
                if user is not None:
                   auth.login(request,user)
                u = User.objects.get(username=username)
                reg=UserProfile(user=u,usernames=username,year="none",degree="none",pemail="none",phoneno=mobno,address="none",desc="none",college="none",link="none",utype="normal")
                reg.save()
                auth.logout(request)
        else:
            messages.info(request,"password not matching")
            return redirect('signup')
        return redirect('login')
    return render(request,"signup.html")
def login(request):
    if request.method=="POST":
        username=request.POST.get("email")
        password=request.POST.get("pwd")
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            p1=request.user
            d=UserProfile.objects.get(usernames=p1.username)
            if(d.utype=="normal"):
                return redirect('/')
            else:
                return render(request,"adminhome.html")
        else:
            messages.info(request,"Invalid Credentials")
            return redirect('login')
    return render(request,"login.html")

def logout(request):
    auth.logout(request)
    return render(request,"login.html")

def events(request):
    return render(request,"event.html")
def profile(request):
    if request.method=="POST":
        id=int(request.POST.get("id"))
        return render(request,"profile.html",{"id":id})
    else:
        id=0
        return render(request,"profile.html",{"id":id})
def editprofile(request):
    id=2
    if request.method=="POST":
        fname=request.POST.get("fname")
        lname=request.POST.get("lname")
        username=request.POST.get("username")
        year=request.POST.get("year")
        degree=request.POST.get("degree")
        pemail=request.POST.get("pemail")
        phoneno=request.POST.get("phoneno")
        address=request.POST.get("address")
        desc=request.POST.get("des")
        link=request.POST.get("link")
        college=request.POST.get("college")
        User.objects.filter(username=username).update(first_name=fname,last_name=lname)
        UserProfile.objects.filter(usernames=username).update(usernames=username,college=college,year=year,degree=degree,pemail=pemail,phoneno=phoneno,address=address,desc=desc,link=link)
        SignUp.objects.filter(username=username).update(college=college,year=year,degree=degree,pemail=pemail,phoneno=phoneno,address=address,descr=desc,link=link)
        messages.info(request,"Profile Updated Properly")
        return render(request,"profile.html",{"id":id})
    return render(request,"profile.html",{"id":id})
def instructor(request):
    if request.method=="POST":
        names=request.POST.get("name")
        email=request.POST.get("email")
        phone=request.POST.get("phoneno")
        desc=request.POST.get("desc")
        qual=request.POST.get("qual")
        link=request.POST.get("link")
        fo=Instructor(name=names,email=email,phone=phone,desc=desc,qual=qual,link=link)
        fo.save()
        try:
            subject = 'Received Application'   
            message = f'Hi{names}--{email},Your application is received by reverse classroom club.we will reply you soon.'
            email_from = settings.EMAIL_HOST_USER 
            recipient_list = [email] 
            send_mail( subject, message, email_from, recipient_list ,fail_silently=False)
            messages.info(request,"We Have received your application,we wil contact you soon.")
        except:
            messages.info(request,"We Have received your application,we wil contact you soon.")
        return render(request,"instructor.html")
    return render(request,"instructor.html")
def workshop(request):
    w=reversed(Workshop.objects.all())
    return render(request,"workshop.html",{'w':w})
def courses(request):
    c=reversed(Courses.objects.all())
    return render(request,"courses.html",{'c':c})
def ngo(request):
    n=reversed(Ngo.objects.all())
    return render(request,"ngo.html",{'c':n})
def newsletter(request):
    if request.method=="POST":
        g=1
        email=request.POST.get("email")
        d=Newsletter.objects.all()
        for d in d:
            if(email == d.email):
                messages.info(request,"Email already present in Newsletter database.")
                break
        else:
            wo=Newsletter(email=email)
            wo.save()
            try:
                subject = 'Newsletter Activated'   
                message = f'Hi {email},Newsletter Activated for your entered email address.Now you will get all the updates from reverse classroom club.'
                email_from = settings.EMAIL_HOST_USER 
                recipient_list = [email] 
                send_mail( subject, message, email_from, recipient_list ,fail_silently=False)
                messages.info(request,"Newsletter Activated.")
            except:
                messages.info(request,"Newsletter Activated.")
        return render(request,"contact.html",{"g":g})   
    return render(request,"contact.html")

def changepassword(request):
    id=3
    if request.method == 'POST':
        old=request.POST.get("old")
        new1=request.POST.get("new1")
        new2=request.POST.get("new2")
        def passwordcheck(password):
            SpecialSym =['$', '@', '#', '%'] 
            val = True
            if len(password) < 8:
                print('length should be at least 6') 
                val = False
            if len(password) > 20: 
                print('length should be not be greater than 20') 
                val = False
            if not any(char.isdigit() for char in password): 
                print('Password should have at least one numeral') 
                val = False
            if not any(char.isupper() for char in password): 
                print('Password should have at least one uppercase letter') 
                val = False
            if not any(char.islower() for char in password): 
                print('Password should have at least one lowercase letter') 
                val = False
            if not any(char in SpecialSym for char in password): 
                print('Password should have at least one of the symbols $@#') 
                val = False
            return val
        p=request.user
        u1 = SignUp.objects.get(username=p.username)
        if(u1.password==old):
            if(new1==new2):
                password=new1
                if(passwordcheck(password)==True):
                    u = User.objects.get(username=p.username)
                    u.set_password(new1)
                    u.save()
                    SignUp.objects.filter(username=p.username).update(password=new1)
                    messages.info(request,"password Changed succesfully.Login using new Password.")
                    return redirect('logout')
                else:
                    messages.info(request,"Password should contain(0-9,a-z,A-Z,@)")
                    id=3
                    return render(request,"profile.html",{"id":id})    
            else:
                messages.info(request,"Password Don't Match")
                id=3
                return render(request,"profile.html",{"id":id})
        else:
            messages.info(request,"Old Password is not Correct or error occured.")
            id=3
            return render(request,"profile.html",{"id":id})
    id=3
    return render(request,"profile.html",{"id":id})

def resendpass(request):
    if request.method == 'POST':
        fname=request.POST.get("fname")
        lname=request.POST.get("lname")
        username=request.POST.get("email")
        phoneno=request.POST.get("phoneno")
        u=1
        try:
            pa=SignUp.objects.get(username=username)
        except:
            u=0
        if(u==1):
            password=pa.password
            if(fname == pa.first_name and lname == pa.last_name and phoneno ==pa.phoneno):
                try:
                    subject = 'Forget Password(Resend)'   
                    message = f'Hi {pa.username},your password for the Reverse Classroom Club is {password}. try logging in once again and change the password.'
                    email_from = settings.EMAIL_HOST_USER 
                    recipient_list = [pa.email] 
                    send_mail( subject, message, email_from, recipient_list ,fail_silently=False)
                    messages.info(request,"password has been sent to your registered email address,kindly check.")
                except:
                    messages.info(request,"sorry for inconvenience.email sending fail. kindly send query on conact page with proper subject and text.we will contact you soon..")
            else:
                messages.info(request,"Entered incorrect information.Try using correct credentials.")
            return render(request,"resend.html")
        else:
            messages.info(request,"User is not registered.kindly go to signup page and register.")
            return render(request,"login.html")
        return render(request,"login.html")
    return render(request,"resend.html")

def adminhome(request):
    return render(request,"adminhome.html")

def admintrack(request):
    if request.method == 'POST':
        id=int(request.POST.get("id"))
        if(id == 1):
            m=reversed(Newsletter.objects.all())
        elif(id == 2):
            m=reversed(Contact.objects.all())
        else:
            m=reversed(Instructor.objects.all())
        return render(request,"admintrack.html",{"id":id,'m':m})
    return render(request,"admintrack.html")

def adminevent(request):
    if request.method == 'POST':
        id=int(request.POST.get("id"))
        if(id<5 and id>0):
            n=Workshop.objects.all()
        elif(id>4 and id<9):
            n=Courses.objects.all()
        else:
            n=Ngo.objects.all()
        return render(request,"adminevent.html",{"id":id,'n':n})    
    return render(request,"adminevent.html")

def adminenroll(request):
    e=reversed(Workshop.objects.all())
    c=reversed(Courses.objects.all())
    n=reversed(Ngo.objects.all())
    return render(request,"adminenroll.html",{'e':e,'c':c,'n':n})

def addworkshop(request):
    id=2
    n=Workshop.objects.all()
    if request.method == 'POST':
        etitle=request.POST.get("etitle")
        edesc=request.POST.get("edesc")
        edoclink=request.POST.get("edoclink")
        einame=request.POST.get("einame")
        eidesc=request.POST.get("eidesc")
        eilink=request.POST.get("eilink")
        edate=request.POST.get("edate")
        etime=request.POST.get("etime")
        eapply=request.POST.get("eapply")
        df=Workshop(etitle=etitle,edesc=edesc,edoclink=edoclink,einame=einame,eidesc=eidesc,eilink=eilink,edate=edate,etime=etime,eapply=eapply)
        df.save()
        messages.info(request,"Workshop added Successfully.")
        return render(request,"adminevent.html",{"id":id,'n':n})    
    return render(request,"adminevent.html",{"id":id,'n':n})
def upworkshop(request):
    id=3
    n=Workshop.objects.all()
    if request.method == 'POST':
        etitle=request.POST.get("id")
        edesc=request.POST.get("edesc")
        edoclink=request.POST.get("edoclink")
        einame=request.POST.get("einame")
        eidesc=request.POST.get("eidesc")
        eilink=request.POST.get("eilink")
        edate=request.POST.get("edate")
        etime=request.POST.get("etime")
        eapply=request.POST.get("eapply")
        Workshop.objects.filter(etitle=etitle).update(etitle=etitle,edesc=edesc,edoclink=edoclink,einame=einame,eidesc=eidesc,eilink=eilink,edate=edate,etime=etime,eapply=eapply)
        messages.info(request,"Workshop updated Successfully.")
        return render(request,"adminevent.html",{"id":id,'n':n})    
    return render(request,"adminevent.html",{"id":id,'n':n})
def delworkshop(request):
    id=4
    n=Workshop.objects.all()
    if request.method == 'POST':
        etitle=request.POST.get("id")
        Workshop.objects.filter(etitle=etitle).delete()
        messages.info(request,"Workshop deleted Successfully.")
        return render(request,"adminevent.html",{"id":id,'n':n})    
    return render(request,"adminevent.html",{"id":id,'n':n})

def addcourses(request):
    id=6
    n=Courses.objects.all()
    if request.method == 'POST':
        ctitle=request.POST.get("ctitle")
        cdesc=request.POST.get("cdesc")
        cdoclink=request.POST.get("cdoclink")
        ciname=request.POST.get("ciname")
        cidesc=request.POST.get("cidesc")
        cilink=request.POST.get("cilink")
        csdate=request.POST.get("csdate")
        cedate=request.POST.get("cedate")
        ctime=request.POST.get("ctime")
        capply=request.POST.get("capply")
        df=Courses(ctitle=ctitle,cdesc=cdesc,cdoclink=cdoclink,ciname=ciname,cidesc=cidesc,cilink=cilink,csdate=csdate,cedate=cedate,ctime=ctime,capply=capply)
        df.save()
        messages.info(request,"Course added Successfully.")
        return render(request,"adminevent.html",{"id":id,'n':n})    
    return render(request,"adminevent.html",{"id":id,'n':n})
def upcourses(request):
    id=7
    n=Courses.objects.all()
    if request.method == 'POST':
        ctitle=request.POST.get("id")
        cdesc=request.POST.get("cdesc")
        cdoclink=request.POST.get("cdoclink")
        ciname=request.POST.get("ciname")
        cidesc=request.POST.get("cidesc")
        cilink=request.POST.get("cilink")
        csdate=request.POST.get("csdate")
        cedate=request.POST.get("cedate")
        ctime=request.POST.get("ctime")
        capply=request.POST.get("capply")
        Courses.objects.filter(ctitle=ctitle).update(ctitle=ctitle,cdesc=cdesc,cdoclink=cdoclink,ciname=ciname,cidesc=cidesc,cilink=cilink,csdate=csdate,cedate=cedate,ctime=ctime,capply=capply)
        messages.info(request,"Course updated Successfully.")
        return render(request,"adminevent.html",{"id":id,'n':n})    
    return render(request,"adminevent.html",{"id":id,'n':n})
def delcourses(request):
    id=8
    n=Courses.objects.all()
    if request.method == 'POST':
        ctitle=request.POST.get("id")
        Courses.objects.filter(ctitle=ctitle).delete()
        messages.info(request,"Course deleted Successfully.")
        return render(request,"adminevent.html",{"id":id,'n':n})    
    return render(request,"adminevent.html",{"id":id,'n':n})

def addngo(request):
    id=10
    n=Ngo.objects.all()
    if request.method == 'POST':
        ngoname=request.POST.get("ngoname")
        ngodetails=request.POST.get("ngodetails")
        ntitle=request.POST.get("ntitle")
        ndesc=request.POST.get("ndesc")
        ndoclink=request.POST.get("ndoclink")
        niname=request.POST.get("niname")
        nidesc=request.POST.get("nidesc")
        nilink=request.POST.get("nilink")
        nsdate=request.POST.get("nsdate")
        nedate=request.POST.get("nedate")
        ntime=request.POST.get("ntime")
        napply=request.POST.get("napply")
        df=Ngo(ngoname=ngoname,ngodetails=ngodetails,ntitle=ntitle,ndesc=ndesc,ndoclink=ndoclink,niname=niname,nidesc=nidesc,nilink=nilink,nsdate=nsdate,nedate=nedate,ntime=ntime,napply=napply)
        df.save()
        messages.info(request,"NGO Event added Successfully.")
        return render(request,"adminevent.html",{"id":id,'n':n})    
    return render(request,"adminevent.html",{"id":id,'n':n})
def upngo(request):
    id=11
    n=Ngo.objects.all()
    if request.method == 'POST':
        ngoname=request.POST.get("ngoname")
        ngodetails=request.POST.get("ngodetails")
        ntitle=request.POST.get("id")
        ndesc=request.POST.get("ndesc")
        ndoclink=request.POST.get("ndoclink")
        niname=request.POST.get("niname")
        nidesc=request.POST.get("nidesc")
        nilink=request.POST.get("nilink")
        nsdate=request.POST.get("nsdate")
        nedate=request.POST.get("nedate")
        ntime=request.POST.get("ntime")
        napply=request.POST.get("napply")
        Ngo.objects.filter(ntitle=ntitle).update(ngoname=ngoname,ngodetails=ngodetails,ntitle=ntitle,ndesc=ndesc,ndoclink=ndoclink,niname=niname,nidesc=nidesc,nilink=nilink,nsdate=nsdate,nedate=nedate,ntime=ntime,napply=napply)
        messages.info(request,"NGO Event updated Successfully.")
        return render(request,"adminevent.html",{"id":id,'n':n})    
    return render(request,"adminevent.html",{"id":id,'n':n})
def delngo(request):
    id=12
    n=Ngo.objects.all()
    if request.method == 'POST':
        ntitle=request.POST.get("id")
        Ngo.objects.filter(ntitle=ntitle).delete()
        messages.info(request,"NGO Event deleted Successfully.")
        return render(request,"adminevent.html",{"id":id,'n':n})    
    return render(request,"adminevent.html",{"id":id,'n':n})

def adminemail(request):
    m=reversed(Emailsystem.objects.all())
    id=0
    if request.method == 'POST':
        id=int(request.POST.get("id"))
        return render(request,"adminemail.html",{"id":id,'m':m})
    return render(request,"adminemail.html",{"id":id,'m':m})
    
def personalemail(request):
    id=2
    if request.method == 'POST':
        email=request.POST.get("email")
        sub=request.POST.get("sub")
        msg=request.POST.get("msg")
        time=datetime.datetime.now()
        s=Emailsystem(email=email,sub=sub,msg=msg,time=time)
        s.save()
        try:
            subject = sub   
            message = msg
            email_from = settings.EMAIL_HOST_USER 
            recipient_list = [email] 
            send_mail( subject, message, email_from, recipient_list ,fail_silently=False)
            messages.info(request,"Personal mail sent Succesfully.")
        except:
            messages.info(request,"Personal mail Failed.")
        return render(request,"adminemail.html",{"id":id})
    return render(request,"adminemail.html",{"id":id})
def broadcastemail(request):
    id=3
    if request.method == 'POST':
        email="Broadcast email sent"
        sub=request.POST.get("sub")
        msg=request.POST.get("msg")
        time=datetime.datetime.now()
        k=Emailsystem(email=email,sub=sub,msg=msg,time=time)
        k.save()
        f=User.objects.all()
        g=[]
        for f in f:
            g.append(f.email)
        g1=Newsletter.objects.all()
        for g1 in g1:
            g.append(g1.email)
        e=list(set(g))
        try:
            subject = sub   
            message = msg
            email_from = settings.EMAIL_HOST_USER 
            recipient_list = e
            send_mail( subject, message, email_from, recipient_list ,fail_silently=False)
            messages.info(request,"broadcast mail sent Succesfully.")
        except:
            messages.info(request,"broadcast mail Failed.")
        return render(request,"adminemail.html",{"id":id})
    return render(request,"adminemail.html",{"id":id})