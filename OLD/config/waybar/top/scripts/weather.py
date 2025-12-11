#!/usr/bin/python3

import json
from datetime import datetime

import requests


def map_weather_code_to_condition() -> dict:
    """See the wttr.in source code: https://github.com/chubin/wttr.in/blob/master/lib/constants.py"""
    return {
        "113": "Sunny",
        "116": "PartlyCloudy",
        "119": "Cloudy",
        "122": "VeryCloudy",
        "143": "Fog",
        "176": "LightShowers",
        "179": "LightSleetShowers",
        "182": "LightSleet",
        "185": "LightSleet",
        "200": "ThunderyShowers",
        "227": "LightSnow",
        "230": "HeavySnow",
        "248": "Fog",
        "260": "Fog",
        "263": "LightShowers",
        "266": "LightRain",
        "281": "LightSleet",
        "284": "LightSleet",
        "293": "LightRain",
        "296": "LightRain",
        "299": "HeavyShowers",
        "302": "HeavyRain",
        "305": "HeavyShowers",
        "308": "HeavyRain",
        "311": "LightSleet",
        "314": "LightSleet",
        "317": "LightSleet",
        "320": "LightSnow",
        "323": "LightSnowShowers",
        "326": "LightSnowShowers",
        "329": "HeavySnow",
        "332": "HeavySnow",
        "335": "HeavySnowShowers",
        "338": "HeavySnow",
        "350": "LightSleet",
        "353": "LightShowers",
        "356": "HeavyShowers",
        "359": "HeavyRain",
        "362": "LightSleetShowers",
        "365": "LightSleetShowers",
        "368": "LightSnowShowers",
        "371": "HeavySnowShowers",
        "374": "LightSleetShowers",
        "377": "LightSleet",
        "386": "ThunderyShowers",
        "389": "ThunderyHeavyRain",
        "392": "ThunderySnowShowers",
        "395": "HeavySnowShowers",
    }


def map_weather_condition_to_emoji() -> dict:
    """See the wttr.in source code: https://github.com/chubin/wttr.in/blob/master/lib/constants.py"""
    return {
        "Unknown": "✨",
        "Cloudy": "☁️",
        "Fog": "🌫",
        "HeavyRain": "🌧",
        "HeavyShowers": "🌧",
        "HeavySnow": "❄️",
        "HeavySnowShowers": "❄️",
        "LightRain": "🌦",
        "LightShowers": "🌦",
        "LightSleet": "🌧",
        "LightSleetShowers": "🌧",
        "LightSnow": "🌨",
        "LightSnowShowers": "🌨",
        "PartlyCloudy": "⛅️",
        "Sunny": "☀️",
        "ThunderyHeavyRain": "🌩",
        "ThunderyShowers": "⛈",
        "ThunderySnowShowers": "⛈",
        "VeryCloudy": "☁️",
    }


def map_moon_phase_to_emoji() -> dict:
    """See https://spaceplace.nasa.gov/moon-phases/en/ for the names."""
    return {
        "New": "🌑",
        "Waxing Crescent": "🌒",
        "First Quarter": "🌓",
        "Waxing Gibbous": "🌔",
        "Full Moon": "🌕",
        "Waning Gibbous": "🌖",
        "Third Quarter": "🌗",
        "Waning Crescent": "🌘",
    }


def map_moon_phase_to_latin() -> dict:
    return {
        "New": "Novilunium",
        "Waxing Crescent": "Crescens Cornicularis",
        "First Quarter": "Crescens Dimidiata",
        "Waxing Gibbous": "Crescens in Orbem Insinuata",
        "Full Moon": "Plenilium",
        "Waning Gibbous": "Decrescens in Orbem Insinuata",
        "Third Quarter": "Decrescens Dimidiata",
        "Waning Crescent": "Decrescens Cornicularis",
    }


def return_on_error(err_msg: str) -> dict:
    return {
        "text": "WEATHER",
        "alt": "WEATHER",
        "tooltip": err_msg,
    }


def twelve_to_twentyfour_clock(twelve_time: str) -> str:
    in_time = datetime.strptime(twelve_time, "%I:%M %p")
    out_time = datetime.strftime(in_time, "%H:%M")
    return out_time


def format_time(time: str):
    return time.replace("00", "").zfill(2)


