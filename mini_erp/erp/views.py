from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import In_Product,dummy,Out_Product,Master_table
from datetime import datetime
def index(request):
    return render(request,'erp/index.html')

def in_product(in_pro):
    return render(in_pro,'erp/in.html')

def createform(in_pro):
    if in_pro.method == "POST":
        inp = In_Product()
        inp.barcode_number = in_pro.POST['barcode_number']
        inp.product_item = in_pro.POST['product_item']
        inp.product_price = in_pro.POST['product_price']
        inp.Receipt_date = datetime.now()
        inp.Expected_delivery_date = in_pro.POST['Expected_delivery_date']
        inp.destination = in_pro.POST['destination']
        inp.etc = in_pro.POST.get('etc',"없음")
        inp.save()

    return redirect('in_product')


def out_product(out_pro):
    return render(out_pro,'erp/out.html')
def out_create_form(out_pro):
    ot = out_pro.POST.get('barcode_number',False)
    if ot != False:
        out_pr = Out_Product()
        master = Master_table()
        s = In_Product.objects.filter(barcode_number = ot)
        insert_list = []
        for i in s:
            insert_list.append(i.barcode_number)
            insert_list.append(i.product_item)
            insert_list.append(i.product_price)
            insert_list.append(i.Receipt_date)
            insert_list.append(i.Expected_delivery_date)
            insert_list.append(i.destination)
            insert_list.append(i.etc)
        out_pr.barcode_number = insert_list[0]
        out_pr.product_item = insert_list[1]
        out_pr.product_price = insert_list[2]
        out_pr.Receipt_date = insert_list[3]
        out_pr.Expected_delivery_date = insert_list[4]
        out_pr.destination = insert_list[5]
        out_pr.etc = insert_list[6]
        out_pr.save()
        master.barcode_number = insert_list[0]
        master.product_item = insert_list[1]
        master.product_price = insert_list[2]
        master.Receipt_date = insert_list[3]
        master.Expected_delivery_date = insert_list[4]
        master.destination = insert_list[5]
        master.etc = insert_list[6]
        master.save()

        In_Product.objects.filter(barcode_number = ot).delete()
    return redirect('out_product')

def date(da):
    return render(da,'erp/date.html')



def test(map):
    return render(map,'erp/test.html')

