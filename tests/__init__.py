class GlobalSettings(dbsettings.Group):
    gs_boolean = dbsettings.BooleanValue(default=True)
    gs_string = dbsettings.StringValue(default="default")

    site_settings = GlobalSettings()

    from django.contrib.sites.models import Site
    from django.conf import settings
    Site(id=settings.SITE_ID, domain="example.com", name="example.com").save()
    Site(id=settings.SITE_ID + 1, domain="example2.com", name="example2.com").save()

    other_site_settings = GlobalSettings()
    import pdb; pdb.set_trace()
    other_site_settings.site_id = settings.SITE_ID + 1
    other_site_settings.save()

    # less standard
    loading.set_setting_value('dbsettings.tests', '' )
