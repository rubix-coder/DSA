from src.calculator import Calculator
from src.electrical import Electrical
TOOLS = ["calc", "power", "data"]

def calc():
    jpcalc = Calculator()
    opMap = {"add":jpcalc.add,
            "sub":jpcalc.sub}
    userrin = [int(x) for x in input("Enter numbers with space: ").split(" ")]
    userch = input("Enter the operator: add/sub: ")

    addition_res = opMap[userch](userrin)
    print(f"The {userch} result is {addition_res}")

def power():
    jpelec = Electrical()
    userrin = [int(x) for x in input("Enter Voltage and Current with space: ").split(" ")]
    power = jpelec.power(userrin)
    print(f"The calculated power is {power}W.")

if __name__=="__main__":
    usertool = input("Select the tool calc/power/data: ")
    assert usertool in TOOLS,"No such tool available"

    
    match usertool:
        case "calc":
            calc()
        case "power":
            power()
        case "data":
            print("YTI")
    