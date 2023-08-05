{{ fullname | escape | underline }}

.. .. currentmodule:: {{ fullname }}

.. automodule:: {{ fullname }}

    {% block attributes %}
    {% if attributes %}
    .. rubric:: {{ _('Module Attributes') }}

    .. autosummary::
    {% for item in attributes %}
        {{ item }}
    {%- endfor %}
    {% endif %}
    {% endblock %}

    {% block function %}
    {% if functions %}
    .. rubric:: {{ _('Functions') }}

    .. autosummary::
    {% for item in functions %}
        {{ item }}
    {%- endfor %}
    {% endif %}
    {% endblock %}

    {% block classes %}
    {% if classes %}
    .. rubric:: {{ _('Classes') }}

    .. autosummary::
    {% for item in classes %}
        {{ item }}
        {{ item }}
    {%- endfor %}
    {% endif %}
    {% endblock %}

    {% block exceptions %}
    {% if exceptions %}
    .. rubric:: {{ _('Exceptions') }}

    .. autosummary::
    {% for item in exceptions %}
        {{ item }}
    {%- endfor %}
    {% endif %}
    {% endblock %}

{% block modules %}
{% if modules %}
.. rubric:: {{ _('Modules') }}

.. autosummary::
    :template:
    :recursive:
    :toctree:
{% for item in modules %}
    {{ item }}
{%- endfor %}
{% endif %}
{% endblock %}
