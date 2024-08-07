"""django command to wait for the db to be available"""
import time
from psycopg2 import OperationalError as Psycopg2OpError

from django.db.utils import OperationalError #nqa
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        """Entrypoint for command"""
        self.stdout.write("waiting for database connection...")
        db_up = False
        while db_up is False:
            try:
                self.check(databases=['default'])
                db_ups = True
            except:
                self.stdout.write("Database unavailable, waiting for 1 second")
                time.sleep(1)

            self.stdout.write(self.style.SUCCESS('dATABASE AVAILABLE!'))
