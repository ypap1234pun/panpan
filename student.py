def main():
    student= get_student()
    print(f"{student['name']} from {student['house']}")

def get_student():
    
    name= input("Name: ")
    house  = input("house: ")
    return {"name":name,"house":house}

main()