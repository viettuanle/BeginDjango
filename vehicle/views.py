from django.shortcuts import render

# Create your views here.
def display(request):
    template_name ='display.html'
    context = {"current_user":"nguyen"}
    return render(request,template_name=template_name, context=context)