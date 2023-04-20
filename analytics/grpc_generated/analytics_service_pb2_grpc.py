# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import analytics_service_pb2 as analytics__service__pb2


class AnalyticsServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ProcessEvent = channel.unary_unary(
                '/analytics_service.AnalyticsService/ProcessEvent',
                request_serializer=analytics__service__pb2.AnalyticsEvent.SerializeToString,
                response_deserializer=analytics__service__pb2.EventProcessingResponse.FromString,
                )
        self.GetDailyMetrics = channel.unary_unary(
                '/analytics_service.AnalyticsService/GetDailyMetrics',
                request_serializer=analytics__service__pb2.DailyMetricsRequest.SerializeToString,
                response_deserializer=analytics__service__pb2.DailyMetricsResponse.FromString,
                )
        self.GetProcessedData = channel.unary_unary(
                '/analytics_service.AnalyticsService/GetProcessedData',
                request_serializer=analytics__service__pb2.ProcessedDataRequest.SerializeToString,
                response_deserializer=analytics__service__pb2.ProcessedDataResponse.FromString,
                )


class AnalyticsServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def ProcessEvent(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetDailyMetrics(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetProcessedData(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_AnalyticsServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ProcessEvent': grpc.unary_unary_rpc_method_handler(
                    servicer.ProcessEvent,
                    request_deserializer=analytics__service__pb2.AnalyticsEvent.FromString,
                    response_serializer=analytics__service__pb2.EventProcessingResponse.SerializeToString,
            ),
            'GetDailyMetrics': grpc.unary_unary_rpc_method_handler(
                    servicer.GetDailyMetrics,
                    request_deserializer=analytics__service__pb2.DailyMetricsRequest.FromString,
                    response_serializer=analytics__service__pb2.DailyMetricsResponse.SerializeToString,
            ),
            'GetProcessedData': grpc.unary_unary_rpc_method_handler(
                    servicer.GetProcessedData,
                    request_deserializer=analytics__service__pb2.ProcessedDataRequest.FromString,
                    response_serializer=analytics__service__pb2.ProcessedDataResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'analytics_service.AnalyticsService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class AnalyticsService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def ProcessEvent(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/analytics_service.AnalyticsService/ProcessEvent',
            analytics__service__pb2.AnalyticsEvent.SerializeToString,
            analytics__service__pb2.EventProcessingResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetDailyMetrics(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/analytics_service.AnalyticsService/GetDailyMetrics',
            analytics__service__pb2.DailyMetricsRequest.SerializeToString,
            analytics__service__pb2.DailyMetricsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetProcessedData(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/analytics_service.AnalyticsService/GetProcessedData',
            analytics__service__pb2.ProcessedDataRequest.SerializeToString,
            analytics__service__pb2.ProcessedDataResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)