# Inventory-Management-Backend

This repository contain backend of the Inventory Management.

### Prerequisites

- Python (3.12.10)
- [UV](https://docs.astral.sh/uv/getting-started/installation/) (0.7.8)
- PostgreSQL (16.3)

### Getting Started

1. Clone The Repository.

```commandline
git clone https://github.com/iamj33l/Inventory-Management-Backend.git
cd Inventory-Management-Backend
```

2. Install Dependency with uv and activate virtual enviroment.

```commandline
uv sync
```
This will create virtual environment and install the dependencies.

```commandline
.venv/Scripts/activate
```

3. Create database in Postgres 


4. Create .env file in root directory and create environmental variables, use .env.example for reference.


5. Generate new secret key for Django with following command and add it into environmental variable.

```commandline
python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
```

6. Apply migrations.

```commandline
python manage.py migrate
```

7. Run the server

```commandline
python manage.py runserver
```
