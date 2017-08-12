---
layout: page
title: Projects
excerpt: "An archive of projects sorted by date."
search_omit: true
---

<ul class="post-list">
{% for post in site.categories.project %} 
  <li><article><a href="{{ site.url }}{{ post.url }}">{{ post.title }} <span class="entry-date"><time datetime="{{ post.date | date_to_xmlschema }}">{{ post.date | date: "%B %d, %Y" }}</time></span>{% if post.excerpt %} <span class="excerpt">{{ post.excerpt | remove: '\[ ... \]' | remove: '\( ... \)' | markdownify | strip_html | strip_newlines | escape_once }}</span>{% endif %}</a></article></li>
  
  {% if post.image.teaser %}
    <a href="{{ site.github.url }}{{ post.url }}"><img src="{{ site.github.url }}/images/{{ post.image.teaser }}"></a>
  {% endif %}

{% endfor %}
</ul>
