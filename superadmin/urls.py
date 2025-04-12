from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('logout',views.logout,name='logout'),
    path('lw',views.lw,name='lw'),
    path('deposit',views.deposit,name='deposit'),
    path('depinfo/<str:id>',views.depinfo,name='depinfo'),
    path('withdraw',views.withdraw,name='withdraw'),
    path('withinfo/<str:id>',views.withinfo,name='withinfo'),
    path('delete/<str:id>',views.delete,name='delete'),
    path('backupt',views.backupt,name='backupt'),
    path('backupinfo/<str:id>',views.backupinfo,name='backupinfo'),
    path('backupw',views.backupw,name='backupw'),
    path('backupwinfo/<str:id>',views.backupwinfo,name='backupwinfo'),
    path('addf',views.addf,name='addf'),
    path('adds',views.adds,name='adds'),
    path('addb',views.addb,name='addb'),
    path('addbs',views.addbs,name='addbs'),
    path('setting',views.setting,name='setting'),
    path('cardmake',views.cardmake,name='cardmake'),
    path('cardhis',views.cardhis,name='cardhis'),
    path('cardde/<str:id>',views.cardde,name='cardde'),
    path('alluser',views.alluser,name='alluser'),
]