import os
import sys
import grpc
from concurrent import futures

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'site_proj.settings')

import django
django.setup()

from protos import content_management_pb2, content_management_pb2_grpc
from content_management.grpc.grpc_services import ContentManagementServicer
from user_management.grpc.grpc_services import UserManagementServicer

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    content_management_pb2_grpc.add_ContentManagementServicer_to_server(ContentManagementServicer(), server)
    content_management_pb2_grpc.add_UserManagementServicer_to_server(UserManagementServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("gRPC server started on port 50051.")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
