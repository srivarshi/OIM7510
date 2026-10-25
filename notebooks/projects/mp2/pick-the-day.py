import marimo

__generated_with = "0.24.2"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ##Question - C · Pick the Day#
    A student club is planning an outdoor event somewhere in Massachusetts in the next week and needs to pick the day. The organizer wants a table of the next seven days, today included, whether each day meets the club's rules, and the best day, for whatever town they type in.

    The data is Open-Meteo, which needs no key: its geocoding search turns a place name into coordinates, and its forecast gives seven days ahead.

    place = "Wellesley"
    state = "Massachusetts"
    lowest_high_f = 55
    highest_high_f = 80
    max_rain_chance = 30
    max_wind_mph = 15
    Copy
    The main task

    The coordinates of place from the geocoding search. A name can match places in several states, and several places in one state: use the first match in state, which is the largest, and name it in section 5.
    The daily forecast for those coordinates, in °F and mph: the high, the low, the chance of rain and the strongest wind for each day. The reply gives each of them as its own list; turn them into one record per day.
    A table with one row per day: the date, the high, the low, the chance of rain, the strongest wind, and whether the day passes every rule. A value equal to a limit passes.
    One sentence naming the best day, with the reason. When several days pass, the best has the lowest chance of rain, and on a tie the lower wind. If no day passes, name the day that breaks the fewest rules, and the earlier one on a tie.
    You may need the search's count= parameter, up to 100, since the search returns 10 places by default and Lexington, Massachusetts comes 13th. The forecast takes the daily= parameter, with temperature_unit=fahrenheit, wind_speed_unit=mph and timezone=America/New_York, so that each day runs from midnight to midnight in Boston, and zip() walks several lists at once.

    Going further

    Compare two or three towns and pick the best place as well as the best day.
    Ask a second forecast service and compare the two.
    Score each day out of 10 in place of pass and fail.
    Let the organizer change the rules without editing code.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ##PLAN
    Users - A student club organizing an outdoor event in Massachusetts. Problem - The club needs to identify a suitable day based on temparature, rain probability adn wind conditions. Output - A seven day weather comparision and a recommedation
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ##Execution
    The input should be the organizer can enter a Massachusetts town and weather limits, by using the Open Meteo's geocoding API we can find the town coordinates, which selects the forst match in Massachusetts. By using the forcast API to retrieve seven days of temparatures, rain probabilities and wind speeds. Present all this information as a record for each day and compare each days hight temparature, rain probability adn wind speed against the organizer limits. Values excalty at the limits should pass. Createa table showing the weather and whether each day qualifies. Among the qualifiying days, choose the lowest rain porbability, breaking ties with lower wind speed. If none qualify, choose a day breaking the fewest rukes, breaking ties by choosing the earlier date
    """)
    return


@app.cell
def _():
    import marimo as mo
    import requests
    import pandas as pd

    return mo, pd, requests


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ##Create input Fields
    """)
    return


@app.cell
def _(mo):
    place = mo.ui.text(value="", label="Massachusetts town")

    lowest_high_f = mo.ui.number(
        value=89,
        label="Minimum high temperature (°F)"
    )

    highest_high_f = mo.ui.number(
        value=103,
        label="Maximum high temperature (°F)"
    )

    max_rain_chance = mo.ui.number(
        value=100,
        label="Maximum rain probability (%)"
    )

    max_wind_mph = mo.ui.number(
        value=50,
        label="Maximum wind speed (mph)"
    )

    mo.vstack([
        place,
        lowest_high_f,
        highest_high_f,
        max_rain_chance,
        max_wind_mph
    ])
    return highest_high_f, lowest_high_f, max_rain_chance, max_wind_mph, place


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ##Find the town’s coordinates
    """)
    return


@app.cell
def _(requests):
    def find_coordinates(town):
        url = "https://geocoding-api.open-meteo.com/v1/search"

        params = {
            "name": town,
            "count": 100,
            "language": "en",
            "format": "json"
        }

        response = requests.get(url, params=params, timeout=15)
        response.raise_for_status()

        data = response.json()

        for location in data.get("results", []):
            if (
                location.get("admin1") == "Massachusetts"
                and location.get("country_code") == "US"
            ):
                return location

        return None

    return (find_coordinates,)


@app.cell
def _(find_coordinates):
    test_location = find_coordinates("Lexington")

    print(test_location)
    return (test_location,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ##Fetch the seven-day weather forecast
    """)
    return


