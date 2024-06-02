# Improve Usability
# -> You have a big function, you can seperate it to smaller functions



def check_age(age: int) -> bool:
    if age >= 18:
        return True
    else:
        return False
    
def check_id(has_id: bool) -> bool:
    if has_id:
        return True
    else:
        return False
    
def check_name(name: str) -> bool:
    if name == 'David':
        return False
    else:
        return True

def enter_club(name: str, age: int, has_id: bool) -> None:
    if check_age(age) == True:
        if check_id(has_id) == True:
            if check_name(name) == True:
                print("Welcome to the club")
            else:
                print("David are not allowed in the club")
        else:
            print("You need ID")
    else:
        print("Age Restricted")
            
# put function in main to improve readability (for clean code)
def main():
    enter_club("Nam", 19, True)

    
if __name__ == "__main__":
    main()
    

