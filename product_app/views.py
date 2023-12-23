from django.shortcuts import render
from .models import *

def products(request):
    view_RotaryScrewCompressor = RotaryScrewCompressor.objects.all()
    view_ReciprocatingCompressor = ReciprocatingCompressor.objects.all()
    view_ScrollCompressor = ScrollCompressor.objects.all()
    view_TurboCompressor = TurboCompressor.objects.all()
    view_AirDryerEquipement = AirDryerEquipement.objects.all()
    view_FilterEquipement = FilterEquipement.objects.all()
    view_AirReceiverEquipement = AirReceiverEquipement.objects.all()
    view_NitrogenGeneratorEquipement = NitrogenGeneratorEquipement.objects.all()
    view_DODInkJet = DODInkJet.objects.all()
    view_CIJInkJet = CIJInkJet.objects.all()
    view_TIJInkJet = TIJInkJet.objects.all()
    view_LaserMarkingInkJet = LaserMarkingInkJet.objects.all()
    view_SteelStanless = SteelStanless.objects.all()
    view_WaterInvesemetEquipement = WaterInvesemetEquipement.objects.all()
    view_WaterInvesemetSystem = WaterInvesemetSystem.objects.all()
    product_context = { 'html_RotaryScrewCompressor':view_RotaryScrewCompressor,
                        'html_ReciprocatingCompressor':view_ReciprocatingCompressor,
                        'html_ScrollCompressor':view_ScrollCompressor,
                        'html_TurboCompressor':view_TurboCompressor,
                        'html_AirDryerEquipement':view_AirDryerEquipement,
                        'html_FilterEquipement':view_FilterEquipement,
                        'html_AirReceiverEquipement':view_AirReceiverEquipement,
                        'html_NitrogenGeneratorEquipement':view_NitrogenGeneratorEquipement,
                        'html_DODInkJet':view_DODInkJet,
                        'html_CIJInkJet':view_CIJInkJet,
                        'html_TIJInkJet':view_TIJInkJet,
                        'html_LaserMarkingInkJet':view_LaserMarkingInkJet,
                        'html_SteelStanless':view_SteelStanless,
                        'html_WaterInvesemetEquipement':view_WaterInvesemetEquipement,
                        'html_WaterInvesemetSystem':view_WaterInvesemetSystem,}
 
    return render(request,'products/products.html',product_context)


def air_Compressor(request):
    view_RotaryScrewCompressor = RotaryScrewCompressor.objects.all()
    view_ReciprocatingCompressor = ReciprocatingCompressor.objects.all()
    view_ScrollCompressor = ScrollCompressor.objects.all()
    view_TurboCompressor = TurboCompressor.objects.all()
    view_AirDryerEquipement = AirDryerEquipement.objects.all()
    view_FilterEquipement = FilterEquipement.objects.all()
    view_AirReceiverEquipement = AirReceiverEquipement.objects.all()
    view_NitrogenGeneratorEquipement = NitrogenGeneratorEquipement.objects.all()
    
    air_Compressor_context = { 'html_RotaryScrewCompressor':view_RotaryScrewCompressor,
                               'html_ReciprocatingCompressor':view_ReciprocatingCompressor,
                               'html_ScrollCompressor':view_ScrollCompressor,
                               'html_TurboCompressor':view_TurboCompressor,
                               'html_AirDryerEquipement':view_AirDryerEquipement,
                               'html_FilterEquipement':view_FilterEquipement,
                               'html_AirReceiverEquipement':view_AirReceiverEquipement,
                               'html_NitrogenGeneratorEquipement':view_NitrogenGeneratorEquipement
                            }
 
    return render(request,'products/air_Compressor.html',air_Compressor_context)



def water_Investement(request):
    view_WaterInvesemetEquipement = WaterInvesemetEquipement.objects.all()
    view_WaterInvesemetSystem = WaterInvesemetSystem.objects.all()
    water_Investement_context = {'html_WaterInvesemetEquipement':view_WaterInvesemetEquipement,
                                 'html_WaterInvesemetSystem':view_WaterInvesemetSystem
                                 }
 
    return render(request,'products/water_Investement.html',water_Investement_context)



def jet_Ink(request):
    view_DODInkJet = DODInkJet.objects.all()
    view_CIJInkJet = CIJInkJet.objects.all()
    view_TIJInkJet = TIJInkJet.objects.all()
    view_LaserMarkingInkJet = LaserMarkingInkJet.objects.all()
    jet_Ink_context = { 'html_DODInkJet':view_DODInkJet,
                        'html_CIJInkJet':view_CIJInkJet,
                        'html_TIJInkJet':view_TIJInkJet,
                        'html_LaserMarkingInkJet':view_LaserMarkingInkJet,
                        }
 
    return render(request,'products/jet_Ink.html',jet_Ink_context)


def steel_Stanless(request):
    view_SteelStanless = SteelStanless.objects.all()
    steel_Stanless_context = {'html_SteelStanless':view_SteelStanless}
    return render(request,'products/steel_Stanless.html',steel_Stanless_context)

