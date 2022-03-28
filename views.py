import re
from django.forms import EmailInput
from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth
from django.contrib import messages
from aicteapp.models import AuditoriumData, EventRegistration, GeneralDetails
# import mysql.connector as sql

# Create your views here.

# Home Page
def home(request):
    return render(request, 'aicteapp/landingpage.html')

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('coordinatordb')
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('signin')

    else:
        return render(request,'aicteapp/login.html')

def signup(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if(password1 == password2):
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect('home')

            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email Taken')
                return redirect('home')

            else:
                user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name,last_name=last_name)
                user.save()
                print('User Created')
    

    return render(request, 'aicteapp/register.html')

def coordinatordb(request):
    return render(request, 'aicteapp/coordinatordb.html')


def coordinatorevent(request):
    user = request.user
    eventlist = EventRegistration.objects.filter(username = user,userid = user.id)
    return render(request, 'aicteapp/coordinatorevent.html',{'eventlist':eventlist})


# def updatecoordinatorprofile(request,username):

#     coordinatordata = GeneralDetails.objects.filter(username = username)
#     print(coordinatordata)

#     if request.method == 'POST':
#         # m = sql.connect(host="localhost",user="root",password="admin@123", database= "aicte")
#         # cursor = m.cursor()
#         username = coordinatordata.username
#         firstname =request.POST['firstname']
#         lastname =request.POST['lastname']
#         gender =request.POST['gender']
#         phonenumber =request.POST['phonenumber']
#         email = request.POST['email']
#         dob = request.POST['dob']
#         fathername = request.POST['fathername']
#         city = request.POST['city']
#         address = request.POST['address']
#         state = request.POST['state']
#         district = request.POST['district']
#         alternameemail = request.POST['alternateemail']
#         whatsappnumber = request.POST['whatsappnumber']
#         institutename = request.POST['institutename']
#         instituteweblink = request.POST['instituteweblink']
#         instituteaddress = request.POST['instituteaddress']
#         institutecity = request.POST['institutecity']
#         institutedstate = request.POST['institutestate']
#         institutedistrict = request.POST['institutedistrict']
#         instituteemail = request.POST['instituteemail']
#         institutetype = request.POST['instituetype']
#         designation = request.POST['designation']

#         # c = "update aicte.aicteapp_generaldetails set username='{}',firstname='{}',lastname='{}',gender='{}',phonenumber='{}',email='{}',dob='{}',fathername='{}',city='{}',address='{}',state='{}',district='{}',alternameemail='{}',whatsappnumber='{}',institutename='{}',instituteweblink='{}', instituteaddress='{}',institutecity='{}',institutedstate='{}',institutedistrict='{}',instituteemail='{}',institutetype='{}',designation='{}' where username ='username' ".format(username,firstname,lastname,gender,phonenumber,email,dob,fathername,city,address,state,district,alternameemail,whatsappnumber,institutename,instituteweblink, instituteaddress,institutecity,institutedstate,institutedistrict,instituteemail,institutetype,designation)
#         # cursor.execute(c)
#         # m.commit()

#         generaldetails = GeneralDetails(username=username,firstname=firstname,lastname=lastname,gender=gender,phonenumber=phonenumber,email=email,dob=dob,fathername=fathername,city=city,address=address,state=state,district=district,alternameemail=alternameemail,whatsappnumber=whatsappnumber,institutename=institutename,instituteweblink=instituteweblink, instituteaddress=instituteaddress,institutecity=institutecity,institutedstate=institutedstate,institutedistrict=institutedistrict,instituteemail=instituteemail,institutetype=institutetype,designation=designation)
#         generaldetails.save()
#         return redirect('updatecoordinatorprofile')
#     return render(request,'aicteapp/updatecoordinatorprofile.html',{'coordinatordata':coordinatordata})

def coordinatorprofile(request):
    user = request.user
    print(user)
    coordinatordata = GeneralDetails.objects.filter(username = user)
    if request.method == 'POST':
        username = request.POST['username']
        firstname =request.POST['firstname']
        lastname =request.POST['lastname']
        gender =request.POST['gender']
        phonenumber =request.POST['phonenumber']
        email = request.POST['email']
        dob = request.POST['dob']
        fathername = request.POST['fathername']
        city = request.POST['city']
        address = request.POST['address']
        state = request.POST['state']
        district = request.POST['district']
        alternameemail = request.POST['alternateemail']
        whatsappnumber = request.POST['whatsappnumber']
        institutename = request.POST['institutename']
        instituteweblink = request.POST['instituteweblink']
        instituteaddress = request.POST['instituteaddress']
        institutecity = request.POST['institutecity']
        institutedstate = request.POST['institutestate']
        institutedistrict = request.POST['institutedistrict']
        instituteemail = request.POST['instituteemail']
        institutetype = request.POST['instituetype']
        designation = request.POST['designation']

        generaldetails = GeneralDetails(username=username,firstname=firstname,lastname=lastname,gender=gender,phonenumber=phonenumber,email=email,dob=dob,fathername=fathername,city=city,address=address,state=state,district=district,alternameemail=alternameemail,whatsappnumber=whatsappnumber,institutename=institutename,instituteweblink=instituteweblink, instituteaddress=instituteaddress,institutecity=institutecity,institutedstate=institutedstate,institutedistrict=institutedistrict,instituteemail=instituteemail,institutetype=institutetype,designation=designation)
        generaldetails.save()


        return redirect('coordinatorprofile')
    return render(request, 'aicteapp/coordinatorprofile.html',{'coordinatordata':coordinatordata})

