
from django.contrib import admin
from django.urls import path , include
import product_app.urls , company_app.urls , main_app.urls 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('sidal/', admin.site.urls),
    path('', include(main_app.urls) ),
    path('products/', include(product_app.urls) ),
    path('company/', include(company_app.urls) ),
] + static (settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)




    # path('admin/', admin.site.urls),
    # path('', )
    # path('air-comp/', include(aircompressor.urls) ),
    # path('jet-ink/', include(jetInk.urls) ),
    # path('stanles-steel/', include(steelStanless.urls) ),
    # path('water-investement/', include(waterInvestement.urls) ),