from django.urls import path   # imports the path function from Django's urls module, which is used for defining URL patterns.
from .views import TaskListCreateAPIView, TaskRetrieveUpdateDestroyAPIView   ## Importing the 'TaskListCreateAPIView' and 'TaskRetrieveUpdateDestroyAPIView' classes from the current package or module.

urlpatterns =[  # Defining a list named 'urlpatterns' to store URL patterns for the Django project.
    path('tasks/', TaskListCreateAPIView.as_view(), name = 'task-list-create'),   # It specifies that requests 
    #to the /tasks/ endpoint should be handled by the TaskListCreateAPIView class. The as_view() method is 
    #used to convert the class-based view into a callable view function. The name parameter provides a name 
    #for the URL pattern, which can be used to reverse-resolve URLs in Django templates or views.
    
    
    
    path ('tasks/<int:pk>/' , TaskRetrieveUpdateDestroyAPIView.as_view(), name = 'task-detail'),
    #It specifies that requests to the /tasks/<int:pk>/ endpoint should be handled by the 
    #TaskRetrieveUpdateDestroyAPIView class. The <int:pk> part of the URL pattern is a path converter that 
    #matches an integer value and assigns it to a variable named pk. This variable represents the primary key 
    #of the task. The as_view() method is used to convert the class-based view into a callable view function. 
]