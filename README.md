<p align="center">
<a href="https://github.com/txsadhu/domfu"><img src="https://i.imgur.com/xYoBNoF.png" alt="DomFu logo"></a>
</p>

<p align="center">
  <a href="https://www.python.org/download/releases/3.7">
    <img src="https://img.shields.io/badge/Python-3.7-green.svg">
  </a>
  <a href="https://github.com/txsadhu/domfu/releases">
    <img src="https://img.shields.io/badge/DomFu-v1.0-violet.svg">
  </a>
  <a href="https://github.com/txsadhu/domfu/">
      <img src="https://img.shields.io/badge/Tested%20on-Linux-yellow.svg">
  </a>
  <a href="https://github.com/TxSadhu/DomFu/blob/master/LICENSE.txt">
    <img src="https://img.shields.io/badge/License-GPLv3-orange.svg">
  </a> 
  <a href="https://github.com/0xinfection/TIDoS-Framework/releases/tag/v1.0/">
    <img src="https://img.shields.io/badge/Release-Stable-green.svg">
  </a>
</p>

---

A CLI app to find domains and subdomains of a given domain.

## Installation

**Using pip:**

```bash
pip install DomFu
```

**Manual Installation:**

```
$ git clone https://github.com/TxSadhu/DomFu.git
$ cd DomFu
$ python setup.py install
```

## Usage

**Using as Standalone CLI app:**

```bash
domfu --domain tropyl.com --output tropyl.txt
```

or

```bash
domfu tropyl.com tropyl.txt
```

**Using it as a python module:**

```python
import domfu
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
