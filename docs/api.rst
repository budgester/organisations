API Reference
=============

Endpoints
---------

GET /organisations
~~~~~~~~~~~~~~~~~~

Returns a JSON list of all organisations.

**Response**

.. code-block:: json

   [
     {
       "id": 1,
       "name": "Acme Corp",
       "description": "A technology company"
     },
     {
       "id": 2,
       "name": "Global Industries",
       "description": "Manufacturing and logistics"
     },
     {
       "id": 3,
       "name": "Tech Solutions",
       "description": "Software development services"
     }
   ]

**Response Fields**

* ``id`` (integer): Unique identifier
* ``name`` (string): Organisation name
* ``description`` (string, optional): Organisation description

GET /
~~~~~

Returns an HTML page with a table of all organisations.

Interactive Documentation
-------------------------

* **Swagger UI**: ``/docs``
* **ReDoc**: ``/redoc``
* **OpenAPI JSON**: ``/openapi.json``
