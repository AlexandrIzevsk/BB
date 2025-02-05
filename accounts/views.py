from django.contrib.auth.models import User
from django.views.generic.edit import CreateView
from django.shortcuts import redirect, render
from .forms import SignUpForm
from .models import OneCode


class SignUp(CreateView):
    model = User
    form_class = SignUpForm
    success_url = '/accounts/confirm_signup'
    template_name = 'registration/signup.html'

def confirm_signup(request):
    if request.method == "POST":
        code = request.POST.get("code")
        if OneCode.objects.filter(code=code).exists():
            user = OneCode.objects.get(code=code).user
            user.is_active = True
            user.save()
            OneCode.objects.filter(code=code).delete()
            return redirect("/accounts/login/")
        return render(request, 'registration/confirm_error.html')
    return render(request, 'registration/confirm_signup.html')