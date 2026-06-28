# TODO: Add more country codes
country_codes = {
    "PH": "Philippines",
    "US": "United States",
    "CN": "China",
    "JPN": "Japan",
    "CAN": "Canada",
    "SG": "Singapore",
    "VN": "Vietnam",
    "KOR": "South Korea"
}
code = input("Enter country code:")

#Approach 1
if code not in country_codes:
    print("Key not Found")
else:
    print(country_codes[code])

#Approach 2
print(country_codes.get(code,"Unknown"))

