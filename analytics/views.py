from django.shortcuts import render
from .grpc.analytics_grpc_client import AnalyticsGRPCClient

def analytics(request):
    # Get the user ID from the request
    user_id = request.user.id

    # Check if user_id is not None and is of type int
    if user_id is None or not isinstance(user_id, int):
        return render(request, 'analytics/error.html', {"error": "Invalid user ID"})

    # Create a gRPC client and retrieve the processed data
    grpc_client = AnalyticsGRPCClient()
    processed_data = grpc_client.get_processed_data(user_id)

    # Check if the processed_data is not None
    if processed_data is None:
        return render(request, 'analytics/error.html', {"error": "Failed to retrieve data from the analytics service"})

    # Process the data and create visualizations using Plotly
    # ...

    # Extract the daily pageviews data from the response
    daily_pageviews = [
        {
            "url": metric.url,
            "total_views": metric.total_visits,
        }
        for metric in processed_data.daily_pageviews
    ]

    # Render the analytics dashboard with the extracted daily pageviews data
    context = {
        "daily_pageviews": daily_pageviews,
    }
    return render(request, 'analytics/dashboard.html', context)
