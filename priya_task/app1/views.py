from django.shortcuts import render
from .models import Data_Saved
import pandas as pd

# Create your views here.
from django.views.generic import CreateView


def save(request):

    qs=Data_Saved.objects.all()
    if qs:
        return render(request, 'search.html', {'qs': qs})
    else:
        df = pd.read_csv(r'C:\Users\m pradeep\Desktop\cm27FEB2020bhav.csv', parse_dates=['TIMESTAMP'])
        df = df.drop(['TOTALTRADES', 'ISIN', 'Unnamed: 13'], axis='columns')
        df = df.tail(30)
        a = df.values
        for x in a:
            a,b,c,d,e,f,g,h,i,j,z=x
            print(a,b,c,d,e,f,g,h,i,j,z)
            Data_Saved(sym=a,series=b,open=c,high=d,low=e,close=f,last=g,pre=h,totqty=i,data=j).save()
        return render(request,'search.html',{'msg':'details are saved'})




def detail(request):
    sya=request.POST['sya']
    try:
        qs=Data_Saved.objects.get(sym=sya)
        return render(request,'details.html',{'qs':qs})
    except Data_Saved.DoesNotExist:
        return None
