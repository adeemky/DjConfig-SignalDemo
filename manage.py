#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'newpro.settings')
    os.environ.setdefault("DJANGO_CONFIGURATION", "Dev") # EKLENDI / Dev class'i manage.py'a ekleriz. Boylece server'i baslattigimiz da ayarlarimiz Dev class'i calistirir
    try:
        from configurations.management import execute_from_command_line # GUNCELLENDI / Bu, standart Django yönetim komutlarının yerine, django-configurations kullanarak yapılandırma sınıflarını dikkate alarak komutları yürütmemizi sağlar.
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
