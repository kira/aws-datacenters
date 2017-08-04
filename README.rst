AWS Regional Data Centers mapping
=================================


How to run this:
1. Make a virtualenv
1. `pip install -r requirements.txt`
1. Run `./manage.py runserver`
1. Go to `127.0.0.1:8000`

How to update this:
1. Update the `input/*` files
2. Run `python generate.py`

This project is used to generate the indexes (and `visual map`_ for
reference) used by the `TurnKey Hub`_ to find the closest AWS data
center for a user.

.. _visual map: http://turnkeylinux.github.io/aws-datacenters
.. _TurnKey Hub: https://hub.turnkeylinux.org/

References:

`Finding the closest data center using GeoIP and indexing <http://www.turnkeylinux.org/blog/geoip-amazon-regions>`_

`Finding the closest APT package archive using GeoIP and indexing <http://www.turnkeylinux.org/blog/auto-apt-archive>`_

