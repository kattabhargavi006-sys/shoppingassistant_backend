from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="AI Shopping Assistant")


class ProductQuery(BaseModel):
    query: str


def search_products(query):

    query = query.lower()

    # LAPTOPS
    if "laptop" in query:

        return [
            {
                "name": "HP Victus",
                "price": 58999,
                "pros": [
                    "Powerful Performance",
                    "Good Battery",
                    "Gaming Support"
                ],
                "cons": [
                    "Heavy Weight"
                ]
            },
            {
                "name": "Lenovo IdeaPad Gaming",
                "price": 59999,
                "pros": [
                    "Strong Build",
                    "Good Display"
                ],
                "cons": [
                    "Average Battery"
                ]
            },
            {
                "name": "ASUS Vivobook",
                "price": 56999,
                "pros": [
                    "Light Weight",
                    "Good Battery"
                ],
                "cons": [
                    "Not Suitable For Heavy Gaming"
                ]
            }
        ]

    # MOBILES
    elif "mobile" in query or "phone" in query:

        return [
            {
                "name": "Samsung Galaxy M35",
                "price": 18999,
                "pros": [
                    "Excellent Battery",
                    "Good Camera"
                ],
                "cons": [
                    "Plastic Build"
                ]
            },
            {
                "name": "Redmi Note 14",
                "price": 17999,
                "pros": [
                    "Bright Display",
                    "Good Performance"
                ],
                "cons": [
                    "Average Camera"
                ]
            },
            {
                "name": "Realme Narzo 70",
                "price": 16999,
                "pros": [
                    "Fast Charging",
                    "Good Design"
                ],
                "cons": [
                    "Average Speakers"
                ]
            }
        ]

    # HEADPHONES
    elif "headphone" in query or "earphone" in query:

        return [
            {
                "name": "Boat Rockerz 550",
                "price": 1999,
                "pros": [
                    "Strong Bass",
                    "Long Battery Life"
                ],
                "cons": [
                    "Bulky Design"
                ]
            },
            {
                "name": "JBL Tune 760NC",
                "price": 4999,
                "pros": [
                    "Noise Cancellation",
                    "Premium Sound"
                ],
                "cons": [
                    "Higher Price"
                ]
            }
        ]

    # SMART WATCHES
    elif "watch" in query:

        return [
            {
                "name": "Noise ColorFit Pro",
                "price": 2999,
                "pros": [
                    "Fitness Tracking",
                    "Good Display"
                ],
                "cons": [
                    "Average Battery"
                ]
            },
            {
                "name": "Fire-Boltt Ninja",
                "price": 2499,
                "pros": [
                    "Affordable",
                    "Stylish Design"
                ],
                "cons": [
                    "Limited Features"
                ]
            }
        ]

    # DEFAULT
    else:

        return [
            {
                "name": "Product Not Available",
                "price": 0,
                "pros": [
                    "Try Laptop, Mobile, Watch, Headphone"
                ],
                "cons": [
                    "No Matching Product Found"
                ]
            }
        ]


def recommend_best(products):

    valid_products = [
        p for p in products
        if p["price"] > 0
    ]

    if not valid_products:
        return products[0]

    best = min(valid_products, key=lambda x: x["price"])

    return best


@app.post("/recommend")
def recommend(data: ProductQuery):

    products = search_products(data.query)

    best_product = recommend_best(products)

    return {
        "query": data.query,
        "best_product": best_product,
        "all_products": products
    }