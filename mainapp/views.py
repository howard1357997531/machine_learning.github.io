from django.shortcuts import render


def index(request):
    return render(request, 'index.html', locals())


def a1(request):
    return render(request, 'opencv/a1.html', locals())


def a2(request):
    return render(request, 'opencv/a2.html', locals())


def a3(request):
    return render(request, 'opencv/a3.html', locals())


def a4(request):
    return render(request, 'opencv/a4.html', locals())


def a5(request):
    return render(request, 'opencv/a5.html', locals())


def a6(request):
    return render(request, 'opencv/a6.html', locals())


def a7(request):
    return render(request, 'opencv/a7.html', locals())


def a8(request):
    return render(request, 'opencv/a8.html', locals())
