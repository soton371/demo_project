from django.http import JsonResponse # type: ignore

# Create your views here.
def home(request):
    return JsonResponse({"name":"Start django server"})