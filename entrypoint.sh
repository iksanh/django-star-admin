#!/bin/sh
set -e

# 1. Collect Static (Pindahan dari build.sh)
# Kita taruh di sini agar bisa akses AWS Secrets saat container jalan
echo "Mengumpulkan file statis..."
python manage.py collectstatic --no-input

# 2. Migrate Database (Pindahan dari build.sh)
echo "Melakukan migrasi database..."
python manage.py migrate

# 3. Jalankan Aplikasi
echo "Menjalankan Gunicorn..."
exec "$@"