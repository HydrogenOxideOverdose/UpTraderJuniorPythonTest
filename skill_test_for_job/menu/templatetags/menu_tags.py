from django import template
from django.utils.html import format_html
from ..models import Menu
import json


register = template.Library()


@register.simple_tag(takes_context=True)
def draw_menu(context, name):


    request = context['request']
    path = request.path
    new_path = '?' + '&'.join( [ param[0]+"="+param[1][0] for param in request.GET.lists() if param[0]!=name ] )
    print( new_path, '===========================', path, list(request.GET.lists()) )
    try:
        points = request.GET.get(name)
        print(
            name, points, "-----------------------------------------"
        )
        points = [int(child)-1 for child in points.split(",")] + [-1]

    except:
        points = [-1]


    menu = Menu.objects.all()
    menu = menu.filter(name = name)
    print(menu[0].fields, "-------------------------" )
    print(menu[0].name, "-------------------------" )
    print(menu[0], "-------------------------" )
    menu = json.loads(menu[0].fields)

    result_begin = f"<p><b>{menu['name']}</b></p>"
    result_end = f""

    address = "&" + name + "="
    for iteration in range(len(points)):
        try:
            index = 0
            result_buffer = f""
            new_address = ""
            for element in menu["children"]:
                print(element["name"])
                if index < points[iteration]:
                    result_begin += f"<p><a href='{new_path + address + str(index+1)}' >{'----'*iteration + '> ' + element['name']}</a></p>"
                elif index == points[iteration]:
                    result_begin += f"<p><a href='{new_path + address + str(index+1)}' ><b>{'----'*iteration + '> ' + element['name']}</b></a></p>"
                    new_address = address + str(index+1) + ","
                else:
                    result_buffer += f"<p><a href='{new_path + address + str(index+1)}' >{'----'*iteration + '> ' + element['name']}</a></p>"
                index += 1
            address = new_address
            result_end = result_buffer + result_end
            menu = menu["children"][points[iteration]]
        except:
            break




    return format_html(f"<div class='menu'>{result_begin + result_end}</div>")