def extract_current_condition_relevant(weather_content: dict) -> dict:
    try:
        temperature: str = weather_content["current_condition"][0]["FeelsLikeC"]
        observation_time: str = twelve_to_twentyfour_clock(
            weather_content["current_condition"][0]["observation_time"]
        )
        weather_code: str = weather_content["current_condition"][0]["weatherCode"]
        rain_mm: str = weather_content["current_condition"][0]["precipMM"]
        wind_kph: str = weather_content["current_condition"][0]["windspeedKmph"]
        return {
            "temperature": temperature,
            "time": observation_time,
            "code": weather_code,
            "rain": rain_mm,
            "wind": wind_kph,
        }
    except:
        raise


def extract_location_relevant(weather_content: dict) -> dict:
    try:
        city: str = weather_content["nearest_area"][0]["areaName"][0]["value"]
        country: str = weather_content["nearest_area"][0]["country"][0]["value"]
        provence: str = weather_content["nearest_area"][0]["region"][0]["value"]
        population: str = weather_content["nearest_area"][0]["population"]
        return {
            "city": city,
            "country": country,
            "provence": provence,
            "population": population,
        }
    except:
        raise


def extract_astronomy_relevant(weather_content: dict) -> dict:
    try:
        moon_phase: str = weather_content["weather"][0]["astronomy"][0]["moon_phase"]
        sunrise: str = twelve_to_twentyfour_clock(
            weather_content["weather"][0]["astronomy"][0]["sunrise"]
        )
        sunset: str = twelve_to_twentyfour_clock(
            weather_content["weather"][0]["astronomy"][0]["sunset"]
        )
        return {
            "moon_phase": moon_phase,
            "sunrise": sunrise,
            "sunset": sunset,
        }
    except:
        raise


def extract_forcast_day(weather_content: dict, day: int) -> list[dict]:
    forcast_data: list[dict] = []
    weather_content_day: dict = weather_content["weather"][day]
    for hour_data in weather_content_day["hourly"]:
        forcast: dict = {}
        if (int(format_time(hour_data["time"])) < datetime.now().hour - 2) and (
            day == 0
        ):
            continue
        forcast["time"] = f"{format_time(hour_data["time"])}" + ":00"
        forcast["code"] = hour_data["weatherCode"]
        forcast["temperature"] = hour_data["FeelsLikeC"]
        forcast["chance"] = {
            "fog": (hour_data["chanceoffog"] + "%"),
            "frost": (hour_data["chanceoffrost"] + "%"),
            "overcast": (hour_data["chanceofovercast"] + "%"),
            "rain": (hour_data["chanceofrain"] + "%"),
            "snow": (hour_data["chanceofsnow"] + "%"),
            "sunshine": (hour_data["chanceofsunshine"] + "%"),
            "thunder": (hour_data["chanceofthunder"] + "%"),
            "wind": (hour_data["chanceofwindy"] + "%"),
        }
        forcast_data.append(forcast)
    return forcast_data


def get_text(current_condition: dict, map_condition: dict, map_emoji: dict) -> str:
    temp = current_condition["temperature"]
    code = current_condition["code"]
    emoji = map_emoji[map_condition[code]]
    return f"{emoji} {temp}°C"


def format_title(title: str, text: list[str], line_char: str = "—") -> str:
    max_length = max(len(s) for s in text)
    title_length = len(title)
    times = (max_length - title_length - 2) // 3
    seperator_half = times * line_char
    return f"{seperator_half} {title} {seperator_half}"


def hour_separator_line(text: list[str], separator_char: str = "·") -> str:
    max_length = max(len(s) for s in text)
    return separator_char * max_length


def flatten_generator(nested_list):
    for item in nested_list:
        if isinstance(item, list):
            yield from flatten_generator(item)
        else:
            yield item


