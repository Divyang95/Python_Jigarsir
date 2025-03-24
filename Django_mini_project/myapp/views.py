from django.shortcuts import render
from .models import Contact
from .models import User 
from django.core.mail import send_mail
from django.conf import settings
import random 
# Create your views here.
def index(request):
    return render(request,'index.html')

def contact(request):
    if request.method == 'POST':
        Contact.objects.create(
            name = request.POST['name'],
            email = request.POST['email'],
            mobile = request.POST['mobile'],
            remarks = request.POST['remarks'],
        )
        msg = 'Contact Saved Successfully!!'
        contacts = Contact.objects.all().order_by("-id")[:3]
        return render(request,'contact.html',{'msg':msg,'contacts':contacts})
    else:
        contacts = Contact.objects.all().order_by("-id")[:3]
        return render(request,'contact.html',{'contacts':contacts})

def signup(request):
    if request.method == "POST":
        try:
            User.objects.get(email = request.POST['email'])
            msg = "Your Email already registred"
            return render(request,'signup.html',{'msg':msg})
        except:
            if request.POST['password'] == request.POST['cpassword']:
                profile_picture = request.FILES.get('profile_picture',None)
                User.objects.create(
                    fname = request.POST['fname'],
                    lname = request.POST['lname'],
                    email = request.POST['email'],
                    mobile = request.POST['mobile'],
                    address = request.POST['address'],
                    password = request.POST['password'],
                    profile_picture = profile_picture
                )
                msg = f"{request.POST['fname']+" "+request.POST['lname']} signedup Successfully!!"
                return render(request,'login.html',{"msg":msg})
            else:
                msg = "Password and confirm password does not matched!!"
                return render(request,"signup.html",{"msg":msg})
    else:
        return render(request,'signup.html')

def login(request):
    if request.method == "POST":
        try:
            user = User.objects.get(email=request.POST['email'])
            if(request.POST['password'] == user.password):
                request.session['name'] = user.fname + " " + user.lname 
                request.session['email'] = user.email
                request.session['profile_picture'] = user.profile_picture.url   
                return render(request,'index.html')
        except:
            msg="Your email is not registred first signup"
            return render(request,'index.html',{'msg':msg})
    else:
        return render(request,'login.html')
    
def logout(request):
    try:
        del request.session['name']
        del request.session['email']
        del request.session['profile_picture']
        msg="User logged out successfully"
        return render(request,'login.html',{'msg':msg})
    except:
        return render(request,'login.html')


def changePassword(request):
    if request.method == "POST":
        user = User.objects.get(email = request.session['email'])
        if user.password == request.POST['old_password']:
            if request.POST['new_password'] == request.POST['cnew_password']:
                if user.password != request.POST['new_password']:
                    
                    user.password = request.POST['new_password']
                    user.save()
                    msg = 'Your password changed successfully'
                    del request.session['email']
                    del request.session['name']
                    return render(request,'login.html',{'msg':msg})
                else:
                    msg="New password can not be old password"
                    return render(request,'change-password.html',{'msg':msg})
            else:
                msg = "your new password and confirm new password does not matched!!"
                return render(request,'change-password.html',{'msg':msg})
        else:
            msg = "Your old password is wrong"
            return render(request,'change-password.html',{'msg':msg})
    else:
        return render(request,'change-password.html')
    

def forgotPassword(request):
    if request.method == "POST":
        try:
            user = User.objects.get(email = request.POST['email'])
            otp = random.randint(1000,9999)
            message = 'Your OTP for forgot password'+ str(otp) 
            send_mail('OTP for forgot password', message, settings.EMAIL_HOST_USER, [user.email,])
            request.session['email'] = user.email 
            request.session['otp'] = otp
            return render(request,'otp.html')

        except:
            msg="Email not registered"
            return render(request,'forgot-password.html',{'msg':msg})    
    else:
        return render(request,'forgot-password.html') 
    

def verifyOtp(request):
    if int(request.session['otp']) == int(request.POST['otp']):
        del request.session['otp']
        msg = "Create your new password"
        return render(request,'new-password.html',{'msg':msg}) 
    else:
        msg="Invalid OTP"
        return render(request,'otp.html',{'msg':msg}) 
    

def newPassword(request):
    if request.POST['new_password'] == request.POST['cnew_password']:
        user = User.objects.get(email = request.session['email'])
        user.password = request.POST['new_password']
        user.save()
        msg= "Your password successfully changed"
        del request.session['email']
        return render(request,'login.html',{'msg':msg})
    else:
        msg="New password and confirm new password does not matched"
        return render(request,'new-password.html')

def profile(request): 
    user = User.objects.get(email=request.session['email'])
    if request.method == 'POST':
        user.fname = request.POST['fname']
        user.lname = request.POST['lname']
        user.mobile = request.POST['mobile']
        user.address = request.POST['address']
        try:
            user.profile_picture = request.FILES['profile_picture']
        except:
            pass 
        user.save()
        request.session['profile_picture'] = user.profile_picture.url 
        msg = 'profile updated successfully'
        return render(request,'profile.html',{'user':user,'msg':msg})

    else:
        return render(request,'profile.html',{'user':user})