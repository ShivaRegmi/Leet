class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num == 1:
            return False
        divisors = 1
        i = 2
        while i * i <= num:
            if num % i == 0:
                divisors += i
                
                if i != num // i:
                    divisors += num // i
            i += 1

        return divisors == num