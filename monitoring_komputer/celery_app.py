# monitoring_komputer/celery.py
import os
from monitoring_komputer.celery_app import Celery

# Mengatur default modul pengaturan Django untuk program 'celery'.
# Ini harus selalu sebelum Anda membuat instance Celery().
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'monitoring_komputer.settings')

# Membuat instance aplikasi Celery
app = Celery('monitoring_komputer')

# Memuat konfigurasi Celery dari pengaturan Django.
# Namespace 'CELERY' berarti semua pengaturan Celery harus diawali dengan 'CELERY_'
# di file settings.py Anda (misalnya, CELERY_BROKER_URL).
app.config_from_object('django.conf:settings', namespace='CELERY')

# Menemukan tugas secara otomatis dari semua aplikasi Django terdaftar.
# Ini akan mencari file tasks.py di setiap aplikasi yang ada di INSTALLED_APPS.
app.autodiscover_tasks()

@app.task(bind=True, ignore_result=True)
def debug_task(self):
    print(f'Request: {self.request!r}')