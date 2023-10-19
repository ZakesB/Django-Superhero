from django.urls import path
from .views import MyLoginView,SuperHeroListView, SuperHeroDetailView, SuperHeroCreateView, SuperHeroUpdateView

app_name = "legal"
urlpatterns = [
    path("", MyLoginView.as_view(), name='login'),
    path("superhero/", SuperHeroListView.as_view(), name="list"),
    path("superhero/<int:pk>/detail/", SuperHeroDetailView.as_view(), name="detail"),
    path("create/", SuperHeroCreateView.as_view(), name="add_superhero"),
    path("update/<int:pk>/", SuperHeroUpdateView.as_view(), name="update_superhero"),
]
