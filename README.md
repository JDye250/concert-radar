# Concert Radar

A Python project that checks concert events against artists and a city I track. It saves event IDs so the same event is not announced twice.

## Run

1. Install Python 3.
2. Run `python3 main.py`.
3. Enter a city and, if you want, add an artist.

## Current version

The program reads made-up events from `sample_events.json`. Live event searches and automatic checks are planned.

`settings.json` stores my artists, city, and seen event IDs locally. Git does not upload it.