from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib import messages 
from.forms import EditUser
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as login,logout
from .models import signup_user
import random as r
from django.core.mail import send_mail
import requests
from django.views.decorators.csrf import csrf_exempt,csrf_protect
import json


# Create your views here.
#P2C-21-027
def accounts(request):
    return render(request, 'accounts.html')

def home(request):
    return render(request, 'accounts.html')    


def signup(request):
    if  request.method =="POST":
        
        first_name=request.POST['firstname']
        last_name=request.POST['lastname']
        email=request.POST['email']
        Address=request.POST['Address']
        username=request.POST['username']
        phone_no=request.POST['phoneno']
        collage_name=request.POST['college name']
        Branch=request.POST['Branch']
        password=request.POST['password']
        passwordre=request.POST['passwordre']
        image=request.FILES.get('image')
        
        #email_verify(request ,email)
        if email==email1:
            if  signup_user.objects.filter(email=email).exists():
                 messages.warning(request, 'Email Already Exists !!!')
                 return redirect ('signup')
                 
            else:
                if (password)==(passwordre):
                     signup= signup_user(first_name=first_name ,last_name=last_name ,email=email ,Address=Address,username=username ,phone_no=phone_no, collage_name=collage_name, Branch=Branch, password=password, image=image )
                     messages.success(request,'Registration Successful')
                     signup.save()
                     email_status=send_mail("Power2careear_Account_Details", f" Hello {username}\n \n Your Account Created Sucessfully \n Your Mail is:- {email} \n Your Password Is:- {password} \n \n TKANK YOU \n", "mohitgahalawat158@gmail.com",[f'{email1}'],fail_silently=False)
                     
                     return redirect("signup")
                else:
                    messages.warning(request,'Password not matched')
                    return redirect('signup')  
        else:
            messages.warning(request,'Enter Verified Mail')
            return redirect('signup') 
    else:
        return render(request, 'signup.html')

#for email verification using otp
def email_verify(request):
   global otp_send ,email1
   otp_send=r.randint(1000,9999)
   if request.method =="POST":
       email1=request.POST.get('email')
       email_status=send_mail("Power2careear_Mail_Verification", f"Your OTP Is:-{otp_send}", "mohitgahalawat158@gmail.com",[f'{email1}'],fail_silently=False)
       if email_status==1:
           messages.warning(request,'OTP Send Your Mail')
           return redirect('otp')
       else:
          email_status=send_mail("Power2careear_Mail_Verification", f"Your OTP Is:-{otp_send}", "mohitgahalawat158@gmail.com",[f'{email1}'],fail_silently=False) 
   return render(request,'email_verify.html')
             
             
def otp(request):
    if request.method =="POST":
        otp_reverse=request.POST['otp'] 
        if str(otp_send)==str(otp_reverse):
            messages.warning(request,'Email Verifyed')
            return redirect('signup')
        
        else:
            messages.warning(request,'Email Invalid Try Another Mail')
            return redirect ('email_verify')
    return render(request,"otp.html") 
    
         
def forgot_password(request):
    global otp_forgot
    global email2
    if request.method =="POST":
       otp_forgot=r.randint(1000,9999)
       email2=request.POST.get('email')
       if  signup_user.objects.filter(email=email2).exists():
           email_status=send_mail("Power2careear_Mail_Verification", f"Your OTP Is:-{otp_forgot}", "mohitgahalawat158@gmail.com",[f'{email2}'],fail_silently=False)
           if email_status==1:
               messages.warning(request,'OTP Send Your Mail')
               return redirect('otp_password')
           else:
              email_status=send_mail("Power2careear_Mail_Verification", f"Your OTP Is:-{otp_forgot}", "mohitgahalawat158@gmail.com",[f'{email2}'],fail_silently=False) 
       else:
           messages.warning(request,'First Signup') 
    return render(request, 'forgot_password.html')

def otp_password(request):
    if request.method =="POST":
        otp_reverse=request.POST['otp'] 
        if str(otp_forgot)==str(otp_reverse):
            messages.warning(request,'Email Verifyed')
            return redirect('new_password')
        
        else:
            messages.warning(request,'Email Invalid Try Another Mail')
            return redirect ('email_verify')
    return render(request,"otp_password.html") 

def new_password(request):
    if request.method =="POST":
        newpass=request.POST['new_password'] 
        cnfrmpass=request.POST['confirm_password']
        if newpass==cnfrmpass:
            
            userdata=signup_user.objects.filter(email=email2).update(password=f"{newpass}")
            messages.warning(request,'Password Update Sucessfully')
            return redirect('login')
        else:
            messages.warning(request,'Password Not Match')
            return redirect("new_password")
        
    return render(request,"new_password.html") 


