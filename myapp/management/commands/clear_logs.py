import os
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Log dosyalarını temizler.'

    def add_arguments(self, parser):
        parser.add_argument(
            'logfile',
            type=str,
            help='The path of logs file'
        )

    def handle(self, *args, **options):
        logfile = options['logfile']

        if os.path.exists(logfile):
            try:
                with open(logfile, 'w'):
                    pass
                self.stdout.write(self.style.SUCCESS(f'{logfile} cleared succesfully.'))
            except Exception as e:
                self.stdout.write(self.style.ERROR(f'Hata: {str(e)}'))
        else:
            self.stdout.write(self.style.ERROR(f'{logfile} could not be found.'))

# python3 manage.py clear_logs django_logs.txt