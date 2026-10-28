import marimo

__generated_with = "0.24.2"
app = marimo.App(width="medium")


@app.cell
def _():
    orders = [
        {"OrderID": 10248, "ShipCountry": "France"},
        {"OrderID": 10249, "ShipCountry": "Germany"},
    ]
    orders["ShipCountry"]
    return (orders,)


@app.cell
def _(orders):
    countries = []

    for order in orders:
        country = order['ShipCountry']
        countries.append(country)

    countries
    return


@app.cell
def _():
    bmi = 27
    if bmi >= 18.5:
        category = "Normal"
    elif bmi >= 25:
        category = "Overweight"
    elif bmi >= 30:
        category = "Obese"
    else:
        category = "Underweight"
    return


if __name__ == "__main__":
    app.run()
