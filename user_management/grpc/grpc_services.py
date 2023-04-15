from site_proj.protos import content_management_pb2, content_management_pb2_grpc
from ..models import CustomUser

class UserManagementServicer(content_management_pb2_grpc.UserManagementServicer):
    def CreateUser(self, request, context):
        # Create a new user using the CustomUser model with the information from the request
        user = CustomUser.objects.create_user(
            username=request.username,
            email=request.email,
            password=request.password
        )

        # Return a CreateUserResponse object with the user ID and a success message
        return content_management_pb2.CreateUserResponse(
            user_id=user.pk,
            message="User created successfully."
        )
