import grpc
from protos import content_management_pb2, content_management_pb2_grpc

def run():
    channel = grpc.insecure_channel('localhost:50051')
    stub = content_management_pb2_grpc.ContentManagementStub(channel)

    title = "Test Title"
    content = "This is a test content."
    author_id = 1

    response = stub.CreateTextContent(
        content_management_pb2.CreateTextContentRequest(title=title, content=content, author_id=author_id)
    )

    print("Response received:")
    print(f"Content ID: {response.content_id}")
    print(f"Message: {response.message}")

if __name__ == '__main__':
    run()
