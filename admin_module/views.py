from multiprocessing import context
import os
from django.contrib import messages
import django
from django.shortcuts import redirect, render
from django.db import models
from admin_module.models import WorkAssign, contactUs, category_images, employerDetails
from app1.models import get_an_estimate

# Create your views here.


def fnAdmin_Panel(request):
    obj_get_work_status=WorkAssign.objects.all()
    obj_notification_count = get_an_estimate.objects.filter(
        checkout='notchecked').count()
    context = {'notification_count': obj_notification_count,'work_status':obj_get_work_status}
    return render(request, 'admin_panel.html', context)


def fnLogout(request):
    del request.session['admin']
    return redirect('index')


def fnManage_Website(request):
    obj_notification_count = get_an_estimate.objects.filter(
        checkout='notchecked').count()
    context = {'notification_count': obj_notification_count}
    return render(request, 'admin_manage_website.html', context)


def fnEdit_contact(request):
    if request.method == 'POST':
        whatsapp = request.POST['whatsapp']
        email = request.POST['email']
        phone = request.POST['phone']
        contactUs.objects.update(phone=phone, email=email, whatsapp=whatsapp)
        messages.success(request, 'contact us updated successfully')
        return redirect('editContact')
    else:
        return redirect('editContact')


def fnEditContact(request):
    obj_contact_us = contactUs.objects.get(id=1)
    obj_notification_count = get_an_estimate.objects.filter(
        checkout='notchecked').count()
    context = {'contact_us': obj_contact_us,
               'notification_count': obj_notification_count}
    return render(request, 'editContact.html', context)


def fnUpload_category_photo(request):
    if request.method == 'POST':
        photo = request.FILES['photo']
        title = request.POST['title']
        category = request.POST['category']
        discription = request.POST['discription']
        status = request.POST['status']
        obj = category_images(
            photo=photo, title=title, category=category, discription=discription, status=status)
        obj.save()
        messages.success(request, 'photo uploaded successfully')
        return redirect('admin_manage_website')
    else:
        messages.success(request, 'some thing went wrong')
        return redirect('admin_manage_website')


def fnEdit_photo(request):
    obj_view_category = category_images.objects.filter(status='available')
    obj_notification_count = get_an_estimate.objects.filter(
        checkout='notchecked').count()
    context = {'view_photo': obj_view_category,
               'notification_count': obj_notification_count}
    return render(request, 'edit_photo.html', context)


def fnUpdate_Edit_photo(request):
    if request.method == 'POST':
        photo_id = request.POST['photo_id']
        prod = category_images.objects.get(id=photo_id)
        if len(request.FILES) != 0:
            if len(prod.photo) > 0:
                os.remove(prod.photo.path)
            prod.photo = request.FILES['photo']
            prod.save()
        title = request.POST['title']
        category = request.POST['category']
        category_images.objects.filter(id=photo_id).update(
            title=title, category=category, status='available')
        messages.success(request, 'Photo Updated Successfully')
        return redirect('edit_photo')
    else:
        messages.success(request, 'some thing went wrong')
        return redirect('admin_manage_website')


def fnDelete_photo(request, id):
    category_images.objects.filter(id=id).update(status='deleted')
    messages.success(request, 'Photo Deleted Successfully')
    return redirect('edit_photo')


def view_deleted_photo(request):
    obj_view_deleted = category_images.objects.filter(status='deleted')
    obj_notification_count = get_an_estimate.objects.filter(
        checkout='notchecked').count()
    context = {'view_deleted': obj_view_deleted,
               'notification_count': obj_notification_count}
    return render(request, 'view_deleted_photo.html', context)


def fnRecover_deleted_photo(request):
    if request.method == 'POST':
        photo_id = request.POST['photo_id']
        category_images.objects.filter(id=photo_id).update(status='available')
        messages.success(request, 'Photo Recovered Successfully')
        return redirect('view_deleted_photo')
    else:
        messages.success(request, 'some thing went wrong')
        return redirect('admin_manage_website')


def fnEstimated_client(request):
    obj_estimated_values = get_an_estimate.objects.filter(
        checkout='notchecked')
    obj_notification_count = get_an_estimate.objects.filter(
        checkout='notchecked').count()
    context = {'estimated_values': obj_estimated_values,
               'notification_count': obj_notification_count}
    return render(request, 'estimated_client.html', context)


def fnCheckOut(request, id):
    get_an_estimate.objects.filter(id=id).update(checkout='checked')
    messages.success(request, 'Checked Successfully')
    return redirect('estimated_client')


