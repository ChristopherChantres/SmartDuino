from django.shortcuts import render, redirect
from .controller import *

# Create your views here.
def index_view (request):
  if request.POST:
    id = request.POST['id']
    if int(id) == 1:
      redOn()
    elif int(id) == 2:
      blueOn()
    elif int(id) == 3:
      greenOn()
    elif int(id) == 4:
      yellowOn()
    elif int(id) == 5:
      allOff()
    elif int(id) == 6:
      allON()
    elif int(id) == 7:
      lightshow1()
    print(id)
  return render(request, 'index.html')