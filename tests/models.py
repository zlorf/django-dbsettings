from django.db import models

import dbsettings
import datetime


class TestSettings(dbsettings.Group):
    boolean = dbsettings.BooleanValue()
    integer = dbsettings.IntegerValue()
    string = dbsettings.StringValue()
    list_semi_colon = dbsettings.MultiSeparatorValue()
    list_comma = dbsettings.MultiSeparatorValue(separator=',')
    date = dbsettings.DateValue()
    time = dbsettings.TimeValue()
    datetime = dbsettings.DateTimeValue()
    string_choices = dbsettings.StringValue(choices=(("String1", "First String Choice"), ("String2", "Second String Choice")))
    no_caching_string = dbsettings.StringValue(disable_cache=True)

class Defaults(models.Model):
    class settings(dbsettings.Group):
        boolean = dbsettings.BooleanValue(default=True)
        boolean_false = dbsettings.BooleanValue(default=False)
        integer = dbsettings.IntegerValue(default=1)
        string = dbsettings.StringValue(default="default")
        list_semi_colon = dbsettings.MultiSeparatorValue(default=['one', 'two'])
        list_comma = dbsettings.MultiSeparatorValue(separator=',', default=('one', 'two'))
        date = dbsettings.DateValue(default=datetime.date(2012, 3, 14))
        time = dbsettings.TimeValue(default=datetime.time(12, 3, 14))
        datetime = dbsettings.DateTimeValue(default=datetime.datetime(2012, 3, 14, 12, 3, 14))
        string_choices = dbsettings.StringValue(choices=(("String1", "First String Choice"), ("String2", "Second String Choice")), default="String2")
    settings = settings()


class TestBaseModel(models.Model):
    class Meta:
        abstract = True
        app_label = 'tests'


# These will be populated by the fixture data
class Populated(TestBaseModel):
    settings = TestSettings()


# These will be empty after startup
class Unpopulated(TestBaseModel):
    settings = TestSettings()


# These will allow blank values
class Blankable(TestBaseModel):
    settings = TestSettings()


class Editable(TestBaseModel):
    settings = TestSettings('Verbose name')


class Combined(TestBaseModel):
    class settings(dbsettings.Group):
        enabled = dbsettings.BooleanValue()
    settings = TestSettings() + settings()


# For registration testing
class ClashSettings1(dbsettings.Group):
    clash1 = dbsettings.BooleanValue()


class ClashSettings2(dbsettings.Group):
    clash2 = dbsettings.BooleanValue()


class ClashSettings1_2(dbsettings.Group):
    clash1 = dbsettings.IntegerValue()
    clash2 = dbsettings.IntegerValue()


class ModelClash(TestBaseModel):
    settings = ClashSettings1_2()


class NonRequiredSettings(dbsettings.Group):
    integer = dbsettings.IntegerValue(required=False)
    string = dbsettings.StringValue(required=False)
    fl = dbsettings.FloatValue(required=False)
    decimal = dbsettings.DecimalValue(required=False)
    percent = dbsettings.PercentValue(required=False)


class NonReq(TestBaseModel):
    non_req = NonRequiredSettings()
