Usage
=====

Running the Application
-----------------------

Start the development server:

.. code-block:: bash

   uvicorn main:app --reload

The application will be available at http://127.0.0.1:8000

Endpoints
---------

* **Home page**: http://127.0.0.1:8000/ - HTML table view
* **API endpoint**: http://127.0.0.1:8000/organisations - JSON response
* **Swagger UI**: http://127.0.0.1:8000/docs
* **ReDoc**: http://127.0.0.1:8000/redoc

Testing
-------

Install test dependencies and run tests:

.. code-block:: bash

   pip install pytest httpx
   pytest -v
