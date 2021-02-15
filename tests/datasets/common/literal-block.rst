Basic literal block:

::

    # Some code block
    for a in [5,4,3,2,1]:   # this is program code, shown as-is
        print(a)
    print("it's...")

Partial minimized form: ::

    Literal block

Fully minimized form::

    Literal block

Some Python Code:

.. code-block:: python

   def foo():
       bar()

Some C++ code:

.. code-block:: c++

   class Foo {
       int i;
   };

Note that code-block is a directive specific to Sphinx. The docutils (native)
directive is code. It should return the same doctree.

.. code:: python

   def foo():
       bar()

Test support for line numbers:

.. code-block:: python
   :linenos:

   def foo():
       bar()

.. code:: python
   :number-lines:

   def foo():
       bar()
