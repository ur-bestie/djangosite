from django.shortcuts import render,redirect
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.models import User,auth
from myapp.models import *
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.db.models import Sum

# Create your views here.
@staff_member_required
def index(request):
    x = depht.objects.all()
    td = len(x)
    tdp = td % 100
    b = backt.objects.all()
    tba = len(x)
    tbap = tba % 100
    u = User.objects.all()
    tu = len(u)
    tup = tu % 100
    w = waph.objects.all()
    wp = len(w)
    tw = withdh.objects.all()
    wb = len(tw)
    wbp = wb % 100
    bw = backwh.objects.all()
    tbt = len(bw)
    tbtp = tbt % 100

    totb = tbalance.objects.all()
    total_balance = 0.0
    for a in totb:
       X_total = a.amount
       total_balance += X_total
       total_balancep = total_balance % 100




    return render(request,'admin_temp/index.html',locals())

def logout(request):
    auth.logout(request)
    return redirect('/superadmin')

@staff_member_required
def lw(request):
    x = waph.objects.all()
    return render(request,'admin_temp/lw.html',locals())

@staff_member_required
def deposit(request):
    x = depht.objects.all()

    u = ucoin.objects.all()
    return render(request,'admin_temp/deposit.html',locals())

@staff_member_required
def depinfo(request,id):
    x = depht.objects.get(id=id)
    if request.method == 'POST':
     uid = request.POST.get('u_id')
     tb = request.POST.get('b_id')
     s = ucoin.objects.get(pk=uid)
     b = tbalance.objects.get(pk=tb)
     s.amount += x.amount
     s.save()
     b.amount += x.amount
     b.save()
     x.status = True
     x.save()
     return redirect('/superadmin/deposit')
    else:
     return render(request,'admin_temp/depinfo.html',locals())

@staff_member_required
def withdraw(request):
   x = withdh.objects.all()
   return render(request,'admin_temp/withdraw.html',locals())

@staff_member_required
def withinfo(request,id):
   x = withdh.objects.get(id=id)
   if request.method == 'POST':
     uid = request.POST.get('u_id')
     tb = request.POST.get('b_id')
     s = ucoin.objects.get(pk=uid)
     b = tbalance.objects.get(pk=tb)
     s.amount -= x.amount
     s.save()
     b.amount -= x.amount
     b.save()
     x.status = True
     x.save()
     messages.success(request,'successful')
     return redirect('/superadmin/withdraw')
   else:
    return render(request,'admin_temp/withinfo.html',locals())

@staff_member_required
def delete(request,id):
   x = withdh.objects.get(id=id)
   x.delete()
   messages.success(request,'Deleted')
   return redirect('/superadmin/withdraw')
def backupt(request):
   x = backt.objects.all()
   return render(request,'admin_temp/backup.html',locals())

@staff_member_required
def backupinfo(request,id):
   x = backt.objects.get(id=id)
   if request.method == 'POST':
     uid = request.POST.get('u_id')
     tb = request.POST.get('b_id')
     s = backup.objects.get(pk=uid)
     b = tbalance.objects.get(pk=tb)
     s.amount += x.amount
     s.save()
     b.amount += x.amount
     b.save()
     x.status = True
     x.save()
     messages.success(request,'successful')
     return redirect('/superadmin/backupt')
   else:
    return render(request,'admin_temp/backupinfo.html',locals())

@staff_member_required
def backupw(request):
   x = backwh.objects.all()
   return render(request,'admin_temp/backupw.html',locals())

@staff_member_required
def backupwinfo(request,id):
   x = backwh.objects.get(id=id)
   if request.method == 'POST':
     uid = request.POST.get('u_id')
     tb = request.POST.get('b_id')
     s = backup.objects.get(pk=uid)
     b = tbalance.objects.get(pk=tb)
     s.amount -= x.amount
     s.save()
     b.amount -= x.amount
     b.save()
     x.status = True
     x.save()
     messages.success(request,'successful')
     return redirect('/superadmin/backupw')
   else:
    return render(request,'admin_temp/backupwinfo.html',locals())

