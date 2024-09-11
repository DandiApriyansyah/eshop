from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'application' : 'Shopeeta',
        'name' : 'Dandi Apriyansyah',
        'kelas' : 'PBP A',
       }

    return render(request, "main.html", context)