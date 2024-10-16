from django.shortcuts import render, redirect
from django.http import HttpResponse
from . forms import PostForm
from . forms import ReplyForm
from . models import OriginALevel_PostModel
from . models import OriginALevel_ReplyModel
from . models import OriginALevel_RatingModel
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .post_tagging import apply_tag
from django.shortcuts import render
from django.db.models import Count
from .models import OriginALevel_PostModel, OriginALevel_ReplyModel, User


# Create your views here.

@login_required(login_url='/login/')
def index_view(request):
    post_form = PostForm()
    context = {
        # all posts are put in the variable posts
        'posts': OriginALevel_PostModel.objects.all()
        }

    if request.GET and 'search' in request.GET:
        context = {
            'posts': OriginALevel_PostModel.objects.filter(title__contains=request.GET['search']),
        }

    return render(request,'OriginALevel_app/layout.html', context )
    # this is under the index_view function because form, by default goes to the method that sent the form
    # the method GET when it gets sent to the server, it goes to index_view to request which form to put on the screen
    


@login_required(login_url='/login/')
def contact_view(request):
    context = {'key': 'This is just another page!'}
    return render(request, 'OriginALevel_app/contact.html', context)



@login_required(login_url='/login/')
def newpost_view(request):
    post_form = PostForm()
    context = {
        'post_form': post_form,
        }

    if request.method == 'POST': # Check if the request method is POST
        post_form = PostForm(request.POST) # Create a new instance of the `PostForm` with data from the POST request
        if post_form.is_valid(): # Check if the form data is valid
            if 'code' in apply_tag(post_form.cleaned_data['body'])[0]: # Check if the result of `apply_tag` has a key 'code'
                context['tag_code'] = apply_tag(post_form.cleaned_data['body'])[0]['code'] # Store the code value in `tag_code`
                context['tag_title'] = apply_tag(post_form.cleaned_data['body'])[0]['title'] # Store the title value in `tag_title`
                context['tags'] = apply_tag(post_form.cleaned_data['body'])[1] # Store the tags in `tags`
            else: # If 'code' key is not present in the result of `apply_tag`
                context['tag_code'] = "" # Set `tag_code` to an empty string
                context['tag_title'] = "" # Set `tag_title` to an empty string
                context['tags'] = "" # Set `tags` to an empty string
            # Get or create a new post using the data from the form and additional data
            new_post = OriginALevel_PostModel.objects.get_or_create(
                user_id=request.user, # User who made the post
                tags=context['tags'], # Tags associated with the post
                tag_code=context['tag_code'], # Code extracted from the post
                tag_title=context['tag_title'], # Title extracted from the post
                title=post_form.cleaned_data['title'], # Title of the post
                body=post_form.cleaned_data['body'] # Body of the post
                )

        return redirect('/')
    return render(request, 'OriginALevel_app/post.html', context)


@login_required(login_url='/login/')
def reply_view(request):
    # Initialize a ReplyForm instance
    reply_form = ReplyForm()
    # Create a context dictionary to pass data to the template
    context = {
        'reply_form': reply_form,
        'post_id': request.POST.get('post_id'),
        }

    if request.method == 'POST' and ('btn-send-reply' in request.POST and 'post_id' in request.POST and request.POST['post_id'] != ''):
        # If the request method is a POST request and 'btn-send-reply' and 'post_id' are present in the request POST data
        reply_form = ReplyForm(request.POST)
        if reply_form.is_valid():
            # If the reply form is valid, create a new reply instance
            new_reply = OriginALevel_ReplyModel.objects.get_or_create(
                replied_by=request.user, 
                post=OriginALevel_PostModel.objects.get(id=request.POST.get('post_id')),
                body=reply_form.cleaned_data['body']
            )
        # Redirect the user to the home page
        return redirect('/')
    # Render the 'OriginALevel_app/reply.html' template with the context data
    return render(request, 'OriginALevel_app/reply.html', context)



@login_required(login_url='/login/')
def rate_post_view(request):
    if request.method == 'POST' and 'rating' in request.POST:
        # requests user data
        user=request.user
        post_id=request.POST.get('post_id') # gets the id of the post which the user rated
        rating_value=request.POST.get('rating') # rating value is out of 5
        rating_exists=OriginALevel_RatingModel.objects.filter(post=post_id, rated_by=user).first() # checks for the first rating the user made for a certain question

        if rating_exists:
            rating_exists.delete() # initial rating will be replaced by the second rating made by the user

        # in the new_rating, the objects from the Rating model will be either updated if there is a rating or created if none has been mae for a particular question post
        new_rating = OriginALevel_RatingModel.objects.update_or_create (
            rated_by=user,
            post=OriginALevel_PostModel.objects.get(id=post_id),
            rating=rating_value,
            )
    # returns the user to the main page after rating has been made
    return redirect('/')




# @login_required(login_url='/login/')
# def rate_post_view(request):
#     if request.method == 'POST' and 'rating' in request.POST:
#         # requests user data
#         user=request.user
#         post_id=request.POST.get('post_id') # gets the id of the post which the user rated
#         rating_value=request.POST.get('rating') # rating value is out of 5
#         rating_exists=OriginALevel_RatingModel.objects.filter(post=post_id, rated_by=user).first() # checks for the first rating the user made for a certain question

#         if rating_exists:
#             rating_exists.delete() # initial rating will be replaced by the second rating made by the user

#         # in the new_rating, the objects from the Rating model will be either updated if there is a rating or created if none has been mae for a particular question post
#         new_rating = OriginALevel_RatingModel.objects.update_or_create (
#             rated_by=user,
#             post=OriginALevel_PostModel.objects.get(id=post_id),
#             rating=rating_value,
#             )
#     # returns the user to the main page after rating has been made
#     return redirect('/')