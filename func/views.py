#coding:utf-8
from django.http import HttpResponse
from django.shortcuts import render
from .models import Func
import MySQLdb
import xlrd

from django import forms
from django.utils.translation import gettext as _
from django.core.exceptions import ValidationError
def validate_excel(value):
    if value.name.split('.')[-1] not in ['xls','xlsx']:
        raise ValidationError(_('Invalid File Type: %(value)s'),params={'value': value},)

class UploadExcelForm(forms.Form):
    excel = forms.FileField(validators=[validate_excel]) #这里使用自定义的验证


def chaxunhome(request):
    return render(request,'chaxun.html')


def chaxun(request):
    uname=request.POST['uname']
    print(uname)
    db = MySQLdb.connect("*", "*", "*", "*", charset='utf8')
    cursor = db.cursor()
    sql = "select person.name name ,company.name cname,person.intro intro from person_company,person,company where person_company.person_id=person.id and person_company.company_id=company.id and person.name='%s' " %(uname)
    cursor.execute(sql)
    print(sql)
    res = cursor.fetchall()
    num=0
    ans=[]
    for info in res:
        ans.append(info)
        num+=1
    db.close()
    if num==0:
        return HttpResponse('不存在')
    return render(request,'demo1.html',{'data':ans})


def tianjiahome(request):
    return render(request,'tianjia.html')


def tianjia(request):
    name = request.POST['name']
    intro = request.POST['intro']
    phone = request.POST['phone']
    email = request.POST['email']
    wechat = request.POST['wechat']
    linkedin = request.POST['linkedin']
    address = request.POST['address']
    db = MySQLdb.connect("", "*", "*", "*", charset='utf8')
    cursor = db.cursor()
    sql = "insert into person(name,intro,phone,email,wechat,linkedin,address) values('%s','%s','%s','%s','%s','%s','%s')" %(name,intro,phone,email,wechat,linkedin,address);
    cursor.execute(sql)
    db.commit()
    sql2="insert into logdemo(log_info) values(%s)"
    cursor.execute(sql2, (sql,))
    db.commit()
    db.close()
    return HttpResponse('添加成功')


def xiugaihome(request):
    return render(request, 'xiugaiid.html')


def xiugai(request):
    name=request.POST['name']
    db = MySQLdb.connect("*", "*", "*", "*", charset='utf8')
    cursor = db.cursor()
    sql = "select * from person where name='%s'" %(name)
    cursor.execute(sql)
    res=cursor.fetchall()
    ans=[]
    for i in res:
        ans.append(i)
    print(ans)
    db.close()
    #return render(request,'xiugai.html', {"id":id,"name":res[1],"intro":res[3],"phone":res[4],"email":res[5],"wechat":res[6],"linkedin":res[7],"address":res[8]})
    return render(request,'xiugaitmp.html',{'data':ans})

def xiugai2(request):
    id = request.POST['id']
    name = request.POST['name']
    intro = request.POST['intro']
    phone = request.POST['phone']
    email = request.POST['email']
    wechat = request.POST['wechat']
    linkedin = request.POST['linkedin']
    address = request.POST['address']
    db = MySQLdb.connect("*", "*", "*", "*", charset='utf8')
    cursor = db.cursor()
    sql = "update person set name = '%s',intro ='%s',phone='%s',email='%s',wechat='%s',linkedin='%s',address='%s' where id='%s'" %(name,intro,phone,email,wechat,linkedin,address,id)
    cursor.execute(sql)
    db.commit()
    sql2="insert into logdemo(log_info) values(%s)"
    cursor.execute(sql2, (sql,))
    db.commit()
    db.close()
    return render(request,'xiugai.html')


def xiugai3(request):
    id = request.POST['id']
    name = request.POST['name']
    intro = request.POST['intro']
    phone = request.POST['phone']
    email = request.POST['email']
    wechat = request.POST['wechat']
    linkedin = request.POST['linkedin']
    address = request.POST['address']
    return render(request,'xiugai.html',{"id":id,"name":name,"intro":intro,"phone":phone,"email":email,"wechat":wechat,"linkedin":linkedin,"address":address})


def hebing(request):
    name=request.POST['name']
    db = MySQLdb.connect("*", "*", "*", "*", charset='utf8')
    cursor = db.cursor()
    sql = "select * from person where name= '%s'"%(name)
    cursor.execute(sql)
    res=cursor.fetchall()
    ans=[]
    for i in res:
        ans.append(i)
        print(i)
    db.close()
    return render(request,'hebing.html',{'data':ans})


def hebinghome(request):
    return render(request,'hebinghome.html')


def hebing3(request):
    id1=request.POST['id1']
    id2=request.POST['id2']
    db = MySQLdb.connect("*", "*", "*", "*", charset='utf8')
    cursor = db.cursor()
    sql1 = "select * from person where id= '%s'" % (id1)
    cursor.execute(sql1)
    res1=cursor.fetchone()
    sql2= "select * from person where id= '%s'" % (id2)
    cursor.execute(sql2)
    res2=cursor.fetchone()
    return render(request,'hebing3.html',{'name1':res1[1],'intro1':res1[3],'phone1':res1[4],'email1':res1[5],'wechat1':res1[6],'linkedin1':res1[7],'address1':res1[8],
                                          'name2': res2[1], 'intro2': res2[3], 'phone2': res2[4], 'email2': res2[5],
                                          'wechat2': res2[6], 'linkedin2': res2[7], 'address2': res2[8],'id1':id1,'id2':id2})



