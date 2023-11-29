from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.db.models import Q
from .models import Entries, Installment
from .forms import addForm, instForm, dueForm
from django.http import FileResponse
from django.contrib.auth.decorators import login_required, permission_required
from datetime import date, timedelta
import os 


@login_required
def open(request):
    entries = Entries.objects.all()
    if request.method=="POST":
        form = addForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.due_date = entry.borrow_date + timedelta(days=30)
            entry.save()
            messages.success(request, "Entry Added Succesfully!")
            return redirect('/open')
        else:
            messages.error(request, "Please Try Again!")
    else:
        form = addForm()
    return render(request, 'open.html', {'entries':entries, 'form':form})

@login_required
def closed(request):
    entries = Entries.objects.all()
    if request.method=="POST":
        form = addForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.due_date = entry.borrow_date + timedelta(days=30)
            entry.save()
            messages.success(request, "Entry Added Succesfully!")
            return redirect('/closed')
        else:
            messages.error(request, "Please Try Again!")
    else:
        form = addForm()
    return render(request, 'closed.html', {'entries':entries, 'form':form})


@login_required
def overdue(request):
    entries = Entries.objects.all()
    if request.method=="POST":
        form = addForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.due_date = entry.borrow_date + timedelta(days=30)
            entry.save()
            messages.success(request, "Entry Added Succesfully!")
            return redirect('/overdue')
        else:
            messages.error(request, "Please Try Again!")
    else:
        form = addForm()
    return render(request, 'overdue.html', {'entries':entries, 'form':form})



def loginUser(request):
    if  request.user.is_authenticated:
        return redirect('/open')

    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST['next'])
            else:
                return redirect('/open')
        else:
            messages.error(request, "Invalid Credentials!")
            return render(request, 'index.html')

    return render(request, 'index.html')

def logoutUser(request):
    logout(request)
    messages.success(request, "Successfully Logged Out!")
    return redirect('/')

@login_required
@permission_required("main.view_entries")
def openEntry(request, key):
    entry = Entries.objects.get(id=key)
    installments = Installment.objects.filter(entry=entry)

    due = str(entry.due_date - date.today())
    if due == '0:00:00':
        days = 0
    else:
        days  = int(due.split(" ")[0])


    if request.method=="POST":
        upform = addForm(request.POST or None, request.FILES or None, instance=entry)
        dueform = dueForm(request.POST or None, instance=entry)
        form = instForm(request.POST or None)
        old_image = entry.identity.path
        if upform.is_valid():
            upentry = upform.save(commit=False)
            upentry.due_date = entry.borrow_date + timedelta(days=30)
            upentry.save()
            if 'identity' in upform.changed_data:
                os.remove(old_image)

            messages.success(request, "Entry Updated Succesfully!")
            return redirect(f'/entry/{entry.id}')
        
        elif form.is_valid():
            inst = form.save(commit=False)
            inst.entry = entry
            inst.save()
            messages.success(request, "Installment Added Succesfully!")
            return redirect(f'/entry/{entry.id}')

        elif dueform.is_valid():
            dueform.save()
            messages.success(request, "Due Date Changed Succesfully!")
            return redirect(f'/entry/{entry.id}')

        else:
            messages.error(request, "Please Try Again! DUE")

    else:
        upform = addForm(instance=entry)
        dueform = dueForm(instance=entry)
        form = instForm()


    return render(request, 'entry.html', {'entry':entry, 'insts':installments, 'form':form, 'upform':upform, 'dueform':dueform, 'days':days})


@login_required
@permission_required("main.view_entries")
def secure(request, img):
    document = get_object_or_404(Entries, identity='identities/'+img)
    response = FileResponse(document.identity)
    return response


@login_required
@permission_required("main.delete_entries")
def deleteEntry(request, key):
    entry = Entries.objects.get(id=key)
    os.remove(entry.identity.path)
    entry.delete()
    messages.error(request, "Entry Deleted Succesfully!")
    return redirect("/open")


@login_required
@permission_required("main.view_entries")
def statusEntry(request, key):
    entry = Entries.objects.get(id=key)
    entry.status = not entry.status
    entry.save()
    messages.warning(request, "Entry Status Changed!")
    return redirect('/open')


@permission_required("main.delete_entries")
def deleteInst(request, key):
    inst = Installment.objects.get(id=key)
    inst.delete()
    messages.error(request, "Installment Deleted Succesfully!")
    return redirect(f'/entry/{inst.entry_id}')


@login_required
@permission_required("main.view_entries")
def search(request):
    query = request.GET['query']
    entries = Entries.objects.filter(Q(name__icontains=query) | Q(father__icontains=query) | Q(principal__icontains=query) | Q(father__icontains=query) | Q(address__icontains=query) | Q(guarantor__icontains=query) | Q(contact_guar__icontains=query) | Q(contact_one__icontains=query) | Q(contact_two__icontains=query) | Q(due_date__icontains=query))
    
    if request.method=="POST":
        form = addForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.due_date = entry.borrow_date + timedelta(days=30)
            entry.save()
            messages.success(request, "Entry Added Succesfully!")
            return redirect('/open')
        else:
            messages.error(request, "Please Try Again!")
    else:
        form = addForm()
    
    return render(request, 'search.html', {'entries':entries, 'form':form})
