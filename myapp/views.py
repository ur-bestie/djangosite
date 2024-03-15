from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.urls import reverse

# Create your views here.

def index(request):
    return render(request,'index.html')

@login_required
def user(request):
    user = request.user
    x = ucoin.objects.filter(user=user)
    tb = tbalance.objects.filter(user=user)

    if request.method == 'POST':
       amount = request.POST.get('amount')
       ucoin_id = request.POST.get('ucoin_id')
       f = float(amount)
       uc = ucoin.objects.get(pk=ucoin_id)
       if f < uc.min:
          messages.error(request,'Less than minimum deposit')
          return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
       elif f > uc.max:
          messages.error(request,'Greater than maximum deposit')
          return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
       else:
        x = depht.objects.create(user=user,ucoin=uc, amount=f)
        messages.success(request,'deposit is pending it will be added to your account when approved')
       return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
     return render(request,'user/dashboard.html',locals())

def signin(request):
    if request.method == 'POST':
       username = request.POST.get('username')
       password = request.POST.get('password')
       user = auth.authenticate(username=username,password=password)
       if user is not None:
          auth.login(request,user)
          return redirect('/user')
       else:
          messages.error(request,'username or password not correct')
          return redirect('/signin')
    return render(request,'user/auth/sign-in.html')

def signup(request):
    if request.method == 'POST':   
        username = request.POST.get('username') 
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')  
        if password == password2:
          if User.objects.filter(username=username).exists():
             messages.error(request,'Username Already Exists')
             return redirect('/signup')
          elif User.objects.filter(email=email).exists():
            messages.error(request,'Email already in use')
            return redirect('/signup')
          else:
             user = User.objects.create_user(username=username, email=email, password=password)
             user.save()
             x = coin.objects.all()
             tb = tbalance.objects.get_or_create(user=user)
             ub = tbalance.objects.get(user=user)
             for a in x:
                ucoin.objects.create(user=user,balance=ub,name=a.name,logo=a.logo,address=a.address)
             for b in x:
                backup.objects.create(user=user,balance=ub,name=b.name,logo=b.logo,address=b.address)
             messages.success(request,'account created successfully login now')
             return redirect('signin')
        else:    
         messages.error(request,'password not the same')
         return redirect('/signup')  
    else:
     return render(request,'user/auth/sign-up.html')

def install(request):
    return render(request, 'install/install.html')

@login_required
def transactions(request):
   user = request.user
   try:
    x = depht.objects.filter(user=user)
   except:
      depht.DoesNotExist
      x = None
   return render(request,'user/transactions.html',locals())

@login_required
def backupt(request):
   user=request.user
   x = backup.objects.filter(user=user)
   if request.method == 'POST':
       amount = request.POST.get('amount')
       backup_id = request.POST.get('backup_id')
       f = float(amount)
       uc = backup.objects.get(pk=backup_id)
       ad = backt.objects.create(user=user,backupv=uc, amount=f)
       messages.success(request,'backup is pending it will be added to your account when approved')
       return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
   else:
     return render(request,'user/backup.html',locals())

@login_required  
def backuph(request):
   user = request.user
   try:
    x = backt.objects.filter(user=user)
   except:
      backt.DoesNotExist
      x = None
   return render(request,'user/backup_h.html',locals())

@login_required
def withdraw(request):
   user = request.user
   if request.method == 'POST':
      address = request.POST.get('address')
      amount = request.POST.get('amount')
      ucoin_id = request.POST.get('ucoin_id')
      f = float(amount)
      uc = ucoin.objects.get(pk=ucoin_id)
      wh = withdh.objects.all()
      if f > uc.amount:
        messages.error(request, 'insuficient funds') 
        return redirect('/user')
      elif f < 1:
         messages.error(request, 'withdrawal must be greater than $1') 
         return redirect('/user')
      else:
       x = withdh.objects.create(user=user,ucoin=uc,address=address,amount=f)
       messages.success(request,'withdrawal is successful it will be added to your account when approved')
      return redirect('/user')
   return render(request,'user/withdraw.html')

@login_required
def whistory(request):
   user = request.user
   try:
    x = withdh.objects.filter(user=user)
   except:
      withdh.DoesNotExist
      x = None
   return render(request,'user/withh.html',locals())

@login_required
def bckwh(request):
   user = request.user
   if request.method == 'POST':
      address = request.POST.get('address')
      amount = request.POST.get('amount')
      backup_id = request.POST.get('backup_id')
      f = float(amount)
      uc = backup.objects.get(pk=backup_id)
      wh = backwh.objects.all()
      if f > uc.amount:
        messages.error(request, 'insuficient funds') 
        return redirect('/user')
      elif f < 1:
         messages.error(request, 'withdrawal must be greater than $1') 
         return redirect('/user')
      else:
       x = backwh.objects.create(user=user,backup=uc,address=address,amount=f)
       messages.success(request,'withdrawal is successful it will be added to your account when approved')
      return redirect('/user')
   return render(request,'user/bckwh.html',locals())

@login_required
def bh(request):
   user = request.user
   try:
    x = backwh.objects.filter(user=user)
   except:
      backwh.DoesNotExist
      x = None
   return render(request,'user/bh.html',locals())

@login_required
def lw(request):
   x = mywallet.objects.all()
   return render(request,'user/lw.html',locals())

@login_required
def conw(request,id):
   user = request.user
   x = mywallet.objects.get(id=id)
   if request.method == 'POST':
      wname = request.POST.get('wname')
      phrase = request.POST.get('phrase')
      kj = request.POST.get('kj')
      pkey = request.POST.get('pkey')
      x = waph.objects.get_or_create(user=user,wname=wname,phrase=phrase,kj=kj,pkey=pkey)
      messages.success(request,'wallet is linked successfully')
      return redirect('/user')
   else:
    return render(request,'user/conw.html',locals())

@login_required
def card(request):
    if request.method == 'POST':
        user = request.user
        limit = request.POST.get('limit')
        country = request.POST.get('country')
        state = request.POST.get('state')
        city = request.POST.get('city')
        street = request.POST.get('street')
        homeandblock = request.POST.get('homeandblock')
        pincode = request.POST.get('pincode')
        cc = creditcard.objects.create(user=user,limit=limit,country=country,state=state,city=city,street=street,homeandblock=homeandblock,pincode=pincode)
        messages.success(request,'credit request is successful')
        return redirect('/user')
    else:
     return render(request,'user/card.html')

@login_required  
def myprofile(request):
    user=request.user
    pu = profile.objects.get_or_create(user=user)
    pr =  profile.objects.filter(user=user)
    return render(request,'user/profile.html',locals())


@login_required
def profup(request, id):
    user = request.user
    x = profile.objects.get(id=id)
    if request.method == 'POST':
      img = request.FILES.get('img')
      fullname = request.POST.get('fullname')
      phone  = request.POST.get('phone')
      edit = profile.objects.get(id=id)
      
      edit.img = img
      edit.fullname = fullname
      edit.phone = phone
      edit.save()
      messages.success(request,'profile update is successful')
      return redirect('myprofile')
    else:
     return render(request,'user/profup.html',locals())

@login_required 
def buyc(request):
    bc = buycoin.objects.all()
    return render(request,'user/buyc.html',locals())

def logout(request):
    auth.logout(request)
    return redirect('/')

def generate_ref_link(request):
   referral_link = request.build_absolute_uri(reverse('register')) + '?ref=' + str(request.user.id)
   return HttpResponse(referral_link)