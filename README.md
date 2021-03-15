# ipX

![](https://raw.githubusercontent.com/shaeinst/ipX/main/images/ipX.png)

**Table of Contents**

[TOC]

# Welcome
### find the location of an IP address.
Specifically, you can get the following information for any IP address:
city, region (name & code), country (name & code), continent, postal code / zip code, latitude, longitude, timezone, utc offset, european union (EU) membership, country calling code, country capital, country tld (top-level domain), currency (name & code), area & population of the country, languages spoken, asn and organization

## Features
+ get your own or other ip  address
+ save result to any of following format
  + json
  + jsonp
  + yaml
  + xml
  + csv
+ don't show result on screen, just save result to file

## Uses
##### to get help, use --help/-h flag. Example:
`python ipX.py --help`
##### to know details of your IP,  use --myip/--self/-I flag. Example:
`python ipX.py --myip`
##### to find location of any ip address, use  -i/--ip ip_address flag. Example:
`python ipX.py --ip 8.8.8.8`
here 8.8.8.8 is ip address which i want to find
##### to save result, use --output/-o flag. Example:
`python ipX.py --ip 8.8.8.8 --output result.json`
this will save result to "result.json" file.
note: if you don't specify filename or file extension(here in this example, json), by default it going to save file as result.json


## Author

👤 **Ali Shahid**

* Website:  [click here](shaeinst.github.io/)
* Github: [@shaeinst](https://github.com/shaeinst)


## 📝 License

This project is [MIT](https://github.com/shaeinst/ipX/blob/main/LICENSE) licensed.
