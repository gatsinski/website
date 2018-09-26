from django.contrib.sites.shortcuts import get_current_site


def website(request):
    site = get_current_site(request)
    return {'site_name': site.name}
