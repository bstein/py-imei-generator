# py-imei-generator

Specify 8-12 prefix digits, how many numbers you'd like, and then receive a list of full, 15-digit random IMEI numbers. Unlike other random IMEI generators, py-imei-generator supports creating IMEI numbers for specific device models. Please see [IMEI Basics](#imei-basics) for more information.

## Getting Started
### Prerequisites

You first need to have either Python 2.x or Python 3.x installed (either is fine as imei.py is compatible with both). See [this guide](https://realpython.com/installing-python/) for installing Python 3. Since imei.py is just a module, pip is not required.

### Usage

Download imei.py from this repository. Open your terminal, navigate to the directory where imei.py is located, and run the following command.

```
python imei.py
```

You can then use the tool...

<img src="https://raw.githubusercontent.com/bstein/py-imei-generator/master/usage-screenshot.png"/>

## IMEI Basics

There's a decent [Wikipedia article](https://en.wikipedia.org/wiki/International_Mobile_Equipment_Identity) on International Mobile Equipment Identity (IMEI).

This image, published by [GSMA](https://www.gsma.com/services/gsma-imei/tac-allocation/tac-for-iot/) shows how IMEI numbers are constructed.

<img src="https://raw.githubusercontent.com/bstein/py-imei-generator/master/structure-imei.png"/>

The first 8 digits represent the [Type Allocation Code (TAC)](https://en.wikipedia.org/wiki/Type_Allocation_Code). This identifies the particular model of device to be used on wireless networks. With py-imei-generator, you can specify a TAC (let's say for Phone X) and receive random IMEI numbers that would be interpreted by others as a Phone X device.

The next 6 digits (starting from 1, range would be 9 - 14) are intended to represent the unique serial number given to the device by the manufacturer. You can specify the first 4 of these 6 digits with py-imei-generator.

Finally, the last digit is merely a check digit and is calculated with the [Luhn algorithm](https://github.com/bstein/py-imei-generator/blob/master/structure-imei.png).

## Disclaimer

This tool can be used for a variety of reasons. However, use it at your own risk; be sure to check your local laws to ensure that what you plan on doing is legal (and, ideally – ethical).

For example, at the time of writing, changing the IMEI of a phone was legal in the United States and illegal in the United Kingdom. If your phone's IMEI is "damaged," you should at least try to restore the original IMEI rather than generating a new, random one.
