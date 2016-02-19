# PPCG-Grad-Stats

[![License](https://img.shields.io/:license-wtfpl-blue.svg?style=flat-square)](http://www.wtfpl.net)

This is just a simple Python 3 script that gathers and prints basic graduation statistics for the [Stack Exchange](https://stackexchange.com) site [Programming Puzzles &amp; Code Golf](https://codegolf.stackexchange.com).
It uses the [Stack Exchange API](https://api.stackexchange.com), v2.2.
Data is gathered from the past two weeks.
Since the API is used rather than Stack Exchange Data Explorer, results are up to the minute.
However, this also means that you're limited to 300 API requests per day (without an API key), so don't go too crazy.

It's often pointed out that the statistics on [Area 51](https://area51.stackexchange.com) don't matter.
As such, the only statistics that this currently gathers are the average questions per day (which *does* matter) and the average number of answers per question (for the curious).
If you want to see others stats as well, open an issue, submit a pull request, or just tell me in The Nineteenth Byte.

Run from the command line like `python3 gradstats.py` and all of your dreams will come true.

Disclaimer: This project is in no way affiliated with Stack Exchange, Inc.
