from .models import SiteSetting

def site_settings(request):
    try:
        settings = SiteSetting.objects.first()  # 最初のレコードを取得
    except SiteSetting.DoesNotExist:
        settings = None
    return {'site_setting': settings}
