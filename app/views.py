# django mofules
from django.http import HttpResponse
from django.shortcuts import render, redirect
# models.py modules
from.models import CourseAddPage,SendRegistr
# forms.py modules
from .forms import ProjectForm, MessageForm
from django.contrib import messages
# login logout modules
from django.contrib.auth import login,logout
from app.EmailBackEnd import EmailBackEnd





# Login Logout ADMIN
def Login(request):
    if request.method == 'POST':
        user = EmailBackEnd.authenticate(request,
                                         username=request.POST.get('email'),
                                         password=request.POST.get('password'))
        if user != None:
            login(request, user)
            user_type = user.user_type
            if user_type == '1':
                return redirect('index')
            elif user_type == '2':
                return HttpResponse('This is Staff Panel')
            elif user_type == '3':
                return HttpResponse('This is Student Panel')
            else:
                messages.error(request, 'Email and Password Are Invalide !')
                return redirect('login_page')
        else:
            messages.error(request, 'Email and Password Are Invalide !')
            return redirect('login_page')

def Logout(request):
    logout(request)
    return redirect('index')
##################################################################

#Add Course ADMIN
def addProject(request):
    form = ProjectForm()

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('course')

    context = {'form': form}
    return render(request, 'project_form.html', context)

# Edit Course ADMIN
def editProject(request, pk):
    project = CourseAddPage.objects.get(id=pk)
    form = ProjectForm(instance=project)
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('course')

    context = {'form': form}
    return render(request, 'project_form.html', context)
##############################################################


# Register Course User
def RegisteForm(request):
    registe_form = CourseAddPage.objects.all()
    form = MessageForm()
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Siz muvafaqiyatloi ro\'yhatdan o\'tdingiz siz bilan MANAGER bog\'lanadi!.')
        return redirect('index')
    context = {
        'register_form':registe_form,
        'form':form,
    }
    return render(request,'form.html',context)
#######################################################################

# Send Message ADMIN
def inboxPage(request):
    inbox = SendRegistr.objects.all().order_by('is_read')
    unreadCount = SendRegistr.objects.filter(is_read=False).count()
    context = {'inbox': inbox, 'unreadCount': unreadCount}
    return render(request, 'inbox.html', context)


def messagePage(request, pk):
    message = SendRegistr.objects.get(id=pk)
    message.is_read = True
    message.save()
    context = {'message': message}
    return render(request, 'message.html', context)
############################################################



# All Templates
def Course(request):
    course_all = CourseAddPage.objects.all()
    context = {
        'course_all':course_all
    }
    return render(request,'courses.html',context)

def LOGINPAGE(request):
    return render(request,'login.html')

def Home(request):
    return render(request,'base.html')

def Index(request):
    return render(request,'index.html')

def About(request):
    return render(request,'about.html')

def Contact(request):
    return render(request,'contact.html')
###################################################
