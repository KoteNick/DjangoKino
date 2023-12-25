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

def now():
    return datetime.now().time()

def reset():
    films = Film.objects.all()
    halls = Hall.objects.all()
    for film in films:
        if (now() > film.timeEnd):
            film.done = True
            film.save()
        else:
            film.done=False
            film.save()
        for hall in halls:
            if hall.number == film.hall:
                if (now()<film.timeEnd and now()> film.time):
                    hall.in_use = True
                    hall.save()
                elif now()>film.timeEnd and hall.in_use:
                    hall.in_use = False
                    hall.seats = "0"
                    hall.save()

def home(request):
  films = Film.objects.all()
  fs = []
  reset()
  for film in films:
      if (not film.done):
        fs.append(film)
  template = loader.get_template('home.html')
  context = {
    'films': fs,
    'day': days[datetime.today().weekday()]
  }
  return HttpResponse(template.render(context, request))

def hall(request, num):
    reset()
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
    films = Film.objects.all()
    fs = Film
    for film in films:
        if (film.hall == num):
            if (not film.done and now()<film.timeEnd):
                print(film.title)
                fs = film
                break
    context = {
        'num': str(num),
        'numz': seats,
        'hall': hall,
        'taken': taken,
        'film': fs
    }
    if (request.method == 'POST'):
        cur_seats = strToList.strToList(hall.seats)
        cur_seats.append(int(request.POST.get('s')))
        print(cur_seats)
        hall.seats = strToList.listToStr(cur_seats, True)
        hall.save()
        #return redirect(f"/hall{num}")
        return redirect("/")
    return HttpResponse(template.render(context, request))