from django.shortcuts import render
from .models import  Employee, About, Contact, Team
                    


def index(request):
    return render(request,"home.html")


def employees(request):
    employees = Employee.objects.all()
    return render(request,"employees.html", {"employees":employees})


def about(request):
    about_text = About.objects.all()
    team = Team.objects.all()
    return render(request,"about.html", {
        "about_text":about_text,
        "team": team
    })


def contact(request):
    contact_text = Contact.objects.all()
    return render(request,"contact.html", {"contact_text":contact_text})


def single_employee(request, employee_id):
    employee = Employee.objects.get(pk=employee_id)
    return render(request,"single_employee.html",{"employee":employee})
     

def single_member(request, member_id):
    member =Team.objects.get(pk=member_id)
    return render(request, "single_member.html", {"member":member})
    


