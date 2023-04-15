import os
import sys

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'site_proj.settings')
import django
django.setup()

import grpc
from concurrent import futures
import time
from analytics import data_processing
from analytics.grpc_generated import analytics_service_pb2, analytics_service_pb2_grpc
import datetime
from datetime import timedelta


class AnalyticsServiceServicer(analytics_service_pb2_grpc.AnalyticsServiceServicer):

    def __init__(self):
        pass

    def GetProcessedData(self, request, context):
        # Call data processing and analysis functions
        dummy_start_timestamp = datetime.datetime.now() - timedelta(days=30)
        dummy_end_timestamp = datetime.datetime.now()
        daily_metrics = data_processing.get_daily_metrics(dummy_start_timestamp, dummy_end_timestamp)

        # Convert the results into the response format defined in the .proto file
        response = analytics_service_pb2.ProcessedDataResponse()
        for url, total_visits, avg_session_duration, bounce_rate in daily_metrics:
            daily_metric = analytics_service_pb2.DailyMetric(url=url, total_visits=total_visits, avg_session_duration=avg_session_duration, bounce_rate=bounce_rate)
            response.daily_pageviews.append(daily_metric)

        response.average_session_duration = data_processing.get_average_session_duration(request.user_id)
        response.bounce_rate = data_processing.get_bounce_rate(request.user_id)

        return response

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    analytics_service_pb2_grpc.add_AnalyticsServiceServicer_to_server(AnalyticsServiceServicer(), server)
    server.add_insecure_port('[::]:50052')  
    server.start()
    print("Server started and listening on [::]:50052") 

    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    serve()
