workout_duration = 45
message = ""

# Check if the workout duration is more than 60 minutes
if workout_duration>60:
    message = "Excellent job! You've worked out for over an hour!"
# Check if the workout duration is between 30 and 60 minutes
elif 30<=workout_duration<=60:
    message = "Great job! Keep it up!"
# If the workout duration is less than 30 minutes 
elif workout_duration<30:
    message = "Try to aim for at least 30 minutes of exercise."
else :
    message = "get on with your workout"
# Testing
print("Exercise feedback:", message)