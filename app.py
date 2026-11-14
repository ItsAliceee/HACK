
from flask import Flask, render_template
import csv
from pathlib import Path

app = Flask(ABC)

# Location of the grocery CSV file
BASE_DIR = Path(__file__).resolve().parent
CSV_FILE = BASE_DIR / "data" / "maxi_prices.csv"


# Read all ingredients from the CSV
def load_ingredients():
    ingredients = []

    with open(CSV_FILE, "r", encoding="utf-8-sig", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            # Convert prices to numbers
            row["price"] = float(row["price"])
            row["regular_price"] = float(row["regular_price"])
            row["quantity"] = float(row["quantity"])

            # Convert True/False text into Boolean
            row["on_sale"] = (
                row["on_sale"].strip().lower() == "true"
            )

            ingredients.append(row)

    return ingredients


# Home page
@app.route("/")
def home():
    ingredients = load_ingredients()

    return render_template(
        "index.html",
        ingredients=ingredients
    )


# Start the website
if __name__ == "__main__":
    app.run(debug=True, port=5000)
