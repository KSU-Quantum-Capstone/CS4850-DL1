---
layout: page
title: Project Report
permalink: /report/
nav_order: 3
---

# CS4850 Report

For our class, we were tasked to create a report which details our development process. This can be viewed below.

{% for report in site.static_files %}

{% if report.path contains "A_Quantum_Computing_ALU.pdf" %}

<object data="{{site.url}}{{site.baseurl}}{{report.path}}" width="850" height="1100" type='application/pdf'/>
</object>

{% endif %}

{% endfor %}
