# #!/usr/bin/env python
# """Django's command-line utility for administrative tasks."""
# import os
# import sys
#
#
# def main():
#     """Run administrative tasks."""
#     os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pasarpolis_stackoverflow.settings')
#     try:
#         from django.core.management import execute_from_command_line
#     except ImportError as exc:
#         raise ImportError(
#             "Couldn't import Django. Are you sure it's installed and "
#             "available on your PYTHONPATH environment variable? Did you "
#             "forget to activate a virtual environment?"
#         ) from exc
#     execute_from_command_line(sys.argv)
#
#
# if __name__ == '__main__':
#     main()
import os
from random import randint
for i in range(300, 400):
    for j in range(1, randint(0, 3)):
        d = str(i)+"days ago"
        with open("file.txt", 'a') as f:
            f.write(d)
        os.system('git add .')
        os.system('git commit --date="' + d + '" -m "commit"')
os.system('git push origin master')