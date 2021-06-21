# jcalendar
jcalendar is [Jalali](https://en.wikipedia.org/wiki/Iranian_calendars) implementation of Python's calendar module

## Status
![build workflow](https://github.com/IKermani/jcalendar/actions/workflows/python-publish.yml/badge.svg)
![version](https://img.shields.io/pypi/v/jcalendar.svg)
![license](https://img.shields.io/pypi/l/jcalendar)


## Install

```
pip install jcalendar
```

## Documents

This module *almost* follows [Python calendar](https://docs.python.org/3/library/calendar.html).
> *almost*: locale is not implemented yet.

## Example

```Python console
>>> c = calendar.TextCalendar()
>>> c.prmonth(1400, 5)
    Mordad 1400
Sa Su Mo Tu We Th Fr
                   1
 2  3  4  5  6  7  8
 9 10 11 12 13 14 15
16 17 18 19 20 21 22
23 24 25 26 27 28 29
30 31
```

## Todo
- [ ] support calendar locale


