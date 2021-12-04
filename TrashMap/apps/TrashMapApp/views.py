from  django.http import HttpResponse
from django.shortcuts import render
from .models import CamMarker
import json


# Процесс создания точки и ее содержимого
def create_marker(cord, name, adress_name, mode, imagePath, date, request):

    # Есть мусорка - иконка красная
    # Нет мусора - иконка зеленоая
    iconMode = "islands#darkGreenIcon"
    htmlStatus = "Избыток мусора не обнаружен!"
    htmlColor = "green"
    if (mode == 1):
        iconMode = "islands#redIcon"
        htmlStatus = "Обнаружен избыток мусора!"
        htmlColor = "red"

    rq = request.get_host()
    hrefImage = f'<a href="http://{rq}/static/media/{imagePath}" target="_blank"><h4>Ссылка на скриншот камеры</h4></a>'

    htmlHeader = f'<div><h1>{adress_name}</h1>' \
                 f"<h4>Дата проверки: {date.strftime('%Y-%m-%d %H:%M:%S')}</h4>"\
                 f'<h4>Статус: <font color="{htmlColor}">{htmlStatus}</font></h4>' \
                 f'{hrefImage}</div>'

    res = ''
    cordn = json.loads(cord)
    res += f'var {name} = new ymaps.Placemark(\n' \
           f'{cordn}\n' \
           ',{' \
           f'hintContent: "{adress_name}",' \
           f"balloonContent: '{htmlHeader}'" \
           '},{' \
           f'preset: "{iconMode}"' \
           '});'

    return res

#hintContent: 'Собственный значок метки'

def generate_map(request):
    markers = CamMarker.objects.all()
    res = 'ymaps.ready(init);\n' \
          'function init(){\n' \
          'var map = new ymaps.Map("map", {\n' \
          'center: [54.88603796475703,52.330651293579095],\n' \
          'zoom: 12\n' \
          '});\n'

    ending = 'map.geoObjects'
    for i in range(len(markers)):
        marker_name = f'marker{i}'
        res += create_marker(markers[i].c_cord,
                             marker_name,
                             markers[i].c_name,
                             markers[i].c_mode,
                             markers[i].c_image,
                             markers[i].c_date,
                             request)
        ending += f'.add({marker_name})'
    res += ending
    res += '}'

    print (res)

    return res

def index(request):

    script = generate_map(request)

    return render(request, "index.html", {'script': script})