from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from LearningManagementSytem.models import Category, SubCategory, UserProfile
from instructor.models import Courses, Lecture
from .models import Cart, Opted, Orders
from django.contrib.auth.models import User

import random
import datetime


@login_required(login_url = '/')
def stu_dashboard(request):
    uObj = UserProfile.objects.get(user__username=request.user)
    cartObj = Cart.objects.filter(user_id=uObj.id)
    items = []
    total = 0
    for i in cartObj:
        items.append(Courses.objects.get(id=i.course_id))
        cost = Courses.objects.get(id=i.course_id)
        total =+ cost.price

    cartlist = []
    for i in cartObj:
        cartlist.append(i.course_id)

    optObj  = Opted.objects.filter(added_by = uObj)
    optlist = []
    for i in optObj:
        optlist.append(Courses.objects.get(id = i.course_id))

    return  render(request, "studentdashboard.html", {'items':items, 'total':total, 'cartlist':cartlist,'optlist':optlist}) 

@login_required(login_url = '/')
def stu_courses(request):

    cou = Courses.objects.all()
    dict = {}
    for i in cou:
        a = UserProfile.objects.get(id = i.added_by_id)
        b = User.objects.get(id = a.user_id)
        dict[i] = b

    uObj = UserProfile.objects.get(user__username=request.user)
    cartObj = Cart.objects.filter(user_id=uObj.id)
    cartlist = []
    

    for i in cartObj:
        cartlist.append(i.course_id)
    items = []
    total = 0
    for i in cartObj:
        items.append(Courses.objects.get(id=i.course_id))
        cost = Courses.objects.get(id=i.course_id)
        total =+ cost.price

    optObj  = Opted.objects.filter(added_by = uObj)
    optlistid = []
    for i in optObj:
        j = Courses.objects.get(id = i.course_id)
        optlistid.append(j.id)

    return  render(request, "stu_course.html", {'cou': cou, 'dict':dict.items(), 'cartlist':cartlist, 'cartObj':cartObj,'items':items, 'total':total, 'optlistid':optlistid}) 

def add_cart(request, id):
    # try:
        cObj = Courses.objects.get(id=id)
        uObj = UserProfile.objects.get(user__username=request.user)

        c = Cart(course=cObj, user=uObj)
        c.save()
        return redirect('/student/courses/')
    # except:
    #     messages.error(request, "Aleady in your cart")
    #     return redirect('/buyer/')

def del_cart(request, id):
	uObj = UserProfile.objects.get(user__username=request.user)
	cObj = Courses.objects.get(id=id)

	c = Cart.objects.get(user=uObj, course=cObj)
	c.delete()
	return redirect('/student/dashboard/')

def cartcalculate(request):
    uObj = UserProfile.objects.get(user__username=request.user)
    cid = request.POST.getlist('cid')
    price = request.POST.get('price')

    pri = float(price)
    c = Cart.objects.filter(user_id = uObj.id)
    c.delete()   

    Or(pri, cid, uObj)
    # send_mail("Order Update", "Order has been placed!", "gpmishra9@gmail.com",["anshika97mishra@gmail.com",])

    return redirect('/student/dashboard/')

def Or(price, c_id, uObj):

    tdate = str(datetime.date.today()).replace("-", "")
    rnum = random.randint(100,999)
    # s = []

    # for i in range(len(prod_id)): 
    #     s.append(str(prod_id[i]))

    l = ''.join(c_id)

    or_id = tdate + "_" + l + "_" + str(rnum)

    O = Orders(order_id=or_id, total_amt=price, placed_by=uObj)
    O.save()

    for i in range(len(c_id)):
        Courses_obj = Courses.objects.get(id = c_id[i])
        Op = Opted(added_by=uObj, category_id=Courses_obj.category_id, subcategory_id=Courses_obj.subcategory_id, course_id=Courses_obj.id, order=O)
        Op.save()

