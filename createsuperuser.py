import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "modular_entity_mapping_system.settings")
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

username = os.getenv("DJANGO_SUPERUSER_USERNAME")
email = os.getenv("DJANGO_SUPERUSER_EMAIL")
password = os.getenv("DJANGO_SUPERUSER_PASSWORD")

if username and password:
    if not User.objects.filter(username=username).exists():
        User.objects.create_superuser(
            username=username,
            email=email or "",
            password=password
        )
        print(f"Superuser '{username}' created successfully!")
    else:
        print(f"Superuser '{username}' already exists. Skipping creation.")
else:
    print("Superuser environment variables not set.")