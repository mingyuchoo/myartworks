from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.shortcuts import render, redirect


from .forms import ContactForm


def index(request):
    """
    Index
    """
    # context = {}
    # return render(request, 'common/index.html', context)

    return redirect('gallery:portfolio.tile')

    # if request.user is not None:
    #     return redirect('accounts:profile.detail', username=request.user.username)
    # else:
    #     return redirect('gallery:portfolio.user')


def about(request):
    return render(request, 'common/about.html')


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['playanetworks@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('common:thanks')
    else:
        form = ContactForm()
    return render(request, "common/contact.html", {'form': form})


def thanks(request):
    message = 'Thank you for your message.'
    return render(request, "common/thanks.html", {'message': message})


def privacy(request):
    """
    Privacy Policy

    """
    return render(request, 'common/privacy.html')


def terms(request):
    """
    Terms of Us
    """
    return render(request, 'common/terms.html')


def logout(request):
    """
    Logout
    """
    return render(request, 'common/logout.html', {})


def password_change(request):
    """
    Password Change
    """
    return render(request, 'common/password_change.html', {})


def handler400(request):
    """
    HTTP Error 404 Bad request
    """
    return HttpResponse('<h1>HTTP Error 400 Bad request</h1>', {})


def handler403(request):
    """
    HTTP Error 403 Forbidden
    """
    return HttpResponse('<h1>HTTP Error 403 Forbidden.</h1>', {})


def handler404(request):
    """
    HTTP Error 404 Not Found
    """
    return HttpResponse('<h1>HTTP Error 404 Not Found</h1>', {})


def handler404(request):
    """
    HTTP Error 405 Method Not Allowed
    """
    return HttpResponse('<h1>HTTP Error 405 Method not allowed</h1>', {})


def handler500(request):
    """
    HTTP Error 500 Internal Server Error
    """
    return HttpResponse('<h1>HTTP Error 500 Internal server error</h1>', {})
