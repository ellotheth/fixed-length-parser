# FixedLengthParser

## About

The `FixedLengthParser` class is a tiny, read-only helper to parse fixed-length text records (like [this][1] and [these][2]) into something more usable (an [OrderedDict][3], in this case).

## Requirements

Python 3.3

## todo

- add a sample
- be more flexible with the incoming field definitions
- don't require Python 3.3, that's dumb
- support fixed-length record writing

[1]: https://ribbs.usps.gov/pave/documents/tech_guides/pubs/PAVE_Appendix_B.PDF
[2]: http://www.idealliance.org/sites/default/files/MD_13_1_FS_v13%201%200%200.pdf
[3]: http://docs.python.org/3.3/library/collections.html#collections.OrderedDict