from django.shortcuts import render
from django.http import HttpResponse

def bar_chart_view(request):
    context = {
        'delivered': 4,
        'claimed':2,
        'carrier_block':2,
        'error':1,
        'unsent':6
    }
    return render(request, 'bar_chart/bar_chart.html', context)