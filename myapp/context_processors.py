from myapp.models import settings

def sett(request):
   ss = settings.objects.filter().first
   return {'ss':ss}