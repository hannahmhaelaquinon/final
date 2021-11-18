from django.shortcuts import render
from django.core.checks import messages
from django.contrib import messages
from django.shortcuts import render, HttpResponse
from django.views.generic import View
from .form import *
from django.shortcuts import redirect
# from django.contrib.auth import authenticate, login, logout
import mysql.connector

from operator import itemgetter

# Create your views here.



#LANDING PAGE==================================================================================================================================
class MyIndexView(View):
    def get(self,request):
        return render(request, 'index.html')

    def post(self, request):        
        form = RegistrationsForm(request.POST)        
      
        if form.is_valid():
            # try:
            ID_Number = request.POST.get("ID_Number")
            fName = request.POST.get("fName")
            plateNum = request.POST.get("plateNum")
            vType = request.POST.get("vType")

            form = Registrations(ID_Number = ID_Number, fName = fName, plateNum = plateNum, vType = vType)
            form.save()

                 
            return redirect('my_index_view')
          
        else:
            print(form.errors)
            return HttpResponse('not valid')

#LAnding Page When User Signs in
class MyIndexView2(View):
    def get(self, request):
        return render(request, 'index2.html')

    def post(self, request):
        form = RegistrationsForm(request.POST)

        if form.is_valid():
            fName = request.POST.get("fName")
            ID_Number = request.POST.get("ID_Number")
            plateNum = request.POST.get("plateNum")
            vType = request.POST.get("vType")

            form = Registrations(fName = fName, ID_Number = ID_Number, plateNum = plateNum,
                        vType= vType)

            form.save()

            return redirect('Dashboard_View')

        else:
            print(form.errors)
            return HttpResponse('not valid')

class SignupView(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        form = UserForm(request.POST)

        if form.is_valid():
            fname = request.POST.get("fname")
            lname = request.POST.get("lname")
            Uname = request.POST.get("Uname")
            Pass = request.POST.get("Pass")
            email = request.POST.get("email")

            form = User(fname = fname, lname = lname, Uname = Uname,
                        Pass= Pass, email = email)

            form.save()

            return redirect('my_login_view')

        else:
            print(form.errors)
            return HttpResponse('not valid')

# AYUHONON ANG LOG IN

def login(request):
        con = mysql.connector.connect(host="localhost",user="root",passwd="", database="dbsampol")
        cursor=con.cursor()
        con2 = mysql.connector.connect(host="localhost",user="root",passwd="", database="dbsampol")
        cursor2=con2.cursor()
        sqlcommand="SELECT Uname from sampolapp_user"
        sqlcommand2="SELECT Pass from sampolapp_user"
        cursor.execute(sqlcommand)
        cursor2.execute(sqlcommand2)
        u=[]
        p=[]

        for i in cursor:
            u.append(i)

        for j in cursor2:
            p.append(j)

        res= list(map(itemgetter(0),u))
        res2= list(map(itemgetter(0),p))


        if request.method=="POST":
            Uname = request.POST.get("Uname")
            pword = request.POST.get("Pass")
            i=1
            k=len(res2)
            while i<k:
                if res[i] == Uname and res2[i] == pword:
                    return render(request,'index2.html',{'Uname': Uname})
                    break
                i+=1
            else:
                messages.info(request,"*Check Username or Password*")
    

        return render(request,'login.html')



def dashboard(request):
    return render(request, 'dashboard.html')

#DASHBOARD VIEWS =========================================================================================================================

#User Dashboard
       
class UserDashboardView1(View):
    def get(self,request):    
        user = User.objects.all()
        registrations = Registrations.objects.all()
        return render(request, 'Dashboard1.html',{"user" : user, "registrations" : registrations})

    def post(self, request):
                    if request.method == 'POST':
                        if 'btnUpdate' in request.POST: 
                            print('update profile button clicked')
                            uid = request.POST.get("user-id")            
                            fname = request.POST.get("user-fname")            
                            lname = request.POST.get("user-lname")
                            Uname = request.POST.get("user-Uname")
                            Pass = request.POST.get("user-Pass")
                            email = request.POST.get("user-email")
                            print(email)
                # email = request.POST.get("student-email")
                # phone = request.POST.get("student-phone")
                            update_User = User.objects.filter(id = uid).update(fname = fname, lname = lname,
                            Uname = Uname, Pass = Pass, email = email)
                            print(update_User)
                            print('profile updated')
                        elif 'btnDelete' in request.POST:
                            print('delete button clicked')
                        uid = request.POST.get("uuser-id")
                        book = User.objects.filter(id = uid).delete()
                        # return redisrect('my_user_view')

                    if request.method == 'POST':
                        if 'btnUpdate2' in request.POST: 
                            print('update profile button clicked')
                            rid = request.POST.get("reg-id")            
                            ID_Number = request.POST.get("reg-ID_Number")            
                            fName = request.POST.get("reg-fName")
                            plateNum = request.POST.get("reg-plateNum")
                            vType = request.POST.get("reg-vType")

                            print(vType)
                # email = request.POST.get("student-email")
                # phone = request.POST.get("student-phone")
                            update_Registration = Registrations.objects.filter(id = rid).update(ID_Number = ID_Number, fName = fName,
                            plateNum = plateNum, vType = vType)
                            print(update_Registration)
                            print('profile updated')
                        elif 'btnDelete2' in request.POST:
                            print('delete button clicked')
                        uid = request.POST.get("rreg-id")
                        book = Registrations.objects.filter(id = uid).delete()
                        return redirect('my_dash_view')


#dashboards
def UserDashboard(request):
    user = User.objects.all()
    context = {
        'user': user,
    }
    return render(request, 'User/UserDashboard.html',context)

def RegistrationDashboard(request):
    registrations = Registrations.objects.all()
    context = {
        'registrations' : registrations,
    }
    return render(request, 'Registration/RegistrationDashboard.html', context)

#Edit
def editUser(request, id):
    user = User.objects.get(id = id)
    context = {
        'user': user
    }
    return render(request,'User/EditUser.html',context)

def updateUser(request, id):  
    user = User.objects.get(id = id)
    form = UserForm(request.POST, instance = user)  
    if form.is_valid():  
        form.save()  
        return redirect('UserDashboard_View')  
    return render(request, 'User/EditUser.html', {'user': user}) 

#EDIT REGISTRATIONS
def editRegistration(request, id):
    registrations = Registrations.objects.get(id = id)
    context = {
        'registrations': registrations
    }
    return render(request,'Registration/EditRegistration.html',context)

def updateRegistration(request, id):  
    registrations = Registrations.objects.get(id = id)
    form = RegistrationsForm(request.POST, instance = registrations)  
    if form.is_valid():  
        form.save()  
        return redirect('RegistrationDashboard_View')  
    return render(request, 'Registration/EditRegistration.html', {'registrations': registrations})  

#DELETE
def deleteUser(request, id):
    user = User.objects.get(id = id)
    user.delete()
    return redirect('UserDashboard_View')

def deleteRegistrations(request, id):
    registrations = Registrations.objects.get(id = id)
    registrations.delete()
    return redirect('RegistrationDashboard_View')

#FOR QR
def qr(request):
    return render(request, 'qr.html')


def GetRegistrationQr(request, id):
    register = Registrations.objects.get(id = id)
    context = {
        'register': register
    }
    return render(request,'qr.html',context)
