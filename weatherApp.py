import argparse
import requests
import time
from bs4 import BeautifulSoup
from ftplib import FTP

parser = argparse.ArgumentParser()               
parser.add_argument('-n', '--now', help='Checks for current weather temps repeatedly from weatherzone', action='store_true')
parser.add_argument('--bom', help='Checks for current weather temps repeatedly from BOM', action='store_true')
parser.add_argument('--report', help='Downloads weather report from BOM', action='store_true')
args = parser.parse_args()

def requestPageCurrentTemp():
    try:
        page = requests.get('https://www.weatherzone.com.au/wa/perth/perth')
        soup = BeautifulSoup(page.text, "html.parser")
        nowTemp = str(soup.find(class_='tempnow')) 
        print(BeautifulSoup(nowTemp, "html.parser").get_text())
        time.sleep(5)
    except requests.ConnectionError:
        print("N/A")
        time.sleep(5)

def requestPageCurrentTempBom():
    try:
        page = requests.get('http://www.bom.gov.au/wa/observations/perth.shtml?ref=dropdown')
        nowTemp = str(BeautifulSoup(page.text, "html.parser").findAll( headers="tPERTH-tmp tPERTH-station-perth"))
        print(BeautifulSoup(nowTemp, "html.parser").get_text())
        time.sleep(5)
    except requests.ConnectionError:
        print("N/A")
        time.sleep(5)

def requestPageWeatherSummary():
    try:
        page = requests.get('https://www.weatherzone.com.au/wa/perth/perth')
        soup = BeautifulSoup(page.text, "html.parser")
        summaryForecast = str(soup.find(class_='summary_forecast'))
        summaryWeather = str(soup.find(class_='district-forecast'))
        weatherDetials = str(BeautifulSoup(summaryWeather, "html.parser").get_text('\n',strip=True))
        weather = str(BeautifulSoup(summaryForecast, "html.parser").find(id='wz_lwp_precis'))
        maxTemp = str(BeautifulSoup(summaryForecast, "html.parser").find(class_='local_grad_tdb_15'))
        minTemp = str(BeautifulSoup(summaryForecast, "html.parser").find(class_='local_grad_tdb_5'))
        nowTemp = str(soup.find(class_='tempnow')) 
        print("Summary for Weather: \n{}\n".format(weatherDetials), "\nDetials:"
            "\nMinimum Temp {}".format(BeautifulSoup(minTemp, "html.parser").get_text()), 
            "\nMaximum Temp {}".format(BeautifulSoup(maxTemp, "html.parser").get_text()),
            "\nCurrent Temp {}\n".format(BeautifulSoup(nowTemp, "html.parser").get_text()),
            "\nWeather {}".format(BeautifulSoup(weather, "html.parser").get_text()),
            )
        exit(0)
    except requests.ConnectionError:
        print("N/A")
        exit(0)
        
def ftpService():
    try:
        ftp = FTP('ftp.bom.gov.au')
        ftp.login()
        ftp.cwd('/anon/gen/fwo/')
        with open('IDW12300.txt', 'wb') as perthForecast:
            ftp.retrbinary('RETR IDW12300.txt', perthForecast.write)
        ftp.quit()
        exit(0)
    except:
        print('FTP is Down')
        exit(0)

while True:
    try:
        if args.now is True: 
            requestPageCurrentTemp()
        elif args.report is True:
            ftpService()
        elif args.bom is True:
            requestPageCurrentTempBom()
        else:
            requestPageWeatherSummary()
    except KeyboardInterrupt:
        print('\nClosing Program')
        exit(0)