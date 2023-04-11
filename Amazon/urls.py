from django.urls import path
from Amazon.views import productIndexDB, productShowDB, productDeleteDB, \
    create_product, edit_product
urlpatterns = [
    path('db/index', productIndexDB, name='db.products.index'),
    path('db/<int:id>', productShowDB, name='db.products.show'),
    path('db/<int:id>/delete', productDeleteDB, name='db.products.delete'),
    path('db/create', create_product, name='db.products.create'),
    path('db/<int:id>/edit', edit_product, name='db.products.edit')



]