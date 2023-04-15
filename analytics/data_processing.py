import datetime
import random
from collections import defaultdict

# Simulated data for demonstration purposes
data = [
    {"user_id": 1, "url": "/home", "timestamp": datetime.datetime.now()},
    {"user_id": 2, "url": "/about", "timestamp": datetime.datetime.now()},
]

def aggregate_daily_pageviews(data):
    daily_pageviews = defaultdict(int)

    for entry in data:
        date = entry["timestamp"].date()
        daily_pageviews[date] += 1

    return dict(daily_pageviews)

def compute_average_session_duration(data):
    # For the sake of demonstration, we'll just generate random numbers
    return random.uniform(60, 300)

def compute_bounce_rate(data):
    # For the sake of demonstration, we'll just generate random numbers
    return random.uniform(0, 100)

def get_daily_metrics(start_timestamp, end_timestamp):
    filtered_data = [entry for entry in data if start_timestamp <= entry["timestamp"] <= end_timestamp]

    daily_pageviews = aggregate_daily_pageviews(filtered_data)
    avg_session_duration = compute_average_session_duration(filtered_data)
    bounce_rate = compute_bounce_rate(filtered_data)

    metrics = []

    for url, total_visits in daily_pageviews.items():
        metrics.append((
            url,
            total_visits,
            avg_session_duration,
            bounce_rate,
        ))

    return metrics


