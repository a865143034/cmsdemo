from django.urls import path
from . import views

urlpatterns = [
    path('chaxun/',views.chaxunhome),
    path('chaxun/ans',views.chaxun),
    path('tianjia/',views.tianjiahome),
    path('tianjia/ans',views.tianjia),
    path('xiugai/',views.xiugaihome),
    path('xiugai/ans',views.xiugai),
    path('xiugai/2',views.xiugai2),
    path('hebing/',views.hebinghome),
    path('hebing/2',views.hebing),
    path('hebing/3',views.hebing3),
    path('hebing/4',views.hebing4),
    path('piliang',views.pilianghome),
    path('piliang/2',views.piliang),
    path('piliang/3',views.piliang2),
    path('piliang/4',views.xiugai),
    path('piliang/5',views.pilianghebing),
    path('piliang/6',views.pilianghebing2),
    path('piliang/7',views.piliangtianjia),
    path('xiugai/3',views.xiugai3),
]
