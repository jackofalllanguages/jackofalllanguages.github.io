---
layout: single
title: Categories
permalink: categories/
---

{% include group-by-array.html collection=site.posts field='categories' %}

<ul>
  {% for tag in group_names %}
    {% assign posts = group_items[forloop.index0] %}

    <li>
      <h2>{{ tag }}</h2>
      <ul>
        {% for post in posts %}
        <li>
          <a href='{{ site.baseurl }}{{ post.url }}'>{{ post.title }}</a><p>{{ post.excerpt }}</p>
        </li>
        {% endfor %}
      </ul>
    </li>
  {% endfor %}
</ul>