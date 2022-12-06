from django.urls import path

from engineering import views

app_name = 'engineering'

urlpatterns = [
    path('create/ac_model/', views.CreateACModel.as_view(), name='ac_model_add'),
    path('create/effectivity/', views.CreateEffectivity.as_view(), name='effectivity_add'),
    path('create/ac/', views.CreateAC.as_view(), name='ac_add'),
    path('create/control/', views.CreateControl.as_view(), name='control_add'),
    path('create/rotable_pn/', views.CreateRotablePN.as_view(), name='rotable_pn_add'),
    path('create/repairable_pn/', views.CreateRepairablePN.as_view(), name='repairable_pn_add'),
    path('create/expendable_pn/', views.CreateExpendablePN.as_view(), name='expendable_pn_add')
]
