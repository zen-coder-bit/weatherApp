<br/>
<p align="center">
  <h2 align="center">Python CLI Weather App</h2>

  <p align="center">
    Basic CLI weather app that scraps weather sites such as BOM and WeatherZone for Perth's current weather.
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

* [os](https://docs.python.org/3/library/os.html)
* [argparse](https://docs.python.org/3/library/argparse.html)
* [requests](https://docs.python-requests.org/en/master/)
* [time](https://docs.python.org/3/library/time.html)
* [bs4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
* [ftplib](https://docs.python.org/3/library/ftplib.html)

## Getting Started
### Prerequisites

At least [Python 3.6+](https://www.python.org/).

Install:
 ```sh
pip install bs4
```
```sh
pip install requests
```
### Installation

Clone the repo

```sh
git clone https://github.com/zen-coder-bit/weatherApp.git
```

## Usage

Please note before using any BOM or Weatherzone related commands.

- Copyright from: http://www.bom.gov.au/other/copyright.shtml
- Service usage for FTP: http://www.bom.gov.au/catalogue/anon-ftp.shtml
- Refer to Weatherzone conditions: https://www.weatherzone.com.au/about/conditions.jsp



usage: ```weatherApp.py [-h] [--weatherzone] [--summary] [--report]```

optional arguments:

* ```-h, --help```      Show this help message and exit.
* ```--weatherzone```   Checks for current weather temps repeatedly from Weatherzone.
* ```--summary```       Prints summary report for Weatherzone web page.
* ```--report```        Downloads todays weather report from BOM ftp


## License

Distributed under the GNU General Public License v3.0 License. See [LICENSE](https://github.com/zen-coder-bit/weatherApp/blob/master/LICENSE) for more information.

## Authors

* [Zen](https://github.com/zen-coder-bit)




