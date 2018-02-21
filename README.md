# BEC Scraper
Scraps [BEC](https://www.bec.sp.gov.br/BECSP/Home/Home.aspx) "pregão" and saves to [MongoCloud] (https://www.mongodb.com/cloud)
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
$ docker run -dit matheusmoraes/becscraper
```
Command above will print the container created. Access Container:

```
$ docker attach <CONTAINER>
```

And then run the script inside the Container

```
# xvfb-run --server-args="-screen 0 1024x768x24" python spider.py
```
_spider.py_ will log to stdout.


**IMPORTANT:**

* Scraping will take some minutes.
* Every action of scraper will be logged in stdout.
* Data will only be saved to MongoCloud when the scraping finish. Stopping the process manually will prevent data to be stored.



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
* 