@csrf_exempt
@csrf_protect
def linked_in(request):
   
   ##request to code from url 
   code = request.GET['code']
   ###POST REQUEST TO GET TOKEN
   url="https://www.linkedin.com/oauth/v2/accessToken"

   client_id="86is7u5vpfl0ec"
   client_secret="bBzaNrHXlnnpm38h"
   grant_type="authorization_code"
   redirect_uri="http://127.0.0.1:8000/accounts/linked_in/"
   code=str(code)
   
   params={'grant_type':grant_type,'code':code,'client_id':client_id,'client_secret':client_secret,'redirect_uri':redirect_uri}

   token=requests.post(url=url,params=params)
   token=token.json()
   token=(token.get('access_token'))
   
   ##get request for take user data
   url1="https://api.linkedin.com/v2/me"
   headers={'Authorization':f'Bearer {token}'}
   
   #params1=("Bearer "+token)
   data=requests.get(url=url1,headers=headers)
   data=data.json()
   user_id=data.get('id')
   lastname=data.get('localizedLastName')
   pic0=data.get('profilePicture')
   pic=pic0.get('displayImage')
   firstname=data.get('localizedFirstName')
   language00=data.get('lastName')
   language0=language00.get('preferredLocale')
   language=language0.get('language')
   localized0=language00.get('preferredLocale')
   localized=localized0.get('country')
   
   #retreve pic data
   #GET https://api.linkedin.com/v2/me?projection=(id,firstName,lastName,profilePicture(displayImage~:playableStreams))
  
   #urlp="https://api.linkedin.com/v2/me"
   #paramss={'projection':'(profilePicture(displayImage~:playableStreams))'}
   #datap=requests.get(url=urlp,params=paramss,headers=headers)
   #datap=datap.json()
   #data=data.get('profilePicture')
   #data=data.get('displayImage~')
   #data=data.get('elements')
   #data=data[0]
   #data=data.get('identifiers')
   #data=data[0]
   #data=data.get('identifier')
   #urlimg=f"{data}"
   
   #user_image=requests.get(url=urlimg)
   #user_image = f"{user_image}"
   user_image="None"
   #user_image=urllib.request.urlretrieve(image_url, f'{user_id}.jpg')
   
   
   #retreve email add
   #GET https://api.linkedin.com/v2/emailAddress?q=members&projection=(elements*(handle~))
   urlm="https://api.linkedin.com/v2/emailAddress"
   paramsm={'q':'members','projection':'(elements*(handle~))'}
   
   datag=requests.get(url=urlm,params=paramsm,headers=headers)
   datag=datag.json()
   datag=datag.get('elements')
   datag=datag[0]
   datag=datag.get('handle~')
   email=datag.get('emailAddress')
   
   #data stores in database
   passg=r.randint(1000,9999)
   password=f"{firstname}"+"@"+f"{passg}"
   Address="None"
   phone_no="None"
   collage_name="None"
   Branch="None"
   username=f"{firstname}"+"@"+f"{lastname}"
   if  signup_user.objects.filter(email=email).exists():
       messages.warning(request, 'Email Already Exists !!!')
       return redirect ('signup')
   else:
       linkedin=signup_user(last_name=lastname,image=user_image,first_name=firstname,email=email,username=username,Address=Address,phone_no=phone_no,collage_name=collage_name,Branch=Branch,password=password)
       linkedin.save()
       messages.success(request,'Registration Successful')
       email_status=send_mail("Power2careear_Account_Details", f" Hello {username}\n \n Your Account Created Sucessfully \n Your Mail is:- {email} \n Your Password Is:- {password} \n \n TKANK YOU \n", "mohitgahalawat158@gmail.com",[f'{email}'],fail_silently=False)
                     
       return redirect("signup")
  
   
   
  
  
   return render(request,'linked_in.html')
   
def loginuser(request):
     
     if   request.method =="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        print(username,password)
        user= authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect("../index")
        # A backend authenticated the creden
        else:
   
        # No backend authenticated the crede
          return render(request, 'login.html')
     else:
       return render(request, 'login.html')
    



#p2c-21-105
def profile(request):  
    if request.user.is_authenticated:
        fm=EditUser(instance=request.user)
        return render(request,'profile.html',{'name':request.user,'form':fm})
    else:
        return HttpResponseRedirect('/login/')

def register(request):                         
    if request.method == 'POST':
        fname = request.POST.get('firstname')
        lname = request.POST.get('lastname')
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')
        if pass1!=pass2:
            messages.warning(request,'Password not matched')
            return redirect('register')
        elif User.objects.filter(username=uname).exists():
            messages.warning(request,'username already exist')
            return redirect('register')
        elif User.objects.filter(email=email).exists():
            messages.warning(request,'email already exist')
            return redirect('register')
        else:
            user = User.objects.create_user(first_name=fname, last_name=lname, username=uname, email=email,
                                            password=pass1)
            user.save()
            messages.success(request, 'successfully register')
            return redirect('login')
    return render(request, 'register.html')

def login(request): 
   if request.method =="POST":
        
        email = request.POST['email']
        password = request.POST['password']
        # user data fetch using email
        if  signup_user.objects.filter(email=email).exists():
            userdata=signup_user.objects.filter(email=email)
            userdata=userdata[0]
            userpass=userdata.password
            
            #data_all=signup_user.objects.all()
            if password==userpass:
                  return render(request,'profile.html',{"userdata":userdata})
            else:
                  messages.warning(request, 'Invalid Password !!!')
                  return redirect('login')
        else:
             messages.warning(request, 'Invalid Email !!!')
                               
   return render(request,'login.html')

