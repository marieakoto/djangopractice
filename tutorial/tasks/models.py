from django.db import models        #Default import statement to be included in all model modules from Django's database.

# The actual model is created here.
class Task(models.Model):           ##creates a model called task that inherits from Django's Model class.
    title = models.CharField(max_length = 100) #adds title field and sets it to maximum 100 characters
    description = models.TextField()   # adds description field with no maximum characters
    completed = models.BooleanField(default = False)  #adds a completed checker set to false by default
    created_at = models.DateTimeField(auto_now_add = True) # adds a time stamp to log the time entry was made.
