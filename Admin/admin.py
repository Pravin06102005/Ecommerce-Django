from Admin.address_master.models import stateModel
from Admin.category.models import categoryModel
from Admin.product.models import productModel
from Admin.slider.models import GalleryModel
from django.contrib import admin

admin.site.register(stateModel)
admin.site.register(categoryModel)
admin.site.register(productModel)
admin.site.register(GalleryModel)


def has_superuser_permission(request):
    return request.user.is_active and request.user.is_superuser


# Only active superuser can access root admin site (default)
admin.site.has_permission = has_superuser_permission
