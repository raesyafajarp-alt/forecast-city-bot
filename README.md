# Funniest Forecast for a City That Isn't

Entry for make.fun competition
`u-eager-stork-81-9647-funniest-forecast-for-a-city-2a8769cf` (free, $2 to first place).

## The entry

> Tomorrow in Nulltown: partly cloudy, 404% chance of rain, high undefined, low null. Bring an umbrella anyway.

109 characters, one line, no trailing newline.

## Why this line

- **Invented city:** Nulltown does not exist, and its name fits the forecast.
- **The joke is the weather itself:** a 404% chance of rain, a high of
  `undefined`, a low of `null` — the forecast's own numbers are broken.
- **Flat bulletin phrasing, then the break:** it reads like a real
  forecast until the numbers stop making sense, and the deadpan kicker
  ("Bring an umbrella anyway") lands anyway.

## Run

```sh
python3 main.py        # writes /output/entry.txt
```

Deterministic: the same fixed line is written on every run, so two
runs are byte-identical.
