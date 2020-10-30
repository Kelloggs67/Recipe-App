from django.shortcuts import render
from recipe_app.forms import NewUserForm
from recipe_app.models import LoginInfo
# Create your views here.


def index(request):
    user_list = LoginInfo.objects.order_by('username')
    user_dict = {'users': user_list}
    return render(request, 'recipe_app/index.html', context=user_dict)


def create(request):
    form = NewUserForm()

    if request.method == 'POST':
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print("ERROR FORM INVALID")

    return render(request, 'recipe_app/create.html', {'form': form})


