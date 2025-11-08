import datetime,math
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.db.models import Count, Avg, Min, Max, StdDev, Sum
from .forms import  businessAppForm
from .models import businessApp


def form(request):
    print("request.method: ", request.method)
    if request.method == "POST":
        form = businessAppForm(request.POST)
        if form.is_valid():
            print("\nform_is_valid:\n", form)
            form.save()
            return redirect("businessApp:table")
    else:
        form = businessAppForm()
        print("\nform_else:\n", form)
    context = {"form": form}
    print("\ncontext:\n", context)
    return render(request, "b_form.html", context)




def solution(objects_values_list):
    print("\nobjects_values_list:", objects_values_list)
    result = "С не равна сумме A и B"
    return result



def table(request):
    # all = AbcModel.objects.all()
    # all.delete()
    # objects_list
    objects_values = businessApp.objects.values()
    print("\nobjects_values:", objects_values)

    objects_values_list = businessApp.objects.values_list()
    print("\nobjects_values_list:", objects_values_list)    

    result = solution(objects_values_list)
    print("\nresult", result)


    context = {
        "objects_values": objects_values,
    }

    return render(request, "b_table.html", context)

