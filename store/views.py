from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Item, Employee, Customer, Order, OrderItem
import json
import datetime

@csrf_exempt
def create_item(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        item = Item.objects.create(
            name=data['name'],
            description=data['description'],
            price=data['price'],
            category=data['category']
        )
        return JsonResponse({'message': 'Item created successfully!', 'status': '201'}, status=201)
    else:
        return JsonResponse({'error': 'Invalid request', 'status': '400'}, status=400)

@csrf_exempt
def get_items(request):
    items = list(Item.objects.all().values())
    return JsonResponse({'items': items, 'status': '200'}, status=200)

@csrf_exempt
def create_employee(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        employee = Employee.objects.create(
            first_name=data['first_name'],
            last_name=data['last_name'],
            position=data['position'],
            hire_date=data['hire_date'],
            end_date=data['end_date'],
            birth_date=data['birth_date']
        )
        return JsonResponse({'message': 'Employee created successfully!', 'status': '201'}, status=201)
    else:
        return JsonResponse({'error': 'Invalid request', 'status': '400'}, status=400)

@csrf_exempt
def get_employees(request):
    employees = list(Employee.objects.all().values())
    return JsonResponse({'employees': employees, 'status': '200'}, status=200)

@csrf_exempt
def get_customers(request):
    customers = list(Customer.objects.all().values())
    return JsonResponse({'customers': customers, 'status': '200'}, status=200)

@csrf_exempt
def add_customer(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        customer = Customer.objects.create(
            first_name=data['first_name'],
            last_name=data['last_name'],
            email=data['email'],
            phone_number=data['phone_number']
        )
        return JsonResponse({'message': 'Customer created successfully!', 'status': '201'}, status=201)
    else:
        return JsonResponse({'error': 'Invalid request', 'status': '400'}, status=400)

@csrf_exempt
def get_orders(request):
    orders = list(Order.objects.all().values())
    return JsonResponse({'orders': orders, 'status': '200'}, status=200)

@csrf_exempt
def make_order(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        item_list = data['item_list']
        subtotals = []
        for item in item_list:
            _item_id = item['item_id']
            _quantity = item['quantity']
            _item = Item.objects.get(id=_item_id)
            _subtotal = _item.price * _quantity
            subtotals.append(_subtotal) 

        _total_amount = sum(subtotals)

        customer = get_object_or_404(Customer, id=data['customer_id'])
        employee = get_object_or_404(Employee, id=data['employee_id'])

        order = Order.objects.create(
            customer_id=customer,
            employee_id=employee,
            order_date=datetime.datetime.now(),
            total_amount=_total_amount
        )
        
        orderitems = []
        for i in range(len(item_list)):
            _item = get_object_or_404(Item, id=item_list[i]['item_id'])

            orderitems.append(OrderItem.objects.create(
                order_id=order,
                item_id=_item,
                quantity=item_list[i]['quantity'],
                subtotal=subtotals[i]
            )) 
        return JsonResponse({'message': 'Order created successfully!', 'status': '201'}, status=201)
    else:
        return JsonResponse({'error': 'Invalid request', 'status': '400'}, status=400)
  
@csrf_exempt
def get_orders_details(request):
    orders = list(Order.objects.all().values())
    order_details = []
    for order in orders:
        order_id = order['id']
        order_items = list(OrderItem.objects.filter(order_id=order_id).values())
        order['order_items'] = order_items
        order_details.append(order)
    return JsonResponse({'orders': order_details, 'status': '200'}, status=200)



