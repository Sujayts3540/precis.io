from django.shortcuts import render,redirect
from .models import Resume 
from django.contrib.auth.models import User
# from django.http import HttpResponse

# Create your views here.

def home(request):
    # print(request)
    return render(request,'home.html')

def redirect_view(request):

    # for key,value in dict(request.POST).items():
    #     print(key,value)
    if not User.is_authenticated :
        return redirect('accounts/login')

    name=request.POST['name']
    email=request.POST['email']
    phone=request.POST['phone']
    title=request.POST['title']

    website=request.POST['website']
    profile=request.POST['profile']
    location=request.POST['location']
    job_profile=request.POST['job-profile']
    
    skills=request.POST['skills'].split()

    jobs={
        'employers':[],
        'titles':[],
        'end':[],
        'start':[]
    }

    edu={
        'degrees':[],
        'institutions':[],
        'end':[],
        'start':[]
    }

    for i in range(3):
       if len(request.POST[f"employer-{i+1}"].strip())!=0: 
            jobs['employers'].append(request.POST[f"employer-{i+1}"].strip())
       if len(request.POST[f"job-title-{i+1}"].strip())!=0: 
            jobs['titles'].append(request.POST[f"job-title-{i+1}"].strip())
       if len(request.POST[f"end-work-{i+1}"].strip())!=0:
            jobs['end'].append(request.POST[f"end-work-{i+1}"].strip())
       if len(request.POST[f"start-work-{i+1}"].strip())!=0: 
            jobs['start'].append(request.POST[f"start-work-{i+1}"].strip())

    for i in range(3):
        edu['degrees'].append(request.POST[f'degree-{i+1}'])
        edu['institutions'].append(request.POST[f'institution-{i+1}'])
        edu['end'].append(request.POST[f'end-education-{i+1}'])
        edu['start'].append(request.POST[f'start-education-{i+1}'])

    # print(jobs,edu)
    # resume=Resume.objects.create(name=name, email=email,phone=phone,title=title);
    resume=Resume.objects.create(name=name, email=email,phone=phone,title=title, profile=profile, job_profile=job_profile,skills=skills,
    website=website,location=location, employers=jobs['employers'], titles=jobs['titles'],job_start=jobs['start'],job_end=jobs['end'],
     degrees=edu['degrees'], institutions=edu['institutions'], edu_start=edu['start'],edu_end=edu['end'], uid=request.user);
    response = redirect('resumes')
    return response
    

def form(request,pk=''):
    
    if User.is_authenticated :
        if pk.strip()=='':
            return render(request,'formedit.html',{
                'edit':False
            })
        else:
            print('pk:',pk)
            res=Resume.objects.get(id=pk)
            # print('KYAA REEE',res);
            if res.uid != request.user:
                return redirect('')
            else:
                el='\n'.join(res.skills)
                print(el);
                return render(request,'formedit.html', {
                    'resume': res,
                    'edit':True
        })
    else: 
        return redirect('accounts/login')

def resume(request, pk):
    res=Resume.objects.filter(id=pk).values()
    # print(res)
    # print(Resume.objects.filter(id=pk))
    return render(request,'resume.html', {
        'resume': res
    })
    

def resumes(request):
    # print()

    # Creating a row in the database (the conventional way)
    # print(request)
    # name=request.POST['name']
    # email=request.POST['email']
    # phone=request.POST['phone']
    # title=request.POST['title']
    # resume=Resume.objects.create(name=name, email=email,phone=phone,title=title);

    resumes= Resume.objects.filter(uid=request.user);
    # print(resume)
    # print(resumes[0].id)

    return render(request,'result.html',{
        'resumes': resumes
    })

def editredirect(request,id):
    res=Resume.objects.get(id=id)
    
    if not User.is_authenticated :
        return redirect('accounts/login')
    if res.uid != request.user:
         return redirect('')


    name=request.POST['name']
    email=request.POST['email']
    phone=request.POST['phone']
    title=request.POST['title']

    website=request.POST['website']
    profile=request.POST['profile']
    location=request.POST['location']
    job_profile=request.POST['job-profile']
    
    skills=request.POST['skills'].split()

    jobs={
        'employers':[],
        'titles':[],
        'end':[],
        'start':[]
    }

    edu={
        'degrees':[],
        'institutions':[],
        'end':[],
        'start':[]
    }

    for i in range(3):
       if len(request.POST[f"employer-{i+1}"].strip())!=0: 
            jobs['employers'].append(request.POST[f"employer-{i+1}"].strip())
       if len(request.POST[f"job-title-{i+1}"].strip())!=0: 
            jobs['titles'].append(request.POST[f"job-title-{i+1}"].strip())
       if len(request.POST[f"end-work-{i+1}"].strip())!=0:
            jobs['end'].append(request.POST[f"end-work-{i+1}"].strip())
       if len(request.POST[f"start-work-{i+1}"].strip())!=0: 
            jobs['start'].append(request.POST[f"start-work-{i+1}"].strip())

    for i in range(3):
        edu['degrees'].append(request.POST[f'degree-{i+1}'])
        edu['institutions'].append(request.POST[f'institution-{i+1}'])
        edu['end'].append(request.POST[f'end-education-{i+1}'])
        edu['start'].append(request.POST[f'start-education-{i+1}'])

    # print(jobs,edu)
    # resume=Resume.objects.create(name=name, email=email,phone=phone,title=title);
    res.name=name
    res.email=email
    res.phone=phone
    res.title=title
    res.profile=profile
    res.job_profile=job_profile
    res.skills=skills

    print(jobs['end'], jobs['start'])

    res.website=website
    res.location=location
    res.employers=jobs['employers']
    res.titles=jobs['titles']
    res.job_start=jobs['start']
    res.job_end=jobs['end']
    res.degrees=edu['degrees']
    res.institutions=edu['institutions']
    res.edu_start=edu['start']
    res.edu_end=edu['end']
    res.save();
    response = redirect('resumes')
    return response


def delete(request, id):
    resume = Resume.objects.get(id=id)
    if resume.uid == request.user:
        resume.delete();
        return redirect('resumes')
    else:
        return redirect('')