@staff_member_required
def addf(request):
   x = ucoin.objects.all()
   if request.method == 'POST':
      u_id = request.POST.get('u_id')
      ub_id = request.POST.get('ub_id')
      amount = request.POST.get('amount')
      uid = ucoin.objects.get(pk=u_id)
      ubb = tbalance.objects.get(pk=ub_id)
      uid.amount += float(amount)
      uid.balance.amount += float(amount)
      uid.save()
      ubb.amount += float(amount)
      ubb.save()
      messages.success(request,'successful')
      return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
   return render(request,'admin_temp/addf.html',locals())

@staff_member_required
def adds(request):
   if request.method == 'POST':
      u_id = request.POST.get('u_id')
      ub_id = request.POST.get('ub_id')
      amount = request.POST.get('amount')
      uid = ucoin.objects.get(pk=u_id)
      ubb = tbalance.objects.get(pk=ub_id)
      if float(amount) > uid.amount:
         messages.info(request,'insufficent funds')
         return redirect('/superadmin/addf')
      else:
         uid.amount -= float(amount)
         uid.save()
         ubb.amount -= float(amount)
         ubb.save()
         messages.success(request,'successful')
      return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
   return render(request,'admin_temp/adds.html',locals())

@staff_member_required
def addb(request):
   x = backup.objects.all()
   if request.method == 'POST':
      u_id = request.POST.get('u_id')
      ub_id = request.POST.get('ub_id')
      amount = request.POST.get('amount')
      uid = backup.objects.get(pk=u_id)
      ubb = tbalance.objects.get(pk=ub_id)
      uid.amount += float(amount)
      uid.balance.amount += float(amount)
      uid.save()
      ubb.amount += float(amount)
      ubb.save()
      messages.success(request,'successful')
      return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
   return render(request,'admin_temp/addb.html',locals())

@staff_member_required
def addbs(request):
   if request.method == 'POST':
      u_id = request.POST.get('u_id')
      ub_id = request.POST.get('ub_id')
      amount = request.POST.get('amount')
      uid = backup.objects.get(pk=u_id)
      ubb = tbalance.objects.get(pk=ub_id)
      uid.amount -= float(amount)
      uid.balance.amount -= float(amount)
      uid.save()
      ubb.amount -= float(amount)
      ubb.save()
      messages.success(request,'successful')
      return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
   return render(request,'admin_temp/addbs.html',locals())

@staff_member_required
def setting(request):
   x =  settings.objects.get_or_create()
   if request.method == 'POST':
      sitename = request.POST.get('sitename')
      siteemail = request.POST.get('siteemail')
      logo = request.FILES.get('logo')
      edit = settings.objects.get()

      edit.sitename = sitename
      edit.siteemail = siteemail
      edit.logo = logo
      edit.save()
      messages.success(request,'successful')
      return redirect('/superadmin/setting')
   else:
    return render(request,'admin_temp/setting.html',locals())

@staff_member_required
def cardmake(request):
   if request.method == 'POST':
      x = cardcreate(
         cardtype = request.POST.get('cardtype'),
         amount = request.POST.get('amount'),
         uniqcode1 = request.POST.get('uniqcode1'),
         uniqcode2 = request.POST.get('uniqcode2'),
         uniqcode3 = request.POST.get('uniqcode3'),
         uniqcode4 = request.POST.get('uniqcode4'),
         secretpin = request.POST.get('secretpin'),
         expdate = request.POST.get('expdate'),
         logo = request.FILES.get('logo'),
      )
      x.save()
      messages.success(request,'cardcreated successfully')
      return redirect('/superadmin/cardmake')
   return render(request,'admin_temp/cardcreate.html')

def cardhis(request):
   x = cardpay.objects.all()
   return render(request,'admin_temp/cardhis.html',locals())

@staff_member_required
def cardde(request, id):
   x = cardpay.objects.get(id=id)
   if request.method == 'POST':
      u_id = request.POST.get('u_id')
      uid = cardpay.objects.get(id=id)
      uid.status = True
      uid.save()
      messages.success(request,'successful')
      return redirect('/superadmin/cardhis')
   return render(request,'admin_temp/cardde.html',locals())


@staff_member_required
def alluser(request):
   x = User.objects.all()
   return render(request,'template/admin_temp/alluser.html',locals())