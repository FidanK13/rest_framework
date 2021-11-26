from django.urls import path
from .views import BookView, RegisterView, LoginView

urlpatterns = [
    path('book-list/', BookView.as_view(), name='book-api'),
    path('register/', RegisterView.as_view(), name='register-api'),
    path('login/', LoginView.as_view(), name='login-api')
]

'''
else:
    context['error_message']='No such user'
    messages.error(request, "username or password is incorrect" )
    return render(request,'login.html', context)
'''