# Simple CLI Unit converter

# Kilometers into miles


def km_to_miles(km):
    miles = km / 1.6093
    return round(miles, 2)


# LBS into Kilograms


def lbs_to_kg(kg):
    return round((kg * 0.4535), 2)


# Seconds into Minutes


def sec_to_min(sec):
    return round((sec / 60), 2)


# °C into °F


def celcius_to_farenheit(celcius):
    return round(((celcius * 9 / 5) + 32), 2)


# Length conversion centimeters into inches


def cm_to_inches(cm):
    return round((cm / 2.54), 2)


# Currency conversion


def currency_conversion(inr):
    print("----- Currency Conversion -----")
    print("1. INR to USD")
    print("2. INR to Euro")
    currency_choice = int(input("Enter currency choice: "))
    if currency_choice == 1:
        conv = f"${round((inr*86.41),2)}/-"
        return conv
    elif currency_choice == 2:
        conv = f"€{round((inr*101.50),2)}/-"
        return conv
    else:
        print("INVALID CURRENCY CHOICE")


print("Choose a conversion: ")
print("1. LBS into Kilograms")
print("2. Kilometers into Miles")
print("3. Seconds into Minutes")
print("4. Celcius into Farenheit")
print("5. Centimeters into Inches")
print("6. Currency conversion")

choice = int(input("Enter your choice: "))

if choice == 1:
    kg = float(input("Enter weight in kilograms: "))
    print(f"{kg}kgs into lbs = {lbs_to_kg(kg)}lbs")

elif choice == 2:
    km = float(input("Enter distance in kilometers: "))
    print(f"{km}kms into miles = {km_to_miles(km)}miles")

elif choice == 3:
    sec = float(input("Enter time in seconds: "))
    print(f"{sec}secs into minutes = {sec_to_min(sec)}min")

elif choice == 4:
    celcius = float(input("Enter temperature in degree celcius: "))
    print(f"{celcius}°C into farenheit = {celcius_to_farenheit(celcius)}°F")

elif choice == 5:
    cm = float(input("Enter length in centimeters: "))
    print(f"{cm}cms into inches = {cm_to_inches(cm)}inches")

elif choice == 6:
    inr = float(input("Enter INR: "))
    print(f"₹{inr}/- conversion = {currency_conversion(inr)}")

else:
    print("x-- INVALID CHOICE --x")
