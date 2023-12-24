from django.shortcuts import redirect, render
from django.views.generic import ListView
from django.http import HttpResponse
from django.template import loader
from .models import Film
from .models import Hall
from datetime import datetime
from . import strToList
days = ["Понеділок", "Вівторок", "Середа", "Четвер", "П'ятниця", "Субота", "Неділя"]

class HomePageView(ListView):
    model = Film
    template_name = 'home.html'
    context_object_name = 'films'

def home(request):
  films = Film.objects.all()
  fs = []
  for film in films:
      if (film.time > datetime.now().time()):
        fs.append(film)
  print(films[0])
  print(datetime.now())
  print(films[0].time > datetime.now().time())
  template = loader.get_template('home.html')
  context = {
    'films': fs,
    'day': days[datetime.today().weekday()]
  }
  return HttpResponse(template.render(context, request))

def hall(request, num):
    template = loader.get_template('hall.html')
    seats = []
    halls = Hall.objects.all()
    hall = None
    for h in halls:
        if h.number == num:
            hall = h
            break
    else:
        return redirect('/')
    for i in range(20):
        if i < 9:seats.append('0'+str(i+1))
        else: seats.append(str(i+1))
    t = strToList.strToList(hall.seats)
    taken = []
    for i in t:
        taken.append(str(i))
    context = {
        'num': str(num),
        'numz': seats,
        'hall': hall,
        'taken': taken
    }
    if (request.method == 'POST'):
        cur_seats = strToList.strToList(hall.seats)
        cur_seats.append(int(request.POST.get('s')))
        print(cur_seats)
        hall.seats = strToList.listToStr(cur_seats, True)
        hall.save()
        return redirect(f"/hall{num}")
    return HttpResponse(template.render(context, request))