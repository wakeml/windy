# Windy -- a Reddit Django evaluation

## The prompt
The test is simple:
You have wind speed measuring devices across the globe, called anemometers.
The test is to make a django backend with these features:

* CRUD anemometers
* Submit a wind reading at any time for any anemometer
* Ability to give tags to anemometers, and filter _the readings_ using them.

The anemometers list endpoint should be _paginated_ and feature the _5 last readings and statistics_: 
daily readings, speed average, and weekly average.

Bonus:
* Write tests
* Add an endpoint to would give you statistics (avg) on anemometers reading within a certain radius (like 5 miles around a given coordinate)

>It is not that hard, but man I've reviewed like 20 of those tests in the past 6 months, many candidates with +6 years did really poorly to this test. I think over the tests, I've only seen like 4 tests that were close to "perfect" in terms of best practices, performances, and simply implementation... And we're looking for senior profiles!


## The approach

We're using Django, Django-ninja, taggit, and postgis running in docker.  The routes are in `windspeed/api/routes`.

## Models


## Routes















