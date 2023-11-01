from django.shortcuts import render
from main.models import Index
# Create your views here.
def index(request):
    index = Index.objects.latest("id")
    return render(request, "index.html", locals())
