import datetime
from django.test import TestCase
from store.models import Employee
import pytest

@pytest.mark.django_db
def test_over_18():
    test_employee = Employee.objects.create(
        first_name="John",
        last_name="Doe",
        position="Manager",
        hire_date=datetime.date(2018, 1, 1),
        birth_date=datetime.date(2005, 1, 1)
    )
    assert test_employee.under_18() == False

@pytest.mark.django_db
def test_under_18():
    test_employee2 = Employee.objects.create(
        first_name="Jane",
        last_name="Doe",
        position="Crew Member",
        hire_date=datetime.date(2020, 1, 1),
        birth_date=datetime.date(2008, 1, 1)
    )

    assert test_employee2.under_18() == True

@pytest.fixture
def employee(db):
    return Employee.objects.create(
        first_name="Jake",
        last_name="Doke",
        position="Shift Lead",
        hire_date=datetime.datetime.now().date(),
        birth_date=datetime.date(1990, 1, 1)
    )

def test_search_employee(employee):
    assert Employee.objects.filter(first_name="Jake").exists()
