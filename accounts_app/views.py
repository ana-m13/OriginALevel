from django.shortcuts import render
from django.contrib.auth.models import User
from . forms import LoginForm, UserRegisterForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required





def login_view(request):
    if request.user.is_authenticated:
        return redirect('/')

    # Initialize an instance of the LoginForm form
    form = LoginForm()
    context = {'form': form}

    # Check if the request method is 'POST'
    if request.method == 'POST':
        form = LoginForm(request.POST) # Re-initialize the form instance with the data from the request.POST dictionary
        context = {'form': form} # Update the context dictionary with the updated form instance
        user = authenticate(request, # Attempt to authenticate the user with the provided username and password
            username=request.POST.get('username'), # form.cleaned_data['username'],
            password=request.POST.get('password')
            )
        username_exists = User.objects.filter(username=request.POST.get('username')) or None
            
        if user is not None:
            login(request, user)
            request.session['user_name_from_session'] = request.POST.get('username')
            return redirect('/')
        else:
            if request.POST.get('username') and not username_exists:
                form.errors['username'] = 'Username does not exist!'
            if not user:
                form.errors['password'] = 'Password incorrect!'
            render(request, 'accounts_app/login.html', context)

    # GET request
    return render(request, 'accounts_app/login.html', context)


        

@login_required
def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect("/")
    


def register_view(request):
    form = UserRegisterForm()
    context = {'form': form}

    if request.user.is_authenticated:
        return redirect("/", context)
    
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        context = {'form': form}

        if form.is_valid():
            context = {'email': form.cleaned_data['email']}
            form.save()
            return render(request, 'accounts_app/thankyou.html', context) # if form is valid

        return render(request, 'accounts_app/register.html', context) # if form not valid

    return render(request, 'accounts_app/register.html', context) # request method GET







# from django.shortcuts import render, redirect
# from . forms import LoginForm
# from django.contrib.auth.models import User
# from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.decorators import login_required
# from .forms import UserRegisterForm
# from django.contrib.auth.decorators import login_required





# def login_view(request):
#     if request.user.is_authenticated:
#         return redirect('/')
        
#     form = LoginForm()
#     context = {'form': form}

#     if request.method == 'POST':

#         form = LoginForm(request.POST)
#         context = {'form': form,}
#         user = authenticate(request,
#             username=request.POST.get('username'), # form.cleaned_data['username'],
#             password=request.POST.get('password')
#             )
#         username_exists = User.objects.filter(username=request.POST.get('username'))

#         # if the user details exist in the database, then the login details would be accepted 
#         # and the user would be directed to the main page
#         if user is not None:
#             login(request, user)
#             request.session['user_name_from_session'] = request.POST.get('username')
#             return redirect('/')
#         else:
#             # if the user doesn't exist, the following error messages would appear
#             if request.POST.get('username') and not username_exists:
#                 form.errors['username'] = 'Username does not exist!'
#             if not user:
#                 form.errors['password'] = 'Password incorrect!' 
#             render(request, 'accounts_app/login.html', context)

#     # GET request
#     return render(request, 'accounts_app/login.html', context)




# @login_required
# def logout_view(request):
#     if request.user.is_authenticated:
#         logout(request)
#     return redirect("/")



# def register_view(request):
#     form = UserRegisterForm()
#     context = {'form': form}

#     # when it gets to the register page, the alg looks in the system to see of youre authenticated. It will then send the user tot he main page. If not the user will have to make an account
#     if request.user.is_authenticated:
#         return redirect("/", context)

#     # when user inputs data in input boxes, and then presses the submit button, it checks if data is valid or not
#     # if data is valid then it will register a new user, otherwise the form will be rerendered and it will show errors
#     if request.method == 'POST':
#         form = UserRegisterForm(request.POST)
#         context = {'form': form }

#         if form.is_valid():
#             context = {'email':form.cleaned_data['email'],}
#             form.save()
#             return render(request, 'accounts_app/thankyou.html', context) # if form is valid it goes onto thankyou page
#         # email confirmation
#         return render(request, 'accounts_app/register.html', context) # request method GET
#     return render(request, 'accounts_app/register.html',context) # if form is not valid

