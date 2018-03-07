# BEC Scraper
Scraps [BEC](https://www.bec.sp.gov.br/BECSP/Home/Home.aspx) "pregão" and saves to [MongoCloud](https://www.mongodb.com/cloud)
the colected data. Defaults to [Pregão de Materiais](https://www.bec.sp.gov.br/becsp/aspx/DetalheOCItens.aspx?chave=&detalhe=1).

## Usage
Clone project and follow the instructions.

### Docker (Recommended)
#### Install Docker
[Docker](https://docs.docker.com/install/)

#### Pull image

```
$ docker pull matheusmoraes/becscraper
```

#### Run 
<!--```
$ docker run becscraper
```
Or, alternativilly you can run it interactivelly.-->

```
$ docker run matheusmoraes/becscraper
```
Thats it. Scraping execution will log to stdout.


**IMPORTANT:**

* Scraping will take some minutes.
* Every action of scraper will be logged in stdout.



### Running locally
#### Install dependencies
``` $ pip install -r requirements.txt ```

#### Install OS dependencies
1. Install [Splinter dependencies](http://splinter.readthedocs.io/en/latest/contribute/setting-up-your-development-environment.html)
2. Install [Browser dependencies](http://splinter.readthedocs.io/en/latest/drivers/firefox.html)

*it’s important to note that you also need to have* _**Firefox and geckodriver**_ *installed in your machine and available on PATH environment variable.*

## Running tests
Execute in the root directory

```
$ pip install green
```

```
$ green -vv tests
```

## TODO
* Pagination
* Increase test coverage
