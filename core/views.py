from django.shortcuts import render
from django.http import HttpResponse
import requests

def index(request):
    return render(request, 'core/index.html')

def ipo_proxy(request):
    """
    Proxy endpoint to load the UAT IPO page inside an iframe.
    """
    target_url = "https://uat-ipo.findoc.com"
    try:
        response = requests.get(target_url, headers={"User-Agent": "Mozilla/5.0"})
        return HttpResponse(response.content)
    except requests.exceptions.RequestException as e:
        return HttpResponse(f"Error fetching {target_url}: {e}", status=500)
