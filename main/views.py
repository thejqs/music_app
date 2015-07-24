# Python
import oauth2 as oauth
import cgi

# Django
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from main.models import Artists, Albums, CustomUser


google_token_url = "https://accounts.google.com/o/oauth2/token"
google_auth_url = "https://accounts.google.com/o/oauth2/auth"


def home(request):
    context = {}
    return render_to_response('index.html', context, context_instance=RequestContext(request))


def artist_list(request):
    context = {}

    context['all_artists'] = Artists.objects.all()

    return render_to_response('artist.html', context, context_instance=RequestContext(request))


def artist_detail(request, artist_id):
    context = {}

    context['artist'] = Artists.objects.get(artist_id=artist_id)

    return render_to_response('artist_detail.html', context, context_instance=RequestContext(request))


def google_login(request):
    token_request_uri = "https://accounts.google.com/o/oauth2/auth"
    response_type = "code"
    client_id = settings.CLIENT_ID
    redirect_uri = "http://127.0.0.1:8000/google_auth/"
    scope = "https://www.googleapis.com/auth/userinfo.profile https://www.googleapis.com/auth/userinfo.email"
    url = "{token_request_uri}?response_type={response_type}&client_id={client_id}&redirect_uri={redirect_uri}&scope={scope}".format(
                token_request_uri=token_request_uri,
                response_type=response_type,
                client_id=client_id,
                redirect_uri=redirect_uri,
                scope=scope
                )

    # url = """
    #     { google_auth_url }?
    #     scope=email%20profile&
    #     redirect_uri=https%3A%2F%2Foauth2-login-demo.appspot.com%2Fcode&,
    #     response_type=code&
    #     client_id={ client id }
    #     approval_prompt=force""".format(redirect_uri="http://127.0.0.1:8000/google_auth/",
    #                                                 client_id=settings.CLIENT_ID,
    #                                                 google_auth_url=google_auth_url,
    #                                                 )
    return HttpResponseRedirect(url)
