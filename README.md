# Inventory-Management-Backend

This repository contain backend of the Inventory Management.

### Prerequisites

- Python (3.12.10)
- [UV](https://docs.astral.sh/uv/getting-started/installation/) (0.7.8)
- PostgreSQL (16.3)

### API Endpoints

Products
| Method | Endpoint              -| Description                        |
|--------|------------------------|------------------------------------|
| GET    | `products/`              | List all products                  |
| GET    | `products/<id>/`         | Retrieve a product by ID           |
| POST   | `products/create/`       | Create a new product               |
| PUT    | `products/<id>/update/`  | Update a product by ID             |

Locations
| Method | Endpoint                 | Description                        |
|--------|--------------------------|------------------------------------|
| GET    | `locations/`               | List all locations                 |
| GET    | `locations/<id>/`          | Retrieve a location by ID          |
| POST   | `locations/create/`        | Create a new location              |
| PUT    | `locations/<id>/update/`   | Update a location by ID            |

Product Movements
| Method | Endpoint                      | Description                        |
|--------|-------------------------------|------------------------------------|
| GET    | `product-movements/`            | List all product movements         |
| GET    | `product-movements/<id>/`       | Retrieve a product movement by ID  |
| POST   | `product-movements/create/`     | Create a new product movement      |
| PUT    | `product-movements/<id>/update` | Update a product movement by ID    |

Reports
| Method | Endpoint                           | Description                        |
|--------|------------------------------------|------------------------------------|
| GET    | `reports/product-balance`          | List product balance report        |

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
