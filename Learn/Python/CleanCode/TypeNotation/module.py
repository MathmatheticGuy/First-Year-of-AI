'''
    #! Document right inside parameter instead of write it out for simple function (save time and cleaner code)
    #? Why Annotation -> More Readable, More Understandable, More Maintainable 
    #? Better for coding bot to understand the code
'''

#? This mean the function will take a list of type string and return a list of type string
def upper_everything(elements: list[str]) -> list[str]:
    return [element.upper() for element in elements]

#? func take a list of type int and return a list of type string
def number_to_letter(numbers: list[int]) -> list[str]:
    translate = {
        1: 'One',
        2: 'Two',
        3: 'Three',
        4: 'Four',
        5: 'Five'
    }
    
    # [print(number) for number in numbers]
    # translate[number] mean get the value of the key number in translate dictionary
    # e.g. translate[1] = 'One'
    return [translate[number] for number in numbers]


list_str = ['a', 'b', 'c']
# list_int = [1, 2, 3, 4, 5]

load_list: list[int] = [1, 2, 3, 'd', 'sfsf']  

def main():
    print(upper_everything(list_str)) # ['A', 'B', 'C']
    print(number_to_letter(load_list)) # ['One', 'Two', 'Three', 'Four', 'Five']
    
if __name__ == "__main__":
    main()