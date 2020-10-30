# MASHAPP
## Description

Mashapp is a web application used aiming to combine anything with anything according to interests, goals or anything that matter.

## Dependencies

* Django 3.*
* Python 3.*

## Actual state
Mashapp relies on [Gale & Shapley algorithm](https://fr.wikipedia.org/wiki/Algorithme_de_Gale_et_Shapley) which uses some criterion combined to their scores to produce
preference lists.

## Pipeline
Data is fed in algorithm by using a Google Form.

## Deploying
To deploy the app on your computer, follow these simple steps:
```
git clone https://github.com/Nprime496/pyMashapp
py env/activate
cd mashapp
py manage.py runserver
```


