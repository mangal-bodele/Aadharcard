from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import AadharCardForm
from .models import AadharCard

@login_required(login_url='login_url')
def create_aadhar(request):
    template_name = 'crud_app/create.html'
    form = AadharCardForm()
    if request.method == "POST":
        form = AadharCardForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_url')
    context = {'form': form}
    return render(request, template_name, context)

@login_required(login_url='login_url')
def show_aadhar(request):
    template_name = 'crud_app/show.html'
    aadharcards = AadharCard.objects.all()
    context = {'aadharcards': aadharcards}
    return render(request, template_name, context)


def update_aadhar(request,pk):
    template_name = 'crud_app/create.html'
    obj=AadharCard.objects.get(id=pk)
    form = AadharCardForm(instance=obj)
    if request.method == "POST":
        form = AadharCardForm(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            return redirect('show_url')
    context = {'form': form}
    return render(request, template_name, context)

def delete_aadhar(request,pk):
    template_name = 'crud_app/confirm.html'
    obj = AadharCard.objects.get(id=pk)
    if request.method == "POST":
        obj.delete()
    return render(request, template_name)

