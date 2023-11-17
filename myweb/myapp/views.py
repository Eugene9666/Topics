from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Login, Goods, DailyInOut,Transfer,Client
from django.db.models import Sum

# Create your views here.
def login(request):
    if request.method == "POST":
        print(request.POST)
        print(request.POST.get('submit'))
        if request.POST.get('submit') == 'login':
            userName = request.POST['username']
            password = request.POST['password']
            account = Login.objects.filter(userName = userName, password = password)
            print(account)
            if account:
                request.session['user'] = userName
                return redirect(Tgoods)
            else:
                return HttpResponse('Please enter valid Username or Password.')
    else:
        print("\n\n\n沒有posted")
    return render(request,'login.html')

def Tgoods(request):
    if 'user' in request.session:
        current_user = request.session['user']
        goods = Goods.objects.all()
        dailys = DailyInOut.objects.values('productId').annotate(total_count_quantity=Sum('countQuantity'))
        for good in goods:
            count_sum = DailyInOut.objects.filter(productId=good.productId).aggregate(total_count_quantity=Sum('countQuantity'))
            purchase_sum = DailyInOut.objects.filter(productId=good.productId).aggregate(total_purchase_quantity=Sum('purchaseQuantity')) 
            export_sum = DailyInOut.objects.filter(productId=good.productId).aggregate(total_export_quantity=Sum('exportQuantity'))  
            transfers = Transfer.objects.filter(productId=good.productId)

            positions = []
            for transfer in transfers:
                if transfer.position1:
                    positions.append(transfer.position1)
                if transfer.position2:
                    positions.append(transfer.position2)
                if transfer.position3:
                    positions.append(transfer.position3)
            good.positions = ', '.join(positions)
            
            good.total_count_quantity = count_sum['total_count_quantity']
            good.total_purchase_quantity = purchase_sum['total_purchase_quantity']
            good.total_export_quantity = export_sum['total_export_quantity']
    return render(request,'Tgoods.html',locals())


def logout(request):
    try:
        del request.session['user']
    except:
        return redirect('/')
    return redirect('/') 

def Tdaily(request):
    if 'user' in request.session:
        current_user = request.session['user']
        dailys = DailyInOut.objects.all()
    return render(request,'Tdaily.html',locals())

def Ttransfer(request):
    if 'user' in request.session:
        current_user = request.session['user']
        transfers = Transfer.objects.all()
    return render(request,'Ttransfer.html',locals())

def Tclient(request):
    if 'user' in request.session:
        current_user = request.session['user']
        clients = Client.objects.all()
    return render(request,'Tclient.html',locals())



