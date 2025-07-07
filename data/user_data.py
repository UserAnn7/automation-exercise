class UserData:
    first_name = "Ann"
    last_name = "Skipor"
    company = "ITS"
    address = "Best street"
    address2 = "Best street2"
    state = "NY"
    city = "New York"
    zipcode = "02776"
    mobile_number = "+2345678990"
    email = "qwerty1234567@gmail.com"
    password = "1234"

    address_info = {
        'input[data-qa="first_name"]': first_name,
        'input[data-qa="last_name"]': last_name,
        'input[data-qa="company"]': company,
        'input[data-qa="address"]': address,
        'input[data-qa="address2"]': address2,
        'input[data-qa="state"]': state,
        'input[data-qa="city"]': city,
        'input[data-qa="zipcode"]': zipcode,
        'input[data-qa="mobile_number"]': mobile_number,
    }