def coordinatorbooking(request):
    audibookinglist = AuditoriumData.objects.all()
    return render(request, 'aicteapp/coordinatorbooking.html',{'audibookinglist':audibookinglist})

def coordinatorcanteen(request):
    return render(request, 'aicteapp/coordinatorcanteen.html')

def coordinatorreport(request):
    return render(request, 'aicteapp/coordinatorreport.html')

def bookingform(request,pk):
    audidata = AuditoriumData.objects.get(id = pk)
    return render(request, 'aicteapp/bookingform.html',{'audidata':audidata})

def coordinatoreventform(request):
    user = request.user
    print(user)
    if request.method == "POST":
        eventname = request.POST['eventname']
        eventdesc = request.POST['eventdesc']
        eventfromdate = request.POST.get('eventfromdate')
        eventtodate = request.POST.get('eventtodate')
        eventfromtime = request.POST['eventfromtime']
        eventtotime = request.POST['eventtotime']
        eventmode = request.POST['eventmode']
        eventhost = request.POST['eventhost']
        eventvenue = request.POST['eventvenue']
        eventnoattendees = request.POST['eventnoattendees']
        eventcontactname = request.POST['eventcontactname']
        eventcontactemail = request.POST['eventcontactemail']
        eventcontactphoneno = request.POST['eventcontactphoneno']
        eventposter = request.POST['eventposter']
        eventadposter = request.POST['eventadposter']
        username = request.POST['username']
        userid = request.POST['userid']

        eventregistration = EventRegistration(eventname = eventname, eventdesc=eventdesc,eventfromdate = eventfromdate,eventtodate=eventtodate,eventfromtime=eventfromtime,eventtotime=eventtotime,eventmode=eventmode,eventhost=eventhost,eventvenue=eventvenue,eventnoattendees=eventnoattendees,eventcontactname=eventcontactname,eventcontactemail=eventcontactemail,eventcontactphoneno=eventcontactphoneno,eventposter=eventposter,eventadposter=eventadposter,username = username,userid=userid)
        eventregistration.save()
        return redirect('coordinatorevent')



    return render(request, 'aicteapp/coordinatoreventform.html')

def canteenform(request):
    return render(request, 'aicteapp/canteenform.html')

def logout(request):
    auth.logout(request)
    return redirect('home')


def eventupdateform(request,pk):
    print(pk)

    eventlist = EventRegistration.objects.get(id = pk)
    if request.method == "POST":
        id = eventlist.id
        eventname = request.POST['eventname']
        eventdesc = request.POST['eventdesc']
        eventfromdate = request.POST.get('eventfromdate')
        eventtodate = request.POST.get('eventtodate')
        eventfromtime = request.POST['eventfromtime']
        eventtotime = request.POST['eventtotime']
        eventmode = request.POST['eventmode']
        eventhost = request.POST['eventhost']
        eventvenue = request.POST['eventvenue']
        eventnoattendees = request.POST['eventnoattendees']
        eventcontactname = request.POST['eventcontactname']
        eventcontactemail = request.POST['eventcontactemail']
        eventcontactphoneno = request.POST['eventcontactphoneno']
        eventposter = request.POST['eventposter']
        eventadposter = request.POST['eventadposter']
        username = request.POST['username']
        userid = request.POST['userid']

        eventregistration = EventRegistration(id=id,eventname = eventname, eventdesc=eventdesc,eventfromdate = eventfromdate,eventtodate=eventtodate,eventfromtime=eventfromtime,eventtotime=eventtotime,eventmode=eventmode,eventhost=eventhost,eventvenue=eventvenue,eventnoattendees=eventnoattendees,eventcontactname=eventcontactname,eventcontactemail=eventcontactemail,eventcontactphoneno=eventcontactphoneno,eventposter=eventposter,eventadposter=eventadposter,username = username,userid=userid)
        eventregistration.save()
        return redirect('coordinatorevent')

    return render(request, 'aicteapp/eventupdateform.html',{'eventlist':eventlist})