@login_required(login_url = '/')
def up_profile(request):
    upObj = UserProfile.objects.get(user__username=request.user)
    uObj = User.objects.get(username = request.user)

    cartObj = Cart.objects.filter(user_id=upObj.id)
    cartlist = []
    for i in cartObj:
        cartlist.append(i.course_id)

    items = []
    total = 0
    for i in cartObj:
        items.append(Courses.objects.get(id=i.course_id))
        cost = Courses.objects.get(id=i.course_id)
        total =+ cost.price


    if request.method == "POST":
        d   = request.POST['mobile']
        e   = request.POST['gen']
        f   = request.POST['address']

        upObj.mobile = d
        upObj.gender = e
        upObj.address = f
        upObj.save()

        return redirect('/student/profile/')
    return render(request, "stu_profile.html", {'upObj' : upObj, 'uObj' : uObj, 'items':items, 'total':total, 'cartlist':cartlist,})

@login_required(login_url = '/')
def view_course(request, id):
    cou = Courses.objects.get(id = id)
    lect = Lecture.objects.filter(course_id = cou.id)

    upObj = UserProfile.objects.get(user__username=request.user)
    cartObj = Cart.objects.filter(user_id=upObj.id)
    cartlist = []
    for i in cartObj:
        cartlist.append(i.course_id)

    items = []
    total = 0
    for i in cartObj:
        items.append(Courses.objects.get(id=i.course_id))
        cost = Courses.objects.get(id=i.course_id)
        total =+ cost.price

    return render(request, "view_course.html", {'cou':cou, 'lect':lect, 'items':items, 'total':total, 'cartlist':cartlist,})

@login_required(login_url = '/')
def view_lecture(request, cid, id):
    cou = Courses.objects.get(id = cid)
    lect = Lecture.objects.get(id = id)

    upObj = UserProfile.objects.get(user__username=request.user)
    cartObj = Cart.objects.filter(user_id=upObj.id)
    cartlist = []
    for i in cartObj:
        cartlist.append(i.course_id)

    items = []
    total = 0
    for i in cartObj:
        items.append(Courses.objects.get(id=i.course_id))
        cost = Courses.objects.get(id=i.course_id)
        total =+ cost.price

    return render(request, "view_lecture.html", {'cou':cou, 'lect':lect, 'items':items, 'total':total, 'cartlist':cartlist,})

@login_required(login_url = '/')
def payment_history(request):
    
    upObj = UserProfile.objects.get(user__username=request.user)
    cartObj = Cart.objects.filter(user_id=upObj.id)
    cartlist = []
    for i in cartObj:
        cartlist.append(i.course_id)

    items = []
    total = 0
    for i in cartObj:
        items.append(Courses.objects.get(id=i.course_id))
        cost = Courses.objects.get(id=i.course_id)
        total =+ cost.price

    or_dict = {}

    orObj = Orders.objects.filter(placed_by = upObj)
    for i in orObj:
        optObj = Opted.objects.filter(order_id = i.id)
        couObj = []
        for j in optObj :
            couObj.append(Courses.objects.get(id = j.course_id))
        or_dict[i] = couObj
            

    return render(request, "stu_paymenthistory.html", {'items':items, 'total':total, 'cartlist':cartlist, 'or_dict': or_dict.items()})

@login_required(login_url = '/')
def filter(request):
    a = request.POST.get('filter')

    if a == "All":
        return redirect('/student/courses/')
    else:
        cou = Courses.objects.filter(level = a)
        dict = {}
        for i in cou:
            a = UserProfile.objects.get(id = i.added_by_id)
            b = User.objects.get(id = a.user_id)
            dict[i] = b

    uObj = UserProfile.objects.get(user__username=request.user)
    cartObj = Cart.objects.filter(user_id=uObj.id)
    cartlist = []
    

    for i in cartObj:
        cartlist.append(i.course_id)
    items = []
    total = 0
    for i in cartObj:
        items.append(Courses.objects.get(id=i.course_id))
        cost = Courses.objects.get(id=i.course_id)
        total =+ cost.price

    optObj  = Opted.objects.filter(added_by = uObj)
    optlistid = []
    for i in optObj:
        j = Courses.objects.get(id = i.course_id)
        optlistid.append(j.id)

    return  render(request, "stu_filter.html", {'cou': cou, 'dict':dict.items(), 'cartlist':cartlist, 'cartObj':cartObj,'items':items, 'total':total, 'optlistid':optlistid}) 