def get_tooltip(
    current_condition: dict,
    location_info: dict,
    astronomy: dict,
    forcast: list[list[dict]],
    map_condition: dict,
    map_weather_emoji: dict,
    map_moon_emoji: dict,
    map_moon_latin: dict,
) -> str:
    lines: list[str] = []

    temp = current_condition["temperature"]
    weather_emoji = map_weather_emoji[map_condition[current_condition["code"]]]
    rain = current_condition["rain"]
    wind = current_condition["wind"]
    time = current_condition["time"]
    city = location_info["city"]
    provence = location_info["provence"]
    country = location_info["country"]
    population = location_info["population"]

    lines_today: list[str] = []
    lines_today.append(f"{country}, {city} ({provence}) —   {int(population):,}")
    lines_today.append(f"Polled at {time}")
    lines_today.append(f"{weather_emoji} — {temp}°C")
    lines_today.append(f"💧 — {rain} mm")
    lines_today.append(f"🍃 — {wind} kph")

    lines_astronomy: list[str] = []
    moon_emoji = map_moon_emoji[astronomy["moon_phase"]]
    moon_latin = map_moon_latin[astronomy["moon_phase"]]
    sunrise = astronomy["sunrise"]
    sunset = astronomy["sunset"]
    lines_astronomy.append(f"{moon_emoji} — {moon_latin}")
    lines_astronomy.append(f"🌄 — {sunrise}")
    lines_astronomy.append(f"🌇 — {sunset}")

    lines_forecast: list[list[list[str]]] = []
    for day_forecast in forcast:
        lines_dayforecast: list[list[str]] = []
        for hour_forecast in day_forecast:
            lines_hourforecast: list[str] = []
            forecast_time = hour_forecast["time"]
            weather_emoji = map_weather_emoji[map_condition[hour_forecast["code"]]]
            temp = hour_forecast["temperature"]
            chances = hour_forecast["chance"]

            lines_hourforecast.append(
                f"  — {forecast_time} | {weather_emoji} — {temp}°C"
            )
            lines_hourforecast.append(
                f"🌁 — {chances["fog"]} | ❄️ — {chances["frost"]} | ☁️ — {chances["overcast"]} | 🌧️ — {chances["rain"]}"
            )
            lines_hourforecast.append(
                f"🌨️ — {chances["snow"]} | ☀️ — {chances["sunshine"]} | ⛈️ — {chances["thunder"]} | 🌪️ — {chances["wind"]}"
            )
            lines_dayforecast.append(lines_hourforecast)
        lines_forecast.append(lines_dayforecast)

    all_lines = lines_today + lines_astronomy + list(flatten_generator(lines_forecast))

    lines.append(format_title(title="Weather Today", text=all_lines))
    lines += lines_today
    lines.append(format_title(title="Astronomy", text=all_lines))
    lines += lines_astronomy
    for i, lines_dayforecast in enumerate(lines_forecast):
        if i == 0:
            lines.append(format_title(title="Forecast Today", text=all_lines))
        elif i == 1:
            lines.append(format_title(title="Forecast Tomorrow", text=all_lines))
        else:
            continue

        for idx, lines_hourforecast in enumerate(lines_dayforecast):
            for line in lines_hourforecast:
                lines.append(line)
            if idx < len(lines_dayforecast) - 1:
                lines.append(hour_separator_line(text=all_lines))

    return "\n".join(lines)


if __name__ == "__main__":
    try:
        # Get city name via IP information
        ip_response: requests.Response = requests.get("https://ipinfo.io/json")
        ip_content: dict = ip_response.json()
        location: str = ip_content["city"].lower()
    except Exception as e:
        print(
            json.dumps(
                return_on_error(
                    err_msg=f"Request did not yield weather information: {e}"
                )
            )
        )
        exit()

    try:
        # Get weather information
        weather_response: requests.Response = requests.get(
            f"https://wttr.in/{location}?format=j1"
        )
        weather_content: dict = dict(weather_response.json())
    except Exception as e:
        print(
            json.dumps(
                return_on_error(
                    err_msg=f"Request did not yield weather information: {e}"
                )
            )
        )
        exit()

    map_condition: dict = map_weather_code_to_condition()
    map_weather_emoji: dict = map_weather_condition_to_emoji()
    map_moon_emoji: dict = map_moon_phase_to_emoji()
    map_moon_latin: dict = map_moon_phase_to_latin()
    try:
        current_condition: dict = extract_current_condition_relevant(weather_content)
        location_info: dict = extract_location_relevant(weather_content)
        astronomy: dict = extract_astronomy_relevant(weather_content)
        forcast: list[list[dict]] = []
        for i in range(len(weather_content["weather"])):
            forcast.append(extract_forcast_day(weather_content, day=i))
    except Exception as e:
        print(
            json.dumps(
                return_on_error(err_msg=f"Could not extract required information: {e}")
            )
        )
        exit()

    try:
        text = get_text(
            current_condition=current_condition,
            map_condition=map_condition,
            map_emoji=map_weather_emoji,
        )

        tooltip = get_tooltip(
            current_condition=current_condition,
            location_info=location_info,
            astronomy=astronomy,
            forcast=forcast,
            map_condition=map_condition,
            map_weather_emoji=map_weather_emoji,
            map_moon_emoji=map_moon_emoji,
            map_moon_latin=map_moon_latin,
        )
    except Exception as e:
        print(
            json.dumps(
                return_on_error(err_msg=f"Error while making text or tooltip: {e}")
            )
        )
        exit()

    waybar_content: dict = {
        "text": text,
        "alt": text,
        "tooltip": tooltip,
    }
    print(json.dumps(waybar_content))
