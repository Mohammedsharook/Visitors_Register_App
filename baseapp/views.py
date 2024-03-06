from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import VisitorForm
from .models import VisitorDetails

def home(request):
    if request.method == "POST":
        form = VisitorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Visitor Added successfully.')
            return redirect('home')
    else:
        form = VisitorForm()

    visitor_details = VisitorDetails.objects.all()
    context = {'form':form, 'visitor_details':visitor_details}
    return render(request, 'baseapp/home.html', context)

def update_visitor(request, visitor_id):
    try:
        visitor = VisitorDetails.objects.get(pk=visitor_id)
    except VisitorDetails.DoesNotExist:
        messages.error(request, 'Visitor not found.')
        return redirect('home')
    
    if request.method == 'POST':
        form = VisitorForm(request.POST, instance=visitor)
        if form.is_valid():
            form.save()
            messages.success(request, 'Visitor updated successfully.')
            return redirect('home')
    else:
        form = VisitorForm(instance=visitor)
    return render(request, 'baseapp/home.html', {'form': form, 'action':'update'})


def delete_visitor(request, visitor_id):
    try:
        visitor = VisitorDetails.objects.get(pk=visitor_id)
        visitor.delete()
        messages.success(request, 'Visitor Deleted successfully.')
        return redirect('home')
    except VisitorDetails.DoesNotExist:
        messages.error(request, 'Visitor not found.')
        return redirect('home')
    
    

