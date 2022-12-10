---
layout: page
title: A Quantum Computing ALU
permalink: /research/
nav_order: 2
---

# A Quantum Computing ALU

Here you can see our manuscript that we plan to submit to ACM. As the submission date has been extended to January, some minor changes may be made before then. This page will be updated as necessary to showcase the most current version.

{% for report in site.static_files %}

{% if report.path contains "A_Quantum_Computing_ALU.pdf" %}

<object data="{{site.url}}{{site.baseurl}}{{report.path}}" width="850" height="1100" type='application/pdf'/>
</object>

{% endif %}

{% endfor %}
