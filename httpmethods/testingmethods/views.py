from django.shortcuts import render

# Create your views here
def testingapp(request):
    firstName=request.GET.get("fname") if request.GET.get("fname") else "john"
    lastName=request.GET.get("lname") if request.GET.get("fname") else "doe"
    fullName=firstName +' ' + lastName
    context={"fullname":fullName}
    return render(request,'home.html',context)

def testingappPOST(request):
    number1=request.POST.get("number1") if request. POST.get("number1") else 1
    print(number1)
    number2=request.POST.get("number2") if request.POST.get("number2") else 1
    print(number2)
    sum=number1+number2
    context={"sum" :sum}
    return render(request,'home.html',context)