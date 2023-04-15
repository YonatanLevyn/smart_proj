import grpc
from site_proj.protos import content_management_pb2, content_management_pb2_grpc

# Function to create text content using the gRPC ContentManagement service
def create_text_content(author_id, title, content):
    # Set up a channel to the gRPC server at 'localhost:50051'
    channel = grpc.insecure_channel('localhost:50051')
    
    # Create a stub (client) using the ContentManagementStub
    stub = content_management_pb2_grpc.ContentManagementStub(channel)

    # Create a request object with the required parameters
    request = content_management_pb2.CreateTextContentRequest(
        author_id=author_id,
        title=title,
        content=content
    )

    # Send the request to the gRPC server using the stub and get the response
    response = stub.CreateTextContent(request)
    
    # Return the response object
    return response

# Function to create a user using the gRPC UserManagement service
def create_user(username, email, password):
    # Set up a channel to the gRPC server at 'localhost:50051'
    with grpc.insecure_channel('localhost:50051') as channel:
        # Create a stub (client) using the UserManagementStub
        stub = content_management_pb2_grpc.UserManagementStub(channel)
        
        # Create a request object with the required parameters
        request = content_management_pb2.CreateUserRequest(
            username=username,
            email=email,
            password=password
        )

        # Send the request to the gRPC server using the stub and get the response
        response = stub.CreateUser(request)
    
    # Return the response object
    return response
