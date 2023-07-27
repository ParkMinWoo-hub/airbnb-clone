from rest_framework.decorators import api_view
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.status import HTTP_204_NO_CONTENT
from .models import Category
from .serializers import CategorySereializer


# Create your views here.
@api_view(["GET", "POST"])
def categories(request):
    if request.method == "GET":
        all_categories = Category.objects.all()
        serializer = CategorySereializer(all_categories, many=True)
        return Response(
            {
                "ok": True,
                "categories": serializer.data,
            },
        )
    elif request.method == "POST":
        serializer = CategorySereializer(data=request.data)
        if serializer.is_valid():
            new_category = serializer.save()
            return Response(CategorySereializer(new_category).data)
        else:
            return Response(serializer.errors)


@api_view(["GET", "PUT", "DELETE"])
def category(request, pk):
    try:
        category = Category.objects.get(pk=pk)
    except Category.DoesNotExist:
        raise NotFound

    if request.method == "GET":
        serializer = CategorySereializer(category)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = CategorySereializer(
            category,
            data=request.data,
            partial=True,
        )
        if serializer.is_valid():
            update_category = serializer.save()
            return Response(CategorySereializer(update_category).data)
        else:
            return Response(serializer.errors)
    elif request.method == "DELETE":
        category.delete()
        return Response(status=HTTP_204_NO_CONTENT)
