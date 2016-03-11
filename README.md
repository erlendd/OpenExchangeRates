# About
This is an (unofficial) Python API for use with OpenExchangeRates.org.
It enables very simple conversion between common currencies using 
data provided by the OpenExchangeRates.org API.

Up to date exchange rates are automatically downloaded from OpenExchangeRates.org at most 
every hour (to comply with their policy regarding query rates).

It uses the builtin Python 'decimal' package for accuracy, 
but note that for extremely large numbers you may been to adjust the precision.

Some robustness via exception handling is implemented.

This code comes with absolutely no guarantee or warranty. Nor does it come with any
expectation of correctness. Use at your own risk.

**Requirements: Python-2.7.**

# Example of use
SECRET_KEY='insert key obtained from openexhcangerates.org'

### Convert from USD to EURO:
```python
r = Rates('USD', 'EUR', SECRET_KEY)
print r.convert(1.0)
```

### Convert from EURO to USD:
```python
r = Rates('EUR', 'USD', SECRET_KEY)
print r.convert(2.0)
```
