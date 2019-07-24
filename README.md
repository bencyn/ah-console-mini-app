[![Build Status](https://travis-ci.org/bencyn/ah-console-mini-app.svg?branch=develop)](https://travis-ci.org/bencyn/ah-console-mini-app) [![Coverage Status](https://coveralls.io/repos/github/bencyn/ah-console-mini-app/badge.svg?branch=develop)](https://coveralls.io/github/bencyn/ah-console-mini-app?branch=develop)

## AH Console Mini App

A CLI app that interacts with Author's Haven

### Set up application
-  clone the repository 
    `git clone https://github.com/bencyn/ah-console-mini-app.git`

- create a virtual environment
  `virtualenv --python python3 venv`

- install the app
   `pip install --editable .`

-  run app 
   `ah`.

## Commands

1. View all articles

   `ah list`

2. View specific article

   `ah view <article-slug>`

3. Save specific article to file

   `ah export <article-slug>`
  
4. Search using a query string

   `ah search <query-string>`

4. View Ah help

   `ah help`

