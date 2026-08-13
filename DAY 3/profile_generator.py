# ==========================================
# Username & Profile Generator
# ==========================================

def generate_profile():
    print("Please enter the following details:")
    
    # Prompting the user for input
    name = input("Name   : ")
    age = input("Age    : ")
    city = input("City   : ")
    college = input("College: ")
    course = input("Course : ")
    
    # Displaying the formatted output profile
    print("\n" + "=" * 34)
    print("        STUDENT PROFILE")
    print("=" * 34 + "\n")
    
    print(f"Name    : {name}")
    print(f"Age     : {age}")
    print(f"City    : {city}")
    print(f"College : {college}")
    print(f"Course  : {course}")
    print("\n" + "=" * 34)

if __name__ == "__main__":
    generate_profile()