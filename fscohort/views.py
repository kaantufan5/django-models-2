from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("Hello. Welcome!")

def fscohort(request):
    return HttpResponse('Now, you are in fscohort')

def subfolder(request):
    return HttpResponse('Bla Bla Subfolder!')

