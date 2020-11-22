# Misson to Mars
> Web-scraping challenge.

## Table of contents
* [General info](#general-info)
* [Screenshots](#screenshots)
* [Technologies](#technologies)
* [Features](#features)
* [Status](#status)
* [Inspiration](#inspiration)
* [Contact](#contact)

## General info
Add more general information about project. What the purpose of the project is? Motivation?

## Screenshots
![Full Website](https://github.com/Jen-Dean/web-scraping-challenge/blob/main/Mission_to_Mars.png)

## Technologies
* Python
* Pymongo
* Flask
* MongoDB
* HTML
* CSS
* Bootstrap
* Pandas
* Splinter
* Beautiful Soup

## Code Examples
Example For Loop:
`{% for dict in mars_data.hemi_scrape %}
  <div class="col-lg-6">
     <div class="card">
        <div class="card-body">
          <h4 class="card-title">{{ dict.title }}</h4>
          <img src='{{ dict.image_url }}' class="img-fluid" alt={{ dict.title }}>
        </div>
     </div>
  </div>
{% endfor %}`

## Features

* Pulls the latest Headline from the NASA website about Mars.
* Pulls the latest feature image from NASA (updates often)
* Pulls the most up-to-date statistics about Mars
* Pulls the latest hemisphere images about Mars


## Status
Project is:  _finished_

## Inspiration
Rutegers Data Science Course

## Contact
Created by [@JenniferDean](https://github.com/Jen-Dean)
