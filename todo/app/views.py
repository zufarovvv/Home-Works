from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from app.models import Work


# Create your views here.

def index(request):
    works = Work.objects.all()
    ctx = {
        "works":works
    }
    return render(request, 'app/index.html', ctx)

def delete_work(request, work_id):
    work = get_object_or_404(Work, id=work_id)
    if request.method == 'POST':
        work.delete()
        return redirect('index')
    return render(request, 'app/confirm_delete.html', {'work': work})


def mark_work_as_done(request, work_id):
    work = get_object_or_404(Work, id=work_id)
    work.status = True
    work.save()
    return redirect('index')

