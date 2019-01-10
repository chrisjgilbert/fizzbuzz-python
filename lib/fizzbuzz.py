class FizzBuzz:

    def says(self, number):
        if self.__isDivisibleBy15(number):
            return 'FizzBuzz'
        elif self.__isDivisibleBy5(number):
            return 'Buzz'
        else:
            return 'Fizz'

    def __isDivisibleBy5(self, number):
        return True if number % 5 == 0 else False

    def __isDivisibleBy15(self, number):
        return True if number % 15 == 0 else False
