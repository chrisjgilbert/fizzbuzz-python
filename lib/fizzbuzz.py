class FizzBuzz:

    def says(self, number):
        if self.__isDivisibleBy5(number):
            return 'Buzz'
        else:
            return 'Fizz'

    def __isDivisibleBy5(self, number):
        return True if number % 5 == 0 else False
