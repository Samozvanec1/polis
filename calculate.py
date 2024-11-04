import json
from dadata_integration import get_standardized_address

# Входные данные
email = "44444444@mail.ru"
phone = "+7 (911) 111-11-11"
markId = "59"
carYear = "2003"
modelId = "972"
category = "B"
markName = "Honda"
carNumber = "С111СС111"
modelName = "STREAM"
horsePower = "154.00"
policyDate = "27.05.2024"
useTrailer = True
dateDocument = "11.10.2022"
policyPeriod = "12"
checkboxOwner = True
lastNameOwner = "Тестов"
ownerBirthday = "01.04.1993"
targetOfUsing = "personal"
driverBirthday = ["01.04.1993", "04.05.2006"]
firstNameOwner = "Тест"
lastNameDriver = ["Тестов", "Тестовна"]
numberDocument = "666666"
prevPolicyDate = "30.04.2024"
serialDocument = "6666"
firstNameDriver = ["Тест", "Тест"]
insuredBirthday = "01.04.1993"
lastNameInsured = "Тестов"
middleNameOwner = "Тестович"
numberEDocument = ""
prevPolicyCheck = True
allowedMaxWeight = ""
firstNameInsured = "Тест"
middleNameDriver = ["Тестович", "Тестов"]
ownerAddress = "г Санкт-Петербург, Богатырский пр-кт, д 51 к 2, кв 144"
insuredAddress = "г Санкт-Петербург, Богатырский пр-кт, д 51 к 2, кв 144"
prevPolicyNumber = "444444444444"
prevPolicySerial = "ХХХ"
unlimitedDrivers = False
driverPrevLicence = [False, True]
middleNameInsured = "Тестович"
ownerPassportDate = "01.02.2014"
prevLastNameDriver = ["", "Тестовна"]
driverLicenceNumber = ["333333", "111111"]
driverLicenceSerial = ["2222", "4444"]
insuredPassportDate = "01.02.2014"
prevPolicyInsurance = "7468"
vehicleTypeDocument = "sertificate"
driverExperienceDate = ["04.02.2023", "24.05.2024"]
driverForeignLicence = ["", True]
ownerPassportIssuedBy = "ОТДЕЛОМ №2"
driverPrevLicenceNumber = ["", "234234"]
driverPrevLicenceSerial = ["", "4444"]
insuredPassportIssuedBy = "ОТДЕЛОМ №2"
ownerPassportUnitNumber = "550007"
registrationNumberBlank = False
driverCurrentLicenceDate = ["01.02.2023", "01.05.2024"]
driverPrevForeignLicence = [False, True]
insuredPassportUnitNumber = "550007"
ownerPassportNumberSerial = "5555555555"
vehicleIdentificationType = "vin"
vehiclePassengersCapacity = ""
driverForeignLicenceCountry = ["", "Южный Судан"]
insuredPassportNumberSerial = "5555555555"
vehicleIdentificationNumberVin = "AAAAA123123123AAA"
driverPrevForeignLicenceCountry = ["", "Танзания, Объединенная Республика"]
vehicleIdentificationNumberBody = ""
vehicleIdentificationNumberChassis = ""

data = {
    "email": email,
    "phone": phone,
    "markId": markId,
    "carYear": carYear,
    "modelId": modelId,
    "category": category,
    "markName": markName,
    "carNumber": carNumber,
    "modelName": modelName,
    "horsePower": horsePower,
    "policyDate": policyDate,
    "useTrailer": useTrailer,
    "dateDocument": dateDocument,
    "policyPeriod": policyPeriod,
    "checkboxOwner": checkboxOwner,
    "lastNameOwner": lastNameOwner,
    "ownerBirthday": ownerBirthday,
    "targetOfUsing": targetOfUsing,
    "driverBirthday": driverBirthday,
    "firstNameOwner": firstNameOwner,
    "lastNameDriver": lastNameDriver,
    "numberDocument": numberDocument,
    "prevPolicyDate": prevPolicyDate,
    "serialDocument": serialDocument,
    "firstNameDriver": firstNameDriver,
    "insuredBirthday": insuredBirthday,
    "lastNameInsured": lastNameInsured,
    "middleNameOwner": middleNameOwner,
    "numberEDocument": numberEDocument,
    "prevPolicyCheck": prevPolicyCheck,
    "allowedMaxWeight": allowedMaxWeight,
    "firstNameInsured": firstNameInsured,
    "middleNameDriver": middleNameDriver,
    "ownerAddress": ownerAddress,
    "insuredAddress": insuredAddress,
    "prevPolicyNumber": prevPolicyNumber,
    "prevPolicySerial": prevPolicySerial,
    "unlimitedDrivers": unlimitedDrivers,
    "driverPrevLicence": driverPrevLicence,
    "middleNameInsured": middleNameInsured,
    "ownerPassportDate": ownerPassportDate,
    "prevLastNameDriver": prevLastNameDriver,
    "driverLicenceNumber": driverLicenceNumber,
    "driverLicenceSerial": driverLicenceSerial,
    "insuredPassportDate": insuredPassportDate,
    "prevPolicyInsurance": prevPolicyInsurance,
    "vehicleTypeDocument": vehicleTypeDocument,
    "driverExperienceDate": driverExperienceDate,
    "driverForeignLicence": driverForeignLicence,
    "ownerPassportIssuedBy": ownerPassportIssuedBy,
    "driverPrevLicenceNumber": driverPrevLicenceNumber,
    "driverPrevLicenceSerial": driverPrevLicenceSerial,
    "insuredPassportIssuedBy": insuredPassportIssuedBy,
    "ownerPassportUnitNumber": ownerPassportUnitNumber,
    "registrationNumberBlank": registrationNumberBlank,
    "driverCurrentLicenceDate": driverCurrentLicenceDate,
    "driverPrevForeignLicence": driverPrevForeignLicence,
    "insuredPassportUnitNumber": insuredPassportUnitNumber,
    "ownerPassportNumberSerial": ownerPassportNumberSerial,
    "vehicleIdentificationType": vehicleIdentificationType,
    "vehiclePassengersCapacity": vehiclePassengersCapacity,
    "driverForeignLicenceCountry": driverForeignLicenceCountry,
    "insuredPassportNumberSerial": insuredPassportNumberSerial,
    "vehicleIdentificationNumberVin": vehicleIdentificationNumberVin,
    "driverPrevForeignLicenceCountry": driverPrevForeignLicenceCountry,
    "vehicleIdentificationNumberBody": vehicleIdentificationNumberBody,
    "vehicleIdentificationNumberChassis": vehicleIdentificationNumberChassis
}

