from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('',views.index,name="index"),
    path('OTP',views.OTP,name="otp"),
    path('home',views.home,name="home"),
    path('movie',views.movie,name="movie"),
    path('movies',views.allmovies,name="movies"),
    path('theatres',views.theatres,name="theatres"),
    path('search',views.search,name="search"),
    path('theatrehall',views.theatrehall,name="theatrehall"),
    path('bookingSummary',views.bookingSummary,name="bookingsummary"),
    path('payment',views.payment,name="payment"),
    path('paymentOTP',views.paymentOTP,name="paymentOtp"),
    path('booked',views.booked,name="ticket")
]

urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)