#复选框
def hebing4(request):
    id1=request.POST['id1']
    id2=request.POST['id2']
    name=request.POST['name']
    intro=request.POST['intro']
    phone=request.POST['phone']
    email=request.POST['email']
    wechat=request.POST['wechat']
    linkedin=request.POST['linkedin']
    address=request.POST['address']
    db = MySQLdb.connect("*", "*", "*", "*", charset='utf8')
    cursor = db.cursor()
    sql ="update person set name = '%s',intro ='%s',phone='%s',email='%s',wechat='%s',linkedin='%s',address='%s' where id='%s'" %(name,intro,phone,email,wechat,linkedin,address,id1)
    cursor.execute(sql)
    db.commit()
    sql2="insert into logdemo(log_info) values(%s)"
    cursor.execute(sql2, (sql,))
    db.commit()

    sql="delete from person where id='%s'"%(id2)
    cursor.execute(sql)
    db.commit()
    sql2="insert into logdemo(log_info) values(%s)"
    cursor.execute(sql2, (sql,))
    db.commit()
    db.close()
    return HttpResponse('合并成功')


def piliang(request):
    form = UploadExcelForm(request.POST, request.FILES)
    res=[]
    ans=[]
    aans={}
    les=[]
    if form.is_valid():
        wb = xlrd.open_workbook(
        filename=None, file_contents=request.FILES['excel'].read())
        table = wb.sheets()[0]
        row = table.nrows
        for i in range(1, row):
            col = table.row_values(i)
            res.append(col)
        for re in res:
            tmp=[]
            tmp.append(re[0])
            tmp.append(re[1])
            ans.append(tmp)


        db = MySQLdb.connect("*", "*", "*", "*", charset='utf8')
        cursor = db.cursor()
        for i in ans:
            tmp=[]
            sql = "select person.id id,person.name name ,company.name cname,person.intro intro from person_company,person,company where person_company.person_id=person.id and person_company.company_id=company.id and person.name='%s' and (company.name like '%%%s%%' or company.full_name like '%%%s%%');" %(i[0],i[1],i[1])
            cursor.execute(sql)
            re=cursor.fetchall()
            num=0
            for j in re:
                tmp.append(j)
                num+=1
            if num==0:
                les.append(i[0]+'-'+i[1])
            else:
                aans[(i[0],i[1])]=tmp
        db.close()
    return render(request, 'piliangans.html', {'data':aans,'les':les})



def pilianghome(request):
    return render(request,"pilianghome.html")


def piliang2(request):
    li = request.POST.getlist('check_box_list')
    db = MySQLdb.connect("*", "*", "*", "*", charset='utf8')
    cursor = db.cursor()
    for i in li:
        index=i.find('-')
        name=i[0:index]
        if index+1>=len(i):
            company=""
        else:
            company=i[index:]
        sql="insert into person(name,intro) values('%s','%s' )" %(name,company)
        cursor.execute(sql)
        sql2 = "insert into logdemo(log_info) values(%s)"
        cursor.execute(sql2, (sql,))
        db.commit()
    db.commit()
    db.close()
    return HttpResponse('添加成功')


def piliang4(request):
    return render(request,'xiugai.html')


def pilianghebing(request):
    name=[]
    intro=[]
    phone=[]
    email=[]
    wechat=[]
    linkedin=[]
    address=[]
    id=request.POST.getlist('ids')
    print()
    db = MySQLdb.connect("*", "*", "*", "*", charset='utf8')
    cursor = db.cursor()
    for i in id:
        sql="select * from person where id='%s'" %(i)
        cursor.execute(sql)
        re=cursor.fetchone()
        name.append(re[1])
        intro.append(re[3])
        phone.append(re[4])
        email.append(re[5])
        wechat.append(re[6])
        linkedin.append(re[7])
        address.append(re[8])
    db.close()
    return render(request,'pilianghebing.html',{'name':name,'intro':intro,'phone':phone,'email':email,'wechat':wechat,'linkedin':linkedin,'address':address,'id':id})


def pilianghebing2(request):
    id=request.POST.getlist('id')
    name=request.POST['name']
    intro=request.POST['intro']
    phone=request.POST['phone']
    email=request.POST['email']
    wechat=request.POST['wechat']
    linkedin=request.POST['linkedin']
    address=request.POST['address']
    db = MySQLdb.connect("*", "*", "*", "*", charset='utf8')
    cursor = db.cursor()
    sql ="update person set name = '%s',intro ='%s',phone='%s',email='%s',wechat='%s',linkedin='%s',address='%s' where id='%s'" %(name,intro,phone,email,wechat,linkedin,address,id[0])
    cursor.execute(sql)
    db.commit()
    sql2="insert into logdemo(log_info) values(%s)"
    cursor.execute(sql2, (sql,))
    db.commit()
    for item in id[1:]:
        sql="delete from person where id='%s'"%(item)
        cursor.execute(sql)
        db.commit()
        sql2 = "insert into logdemo(log_info) values(%s)"
        cursor.execute(sql2, (sql,))
        db.commit()
    db.close()
    return HttpResponse('OK')


def piliangtianjia(request):
    return HttpResponse('批量添加')