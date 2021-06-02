# Censys Python Library

[![PyPI](https://img.shields.io/pypi/v/censys?color=orange&logo=pypi&logoColor=orange)](https://pypi.org/project/censys/)
[![Python Version](https://img.shields.io/badge/python-3.6%2B-blue?logo=python)](https://www.python.org/downloads/)
[![Read the Docs (version)](https://img.shields.io/readthedocs/censys-python/latest?logo=read%20the%20docs)](https://censys-python.readthedocs.io/en/stable/?badge=stable)
[![GitHub Discussions](https://img.shields.io/badge/GitHub-Discussions-brightgreen?logo=github)](https://github.com/censys/censys-python/discussions)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-organge.svg?logo=git&logoColor=organge)](http://makeapullrequest.com)
[![License](https://img.shields.io/github/license/censys/censys-python?logo=apache)](https://github.com/censys/censys-python/blob/main/LICENSE)

An easy-to-use and lightweight API wrapper for Censys APIs ([censys.io](https://censys.io/)). Python 3.6+ is currently supported.

## Getting Started

The library can be installed using `pip`.

```bash
pip install censys
```

To configure your search credentials run `censys config` or set both `CENSYS_API_ID` and `CENSYS_API_SECRET` environment variables.

```bash
$ censys config

Censys API ID: XXX
Censys API Secret: XXX

Successfully authenticated for your@email.com
```

To configure your ASM credentials run `censys config-asm` or set the `CENSYS_ASM_API_KEY` environment variables.

```bash
$ censys config-asm

Censys ASM API Key: XXX

Successfully authenticated
```

## API Reference and User Guide available on [Read the Docs](https://censys-python.readthedocs.io/)

## Upgrading

The library can be upgraded using `pip`.

```bash
pip install --upgrade censys
```

## Resources

- [Source](https://github.com/censys/censys-python)
- [Issue Tracker](https://github.com/censys/censys-python/issues)
- [Changelog](https://github.com/censys/censys-python/releases)
- [Documentation](https://censys-python.rtfd.io)
- [Discussions](https://github.com/censys/censys-python/discussions)
- [Censys Homepage](https://censys.io/)

## Contributing

All contributions (no matter how small) are always welcome.

## Development

```bash
git clone git@github.com:censys/censys-python.git
cd censys-python/
pip install -e ".[dev]"
```

## Testing

```bash
pytest
```

## License

This software is licensed under [Apache License, Version 2.0](http://www.apache.org/licenses/LICENSE-2.0)

- Copyright (C) 2021 Censys, Inc.
