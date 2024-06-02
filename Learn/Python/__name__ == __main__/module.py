import time

def connect():
    print('Connecting...')
    time.sleep(1)
    print('You are Connected!')
    
        
def calc(x:int, y:float) -> float: # this does not change the function. It just show as notation
    if type(y) != float:
        return "y must be float"
    print(x + y) 

def main() -> None:
    connect()
    calc(2, 4.4)


# Whatever function inside this will not run when imported in another file (main.py)
if __name__ == '__main__':
    print('This is the main module')
    main()
    