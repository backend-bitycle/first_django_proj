from re import template
from django.shortcuts import render
from decouple import config
import requests

# Create your views here.
key = config('API_KEY')
url = config('BASE_URL')

def show_list(request):
    template = 'list.html'
    url1 = url+"list"
    payload = {}
    headers= {
    "apikey": key
    }
    response = requests.request("GET", url1, headers=headers, data = payload)
    data = response.json()
    symbols = data['currencies']
    context = {'symbols': symbols}

    # Pass data to the template
    return render(request, template, context)

def show_live(request):
    template = 'live.html'

    url1 = url+"live?"
    payload = {}
    headers= {
    "apikey": key
    }
    response = requests.request("GET", url1, headers=headers, data = payload)
    # response data converted to json
    data = response.json()
    quotes = data['quotes']
    context = {'quotes': quotes}

    # Pass data to the template
    return render(request, template, context)

def index(request):
    # define the temlate name
    template = 'index.html'
    if request.method == 'POST':

        # first currency
        currency1 = request.POST.get('currency1', False)

        # second currency
        currency2 = request.POST.get('currency2', False)

        # amount to exchnage
        amount= request.POST.get('amount', False)
        url1 = url + f"convert?to={currency2}&from={currency1}&amount={amount}"
        payload = {}
        headers= {
        "apikey": key
        }
        response = requests.request("GET", url1, headers=headers, data = payload)
        # response data convterted to json
        data = response.json()
        rate = data['info']['quote']
        amt = data['result']
        context = {"rate": rate, 'amount': amt}

        # render the template with the data passed to it
        return render(request, template, context)
    else:
        return render(request, template)
    
def show_historical(request):
    # specify the templaet name
    template = 'historical.html'

    if request.method == 'POST':
        # extract date from the post request
        date = request.POST.get('date', False)   
        url1 = url + f"historical?date={date}"
        payload = {}
        headers= {
        "apikey": key
        }
        response = requests.request("GET", url1, headers=headers, data = payload)
        # convert the response data to json
        data = response.json()
        quotes = data['quotes']
        context = {'quotes': quotes}

        # Passing the data to the temlate
        return render(request, template, context)
    else:
        return render(request, template)

