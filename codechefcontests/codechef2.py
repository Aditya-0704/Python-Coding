def get_grade(attendance, marks):
  """
  This function determines the grade awarded to Alice based on the 50-50 rule.

  Args:
      attendance: An integer representing Alice's attendance percentage.
      marks: An integer representing Alice's marks percentage.

  Returns:
      A string representing the grade awarded to Alice ("A", "F", or "Z").
  """

  if attendance < 50:
    return "Z"  # Attendance less than 50% results in a Z grade
  elif marks < 50:
    return "F"  # Marks less than 50% with attendance 50% or more results in an F grade
  else:
    return "A"  # All other cases qualify for an A grade

# Get the number of test cases
num_test_cases = int(input())

# Loop through each test case
for _ in range(num_test_cases):
  # Read attendance and marks
  attendance, marks = map(int, input().split())

  # Get the grade using the function
  grade = get_grade(attendance, marks)

  # Print the grade with a space after
  print(grade, end=" ")  # Add a space after each grade

# Print a newline at the end for proper formatting
print()  # Add a newline at the end
