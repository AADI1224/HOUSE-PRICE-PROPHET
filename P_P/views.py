from django.shortcuts import render, HttpResponse, redirect, reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
@csrf_protect
def welcome(request):
    return render(request, "WELCOME.html")

@csrf_protect
def home(request):
    return render(request, "HOME.html")

@csrf_protect
def aboutus(request):
    return render(request, "ABOUTUS.html")

@csrf_protect
#@login_required(login_url='HOME:LOGIN')
def LOGIN(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('pass')
        print(username, password)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('PREDICTION')
        else:
            data = {"t1": [{"id": 1, "name": "invalid username or password"}]}
            return render(request, 'LOGIN.html', data)
    return render(request, "LOGIN.html")

@csrf_protect
def signup(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 != password2:
            return HttpResponse('Password are not same')

        else:
            my_user = User.objects.create_user(uname, email, password1)
            my_user.save()
            return redirect('LOGIN')
    return render(request, "SIGNUP.html")

@csrf_protect
@login_required(login_url='HOME:LOGIN')
def prediction(request):
    return render(request, "PREDICTION.html")

@csrf_protect
def result(request):
    data = pd.read_csv(r'C:\Users\aadit\Downloads\HOUSE_PRICE_PREDICTION\HOUSE_PRICE_PREDICTION\USA_Housing.csv')
    data.drop(['Address'], axis=1, inplace=True)

    X = data.drop('Price', axis=1)
    Y = data['Price']

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=70)

    model = LinearRegression()
    model.fit(X_train, Y_train)

    var1 = float(request.GET['n1'])
    var2 = float(request.GET['n2'])
    var3 = float(request.GET['n3'])
    var4 = float(request.GET['n4'])
    var5 = float(request.GET['n5'])

    pred = model.predict(np.array([var1, var2, var3, var4, var5]).reshape(1,-1))
    pred = round(pred[0])

    price = "The Predicted Price is $" + str(pred)

    return render(request, "PREDICTION.html", {"result2":price})

