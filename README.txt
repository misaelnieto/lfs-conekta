What is this?
=============

This the payment processor for `LFS (Lightning Fast Shop) <http://www.getlfs.com/>`_
that adds support for `Conekta <https://www.conekta.io>`_ a Mexican Payment Gateway.

Installation
============

Install eggg
------------

If you use pip:

.. code:: bash

    pip install lfs-conecta


If you use the buildout installer for LFS 0.7.x add ``lfs-conecta`` to your list
of eggs and re-run buildout.

.. code:: ini

    [django]
    recipe = djangorecipe
    eggs =
        [...]
        lfs-conekta


Install to django
-----------------

Add ``lfs-conekta`` to your list of ``INSTALLED_APPS`` in ``settings.py`` and
run ``syncdb``.

.. code:: python

INSTALLED_APPS = (
    'django.contrib.contenttypes',  # contenttypes framework is required

    # ...

    'django-settings',
    'lfs_conekta'

    # ...
)



With plain django:

.. code:: bash

    python manage.py syncdb

With Buildout

.. code:: bash

    bin/django syncdb


Integration with the management interface
-----------------------------------------

LFS Conekta can be configured with the management interface, but needs some
integration steps from you.

* Add ``lfs-conekta`` to management panel to **Shop -> Settings** page as new tab:
  copy lfs/templates/manage/shop/shop.html to your theme and modify it by adding:
  {% load lfs_conekta_tags %}
  ( ... )
  <div id="manage-tabs">
    <ul>
        <li class="ui-tabs-nav-item"><a href="#data">{% trans 'Shop' %}</a></li>
        <li class="ui-tabs-nav-item"><a href="#default-values">{% trans 'Default Values' %}</a></li>
        <li class="ui-tabs-nav-item"><a href="#portlets">{% trans 'Portlets' %}</a></li>
        **<li class="ui-tabs-nav-item"><a href="#carousel-items">{% trans 'Conekta' %}</a></li>**
    </ul>
  (...)
  <div id="portlets">
    {{ portlets|safe }}
  </div>
  **{% conekta_management shop %}**