def fnChecked_clients(request):
    obj_checked = get_an_estimate.objects.filter(checkout='checked')
    obj_notification_count = get_an_estimate.objects.filter(
        checkout='notchecked').count()
    context = {'checked': obj_checked,
               'notification_count': obj_notification_count}
    return render(request, 'checkout_clients.html', context)


def fnView_employer(request):
    obj_view_employees = employerDetails.objects.filter(status='available')
    obj_notification_count = get_an_estimate.objects.filter(
        checkout='notchecked').count()
    context = {'notification_count': obj_notification_count,
               'view_employees': obj_view_employees}
    return render(request, 'view_employer.html', context)


def fnAdd_employer(request):
    obj_notification_count = get_an_estimate.objects.filter(
        checkout='notchecked').count()
    context = {'notification_count': obj_notification_count}
    return render(request, 'add_employer.html', context)


def fnAdding_employer_details(request):
    if request.method == 'POST':
        try:
            signIn_Email = request.POST['signIn_Email']
            obj_check_employer_email_exist = employerDetails.objects.filter(
                signIn_Email=signIn_Email).exists()
            if obj_check_employer_email_exist == True:
                messages.error(
                    request, 'Sign In Email Is Already Exist Please Try Another Email')
                return redirect('view_employer')
            else:
                photo = request.FILES['employer_photo']
                first_Name = request.POST['first_Name']
                last_Name = request.POST['last_Name']
                job_Title = request.POST['job_Title']
                title_Position = request.POST['title_Position']
                personal_Email = request.POST['personal_Email']
                phone_Number = request.POST['phone_Number']
                address = request.POST['address']
                gender = request.POST['options']
                account_Holder_Name = request.POST['account_Holder_Name']
                bank_Name = request.POST['bank_Name']
                branch_Name = request.POST['branch_Name']
                account_Number = request.POST['account_Number']
                IFSC_Code = request.POST['IFSC_Code']
                password = request.POST['password']
                id_proof=request.FILES['id_proof']
                date_of_birth=request.POST['date_of_birth']
                employerDetails(photo=photo, first_Name=first_Name, last_Name=last_Name, job_Title=job_Title, title_Position=title_Position, personal_Email=personal_Email, phone_Number=phone_Number, address=address, gender=gender,
                                account_Holder_Name=account_Holder_Name, bank_Name=bank_Name, branch_Name=branch_Name, account_Number=account_Number, IFSC_Code=IFSC_Code, signIn_Email=signIn_Email, signIn_Password=password, status='available').save()
                messages.success(request, 'Employer Added Succesfully')
                return redirect('view_employer')
        except:
            messages.error(request, 'something went wrong')
            return redirect('view_employer')
    else:
        messages.success(request, 'something went wrong')
        return redirect('view_employer')


def fnEdit_employer_admin(request):
    obj_view_edit_employees = employerDetails.objects.filter(
        status='available')
    obj_notification_count = get_an_estimate.objects.filter(
        checkout='notchecked').count()
    context = {'notification_count': obj_notification_count,
               'employer_details': obj_view_edit_employees}
    return render(request, 'edit_employer_admin.html', context)


def fnView_edit_employer_admin(request, id):
    try:
        obj_notification_count = get_an_estimate.objects.filter(
            checkout='notchecked').count()
        obj_get_eployer_value = employerDetails.objects.get(id=id)
        context = {'get_employer_value': obj_get_eployer_value,
                   'notification_count': obj_notification_count}
        return render(request, 'editing_employer_admin.html', context)
    except:
        messages.success(request, 'something went wrong')
        return redirect('view_employer')


