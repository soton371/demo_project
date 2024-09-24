from django.http import JsonResponse # type: ignore
from django.views.decorators.csrf import csrf_exempt # type: ignore
from .models import *


# Create your views here.
@csrf_exempt
def recipes(request):
    print(f'request method: {request.method}')
    if request.method == 'POST':
        data = request.POST
        recipeName = data.get('recipe_name')
        recipeDescription = data.get('recipe_des')
        recipeImage = request.FILES.get('recipe_img')

        Recipe.objects.create(
            recipe_name = recipeName,
            recipe_des = recipeDescription,
            recipe_img = recipeImage,
        )

        print(f'recipeName: {recipeName}, recipeDescription: {recipeDescription}, recipeImage: {recipeImage}')
        return JsonResponse({'recipe_name': recipeName, 'recipe_des': recipeDescription, 'recipe_img': str(recipeImage)})