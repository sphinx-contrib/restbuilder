.. _target:

The hyperlink target above points to this paragraph. Internal
hyperlink targets may be chained. Multiple adjacent internal hyperlink
targets all point to the same element:

.. _target1:
.. _target2:

The targets `target1`_ and `target2`_ are synonyms; they both point to
this paragraph.

.. _one: three_
.. _two: three_
.. _three:

Indirect hyperlink targets have a hyperlink reference in their link
blocks. In the following example, target `one <three_>`_ indirectly
references whatever target `two <three_>`_ references, and target two
references target `three`_, an internal hyperlink target. In effect,
all three reference the same thing.
