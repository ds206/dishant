options = [{"Gender": "Male", "HeightCm": 171, "WeightKg": 96 },{ "Gender": "Male", "HeightCm": 161, "WeightKg": 85 },{ "Gender": "Male", "HeightCm": 180, "WeightKg": 77 },{"Gender": "Female", "HeightCm": 166, "WeightKg": 62},{"Gender": "Female", "HeightCm": 150, "WeightKg": 70},{"Gender": "Female", "HeightCm": 167, "WeightKg": 82}]

#Table took as a dictionary
table_data = [{"BMI Category": "Underweight", "BMI Range (kg/m2)": "18.4 and below", "Health risk": "Malnutrition risk"},{ "BMI Category": "Normal weight", "BMI Range (kg/m2)": "18.5 - 24.9", "Health risk": "Low risk"},{ "BMI Category": "Overweight", "BMI Range (kg/m2)": "25 - 29.9", "Health risk": "Enhanced risk"},{ "BMI Category": "Moderately obese", "BMI Range (kg/m2)": "30 - 34.9", "Health risk": "Medium risk"},{"BMI Category": "Severely obese", "BMI Range (kg/m2)": "5 - 39.9", "Health risk": "High risk"},{"BMI Category": "Very severely obese", "BMI Range (kg/m2)": "40 and above", "Health risk": "Very high risk"}]

try:
    OverWeight = []
    for option in options:
        Height = int(option['HeightCm'])/100
        Weight = int(option['WeightKg'])
        BMI = Weight / Height

        for data in table_data:
            overweight_value = data['BMI Range (kg/m2)']
            starting_point_value = overweight_value.split()[0]
            ending_point_value = overweight_value.split()[-1]

            if "below" in ending_point_value:
                if float(starting_point_value) >= BMI:
                    print(data['Health risk']) #just for referencr
                    break

            elif "above" in ending_point_value:
                if float(starting_point_value) <= BMI:
                    print(data['Health risk']) #just for referencr
                    break

            else:
                if float(starting_point_value)<= BMI <= float(ending_point_value):
                    if data['BMI Category'] == 'Overweight':
                        OverWeight.append(BMI)
                        print("Overweight")
                        break

    total_number_of_overweight = len(OverWeight)
    print("Total Number of OverWeight :- ",total_number_of_overweight)

except Exception as e:
    print(e)
