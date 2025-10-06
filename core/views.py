from django.shortcuts import redirect,render,HttpResponse
from django.views import View
from .models import student
from .forms import AddstudentForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class Signup(View):
    def get(self,request):
        return render(request,'core/SignUp.html')

    def post(self,request):         
        if request.method=='POST':
            uname=request.POST.get('username')
            email=request.POST.get('email')
            pass1=request.POST.get('password')
            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            
            print(uname,email,pass1)
            return redirect('login')  
        return render(request,'core/SignUp.html')

class Login(View):
    def get(self,request):
        return render(request,'core/SignUp.html')

    def post(self,request):         
        if request.method=='POST':
            uname=request.POST.get('username')
            pass1=request.POST.get('pass')
            user = authenticate(request,username=uname,password=pass1)
            if user is not None:
                login(request,user)
                return redirect('home')
            else:
                return HttpResponse("Entered Credentials are not Correct")
        return render(request,'core/SignUp.html')          
                
    #@login_required(login_url='login')
class Home(LoginRequiredMixin,View):
    def get(self, request):
        stu_data =student.objects.all()
        return render ( request, 'core/home.html',{'studata':stu_data} )

class Add_student(View):
    def get(self, request):
        fm =  AddstudentForm()
        return render ( request, 'core/add_student.html',{'form':fm} )
    
    def post(self,request):
        fm= AddstudentForm(request.POST)
        if fm.is_valid():
            fm.save()
            return redirect('/home')
        else:
            return render(request, 'core/add_student.html',{'form':fm})  

class Delete_student(View):
    def post(self,request):
        data=request.POST
        id=data.get('id')
        studata  = student.objects.get(id=id)
        studata.delete()
        return redirect('/home')     

class Editstudent(View):
    def get(self,request,id):
        stu= student.objects.get(id=id)
        fm = AddstudentForm(instance=stu)
        return render(request, 'core/edit_student.html',{'form':fm})    
    
    def post(self,request,id):
        stu =student.objects.get(id=id)
        fm=AddstudentForm(request.POST,instance=stu)
        if fm.is_valid():
            fm.save()
            return redirect('/home')
      
def Logout(request):
    logout(request)
    return redirect('login')