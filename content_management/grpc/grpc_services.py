from concurrent import futures
import grpc
from django.core.exceptions import ObjectDoesNotExist
from site_proj.protos import content_management_pb2, content_management_pb2_grpc
from ..models import TextContent
from user_management.models import CustomUser

class ContentManagementServicer(content_management_pb2_grpc.ContentManagementServicer):
    def CreateTextContent(self, request, context):
        try:
            author = CustomUser.objects.get(pk=request.author_id)
            content = TextContent.objects.create(
                title=request.title,
                content=request.content,
                author=author
            )
            return content_management_pb2.CreateTextContentResponse(
                content_id=content.pk,
                message="Text content created successfully."
            )
        except ObjectDoesNotExist:
            context.abort(grpc.StatusCode.NOT_FOUND, "Author not found.")