def fnUpdate_employer_admin(request):
    if request.method == 'POST':
        signIn_Email = request.POST['signIn_Email']
        obj_check_employer_email_exist = employerDetails.objects.filter(
            signIn_Email=signIn_Email).exists()
        employer_id = request.POST['employer_id']
        ob_check_email_is_not_changed = employerDetails.objects.get(
            id=employer_id)
        if signIn_Email == ob_check_email_is_not_changed.signIn_Email:
            first_Name = request.POST['first_Name']
            last_Name = request.POST['last_Name']
            job_Title = request.POST['job_Title']
            title_Position = request.POST['title_Position']
            personal_Email = request.POST['personal_Email']
            phone_Number = request.POST['phone_Number']
            address = request.POST['address']
            gender = request.POST['options']
            password = request.POST['password']
            employerDetails.objects.filter(id=employer_id).update(first_Name=first_Name, last_Name=last_Name, job_Title=job_Title, title_Position=title_Position,
                                                                  personal_Email=personal_Email, phone_Number=phone_Number, address=address, gender=gender, signIn_Password=password)
            messages.success(request, 'Employer Updated Succesfully')
            return redirect('edit_employer_admin')
        else:
            if obj_check_employer_email_exist == True:
                messages.error(
                    request, 'Sign In Email Is Already Exist Please Try Another Email')
                return redirect('view_employer')
            else:
                first_Name = request.POST['first_Name']
                last_Name = request.POST['last_Name']
                job_Title = request.POST['job_Title']
                title_Position = request.POST['title_Position']
                personal_Email = request.POST['personal_Email']
                phone_Number = request.POST['phone_Number']
                address = request.POST['address']
                gender = request.POST['options']
                password = request.POST['password']
                employerDetails.objects.filter(id=employer_id).update(first_Name=first_Name, last_Name=last_Name, job_Title=job_Title, title_Position=title_Position,
                                                                      personal_Email=personal_Email, phone_Number=phone_Number, address=address, gender=gender, signIn_Email=signIn_Email, signIn_Password=password)
                messages.success(request, 'Employer Updated Succesfully')
                return redirect('edit_employer_admin')
    else:
        messages.success(request, 'some thing went wrong please try again')
        return redirect('view_edit_employer_admin')


def fnTerminate_employer(request, id):
    employerDetails.objects.filter(id=id).update(status='terminated')
    messages.success(request, 'Employer Terminated Succesfully')
    return redirect('edit_employer_admin')


def fnView_terminated_employees(request):
    obj_notification_count = get_an_estimate.objects.filter(
        checkout='notchecked').count()
    terminated_employees = employerDetails.objects.filter(status='terminated')
    context = {'terminated_employees': terminated_employees,
               'notification_count': obj_notification_count}
    return render(request, 'view_terminted_employees.html', context)


def fnEdit_terminated_employer_admin(request, id):
    employerDetails.objects.filter(id=id).update(status='available')
    messages.success(request, 'Employer Recoverd Succesfully')
    return redirect('edit_employer_admin')


def fnView_terminated_employer_bank(request):
    obj_notification_count = get_an_estimate.objects.filter(
        checkout='notchecked').count()
    obj_view_terminated_employer_bank = employerDetails.objects.filter(
        status='terminated')
    context = {'employer_bank': obj_view_terminated_employer_bank,
               'notification_count': obj_notification_count}
    return render(request, 'view_terminated_employer_bank.html', context)


def fnView_employer_bank(request):
    obj_notification_count = get_an_estimate.objects.filter(
        checkout='notchecked').count()
    obj_view_terminated_employer_bank = employerDetails.objects.filter(
        status='available')
    context = {'employer_bank': obj_view_terminated_employer_bank,
               'notification_count': obj_notification_count}
    return render(request, 'view_employer_bank.html', context)


def assign_work(request):
    obj_get_employer_name = employerDetails.objects.filter(status='available')
    obj_notification_count = get_an_estimate.objects.filter(
        checkout='notchecked').count()
    context = {'notification_count': obj_notification_count,
               'employer_name': obj_get_employer_name}
    return render(request, 'assign_work.html', context)


def work_assigning(request):
    if request.method == 'POST':
        employer_id = request.POST['employer_id']
        employer=employerDetails.objects.get(id=employer_id)
        task = request.POST['task']
        starting_date = request.POST['starting_date']
        ending_date = request.POST['ending_date']
        starting_time = request.POST['starting_time']
        ending_time = request.POST['ending_time']
        client_First_name = request.POST['client_First_name']
        Client_second_name = request.POST['Client_second_name']
        gender = request.POST['i']
        street_address = request.POST['street_address']
        city = request.POST['city']
        zip_code = request.POST['zip_code']
        additional_information = request.POST['additional_information']
        WorkAssign(employer=employer, task=task, starting_date=starting_date, ending_date=ending_date, starting_time=starting_time, ending_time=ending_time, client_First_name=client_First_name,
                   Client_second_name=Client_second_name, gender=gender, street_address=street_address, city=city, zip_code=zip_code, additional_information=additional_information,work_status='assigned').save()
        messages.success(request, 'Work Assigned Successfully')
        return redirect('assign_work')
    else:
        messages.success(request, 'something went wrong')
        return redirect('assign_work')
