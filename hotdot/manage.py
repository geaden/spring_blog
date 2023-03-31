#!/usr/bin/env python
import sys


if __name__ == "__main__":
    from django.core.management import execute_from_command_line
    from django.core.management.commands.runserver import Command as runserver
    runserver.default_addr = '0.0.0.0'
    execute_from_command_line(sys.argv)
