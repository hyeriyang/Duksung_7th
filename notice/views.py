import os
from django.shortcuts import render,get_object_or_404,redirect
from .forms import NoticeForm
from .models import Notice
from django.utils import timezone
#from django.conf import settings
#from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse,HttpResponseRedirect,Http404

# Create your views here.
def post(request):
    if request.method=="POST":
        form=NoticeForm(request.POST, request.FILES)
        if form.is_valid():
            notice=form.save(commit=False)
            notice.update_date=timezone.now()
            notice.save()
            return HttpResponseRedirect('/notice/show')
    else:
        form=NoticeForm()
        return render(request,'post.html',{'form':form})

def show(request):
    notices=Notice.objects.order_by('-id')
    return render(request,'show.html',{'notices':notices})

def detail(request,notice_id):
    notice_detail=get_object_or_404(Notice, pk=notice_id)
    return render(request,'detail.html',{'notice':notice_detail})

def edit(request, pk):
    notice = get_object_or_404(Notice, pk=pk)
    if request.method == "POST":
        form=NoticeForm(request.POST, request.FILES,instance=notice)
        if form.is_valid():
            notice=form.save(commit=False)
            notice.update_date=timezone.now()
            notice.save()
            return redirect('show')
    else:
        form=NoticeForm(instance=notice)
        return render(request,'edit.html',{'form':form})


def delete(request,pk):
    notice=Notice.objects.get(id=pk)
    notice.delete()
    return redirect('show')

def download(request,pk):
    notice_download=get_object_or_404(Notice,pk=pk)
    file_url=notice_download.file.url[1:]
    if os.path.exists(file_url):
        with open(file_url,'rb') as fh:
            response=HttpResponse(fh.read(),content_type="application/octet-stream")
            response['attachment']='inline:filename='+os.path.basename(file_url)
            return response
        raise Http404   