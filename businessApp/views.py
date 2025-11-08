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



    # fields_name
    fields = businessApp._meta.get_fields()
    print("\nfields", fields)
    verbose_name_list = []
    name_list = []
    for e in fields:
        verbose_name_list.append(e.verbose_name)
        name_list.append(e.name)

    print ("\n\nname_list", name_list)
    print ("\n\nverbose_ name_list", verbose_name_list)

    context = {
        "verbose_name_list": verbose_name_list,
        "objects_values": objects_values,
        "result": result,
    }

    return render(request, "b_table.html", context)

