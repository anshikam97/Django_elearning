from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from LearningManagementSytem.models import Category, SubCategory, UserProfile
from .models import Courses, Lecture
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.db.utils import IntegrityError

from rest_framework.generics import ListAPIView
from .serializers import *

@login_required(login_url = '/home/')
def tech_dashboard(request):
    try:
        cat = Category.objects.all()
        subc = SubCategory.objects.all()
        uObj = UserProfile.objects.get(user__username=request.user)
        cou = Courses.objects.filter(added_by_id = uObj.id)
        print(cou)

        if request.method == "POST":
            a = request.POST['title']
            b = request.POST['des']
            c = request.FILES['c_img']
            d = request.POST['cat']
            e = request.POST['subcat']
            h = request.POST['level']
            i = request.POST['paidunpaid']
            j = request.POST['price']

            f = Category.objects.get(id = d)
            g = SubCategory.objects.get(id = e)

            u = Courses(title=a, description=b, course_img=c, category=f, subcategory=g, added_by=uObj, level=h, paid=i, price=j)
            u.save()

            mes  = "The Course is successfully added {}".format(u.title)

            messages.info(request, "{}".format(mes))
            return redirect("/instructor/dashboard/")
    except IntegrityError:
            messages.error(request,'Title is not unique')
            return redirect("/instructor/dashboard/")


    return render(request, "teacherdashboard.html", {'cou':cou, 'subc':subc, 'cat':cat})   

@login_required(login_url = '/home/')
def manage_course(request,id):
    cou = Courses.objects.get(id = id)
    lect = Lecture.objects.filter(course_id = cou.id)

    return render(request, "add_course.html", {'cou':cou,  'lect':lect})

@login_required(login_url = '/home/')
def manage_lecture(request,cid,id):
    cou = Courses.objects.get(id = cid)
    lect = Lecture.objects.get(id = id)

    return render(request, "show_lecture.html", {'cou':cou,'lect':lect})

@login_required(login_url = '/home/')
def add_lecture(request):
    a = request.POST.get('title')
    b = request.FILES.get('vid')
    c = request.POST.get('descp')

    f = request.POST.get('cid')
    i = Courses.objects.get(id = f)

    u = Lecture(title=a, video=b, description=c, course=i )
    u.save()

    mes  = "The lecture is successfully added {} in {}".format(u.title, i.title)

    messages.info(request, "{}".format(mes))
    print(i.id)

    return redirect('instructor:manage_course', id=i.id)

@login_required(login_url = '/home/')
def lec_del(request):
    a = request.POST.get('lecid')
    b = request.POST.get('couid')

    u = Lecture.objects.get(id = a)
    u.delete()

    cou = Courses.objects.get(id = b)

    mes  = "The lecture is successfully deleted"

    messages.info(request, "{}".format(mes))

    return redirect('instructor:manage_course', id=cou.id)

@login_required(login_url = '/home/')
def up_profile(request):
    upObj = UserProfile.objects.filter(user__username=request.user)
    uObj = User.objects.filter(username = request.user)
    if request.method == "POST":
        d   = request.POST['mobile']
        e   = request.POST['gen']
        f   = request.POST['address']

        upObj.update(mobile=d, gender=e, address=f)

        mes  = "Your Profile is updated"

        messages.info(request, "{}".format(mes))

        return redirect('/instructor/profile/')
    return render(request, "acc_update.html", {'upObj' : upObj, 'uObj' : uObj,})

@login_required(login_url = '/home/')
def edit_lecture(request):
    a = request.POST.get('title')
    b = request.POST.get('descp')
    c = request.POST.get('lecid')
    d = request.POST.get('cid')

    e = Lecture.objects.filter(id = c)
    print(e)
    e.update(title=a, description=b)

    mes  = "The lecture is successfully edited"

    messages.info(request, "{}".format(mes))
    
    return redirect('instructor:manage_lecture', cid=d, id=c)

def edit_course(request):

    try:
        b = request.POST.get('descp')
        c = request.FILES['c_img']
        d = request.POST.get('cid')
        print(c)
        e = Courses.objects.get(id = d)
        e.description = b 
        e.course_img = c
        e.save()
        # e.update(description=b, course_img=c)

        # mes  = "The course is successfully edited"

        # messages.info(request, "{}".format(mes))
        
        return redirect('instructor:manage_course', id=d)

    except IntegrityError:
            messages.error(request,'Title is not unique')
            return redirect('instructor:manage_course', id=d)  

class CourseLecture(ListAPIView):
    queryset = Lecture.objects.all()
    serializer_class = LectureSerializer