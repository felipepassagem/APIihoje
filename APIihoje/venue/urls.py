from django.urls import path
from venue import views  # Importe as visualizações do aplicativo "venues"


urlpatterns = [
    path('venues/', views.VenueList.as_view(), name='venue-list'),  # Rota para listar estabelecimentos
    path('venues/<int:pk>/', views.VenueDetail.as_view(), name='venue-detail'),  # Rota para detalhes de um estabelecimento
    path('venues/create/', views.CreateVenue.as_view(), name='create-venue'),  # Rota para criar um estabelecimento
    path('venues/<int:pk>/update/', views.UpdateVenue.as_view(), name='update-venue'),  # Rota para atualizar um estabelecimento
    path('venues/<int:pk>/delete/', views.DeleteVenue.as_view(), name='delete-venue'),  # Rota para excluir um estabelecimento
    # Outras rotas, se necessário
]