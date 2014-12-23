checkmate_python
===================

# CheckMate

A Python wrapper for the CheckMate REST API

## Installation

***TODO***

## Usage

```python
import checkmate
client = checkmate.CheckMate(api_key='YOUR_KEY_HERE')
```

**Note:**: You can also pass in a different API url if needed using the *api_base* keyword argument.

```python
client = checkmate.CheckMate(api_key='YOUR_KEY_HERE', api_base='API_URL_HERE')
```

Refer to the [documentation] (https://partners.checkmate.io/docs) for the final word on what's required/optional for each call.

### Fetch a property

You can query the API for a property. All of the fields referenced in the query are required.

***TODO***

### List reservations

You can query the API for all your reservations or the reservations for a specific property.

```python
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
```

### Show reservation

You can request a specific reservation from the Checkmate API.

```python
# reservation with id 123452  
client.reservations.show(123452)
```

### Create reservation

You can create a reservation in Checkmate using either an existing property id, or by creating a new property within the request.

```python
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
```

### Update reservation

You can update an existing reservation in Checkmate using a reservation_id.

```python
# reservation id 12345
client.reservations.update(12345, {'loyalty_number': 'abs2332'})
```

### Delete reservation

You can delete an existing reservation in Checkmate using a reservation_id.

```python
# reservation id 12345
client.reservations.destroy(12345)
```

### Bulk create reservations

***TODO***
