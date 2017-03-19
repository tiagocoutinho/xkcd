# xkcd

downloader of xkcd comics

## Installation

    $ pip install xkcd-get

## Requirements

* bs4
* grequests

## Usage

    # Downloads all xkcd comics to ~/Downloads/xkcd
    $ xkcd-get

    # Downloads xkcd comics [10..20] to /tmp/xkcd
    $ xkcd-get --start=10 --end=20 --output-dir=/tmp/xkcd
