import os
import shutil


project_slug = "{{cookiecutter.project_slug}}"

def delete_resource(resource):
    if os.path.isfile(resource):
        print(f"removing file: {resource}")
        os.remove(resource)
    elif os.path.isdir(resource):
        print(f"removing directory: {resource}")
        shutil.rmtree(resource)

use_elastic = "{{cookiecutter.use_elastic}}"
use_celery = "{{cookiecutter.use_celery}}"
use_simple_history = "{{cookiecutter.use_simple_history_package}}"
use_kavenegar = "{{cookiecutter.use_kavenegar}}"

if use_elastic == 'n':
    delete_resource('elk-config-stg')
if use_celery == 'n':
    delete_resource(f"{project_slug}/celery")
if use_kavenegar == 'n':
    delete_resource(f"core/sms")

