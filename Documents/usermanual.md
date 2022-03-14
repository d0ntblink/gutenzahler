# gutenzahler User Manual
### Gary Khodayari 13th Mar 2022

[Github Link](https://github.com/d0ntblink/gutenzahler)

## Requirements

**This program is only tested on a linux enviorment**

### Required Programs

* BSD-DB
* Python3

### Required Python Libraries

* gutenberg
* sys
* matplotlib

## Setup:

```
## install BSD-DB
apt install libdb++-dev
export BERKELEYDB_DIR=./

## install required python libs
pip install matplotlib gutenberg

## download gutenzahler
git clone https://github.com/d0ntblink/gutenzahler
cd gutenzahler/Code
chmod +x gutenzahler.py
```

## Usage:
to read and analyze a local file:

`gutenzahler.py --read <file format> <file target location>`

to read and analyze a book on Gutenberg Corpus:

`gutenzahler.py --fetch <bookid on gutenberg>`

***NOTE: I highley recommend using the fetch mode as the program will clean up the text and generate a more accurate resaults***

### Arguments:
*    --help: displays this message
*    --read: reads local files
*    --fetch: reads titles available on Gutenberg.org
*    --pie:  generates a pi graph of the alphabet letters
*    --bar: generates a bar graph of the alphabet letters
Accepted file formats:
    txt
    html (WIP)
    epub (WIP)

### Example:

`gutenzahler.py --fetch 10010 --bar`

`gutenzahler.py --read txt "/home/user/Hansel and Gretel.txt" --pie --bar`

`gutenzagler.py --read txt $PWD/lol.txt`