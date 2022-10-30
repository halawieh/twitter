from datetime import datetime
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view

from feed.models import Tweet

def feed(request):
    tweets = Tweet.objects.all()
    tweets = [{"name": tweet.name, "tweet": tweet.tweet, "created_at": datetime.strftime(tweet.created_at, "%H:%M:%S")} for tweet in tweets]

    return render(request, 'templates/home.html', {"tweets": tweets})

@api_view(['POST'])
def tweet(request):
    data = request.data
    tweet = Tweet(name=data['name'], tweet=data['tweet'])
    tweet.save()

    return JsonResponse({"name": tweet.name, "tweet": tweet.tweet, "created_at": datetime.strftime(tweet.created_at, "%H:%M:%S")})