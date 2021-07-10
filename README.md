<br/>
<p align="center">
  <h2 align="center">Python CLI Weather App</h2>

  <p align="center">
    Basic CLI weather app that scraps weather sites such as BOM and Weather Zone for Perth forecasts.
    <br/>
    <br/>
  </p>
</p>

## Table Of Contents

* [Built With](#built-with)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [Usage](#usage)
* [License](#license)
* [Authors](#authors)


## Built With

Used python libraries:

[argparse](https://docs.python.org/3/library/argparse.html)
[requests](https://docs.python-requests.org/en/master/)
[time](https://docs.python.org/3/library/time.html)
[bs4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
[ftplib](https://docs.python.org/3/library/ftplib.html)

## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

At least [Python3.6](https://www.python.org/) or higher.

Install Beautiful Soup 4:
 ```sh
pip install bs4
```
```sh
pip install requests
```
### Installation

Clone the repo

```sh
git clone https://github.com/your_username_/Project-Name.git
```

## Usage
Please note before using any BOM related commands.
Copyright from http://www.bom.gov.au/other/copyright.shtml
Service usage for FTP http://www.bom.gov.au/catalogue/anon-ftp.shtml
  
Refer to Weatherzone conditions
https://www.weatherzone.com.au/about/conditions.jsp



usage: ```weatherApp.py [-h] [-n] [--bom] [--report]```

optional arguments:
 ``` -h, --help```  show this help message and exit
 ``` -n, --now```   Checks for current weather temps repeatedly from weatherzone
``` --bom```    Checks for current weather temps repeatedly from BOM
``` --report```    Downloads weather report from BOM

## License

Distributed under the GNU General Public License v3.0 License. See [LICENSE](https://github.com/zen-coder-bit/weatherApp/blob/master/LICENSE) for more information.

## Authors

* [Zen](https://github.com/zen-coder-bit)




