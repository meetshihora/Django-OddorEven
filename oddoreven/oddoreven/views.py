from django.shortcuts import render

def oddoreven(request):
    result = ""
    try:
        if request.method == 'POST':
            number = eval(request.POST.get('number'))
            if number % 2 == 0:
                result = "Even"
            else:
                result = "Odd"
    except:
        result = "Invalid number"
    return render(request, 'evenorodd.html' , {'result': result})