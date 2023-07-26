from django.contrib import admin
from .models import Review


class WordFilter(admin.SimpleListFilter):
    title = "Filter by words!"
    parameter_name = "word"

    def lookups(self, request, model_admin):
        return [
            ("good", "Good"),
            ("great", "Great"),
            ("awesome", "Awesome"),
        ]

    def queryset(self, request, reviews):
        word = self.value()
        if word:
            return reviews.filter(payload__contains=word)
        else:
            return reviews


class RatingFilter(admin.SimpleListFilter):
    title = "Filter by rating"
    parameter_name = "rating"

    def lookups(self, request, model_admin):
        return [
            ("gte3", ">=3"),
            ("lt3", "<3"),
        ]

    def queryset(self, request, reviews):
        word = request.GET.get("rating")
        if word == "gte3":
            return reviews.filter(rating__gte=3)
        elif word == "lt3":
            return reviews.filter(rating__lt=3)
        else:
            return reviews


# Register your models here.
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        "__str__",
        "payload",
    )
    list_filter = (
        WordFilter,
        RatingFilter,
        "rating",
        "user__is_host",
        "room__category",
        "room__pet_friendly",
    )
