from django.core.management.base import BaseCommand
import sqlite3

class Command(BaseCommand):
    help = 'Check SQLite version'

    def handle(self, *args, **kwargs):
        print(f'SQLite version: {sqlite3.sqlite_version}')
