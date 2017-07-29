Cassiopeia Documentation
########################

What is Cassiopeia?
===================

Cassiopeia (which we fondly call Cass) is a framework for pulling and working with data from the `Riot API <https://developer.riotgames.com/>`_. Cass differentiates itself from other API wrappers by taking a page from one of Cassiopeia's quotes, "I'll take care of everything." Our main goal is to make your life (and ours) as developers *easy*.

Cass is composed of three key pieces:

1) An *interface* for pulling data from the Riot API.

2) A *type system* of classes for holding and working with the data pulled from Riot.

3) *Caches and databases* to temporarily and permanently store that data.

Together, these three pieces provide the user experience we desire. Scroll down for a quick example of how Cass works, what Cass does for you as a user, and information about contributing.


Why use Cass?
=============

* An excellent user interface (which makes working with data from the Riot API fun).

* Guaranteed optimal usage of your API key.

* Built in caching and (coming) the ability to easily link a database for offline storage of data.

* Extendability to non-Riot data. Because Cass is a framework and not just an API wrapper, you can integrate your own data sources into your project. We plan to include Data Dragon and the ``champion.gg`` API as additional sources of data in addition to the Riot API.

* ...


An Example
==========

We will quickly and efficiently look up the champion masteries for the summoner "Kalturi" (one of the developers) and print the champions he is best at. If you just want a quick look at how the interface looks, feel free to just read these three lines and skip the explanation. The explanation explains how the three bullet points above fit together and allow this code to be run.

.. code-block:: python

    kalturi = Summoner(name="Kalturi", id=21359666)
    good_with = kalturi.champion_masteries.filter(lambda cm: cm.level >= 6)
    print([cm.champion.name for cm in good_with])

    # At the time of writing this, this prints:
    ["Vel'Koz", 'Blitzcrank', 'Braum', 'Lulu', 'Sejuani']

The above three lines are relatively concise code, and if you know what lambdas and list comprehensions are then it will likely be readable. However, there is a deceptive amount of logic in these three lines, so let's break it down. (If you don't understand everything immediately, don't worry, that's why you're using Cass. You don't have to understand how everything works behinds the scenes, you just get to write good code.)

.. code-block:: python

    kalturi = Summoner(name="Kalturi", id=21359666)

First, we create a summoner with a ``name`` and ``id``. Note that creating ``kalturi`` doesn't trigger a call to the Riot API -- it merely instantiates a ``Summoner`` object with a name and id.

.. code-block:: python

    ... = kalturi.champion_masteries ...

Next we ask for the champion  masteries for ``kalturi`` by running ``kalturi.champion_masteries``. This creates an un-instantiated list which will contain champion masteries if any item in it is accessed.

.. code-block:: python

    good_with = kalturi.champion_masteries.filter(lambda cm: cm.level >= 6)

Third, the ``.filter`` method is called on the list of champion masteries. ``filter`` is a python built-in that operates on a list and filters the items in it based on some criteria. That criteria is defined py the ``lambda`` function we pass in.

A lambda is a quick way of defining functions in-line without using the ``def`` statement. In this case, ``lambda cm:`` takes in an object and assigns it to the variable ``cm``, then it returns ``cm.level > 6``. So this ``lambda`` will return ``True`` for any champion mastery whose mastery level is greater than or equal to ``6``.

The ``.filter(lambda cm: cm.level > 6)`` therefore operates on the list of champion masteries. When the list is iterated over, the champion masteries are queried. This requires a summoner id, which is pulled from ``kalturi.id``, and the Riot API is queried for Kalturi's champion masteries. With the champion mastery data pulled, ``.filter`` then filters the list looking for all champion masteries with mastery level 6 or higher.

.. code-block:: python

    print([cm.champion.name for cm in good_with])

Finally, the third line prints a list of the champion names for those champions.

Together these three lines illustrate the concise user interface that Cass provides, the way in which the data can be used, when the data is pulled (queried).


Contributing
============

Contributions are welcome! If you have idea or opinions on how things can be improved, don't hesitate to let us know by posting an issue on GitHub or @ing us on the Meraki or Riot API Discord channel. And we always want to hear from our users, even (especially) if it's just letting us know how you are using Cass.

As a user you get to ignore the details and just use the features of Cass. But as a developer you get to dive into the nitty-gritty and pick apart the implementation that makes everything work. If you don't want to dive too deep, you can likely contribute even without knowing all the details. You can read more about how Cass works :ref:`here <inner-workings>`.

If you have an idea but aren't sure about it, feel free to @ us on Discord and we can chat.


Overview
========

.. toctree::
    :maxdepth: 1

    setup
    inner_workings


Top Level APIs
==============

.. currentmodule:: cassiopeia

.. autosummary::
   :toctree: generated/

   Summoner

.. toctree::
    :maxdepth: 1

    cassiopeia/cassiopeia


Submodules used by APIs
=======================

Type System
^^^^^^^^^^^

.. toctree::
    :maxdepth: 1

    cassiopeia/core/index
    cassiopeia/dto/index


Index and Search
################

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`