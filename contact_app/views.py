from django.shortcuts import render, redirect
from .models import Customer
from .forms import CustomerForm


# Create your views here.
def contact_form(request):
    form = CustomerForm(request.POST)
    if request.POST and form.is_valid():
        print('birinchi:', form)
        form.save()
        return redirect('customer-list')

    context = {"form": form}
    print('ikkinchi:', context['form'])
    return render(request, 'form.html')


def contact_list(request):
    queryset = Customer.objects.all()

    context = {'customers': queryset}
    return render(request, 'table.html', context)