@app.cell
def _(requests):
    def get_forecast(latitude, longitude):
        url = "https://api.open-meteo.com/v1/forecast"

        params = {
            "latitude": latitude,
            "longitude": longitude,
            "daily": (
                "temperature_2m_max,"
                "temperature_2m_min,"
                "precipitation_probability_max,"
                "wind_speed_10m_max"
            ),
            "temperature_unit": "fahrenheit",
            "wind_speed_unit": "mph",
            "timezone": "America/New_York",
            "forecast_days": 7
        }

        response = requests.get(url, params=params, timeout=15)
        response.raise_for_status()

        return response.json()["daily"]

    return (get_forecast,)


@app.cell
def _(get_forecast, test_location):
    test_forecast = get_forecast(

        test_location["latitude"],

        test_location["longitude"]

    )

    print(test_forecast)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ##Organize the weather into daily records
    """)
    return


@app.function
def make_daily_records(forecast):
    records = []

    for date, high, low, rain, wind in zip(
        forecast["time"],
        forecast["temperature_2m_max"],
        forecast["temperature_2m_min"],
        forecast["precipitation_probability_max"],
        forecast["wind_speed_10m_max"]
    ):
        records.append({
            "Date": date,
            "High (°F)": high,
            "Low (°F)": low,
            "Rain (%)": rain,
            "Wind (mph)": wind
        })

    return records


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ##Check whether each day qualifies
    """)
    return


@app.function
def check_weather(
    records,
    min_temp,
    max_temp,
    max_rain,
    max_wind
):
    for day in records:
        rules = [
            min_temp <= day["High (°F)"],
            day["High (°F)"] <= max_temp,
            day["Rain (%)"] <= max_rain,
            day["Wind (mph)"] <= max_wind
        ]

        day["Pass"] = all(rules)
        day["Rules Broken"] = rules.count(False)

    return records


@app.cell
def _():
    boundary_test = [
        {
            "Date": "2026-10-25",
            "High (°F)": 55,
            "Low (°F)": 40,
            "Rain (%)": 30,
            "Wind (mph)": 15
        }
    ]

    boundary_result = check_weather(
        boundary_test, 55, 80, 30, 15
    )

    print("Boundary test:", boundary_result[0]["Pass"])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ##Select the best day
    """)
    return


@app.function
def choose_best_day(records):
    qualifying_days = [
        day for day in records
        if day["Pass"]
    ]

    if qualifying_days:
        best = min(
            qualifying_days,
            key=lambda day: (
                day["Rain (%)"],
                day["Wind (mph)"]
            )
        )

        reason = (
            "This day meets all weather requirements "
            "and has the lowest rain probability, "
            "with wind speed used to break ties."
        )

    else:
        best = min(
            records,
            key=lambda day: (
                day["Rules Broken"],
                day["Date"]
            )
        )

        reason = (
            "No day meets all weather requirements. "
            "This day breaks the fewest rules, "
            "with the earlier date used to break ties."
        )

    return best, reason


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ##Connect all the functions
    """)
    return


