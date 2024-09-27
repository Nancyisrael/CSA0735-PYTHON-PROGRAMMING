def caltax(income):
    if income<=150000:
        return "no tax"
    elif income<=300000:
        return income*0.10
    elif income<=500000:
        return income*0.20
    elif income>500000:
        return income*0.30
income=200000
print("TAX :",caltax(income))
