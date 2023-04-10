---
layout: page
title: A Quantum Computing ALU
permalink: /research/
nav_order: 2
---

# A Quantum Computing ALU

Feel free to take at our paper on ACM: [https://doi.org/10.1145/3564746.3587005](DOI)

Or view it here:
{% for report in site.static_files %}

{% if report.path contains "A_Quantum_Computing_ALU.pdf" %}

<object data="{{site.url}}{{site.baseurl}}{{report.path}}" width="850" height="1100" type='application/pdf'/>
</object>

{% endif %}

{% endfor %}
