from django.shortcuts import render
import requests
from django.http import JsonResponse

def pokemon_list(request):
	url = 'https://pokeapi.co/api/v2/pokemon'
	next_view = request.GET.get('next')
	prev_view = request.GET.get('prev')
	if next_view:
		response = requests.get(next_view).json()
	elif prev_view:
		response = requests.get(prev_view).json()
	else:
		response = requests.get(url).json()
	context = {
		'responses' : response['results'],
		'next' : response['next'],
		'prev' : response['previous']
	}
	# return JsonResponse(response)
	return render(request,"list.html",context)

def detail(request):
	url = request.GET.get('detail')
	response = requests.get(url).json()
	context = {
		'results' : response,
	}
	return render(request,'detail.html', context)


