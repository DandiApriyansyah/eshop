from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'name' : 'Kaos Kaki',
        'price': '100000',
        'description': 'kualitas terjamin, harga minimalis'
    }

    return render(request, "main.html", context)