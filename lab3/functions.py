def grams_to_ounces(grams):
    return grams / 28.349523125

def reverse_sentence(sentence):
    return ' '.join(sentence.split()[::-1])

def filter_prime(nums):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    return [n for n in nums if is_prime(n)]

def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False

def spy_game(nums):
    code = [0, 0, 7]
    index = 0
    for num in nums:
        if num == code[index]:
            index += 1
            if index == len(code):
                return True
    return False
