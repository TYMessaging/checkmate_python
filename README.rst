checkmate_python
===================

CheckMate
-----------

A Python wrapper for the CheckMate REST API

Installation
----------------

Install:

    pip install checkmate

or

    easy_install checkmate

Usage
------------

.. code-block:: python

    import checkmate
    client = checkmate.CheckMate(api_key='YOUR_KEY_HERE')

**Note:**: You can also pass in a different API url if needed using the *api_base* keyword argument.

.. code-block:: python

    client = checkmate.CheckMate(api_key='YOUR_KEY_HERE', api_base='API_URL_HERE')

Refer to the [documentation] (https://partners.checkmate.io/docs) for the final word on what's required/optional for each call.

Search for a property
~~~~~~~~~~~~~~~~~~~~~~

You can query the API for a property. All of the fields referenced in the query are required.

.. code-block:: python

    client.properties.search({
        'name': 'Hotel Kabuki',
        'phone': '14159223200',
        'address': {
            'street': '1625 Post St',
            'city': 'San Francisco',
            'region': 'CA',
            'postal_code': '94115',
            'country_code': 'US'
        }
    })

List reservations
~~~~~~~~~~~~~~~~~~~~~~

You can query the API for all your reservations or the reservations for a specific property.

.. code-block:: python

    # paginated list of all reservations
    client.reservations.list()

    # fetching a different page of reservations
    client.reservations.list({'page': 2})

    # reservations with a specific confirmation number
    client.reservations.list({'confirmation_num': '12349asdf'})

    # reservations for property with id 13434543
    client.reservations.list({'property_id': 13434543})

    # exclude property data from the response
    client.reservations.list({'exclude_properties': 'true'})

Show reservation
~~~~~~~~~~~~~~~~~~~~~~

You can request a specific reservation from the Checkmate API.

.. code-block:: python

    # reservation with id 123452  
    client.reservations.show(123452)

Create reservation
~~~~~~~~~~~~~~~~~~~~~~

You can create a reservation in Checkmate using either an existing property id, or by creating a new property within the request.

.. code-block:: python

    # reservation under property 93
    client.reservations.create({
        'external_id': 'someid123',
        'confirmation_number': 'sdlfkjweo324',
        'first_name': 'Jane',
        'last_name': 'Smith',
        'email': 'jane@smith.io',
        'start_on': '2016-12-20',
        'end_on': '2016-12-24',
        'property_id': 93
    })

    # creating a new property
    client.reservations.create({
        'external_id': 'someid123',
        'confirmation_number': 'sdlfkjweo324',
        'first_name': 'Jane',
        'last_name': 'Smith',
        'email': 'jane@smith.io',
        'start_on': '2016-12-20',
        'end_on': '2016-12-24',
        'property': {
            'name': 'New Hotel',
            'address': {
                'street': '123 Leaf Lane',
                'city': 'Brooklyn',
                'region': 'NY',
                'postal_code': '11201',
                'country_code': 'US'
            }
        }
    })

Update reservation
~~~~~~~~~~~~~~~~~~~~~~

You can update an existing reservation in Checkmate using a reservation_id.

.. code-block:: python

    # reservation id 12345
    client.reservations.update(12345, {'loyalty_number': 'abs2332'})

Delete reservation
~~~~~~~~~~~~~~~~~~~~~~

You can delete an existing reservation in Checkmate using a reservation_id.

.. code-block:: python

    # reservation id 12345
    client.reservations.destroy(12345)

Bulk create reservations
~~~~~~~~~~~~~~~~~~~~~~~~~~

Each reservation follows the same format as a single reservation (an optional webhook can be added at the end).

.. code-block:: python

    client.reservations.bulk_create([{
        'external_id': 'fdoo',
        'confirmation_number': '',
        'first_name': 'Frank',
        'last_name': 'Smith',
        'email': 'frank@example.com',
        'start_on': '2015-12-20',
        'end_on': '2015-12-24',
        'property_id': 123
    }, {
        'external_id': 'hfg34',
        'confirmation_number': 'gjhhffgh456',
        'first_name': 'John',
        'last_name': 'Doe',
        'email': 'johndoe@example.com',
        'start_on': '2015-11-20',
        'end_on': '2015-11-24',
        'property_id': 123
    }], 'https://example.com/callback')

Testing
--------

Install [nose testing framework](https://nose.readthedocs.org/en/latest/):

    pip install nose

Install the [mock](http://www.voidspace.org.uk/python/mock/) mocking and testing library:

    pip install mock

You can run tests by running the following command:

    nosetests

Linting
--------

Install [flake8](https://pypi.python.org/pypi/flake8):

    pip install flake8

You can run the linter by running

    flake8 checkmate

in the root directory.

