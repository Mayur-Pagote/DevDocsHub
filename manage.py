#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

def main():
    """Run administrative tasks."""
    # Set the default settings module for the Django application
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DevDocsHub.settings')
    
    try:
        # Import the execute_from_command_line function from Django's management module
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        # Raise an ImportError with a helpful message if Django is not installed
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    # Execute the command-line utility with the provided arguments
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    # Call the main function when the script is executed directly
    main()
