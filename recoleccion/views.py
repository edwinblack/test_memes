import requests
from django.views.generic.base import TemplateView
from django.shortcuts import render
       


class HomePageView(TemplateView):
    
    template_name = "recoleccion/home.html"
    def get(self, request):
      
        memes = {}          
        for intentos in range(15):
            response = requests.get('https://api.chucknorris.io/jokes/random')
            returned_data = response.json()
            
            if returned_data['id'] not in memes:
                memes[returned_data['id']] = returned_data
            
        return render(request, self.template_name, {'memes': memes})    
    
# import asyncio
# from django.shortcuts import render

# import httpx
# from django.http import HttpResponse, request

# memes = {}
# # helpers

# async def http_call_async():
#     async with httpx.AsyncClient() as client:
#         reques = await client.get("https://api.chucknorris.io/jokes/random")
#         reques = reques.json()
#         if reques['id'] not in memes:
#             memes[reques['id']] = reques

#     return memes

# # views

# async def async_view(request):
    
#     await http_call_async()
#     return render(request, "recoleccion/home.html", {'memes': memes})
#     return HttpResponse("Non-blocking HTTP request")
