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
    
    # for get recipes
    if request.method == 'GET':
        queryset = Recipe.objects.all()
        recipeList = []            
        for recipe in queryset:
            print(f'recipeName: {recipe.recipe_name}, recipeDescription: {recipe.recipe_des}, recipeImage: {recipe.recipe_img}')
            recipeList.append({
                'id': recipe.id,
                'recipe_name': recipe.recipe_name, 'recipe_des': recipe.recipe_des, 'recipe_img': str(recipe.recipe_img)})

        return JsonResponse({"data": recipeList}, status=200)


@csrf_exempt
def delete_recipe(request, id):
    print(f'id: {id}')
    if request.method == "DELETE":
        queryset = Recipe.objects.get(id = id)
        queryset.delete()
        return JsonResponse({'message': 'Delete recipe '+str(id)}, status=200)
    
@csrf_exempt
def update_recipe(request, id):
    if request.method == "POST":
        queryset = Recipe.objects.get(id = id)
        data = request.POST
        recipeName = data.get('recipe_name')
        recipeDescription = data.get('recipe_des')
        recipeImage = request.FILES.get('recipe_img')

        queryset.recipe_name = recipeName
        queryset.recipe_des = recipeDescription

        if recipeImage:
            queryset.recipe_img = recipeImage

        queryset.save()
        return JsonResponse({'message': 'Update recipe '+str(id)}, status=200)