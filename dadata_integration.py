from dadata import Dadata
from config import TOKEN, SECRET

# Инициализация клиента DaData
dadata = Dadata(TOKEN,SECRET)

def get_standardized_address(address):
    try:
        result = standardize(dadata.clean("address", address))
        return result
    except Exception as e:
        print(f"Ошибка при выполнении запроса к DaData: {e}")
        return {}

def standardize(data):
    insuredAddressData = {
        "area": data.get('area'),
        "city": data.get('region'),
        "flat": data.get('flat'),
        "block": data.get('block'),
        "house": data.get('house'),
        "okato": data.get('okato'),
        "stead": data.get('stead'),
        "region": data.get('region'),
        "street": data.get('street'),
        "country": data.get('country'),
        "fias_id": data.get('fias_id'),
        "kladr_id": data.get('kladr_id'),
        "city_area": data.get('city_area'),
        "city_type": data.get('region_type'),
        "flat_type": data.get('flat_type'),
        "block_type": data.get('block_type'),
        "house_type": data.get('house_type'),
        "settlement": data.get('settlement'),
        "postal_code": data.get('postal_code'),
        "city_fias_id": data.get('region_fias_id'),
        "flat_fias_id": data.get('flat_fias_id'),
        "house_cadnum": data.get('house_cadnum'),
        "area_kladr_id": data.get('area_kladr_id'),
        "city_district": data.get('city_district'),
        "city_kladr_id": data.get('region_kladr_id'),
        "house_fias_id": data.get('house_fias_id'),
        "city_with_type": data.get('region_with_type'),
        "flat_type_full": data.get('flat_type_full'),
        "house_kladr_id": data.get('house_kladr_id'),
        "region_fias_id": data.get('region_fias_id'),
        "street_fias_id": data.get('street_fias_id'),
        "block_type_full": data.get('block_type_full'),
        "house_type_full": data.get('house_type_full'),
        "region_kladr_id": data.get('region_kladr_id'),
        "street_kladr_id": data.get('street_kladr_id'),
        "federal_district": data.get('federal_district'),
        "region_with_type": data.get('region_with_type'),
        "street_with_type": data.get('street_with_type'),
        "settlement_fias_id": data.get('settlement_fias_id'),
        "settlement_kladr_id": data.get('settlement_kladr_id'),
        "settlement_with_type": data.get('settlement_with_type')
    }
    return insuredAddressData
