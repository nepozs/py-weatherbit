# Python Wrapper for the Weatherbit API
This module communicates with the [Weatherbit API](https://www.weatherbit.io/api) and can retrieve data for:

* Current Conditions
* Forecast Data - Daily and Hourly data. *Note*: Hourly data requires paid plan
* Severe Weather Alerts

It will require an API Key to work, which can be retrieved for free at [Weatherbit](https://www.weatherbit.io/account/create)

See `test_client.py` for examples on how to use this wrapper. And before doing so, create a file in the same directory as `test_client.py` called `secrets.json` and copy the below to that file:

````
{
    "connection": {
        "api_key": "YOURAPIKEY"
    }
}
````
Change YOURAPIKEY to the Api Key you have from Weatherbit.io
