
from django.shortcuts import render
from django.http import HttpResponse
from reviewer.models import Course
from reviewer.models import Review


# Create your views here.

def index(request):

    course_list = Course.objects.order_by('-Name')[:5]
    
    context_dict = {}

    
    context_dict['boldmessage'] = 'WellCome To University Of Glasgow!'
    context_dict['courses'] = course_list
    
    return render(request, 'reviewer/index.html', context=context_dict)

def AllCourses(request):

    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage matches to {{ boldmessage }} in the template!
    context_dict = {'boldmessage': 'This tutorial has been put together by WAD2_team 2A '}
    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.
    return render(request, 'reviewer/Allcourses.html', context=context_dict)

   
def show_course(request, course_name_slug):
    # Create a context dictionary which we can pass
    # to the template rendering engine.
    context_dict = {}
    
    try:
        # Can we find a category name slug with the given name?
        # If we can't, the .get() method raises a DoesNotExist exception.
        # The .get() method returns one model instance or raises an exception.
        course= Course.objects.get(slug=course_name_slug)
        
        # Retrieve all of the associated pages.
        # The filter() will return a list of page objects or an empty list.
        review = Review.objects.filter(course=course)
        
        # Adds our results list to the template context under name pages.
        context_dict['Reviews'] = review
        # We also add the category object from
        # the database to the context dictionary.
        # We'll use this in the template to verify that the category exists.
        context_dict['Course'] = course
    except Course.DoesNotExist:
        # We get here if we didn't find the specified category.
        # Don't do anything -
        # the template will display the "no category" message for us.
        context_dict['Course'] = None
        context_dict['Reviews'] = None
        
    # Go render the response and return it to the client.
    return render(request, 'reviewer/Course.html', context=context_dict)

