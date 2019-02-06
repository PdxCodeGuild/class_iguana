---
title: Development and migration in maps and figures
subtitle: A proposal for a pdxCodeGuild full-stack developer bootcamp capstone project
author: Richard Sherman
date: 2019-02-05
---

# Development and migration in maps and figures
The purpose of this project is to deliver selected data related to economic/political development and human migration in cartographic and statistical form. 

This is a static site. Much of the programming work takes place "before the back-end", in downloading and processing data, performing statistical analyses, and generating choropleth maps to display data. The main effort is to automate the data-acquisition and -analysis steps. 

All of this program execution could be done in response to user requests, but the time required to download, process and display data (seconds to minutes) would render the website an interesting exercise but undesirable from the user's perspective.

The main UI elements are pages with links and drop-down menus allowing users to select maps, graphs and statistical results representing data and analysis. Textual information will be provided to assist with navigation and interpretation.

## Libraries and frameworks
Data processing and analysis is done using `pandas` and `statsmodels`. Maps are drawn using `plotly` and `geopandas` with `matplotlib`. `rpy2` is used to call `R` from within `python`, for some graphical features that are not available in `matplotlib` and associated libraries. I may choose to use `pweave` to render text and data analysis in HTML via `pandoc`, for re-use in `pandoc2latex`. The `bootstrap` framework is used, with modifications, for CSS formatting. 

## The user experience
Some design elements are used to achieve something beyond the experience of a static site of ca. 1995, but it is a static site nonetheless. Users are presented with an introduction to the functionality of the site and simple methods (links and menus) to navigate the site's features. 

The idea behind this is that there is something more interesting than an academic journal article or a set of textual lecture notes that can be achieved best in a web format. Some (but not much) inspiration is taken from Hans Rosling's [gapminder.org](https://www.gapminder.org/tools/#$chart-type=bubbles) site, which renders line graphs and scatterplots of selected data based on user input. 

On the back-end, user input simply triggers the display of pages that have been constructed programmatically in advance. 

## Data model
The data model is a python dictionary of HTML documents. 

## Schedule
The project will take four weeks:

Week 1:
- select data sources
- write code to download and process data

Week 2:
- write code to conduct statistical analyses
- write code to generate maps

Week 3: 
- set up back-end to deliver content
- style and format pages, devise ways to enhance user experience

Week 4:
- test
- test again
- test more
