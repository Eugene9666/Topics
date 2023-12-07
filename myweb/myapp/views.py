from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Login, Goods, DailyInOut,Transfer,Client
from django.db.models import Sum
from django.views.decorators.csrf import csrf_exempt 

# Create your views here.
@csrf_exempt
def login(request):
    if request.method == "POST":
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
    return render(request,'login.html')

@csrf_exempt
def regist(request):
    if request.method == "POST":
        if request.POST.get('submit') == 'regist':
            userName = request.POST['username']
            password = request.POST['password']
            repassword = request.POST['repassword']
            Name = request.POST['name']
            if password == repassword:
                user = Login(userName = userName, password = password, Name = Name)
                user.save()
                return redirect('/')
            else:  
                return HttpResponse('密碼不一樣')
    return render(request,'regist.html')

@csrf_exempt
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

@csrf_exempt
def Tdaily(request):
    if 'user' in request.session:
        current_user = request.session['user']
        dailys = DailyInOut.objects.all()
    return render(request,'Tdaily.html',locals())

@csrf_exempt
def Ttransfer(request):
    if 'user' in request.session:
        current_user = request.session['user']
        transfers = Transfer.objects.all()
    return render(request,'Ttransfer.html',locals())

@csrf_exempt
def Tclient(request):
    if 'user' in request.session:
        current_user = request.session['user']
        clients = Client.objects.all()
    return render(request,'Tclient.html',locals())

def searchGoods(request):
    query = request.GET['searchGoods']
    goods = Goods.objects.filter(productName__icontains = query) | Goods.objects.filter(productId__icontains = query)
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

def searchDaily(request):
    query = request.GET['searchDaily']
    dailys = DailyInOut.objects.filter(productId__icontains = query)
    return render(request,'Tdaily.html',locals())

def searchClient(request):
    query = request.GET['searchClient']
    clients = Client.objects.filter(productId__icontains = query) | Client.objects.filter(client__icontains = query) | Client.objects.filter(productName__icontains = query)
    return render(request,'Tclient.html',locals())

def searchTransfer(request):
    query = request.GET['searchTransfer']
    transfers = Transfer.objects.filter(productId__icontains = query) | Transfer.objects.filter(productName__icontains = query)
    return render(request,"Ttransfer.html",locals())