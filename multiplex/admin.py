from django.contrib import admin
from .models import Crew, Movie
from .models import Theatre
from .models import Cast
from .models import Crew
from .models import Kirthika
from .models import Ticket
from .models import User
# Register your models here.

admin.site.register(Movie)
admin.site.register(Theatre)
admin.site.register(Cast)
admin.site.register(Crew)
admin.site.register(Kirthika)
admin.site.register(Ticket)
admin.site.register(User)