@app.cell
def _(find_coordinates, get_forecast):
    def run_weather_tool(
        town,
        min_temp,
        max_temp,
        max_rain,
        max_wind
    ):

        location = find_coordinates(town)

        if location is None:
            raise ValueError(
                f"No matching Massachusetts town: {town}"
            )

        forecast = get_forecast(
            location["latitude"],
            location["longitude"]
        )

        records = make_daily_records(forecast)

        checked_records = check_weather(
            records,
            min_temp,
            max_temp,
            max_rain,
            max_wind
        )

        best_day, reason = choose_best_day(
            checked_records
        )

        return location, checked_records, best_day, reason

    return (run_weather_tool,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ##Display the final results
    """)
    return


@app.cell
def _(location, mo):
    mo.md(
        f"**Selected location:** {location['name']}, "
        f"{location['admin1']}, {location['country']}  \n"
        f"**Latitude:** {location['latitude']}  \n"
        f"**Longitude:** {location['longitude']}  \n"
        f"**Population:** {location.get('population', 'Not available')}"
    )
    return


@app.cell
def _(
    highest_high_f,
    lowest_high_f,
    max_rain_chance,
    max_wind_mph,
    mo,
    pd,
    place,
    run_weather_tool,
):
    location, weather_records, best_day, reason = run_weather_tool(
        place.value,
        lowest_high_f.value,
        highest_high_f.value,
        max_rain_chance.value,
        max_wind_mph.value
    )

    weather_table = pd.DataFrame(weather_records)

    mo.vstack([
        mo.md(
            f"## Weather Forecast: {location['name']}, Massachusetts"
        ),

        mo.ui.table(
            weather_table[
                [
                    "Date",
                    "High (°F)",
                    "Low (°F)",
                    "Rain (%)",
                    "Wind (mph)",
                    "Pass"
                ]
            ]
        ),

    mo.md(
        f"### Recommended Day: {best_day['Date']}\n\n"
        f"**High temperature:** {best_day['High (°F)']}°F  \n"
        f"**Rain probability:** {best_day['Rain (%)']}%  \n"
        f"**Wind speed:** {best_day['Wind (mph)']} mph  \n\n"
        f"**Reason:** {reason}"
    )
    ])
    return (location,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Testing and Verification
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Wellesley: Verified that the tool retrieves seven days of weather.
    Lexington: Verified that the correct Massachusetts location is selected.
    Boundary test: Confirmed that values exactly at the limits pass.
    No qualifying days: Confirmed that the program recommends the day breaking the fewest rules.
    Interactive inputs: Verified that changing the town and weather limits updates the results.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ##Reflection
    1. What I Built

    I built an interactive weather recommendation tool for a student club organizing outdoor events in Massachusetts. The organizer can enter a town and set weather preferences, including temperature, rain probability, and wind speed. The tool retrieves a seven-day weather forecast, compares each day’s conditions against the requirements, and recommends the most suitable day.

    2. How I Used AI

    I first created my own plan explaining the problem, inputs, and expected output before using AI. After that, I used AI to help me write the Python functions and understand how to connect them. I also used AI to understand how to test the program, identify issues, and improve the final output. I tested the suggestions in Marimo to check whether they worked.

    3. What I Learned

    I learned how to use APIs to retrieve real-time data instead of manually entering information. I understood how dictionaries store information using keys and values, and how lists organize multiple weather measurements. I also learned how zip() combines separate lists of dates, temperatures, rain probabilities, and wind speeds into one record for each day.

    Another important learning was how to use conditional statements to evaluate weather requirements and select the best day based on multiple rules.

    4. How I Verified the Code

    I initially tested the tool using Wellesley and checked whether it displayed seven days of weather and recommended a suitable date. I then changed the town to Lexington and verified that the location and weather forecast updated correctly.

    One challenge I faced was that the results initially did not seem to update when I changed the input values. I had to understand how Marimo’s interactive inputs work and how changes in the input fields affect the final output. After testing the inputs and checking the results, I was able to verify that the program was responding correctly.

    I also tested boundary conditions to confirm that values exactly at the limits would pass. Finally, I tested a scenario where none of the seven days qualified. The program still recommended a day by selecting the one that broke the fewest rules, using the earliest date to break ties.

    5. What I Would Improve

    If I had more time, I would compare weather forecasts from different sources to see how consistent the recommendations are. I would also explore adding a scoring system that rates each day out of 10 instead of only showing whether it passes or fails. This could help organizers compare days more easily, even when none meets all their requirements.
    """)
    return


if __name__ == "__main__":
    app.run()
