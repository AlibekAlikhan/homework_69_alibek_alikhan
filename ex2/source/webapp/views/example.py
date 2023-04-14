import json
from django.http import HttpResponse, JsonResponse, HttpResponseNotAllowed
from django.shortcuts import render
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_exempt


@ensure_csrf_cookie
def get_token_view(request, *args, **kwargs):
    if request.method == 'GET':
        return HttpResponse()
    return HttpResponseNotAllowed(f'Only GET request are allowed {request.method}')


def index(request):
    return render(request, 'index.html')


@csrf_exempt
def add(request, *args, **kwargs):
    if request.method == 'GET':
        answer = {
            "A": 1234,
            "B": 4567
        }
        return JsonResponse(answer)
    if request.method == 'POST' and request.body:
        article = json.loads(request.body)
        a = article.get('A')
        b = article.get('B')
        try:
            answer_result = int(a) + int(b)
            result = {
                "answer": answer_result
            }
            response = JsonResponse(result)
            response.status_code = 201
            print(response.__dict__)
        except Exception:
            response_data = {"error": "Division by zero!"}
            response = JsonResponse(response_data)
            response.status_code = 400
        return response


@csrf_exempt
def subtract(request, *args, **kwargs):
    if request.method == 'GET':
        answer = {
            "A": 1234,
            "B": 4567
        }
        return JsonResponse(answer)
    if request.method == 'POST' and request.body:
        article = json.loads(request.body)
        a = article.get('A')
        b = article.get('B')
        try:
            answer_result = int(a) - int(b)
            result = {
                "answer": answer_result
            }
            response = JsonResponse(result)
            response.status_code = 201
        except Exception:
            response_data = {"error": "Division by zero!"}
            response = JsonResponse(response_data)
            response.status_code = 400
        return response


@csrf_exempt
def multiply(request, *args, **kwargs):
    if request.method == 'GET':
        answer = {
            "A": 1234,
            "B": 4567
        }
        return JsonResponse(answer)
    if request.method == 'POST' and request.body:
        article = json.loads(request.body)
        a = article.get('A')
        b = article.get('B')
        try:
            answer_result = int(a) * int(b)
            result = {
                "answer": answer_result
            }
            response = JsonResponse(result)
            response.status_code = 201
        except Exception:
            response_data = {"error": "Division by zero!"}
            response = JsonResponse(response_data)
            response.status_code = 400
        return response


@csrf_exempt
def divide(request, *args, **kwargs):
    if request.method == 'GET':
        answer = {
            "A": 1234,
            "B": 4567
        }
        return JsonResponse(answer)
    if request.method == 'POST' and request.body:
        article = json.loads(request.body)
        a = article.get('A')
        b = article.get('B')
        try:
            answer_result = int(a) / int(b)
            result = {
                "answer": answer_result
            }
            response = JsonResponse(result)
            response.status_code = 201
        except Exception:
            response_data = {"error": "Division by zero!"}
            response = JsonResponse(response_data)
            response.status_code = 400
        return response
