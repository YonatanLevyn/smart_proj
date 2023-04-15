import grpc
from analytics.grpc_generated import analytics_service_pb2, analytics_service_pb2_grpc

class AnalyticsGRPCClient:
    def __init__(self, host="localhost", port="50052"):
        # Initialize the gRPC channel and stub
        self.channel = grpc.insecure_channel(f"{host}:{port}")
        self.stub = analytics_service_pb2_grpc.AnalyticsServiceStub(self.channel)
    
    def get_processed_data(self, user_id):
        print(f"user_id: {user_id}")

        # Create the request object
        request = analytics_service_pb2.ProcessedDataRequest(
            user_id=int(user_id)
        )

        try:
            # Send the request and get the response
            response = self.stub.GetProcessedData(request)
            return response
        except grpc.RpcError as e:
            print(f"An error occurred while getting processed data: {e}")
            return None

    def close(self):
        # Close the gRPC channel
        self.channel.close()
