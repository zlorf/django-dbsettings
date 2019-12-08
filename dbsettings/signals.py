from django.dispatch import Signal

__all__ = ['setting_changed']

setting_changed = Signal()
