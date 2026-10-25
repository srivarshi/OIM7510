import marimo

__generated_with = "0.24.2"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Section 1 Question - C · Pick the Day#
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
    PLAN -> Users - A student club organizing an outdoor event in Massachusetts. Problem - The club needs to identify a suitable day based on temparature, rain probability adn wind conditions. Output - A seven day weather comparision and a recommedation
    """)
    return


app._unparsable_cell(
    r"""
    Execution - The input should be the organizer can enter a Massachusetts town and weather limits, by using the Open Meteo's geocoding API we can find the town coordinates, which selects the forst match in Massachusetts. By using the forcast API to retrieve seven days of temparatures, rain probabilities and wind speeds. Present all this information as a record for each day and compare each days hight temparature, rain probability adn wind speed against the organizer limits. Values excalty at the limits should pass. Createa table showing the weather and whether each day qualifies. Among the qualifiying days, choose the lowest rain porbability, breaking ties with lower wind speed. If none qualify, choose a day breaking the fewest rukes, breaking ties by choosing the earlier date
    """,
    name="_"
)


if __name__ == "__main__":
    app.run()
