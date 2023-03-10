import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
'soc_courses_review.settings')

import django
django.setup()
from reviewer.models import Course, Review

def populate():
    # First, we will create lists of dictionaries containing the pages
    # we want to add into each category.
    # Then we will create a dictionary of dictionaries for our categories.
    # This might seem a little bit confusing, but it allows us to iterate
    # through each data structure, and add the data to our models.

    OOSE2_Reviews= [
    {'Rating': 5,
     'comment':'Very interesting course'},
    {'Rating': 5,
     'comment':'I really enjoyed this course lectures'},
    {'Rating': 5,
     'comment':'Best ever Course design and very engaging '},]
    
    WAD2_Reviews = [
    {'Rating': 5,
     'comment':'Very interesting course'},
    {'Rating': 5,
     'comment':'I really enjoyed this course lectures'},
    {'Rating': 5,
     'comment':'Best ever Course design and very engaging '},]

    ADS2_Reviews = [
    {'Rating': 5,
     'comment':'Very interesting course'},
    {'Rating': 5,
     'comment':'I really enjoyed this course lectures'},
    {'Rating': 5,
     'comment':'Best ever Course design and very engaging '},]

    Courses = {'OOSE2': {'Reviews': OOSE2_Reviews,'Tag':'Example Tag','Description':'Example Description'},
    'WAD2': {'Reviews': WAD2_Reviews,'Tag':'Example Tag','Description':'Example Description'},
    'ADS2': {'Reviews': ADS2_Reviews,'Tag':'Example Tag','Description':'Example Description'} }


    # If you want to add more courses 
    # add them in the dictionaries stared.

    # The code below goes through the cats dictionary, then adds each category,
    # and then adds all the associated pages for that category.
    for course, course_data in Courses.items():
        c = add_course(course,course_data['Tag'],course_data['Description'])
        for r in course_data['Reviews']:
           add_review(c, r['Rating'], r['comment'])

    # Print out the categories we have added.
    for c in Course.objects.all():
        for r in Review.objects.filter(Course=c):
            print(f'- {c}: {r}')

def add_review(course, rating,  comment):
    r = Review.objects.get_or_create(Course=course, Comment = comment)[0]
    r.Rating = rating
    
    r.save()
    return r

def add_course(name, tag, description):
    c = Course.objects.get_or_create(Name=name)[0]
    c.Tag = tag
    c.Description = description
    c.save()
    return c


# Start execution here!
if __name__ == '__main__':
    print('Starting reviewer population script...')
    populate()

