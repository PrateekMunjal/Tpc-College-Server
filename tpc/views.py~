from django.shortcuts import *
from django.http import *
from forms import *
from models import *
from django.views.decorators.csrf import csrf_exempt

from parse_rest.connection import register
register("xeoM4uYIKaBsbb8qJV9am8cfDu1PUOEuyP5VvIZN","Mr1UJztApG8J9TflhUrLpkq3IT3h3yDzBAx43n1F",master_key="ATfgDGeckya3v3DFpyuAq3GK2Hobw13Eo87ugAxe")

from parse_rest.installation import Push

# Create your views here.

def notice(request):
	n = Notices.objects.all().order_by('-time')
	if(request.method=="GET"):
		form = NoticeForm()
		return render_to_response('notice.html',{"form":form},context_instance=RequestContext(request))
	else:
		#this is post method
		form = NoticeForm(request.POST)
		if(not(str(request.POST['password'])=="pussgrcpussgrc")):
			return HttpResponse('<h1>Wrong Password</h1>')
		
		if form.is_valid():
			form.save()
			Push.message("Important announcement : "+request.POST['heading'],channels=["tpc_students"])
			return HttpResponseRedirect('/')
		else:
			return HttpResponse('<h1>Your Filled form is not valid...Please Check it once</h1>')

def edit(request):
	f = Drives.objects.all().order_by('-time')
	return render_to_response('edit.html',{'drive':f})


def companyWiseRegistration(request,company_name):
	f = User.objects.filter(company_reg = company_name)
	print '------------------------------'
	print 'Company Name --> '+company_name	
	print '------------------------------'
	return render_to_response('allResponses.html',{'drive':f})
	
@csrf_exempt
def mobile(request):	
	if(request.method=="POST"):
		form = DriveRegisteration(request.POST)
		form.fields['name'].initial=str(request.POST['name'])
		form.fields['stream'].initial=str(request.POST['stream'])
		form.fields['cgpa'].initial=str(request.POST['cgpa'])
		form.fields['roll_no'].initial=str(request.POST['roll_no'])
		form.fields['contact'].initial=str(request.POST['contact'])
		form.fields['company_reg'].initial=str(request.POST['company_reg'])
		f = User.objects.filter(roll_no=str(request.POST['roll_no'])).filter(company_reg=str(request.POST['company_reg']))
		if(f):
			return HttpResponse("You have already registered for this drive !!")
		else:		
			form.save()
			return HttpResponse("You Registered Successfully for "+str(request.POST['company_reg']))
	
	else:	
		return HttpResponseRedirect('/allRegistrations')

def home(request):
	return render_to_response('home.html')

def about(request):
	return render_to_response('about.html')

def allRegistrations(request):
	f = User.objects.all()
	return render_to_response('allResponses.html',{'drive':f})

def allDrives(request):
	f = Drives.objects.all().order_by('-time')
	return render_to_response('allDrives.html',{'drive':f})

def post(request):
	print '----------Post-------------------'
	print request.session.keys()
	print '-----------------------------'
	form = RegisterationForm()
	context = {'form':form}
	return render_to_response('form.html',context,context_instance=RequestContext(request))

def postDrive(request):
	print '-----------postDrive------------------'
	print request.session.keys()
	print '-----------------------------'
	if(request.method=="POST"):
		form = RegisterationForm(request.POST)
		if(not(request.POST['password']=="pussgrcpussgrc")):
			return HttpResponse('wrong password')
		request.session['password']=str(request.POST['password'])
		name = str(request.POST['companyName'])
		#print name
		#print '------------------------------------'
		#print form
		if(form.is_valid()):
			form.save()
			Push.message(""+name+" is coming, please have a look over its details",channels=["tpc_students"])
			return HttpResponseRedirect('/allDrives')
	else:
		return HttpResponse("Get method called")
@csrf_exempt
def updateCompany(request,company_name):
	f = Drives.objects.filter(companyName = company_name)
	if(request.method=="POST"):	
		form = RegisterationForm(request.POST)
		if(not(str(request.POST['password'])=="pussgrcpussgrc")):
			return HttpResponse("<h1>Wrong Password</h1>")
		else:			
		#	print '------------------------'
		#	print 'IN POST METHOD'
		#	print '------------------------'
			if(form.is_valid()):
				for i in f:
					if (i.companyName==request.POST['companyName'] and i.venue==request.POST['venue'] and i.description==request.POST['description'] and i.branch==request.POST['branch'] and i.skillsRequired==request.POST['skillsRequired'] and i.dateofdrive==request.POST['dateofdrive']):
						return HttpResponse("<h1>No Changes Observed</h1>")
					i.companyName = (request.POST['companyName'])
					i.venue = (request.POST['venue'])
					i.description =(request.POST['description'])
					i.branch = (request.POST['branch'])
					i.skillsRequired = (request.POST['skillsRequired'])
					i.dateofdrive = (request.POST['dateofdrive'])
					i.save()
					Push.message("Details are updated for "+str(request.POST['companyName'])+" ,Please have a look over it.",channels=["tpc_students"])
					break
				
				return HttpResponseRedirect('/allDrives')
			else:
				return HttpResponse('Error')
	else:
		#print '-------------------------------------'	
		#print str(company_name)
		#print '--------------------------------------'
		return render_to_response('update.html',{'forms':f})
