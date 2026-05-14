heart_rate = 135
zone = " "

if heart_rate >= 150:
    zone = "Max Zone"
elif  100<= heart_rate <= 149:
    zone = "Cardio Zone"
elif 60 <= heart_rate <= 99:
    zone = "Fat-Burning Zone"
elif  heart_rate < 60:
    zone = "Resting Zone"
else: 
    zone = "Low Zone"

# Testing
print("Your heart rate level is:", zone)