def calculate_osago(data):
    email = data["email"]
    phone = data["phone"]
    markId = data["markId"]
    carYear = data["carYear"]
    modelId = data["modelId"]
    category = data["category"]
    markName = data["markName"]
    carNumber = data["carNumber"]
    modelName = data["modelName"]
    horsePower = data["horsePower"]
    policyDate = data["policyDate"]
    useTrailer = data["useTrailer"]
    dateDocument = data["dateDocument"]
    policyPeriod = data["policyPeriod"]
    checkboxOwner = data["checkboxOwner"]
    lastNameOwner = data["lastNameOwner"]
    ownerBirthday = data["ownerBirthday"]
    targetOfUsing = data["targetOfUsing"]
    driverBirthday = data["driverBirthday"]
    firstNameOwner = data["firstNameOwner"]
    lastNameDriver = data["lastNameDriver"]
    numberDocument = data["numberDocument"]
    prevPolicyDate = data["prevPolicyDate"]
    serialDocument = data["serialDocument"]
    firstNameDriver = data["firstNameDriver"]
    insuredBirthday = data["insuredBirthday"]
    lastNameInsured = data["lastNameInsured"]
    middleNameOwner = data["middleNameOwner"]
    numberEDocument = data["numberEDocument"]
    prevPolicyCheck = data["prevPolicyCheck"]
    allowedMaxWeight = data["allowedMaxWeight"]
    firstNameInsured = data["firstNameInsured"]
    middleNameDriver = data["middleNameDriver"]
    ownerAddress = data["ownerAddress"]
    insuredAddress = data["insuredAddress"]
    prevPolicyNumber = data["prevPolicyNumber"]
    prevPolicySerial = data["prevPolicySerial"]
    unlimitedDrivers = data["unlimitedDrivers"]
    driverPrevLicence = data["driverPrevLicence"]
    middleNameInsured = data["middleNameInsured"]
    ownerPassportDate = data["ownerPassportDate"]
    prevLastNameDriver = data["prevLastNameDriver"]
    driverLicenceNumber = data["driverLicenceNumber"]
    driverLicenceSerial = data["driverLicenceSerial"]
    insuredPassportDate = data["insuredPassportDate"]
    prevPolicyInsurance = data["prevPolicyInsurance"]
    vehicleTypeDocument = data["vehicleTypeDocument"]
    driverExperienceDate = data["driverExperienceDate"]
    driverForeignLicence = data["driverForeignLicence"]
    ownerPassportIssuedBy = data["ownerPassportIssuedBy"]
    driverPrevLicenceNumber = data["driverPrevLicenceNumber"]
    driverPrevLicenceSerial = data["driverPrevLicenceSerial"]
    insuredPassportIssuedBy = data["insuredPassportIssuedBy"]
    ownerPassportUnitNumber = data["ownerPassportUnitNumber"]
    registrationNumberBlank = data["registrationNumberBlank"]
    driverCurrentLicenceDate = data["driverCurrentLicenceDate"]
    driverPrevForeignLicence = data["driverPrevForeignLicence"]
    insuredPassportUnitNumber = data["insuredPassportUnitNumber"]
    ownerPassportNumberSerial = data["ownerPassportNumberSerial"]
    vehicleIdentificationType = data["vehicleIdentificationType"]
    vehiclePassengersCapacity = data["vehiclePassengersCapacity"]
    driverForeignLicenceCountry = data["driverForeignLicenceCountry"]
    insuredPassportNumberSerial = data["insuredPassportNumberSerial"]
    vehicleIdentificationNumberVin = data["vehicleIdentificationNumberVin"]
    driverPrevForeignLicenceCountry = data["driverPrevForeignLicenceCountry"]
    vehicleIdentificationNumberBody = data["vehicleIdentificationNumberBody"]
    vehicleIdentificationNumberChassis = data["vehicleIdentificationNumberChassis"]
    # Получение стандартизованного адреса с помощью DaData
    ownerAddressData = get_standardized_address(ownerAddress)
    insuredAddressData = get_standardized_address(insuredAddress)

    # Формирование JSON-объекта
    form_data = {
        "email": email,
        "phone": phone,
        "markId": markId,
        "carYear": carYear,
        "modelId": modelId,
        "category": category,
        "markName": markName,
        "carNumber": carNumber,
        "modelName": modelName,
        "horsePower": horsePower,
        "policyDate": policyDate,
        "useTrailer": useTrailer,
        "dateDocument": dateDocument,
        "policyPeriod": policyPeriod,
        "checkboxOwner": checkboxOwner,
        "lastNameOwner": lastNameOwner,
        "ownerBirthday": ownerBirthday,
        "targetOfUsing": targetOfUsing,
        "driverBirthday": driverBirthday,
        "firstNameOwner": firstNameOwner,
        "lastNameDriver": lastNameDriver,
        "numberDocument": numberDocument,
        "prevPolicyDate": prevPolicyDate,
        "serialDocument": serialDocument,
        "firstNameDriver": firstNameDriver,
        "insuredBirthday": insuredBirthday,
        "lastNameInsured": lastNameInsured,
        "middleNameOwner": middleNameOwner,
        "numberEDocument": numberEDocument,
        "prevPolicyCheck": prevPolicyCheck,
        "allowedMaxWeight": allowedMaxWeight,
        "firstNameInsured": firstNameInsured,
        "middleNameDriver": middleNameDriver,
        "ownerAddress": ownerAddress,
        "insuredAddress": insuredAddress,
        "ownerAddressData": ownerAddressData,
        "insuredAddressData": insuredAddressData,
        "prevPolicyNumber": prevPolicyNumber,
        "prevPolicySerial": prevPolicySerial,
        "unlimitedDrivers": unlimitedDrivers,
        "driverPrevLicence": driverPrevLicence,
        "middleNameInsured": middleNameInsured,
        "ownerPassportDate": ownerPassportDate,
        "prevLastNameDriver": prevLastNameDriver,
        "driverLicenceNumber": driverLicenceNumber,
        "driverLicenceSerial": driverLicenceSerial,
        "insuredPassportDate": insuredPassportDate,
        "prevPolicyInsurance": prevPolicyInsurance,
        "vehicleTypeDocument": vehicleTypeDocument,
        "driverExperienceDate": driverExperienceDate,
        "driverForeignLicence": driverForeignLicence,
        "ownerPassportIssuedBy": ownerPassportIssuedBy,
        "driverPrevLicenceNumber": driverPrevLicenceNumber,
        "driverPrevLicenceSerial": driverPrevLicenceSerial,
        "insuredPassportIssuedBy": insuredPassportIssuedBy,
        "ownerPassportUnitNumber": ownerPassportUnitNumber,
        "registrationNumberBlank": registrationNumberBlank,
        "driverCurrentLicenceDate": driverCurrentLicenceDate,
        "driverPrevForeignLicence": driverPrevForeignLicence,
        "insuredPassportUnitNumber": insuredPassportUnitNumber,
        "ownerPassportNumberSerial": ownerPassportNumberSerial,
        "vehicleIdentificationType": vehicleIdentificationType,
        "vehiclePassengersCapacity": vehiclePassengersCapacity,
        "driverForeignLicenceCountry": driverForeignLicenceCountry,
        "insuredPassportNumberSerial": insuredPassportNumberSerial,
        "vehicleIdentificationNumberVin": vehicleIdentificationNumberVin,
        "driverPrevForeignLicenceCountry": driverPrevForeignLicenceCountry,
        "vehicleIdentificationNumberBody": vehicleIdentificationNumberBody,
        "vehicleIdentificationNumberChassis": vehicleIdentificationNumberChassis
    }

    data = {
        "formData": form_data,
        "type": "osago"
    }


    # Преобразование словаря Python в JSON строку
    json_data = convert_boolean_values(data)
    json_data = json.dumps(json_data, ensure_ascii=False, indent=4)
    return json_data

def convert_boolean_values(json_data):
    def recursive_convert(data):
        if isinstance(data, dict):
            return {key: recursive_convert(value) for key, value in data.items()}
        elif isinstance(data, list):
            return [recursive_convert(item) for item in data]
        elif isinstance(data, str):
            if data.lower() == 'true':
                return True
            elif data.lower() == 'false':
                return False
            else:
                return data
        else:
            return data

    return recursive_convert(json_data)
# Вывод JSON строки

