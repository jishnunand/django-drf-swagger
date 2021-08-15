from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from rest_framework.generics import (CreateAPIView, DestroyAPIView,
                                     ListAPIView, RetrieveAPIView, RetrieveUpdateAPIView)

from .models import Tags as TagsModel, Assessment as AssessmentModel
from .serializers import TagSerializer, AssessmentSerializer


class TagsAPIView(APIView):
    """
    List all Tags, or create a new Tag.
    """
    def get(self, request):
        """
        Function will list all tags
        :param request:
        :return:
        """
        tags = TagsModel.objects.all()
        tag_serializer = TagSerializer(tags, many=True)
        return Response(tag_serializer.data)

    def post(self, request):
        """
        Function will help to create a new tag
        :param request:
        :return:
        """
        tag_serializer = TagSerializer(data=request.data)
        if tag_serializer.is_valid():
            tag_serializer.save()
            return Response(tag_serializer.data, status=status.HTTP_201_CREATED)
        return Response(tag_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AssessmentDetailListView(ListAPIView):
    """
    List/Search all Assessment Records
    """
    serializer_class = AssessmentSerializer
    queryset = AssessmentModel.objects.order_by('id').all()

    def get_queryset(self):
        """
        Filtering against tags based on query parameter in the URL.
        """
        queryset = AssessmentModel.objects.order_by('id').all()
        query = self.request.query_params.get('search')
        if query is not None:
            queryset = queryset.filter(tags__name=query)
        return queryset


class AssessmentCreateView(CreateAPIView):
    """
    Class used to create assessment
    """
    serializer_class = AssessmentSerializer
    queryset = AssessmentModel.objects.order_by('id').all()

    def perform_create(self, serializer):
        """
        Overrides the existing perform_create function to add tags to Assessment data
        :param serializer: AssessmentSerializer
        :return: dict
        """
        tags = self.request.data.get('tags', [])
        object = serializer.save()
        for each_tags in tags:
            try:
                tag = TagsModel.objects.get(name=each_tags)
                object.tags.add(tag)
            except TagsModel.DoesNotExist:
                pass


class AssessmentDetailView(RetrieveAPIView):
    """
    Get Detailed view of assessment data based on pk
    """
    queryset = AssessmentModel.objects.order_by('id').all()
    serializer_class = AssessmentSerializer

    lookup_field = "pk"
