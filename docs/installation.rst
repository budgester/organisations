Installation
============

Requirements
------------

* Python 3.12+
* pip

Local Installation
------------------

Clone the repository:

.. code-block:: bash

   git clone https://github.com/budgester/organisations.git
   cd organisations

Create a virtual environment and install dependencies:

.. code-block:: bash

   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt

Docker
------

Build and run with Docker:

.. code-block:: bash

   docker build -t organisations .
   docker run -p 8000:8000 organisations

Kubernetes
----------

Deploy with Helm:

.. code-block:: bash

   helm install organisations ./helm/organisations
