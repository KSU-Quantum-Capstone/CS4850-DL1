---
layout: page
title: A Quantum Computing ALU
permalink: /research/
nav_order: 2
---

# A Quantum Computing ALU
Our paper cam be viewed at: [https://doi.org/10.1145/3564746.3587005](https://doi.org/10.1145/3564746.3587005)

or here on this page:

{% for report in site.static_files %}

{% if report.path contains "A_Quantum_Computing_ALU.pdf" %}

<object data="{{site.url}}{{site.baseurl}}{{report.path}}" width="850" height="1100" type='application/pdf'/>
</object>

{% endif %}

{% endfor %}

