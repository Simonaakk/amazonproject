class AlgorithmOfSixDigitNumber:
    def calculate(self, number) -> str:
        message = self.validateNumber(number)
        if message != "PASS":
            return message

        firstPart = number[:3]
        secondPart = number[3:]

        if self.calculatePartSum(firstPart) == self.calculatePartSum(secondPart):
            return "True"
        else:
            return "False"

    def calculate_part_sum(self, part):
        sum = 0
        for i in range(len(part)):
            sum +=int(part[i])
        return sum

    def validate_number(self, number):
        if len(str(number)) !=6:
            return "ERROR: Length of number should be 6"
        if not str(number).isdigit():
            return "ERROR: Number should contain only digits"
        return "PASS"

if __name__ == "__main__":
    ourProgramRunner = AlgorithmOfSixDigitNumber()
    myVar = input("Please, enter your number: ")
    print(ourProgramRunner.calculate(myVar))