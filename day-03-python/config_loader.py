try:
    number = int(input("Enter number: "))

except ValueError:
    print("Invalid number.")

else:
    print(f"Valid number: {number}")

finally:
    print("Input processing finished.")