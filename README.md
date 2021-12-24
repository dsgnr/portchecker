<h1 align="center">Welcome to portcheckerio 👋</h1>

![PyPI](https://img.shields.io/pypi/v/portcheckerio)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/portcheckerio)
[![GitHub license](https://img.shields.io/github/license/dsgnr/portchecker)](https://github.com/dsgnr/portchecker/blob/devel/LICENSE)
[![Pytest](https://github.com/dsgnr/portchecker/actions/workflows/pytest.yml/badge.svg)](https://github.com/dsgnr/portchecker/actions/workflows/pytest.yml)
[![CodeQL](https://github.com/dsgnr/portchecker/actions/workflows/codeql-analysis.yml/badge.svg)](https://github.com/dsgnr/portchecker/actions/workflows/codeql-analysis.yml)

This repository is the counterpart script which ports [portchecker.io](https://portchecker.io)

This package is a nice alternative way to using tools like `nc` to query the port connectivity. 
The main benefits is that it will work with hostnames, 
IPv4 and IPv6 addresses (if your client has IPv6 of course). 
You can also query multiple ports at the same time and receive a sweet JSON response.

## Installation

Portchecker can be installed from PyPI using `pip` or your package manager of choice:

```
pip install portcheckerio
```

## Usage

### CLI

You can use Portchecker as a CLI tool using the `portcheck` command.

Example:

```console
$ portcheck --host google.com --ports 443
{
    "2a00:1450:4009:815::200e": {
        "type": "ipv6",
        "results": [
            {
                "port": 443,
                "connectable": true
            }
        ]
    },
    "172.217.16.238": {
        "type": "ipv4",
        "results": [
            {
                "port": 443,
                "connectable": true
            }
        ]
    }
}
```

You can query multiple ports for a given host in the same command:

```console
$ portcheck --host google.com --ports 443 22
{
    "172.217.16.238": {
        "type": "ipv4",
        "results": [
            {
                "port": 443,
                "connectable": true
            },
            {
                "port": 22,
                "connectable": false
            }
        ]
    },
    "2a00:1450:4009:815::200e": {
        "type": "ipv6",
        "results": [
            {
                "port": 443,
                "connectable": true
            },
            {
                "port": 22,
                "connectable": false
            }
        ]
    }
}
```

## 📝 To Do

- [ ] Add more tests 
- [ ] Add the option to query RFC1918 addresses
- [ ] Add the option to increase the timeout limit 

### 🏠 [Homepage](https://portchecker.io)

### ✨ [Demo](https://portchecker.io)

## Author

👤 **Dan Hand**

* Website: https://danielhand.io
* Github: [@dsgnr](https://github.com/dsgnr)

## 🤝 Contributing

Contributions, issues and feature requests are welcome.<br />
Feel free to check [issues page](https://github.com/dsgnr/portchecker.io/issues) if you want to contribute.<br />


## Show your support

Give a ⭐️ if this project helped you!

Any donations to help the running of the site is hugely appreciated!

<a href="https://www.patreon.com/dsgnr_">
  <img src="https://c5.patreon.com/external/logo/become_a_patron_button@2x.png" width="100">
</a>
<a href="https://www.paypal.com/donate?business=RNT9HTKVJ2DDJ&no_recurring=0&item_name=portchecker.io+donation&currency_code=GBP" target="_blank"><img src="https://www.paypalobjects.com/en_GB/i/btn/btn_donate_SM.gif"></a>


## 📝 License

Copyright © 2019 [Dan Hand](https://github.com/dsgnr).<br />
This project is [MIT](https://github.com/kefranabg/readme-md-generator/blob/master/LICENSE) licensed.

---
***
_This README was generated with ❤️ by [readme-md-generator](https://github.com/kefranabg/readme-md-generator)_
