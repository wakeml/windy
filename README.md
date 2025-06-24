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

Yes, the postgis login information / secrets are in the settings module, but for educational purposes that's fine for now.  If someone can access a locally running docker container on my personal machine, I have other problems.  In a production environment you would use env-vars.

## Models

We have a single model, Measurements, that stores all of the required windspeed data.  We have a StatsManager that acts as a table level method, to get well, stats on the data.  We added a constraint on the wind direction to limit it to compass degrees, and finally we have used django taggit for "Tags".


## Routes
--windspeed/api/routes.py
--windspeed/api/schema.py

There are seven routes, the traditional CRUD routes, plus a "get all" route.  

The last two are `get_all_close_by_location` and `filter_all_measurements_by_tag`, which as you can image do what the title implies.

## Gotcha's

The django-ninja library does not natively support GEO-DJANGO Point fields.  As such the various schemas don't actually return the lat/lon.  After working on it for a bit, I decided to pause working on that functionality, as this is just an exercise.  In reality there are several approaches to fixing this issue.

First we could investigate further how other people have handled this problem.  There's a few comments on Stack Overflow and Github about it, but nothing that was easily (and quickly) implementable.

The next option is to _store_ points in the database, but to _display_ and _transmit_ lat/lon pairs as numbers in the APIs.  This would be my recommendation moving forward.














