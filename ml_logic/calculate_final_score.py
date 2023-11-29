import pandas as pd
import numpy as np


def fill_sub_ratings(df, only_price = False):
    if only_price is True:
        df["price_rating"] = np.random.randint(1, 6, size=len(df))
        return df
    else:
        df["price_rating"] = np.random.randint(1, 6, size=len(df))
        df["service_rating"] = np.random.randint(1, 6, size=len(df))
        df["atmosphere_rating"] = np.random.randint(1, 6, size=len(df))
        df["food_rating"] = np.random.randint(1, 6, size=len(df))
        return df


def calculate_average_score(row, price_weight, service_weight, atmosphere_weight, food_weight):
    # Explicitly reference the desired columns for rating
    price_rating = row['price_rating']
    service_rating = row['service_rating']
    atmosphere_rating = row['atmosphere_rating']
    food_rating = row['food_rating']

    # Multiply each rating by its corresponding weight and calculate the weighted sum
    weighted_sum = (
        price_rating * price_weight +
        service_rating * service_weight +
        atmosphere_rating * atmosphere_weight +
        food_rating * food_weight
    )

    # Calculate the weighted average score
    total_weight = price_weight + service_weight + atmosphere_weight + food_weight
    average_score = weighted_sum / total_weight

    return average_score

def calculate_average_score_class(row, price_weight, service_weight, atmosphere_weight, food_weight):
    # Explicitly reference the desired columns for rating
    price_rating = row['price_rating']
    service_rating = row['service_rating']
    atmosphere_rating = row['atmosphere_rating']
    food_rating = row['food_rating']

    price_class = row['price']
    service_class = row['service']
    atmosphere_class = row['atmosphere']
    food_class = row['food']

    # Multiply each rating by its corresponding weight and calculate the weighted sum
    weighted_sum = (
        price_rating * price_weight * price_class +
        service_rating * service_weight * service_class +
        atmosphere_rating * atmosphere_weight * atmosphere_class +
        food_rating * food_weight * food_class
    )

    # Calculate the weighted average score
    total_weight = (price_weight * price_class) + \
    (service_weight * service_class) + (atmosphere_weight * atmosphere_class)  + (food_weight * food_class)
    average_score_class = round((weighted_sum / total_weight),2)

    return average_score_class

def df_with_score(df, price_weight, service_weight, atmosphere_weight, food_weight, with_class = True):
    if with_class is True:
        df['average_score'] = df.apply(calculate_average_score_class,
        args=(price_weight, service_weight, atmosphere_weight, food_weight),
        axis=1
        )
        return df
    else:
        df['average_score'] = df.apply(calculate_average_score,
        args=(price_weight, service_weight, atmosphere_weight, food_weight),
        axis=1
        )
        return df

def overall_score(df):
    return round(df.average_score.mean(), 2)

