from django.shortcuts import render, redirect
from django.utils.html import escape
import re

def home_page(request):
    error = None
    if request.method == "POST":
        search_term = request.POST.get('search')
        print(search_term)
        try:
            injection_check(search_term)
            sanitized_string = escape(search_term)  # Sanitize input
            return redirect('search_results_page', search_term=sanitized_string)
        except ValueError as e:
            error = e
    return render(request, 'home.html', {'error': error})

def search_results_page(request, search_term):
    # Render a template with the search term
    return render(request, 'search_results.html', {'search_term': search_term}, status=200)

def sanitize(input_string):
    # Escaping input to prevent XSS
    return escape(input_string)

def injection_check(input_string):
    # Regex pattern for detecting SQL Injection attempts
    sql_injection_pattern = re.compile(r'(UNION|SELECT|FROM|WHERE|DROP|INSERT|UPDATE|DELETE|--;|\'|")', re.IGNORECASE)
    xss_pattern = re.compile(r'(<script.*?>|javascript:|onmouseover=|onerror=|onload=|<iframe|<img)', re.IGNORECASE)
    if sql_injection_pattern.search(input_string):
        raise ValueError("Potential SQL Injection attack detected.")
    if xss_pattern.search(input_string):
        raise ValueError("Potential XSS attack detected.")
