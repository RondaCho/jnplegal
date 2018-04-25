from django.shortcuts import render, get_object_or_404
from .models import Lawyer


def lawyer_list(request):
    qs = Lawyer.objects.all()
    return render(request, 'lawyer/lawyer_list.html', {
        'lawyer_list' : qs,
    })
'''
def lawyer_detail(request, id):
    lawyer = get_object_or_404(Lawyer, unique_url = id)
    return render(request,'lawyer/lawyer_detail.html', {
        'lawyer':lawyer,
    } )
    '''

def lawyer_detail(request, slug):
    lawyer = get_object_or_404(Lawyer, unique_url = slug)
    return render(request, 'lawyer/lawyer_detail.html',{
        'lawyer':lawyer,
    })