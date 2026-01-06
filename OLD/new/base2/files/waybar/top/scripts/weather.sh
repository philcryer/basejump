#!/bin/sh

LOCATION=darmstadt

WEATHER=$(curl -s "https://wttr.in/$LOCATION?format=%c+%m+%t\n")

# printf '{"text": "%s", "alt": "%s", "tooltip": "%s", "class": "blank"}' "$WEATHER" "$WEATHER" "$WEATHER"
printf '{"text": "%s", "alt": "%s", "tooltip": "%s"}' "$WEATHER" "$WEATHER" "$WEATHER"
