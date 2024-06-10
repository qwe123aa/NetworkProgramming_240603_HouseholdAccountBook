import json

from django.shortcuts import render

def show_chart(request):
    with open('data/data.json', 'r', encoding='utf-8') as file:
        json_data = json.load(file)

    name = [item['name'] for item in json_data]
    price = [item['price'] for item in json_data]
    ctgColor = [item['ctgColor'] for item in json_data]

    context = {
        'name' : name,
        'price' : price,
        'ctgColor' : ctgColor
    }

    return render(request, 'chart_test/chart_view.html', context=context)