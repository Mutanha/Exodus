# views.py

from django.shortcuts import render
from django.http import JsonResponse

from .models import Employee

def search_employees(request):
    if request.method == 'GET':
        # Extract search criteria from the request
        name = request.GET.get('name')
        employer = request.GET.get('employer')
        position = request.GET.get('position')
        department = request.GET.get('department')
        year_started = request.GET.get('year_started')
        year_left = request.GET.get('year_left')
        
        # Build the filter criteria based on the provided parameters
        filter_criteria = {}
        if name:
            filter_criteria['name__icontains'] = name
        if employer:
            filter_criteria['employer__icontains'] = employer
        if position:
            filter_criteria['position__icontains'] = position
        if department:
            filter_criteria['department__icontains'] = department
        if year_started:
            filter_criteria['year_started'] = year_started
        if year_left:
            filter_criteria['year_left'] = year_left
        
        # Perform the search query
        employees = Employee.objects.filter(**filter_criteria)
        
        # Prepare the response data
        results = []
        for employee in employees:
            results.append({
                'name': employee.name,
                'employer': employee.employer,
                'position': employee.position,
                'department': employee.department,
                'year_started': employee.year_started,
                'year_left': employee.year_left,
                # ... other fields
            })
        
        return JsonResponse({'results': results})