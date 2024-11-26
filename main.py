import requests as rq
from calculate import calculate_osago
from config import EMAIL_POLIS, PASSWORD_POLIS
import logging

logging.basicConfig(level=logging.INFO)


headers = {
    'accept': 'application/json',
    # requests won't add a boundary if this header is set when you pass files=
    # 'Content-Type': 'multipart/form-data',
}

files = {
    'email': (None, 'reist@test.com'),
    'password': (None, 'Qwerty123'),
}

response = rq.post('https://test-api.polis.online/api/signin', headers=headers, files=files)

print(response.text)
print(response.status_code)
print("")
access_token = response.json()['token']

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
dAta = calculate_osago(data)

headers = {
    'accept': 'application/json',
    'Authorization': 'Bearer ' + access_token,
    'Content-Type': 'application/json'

}



req = rq.post('https://test-api.polis.online/api/policy', headers=headers, json=dAta)
print(req.status_code)
print(req.text)

