from django.shortcuts import render, redirect
from .model import WorkItem  # import the model

def index(request):
    if request.method == "POST":
        new_work = request.POST.get("work")
        if new_work:
            WorkItem.objects.create(name=new_work)
        return redirect("index")

    all_work = WorkItem.objects.all()
    return render(request, "work/index.html", {
        "work_list": all_work
    })

def delete_work(request, work_id):
    item = WorkItem.objects.get(id=work_id)
    item.delete()
    return redirect("index")
