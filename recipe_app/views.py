from django.shortcuts import render
from recipe_app.forms import NewUserForm
# Create your views here.


def index(request):
    return render(request, 'recipe_app/index.html')


def create(request):
    form = NewUserForm()

    if request.method == 'POST':
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return(index(request))
        else:
            print("ERROR FORM INVALID")

    return render(request, 'recipe_app/create.html', {'form': form})
