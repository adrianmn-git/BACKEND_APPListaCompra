# Shopping List Backend

Backend API for a shopping list application built with:

- Django
- Django Rest Framework

## Setup

```bash
git clone https://github.com/usuario/shopping-list-backend.git
cd shopping-list-backend

python -m venv venv
source venv/bin/activate

pip install -r requirements.txt
python manage.py migrate
python manage.py runserver