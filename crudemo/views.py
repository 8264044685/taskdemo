from django.shortcuts import render, redirect, HttpResponse
from .models import *


from django.views.decorators.csrf import csrf_exempt

from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.views import View




# Create your views here.
def index(request):
    try:
        if request.method == 'POST':
            data = request.POST.get
            users_details = TaskData.objects.filter(zipcode__iexact = data('zipcode'))
            show_search = 'yes'
            context = {
                'users_details':users_details,
                'show_search': show_search,
            }

            return render(request, 'crudemo/index.html', context)
        else:

            users_details = TaskData.objects.all()
            show_search = 'yes'    
            context = {
                'users_details':users_details,
                'show_search': show_search,
            }
            return render(request, 'crudemo/index.html', context)
    except Exception as identifier:
        print("error is ", identifier)
    

def add_data(request):
    
    try:
        if request.method == 'POST':
            data = request.POST.get
            Obj = TaskData(
                    name = data('name'),
                    email = data('email'),
                    address = data('address'),
                    address2 = data('address2'),
                    city = data('city'),
                    state = data('state'),
                    zipcode = data('zipcode')
                )
            Obj.save()
            return redirect('index')
    except Exception as e:
        print("error is", e)
    
    return render(request, 'crudemo/add_data.html')

def user_status(request):
    status = request.POST['status']
    user_id = request.POST['id']
    if request.method == 'POST':
        status = request.POST['status']
        user_id = request.POST['id']

        if status == 'active':
            user_update = TaskData.objects.filter(id=user_id).update(status='inactive')
            user = TaskData.objects.get(id=user_id)
            print("user.status for active", user.status)
            return HttpResponse({'status': user.status})
        else:
            user_update = TaskData.objects.filter(id=user_id).update(status='active')
            user = TaskData.objects.get(id=user_id)
            print("user.status for inactive", user.status)
            return HttpResponse({'status': user.status})


def view_user(request,id):
    user_data = TaskData.objects.get(id=id)

    context = {
        'user_datail':user_data,
    }

    return render(request, 'crudemo/view_user.html',context)

def edit_user(request,id):
    try:

        if request.method == 'POST':
            data = request.POST.get
            print("update function ", data)
            user = TaskData.objects.get(id=id)

            user.name= data('name')
            user.email= data('email')
            user.address= data('address')
            user.address2 = data('address2')
            user.city = data('city')
            user.state = data('state')
            user.zipcode = data('zipcode')
            user.save()
            user_data = TaskData.objects.get(id=id)

            context = {
                'user_datail':user_data,
            }
            return render('crudemo/edit_user.html',context)
        else:

            user_data = TaskData.objects.get(id=id)

            context = {
                'user_datail':user_data,
            }

            return render(request, 'crudemo/edit_user.html',context)
        
    except Exception as e:
        print(e)
        return redirect('index')


def delete_user(request,id):
    if request.method == 'GET':
        user_data = TaskData.objects.get(id=id).delete()
        return redirect('index')
    


def ViewPDF(request):


    if request.method == "GET":

        data = request.POST.get
        print("data is search value",data('zipcode'))
        users_details = TaskData.objects.all()
        
        context = {
            'users_details':users_details,
        } 

        print(users_details)
        
        template = get_template('zip_pdf_template.html')
        html = template.render(context)
        response = BytesIO()
        pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), response)

        if not pdf.err:
            return HttpResponse(response.getvalue(), content_type='application/pdf')
        else:
            return HttpResponse("Error Rendering PDF", status=400)

        