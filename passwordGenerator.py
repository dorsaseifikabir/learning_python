import random
import string


class PasswordGenerator:
    def __init__(self, length, uppercase, lowercase, numbers, special_characters):
        self.length = length
        self.uppercase = uppercase
        self.lowercase = lowercase
        self.numbers = numbers
        self.special_characters = special_characters

#     def your_choice(self):
#         print(f"""length: {self.length}
# uppercase: {self.uppercase}
# lowercase: {self.lowercase}
# numbers: {self.numbers}
# special character: {self.special_characters}
# """)

    def generate(self):
        password = ''
        count = 0
        action_list = []

        def random_upper():
            rand_upper = random.choice(string.ascii_uppercase)
            return rand_upper

        def random_lower():
            rand_lower = random.choice(string.ascii_lowercase)
            return rand_lower

        def random_number():
            rand_num = str(random.randint(1, 9))
            return rand_num

        def random_special_char():
            rand_char = random.choice("!@#$%^&*")
            return rand_char

        if self.uppercase:
            password += random_upper()
            action_list.append(random_upper)
            count += 1

        if self.lowercase:
            password += random_lower()
            action_list.append(random_lower)
            count += 1

        if self.numbers:
            password += random_number()
            action_list.append(random_number)
            count += 1

        if self.special_characters:
            password += random_special_char()
            action_list.append(random_special_char)
            count += 1

        for i in range(0, self.length - count):
            password += random.choice(action_list)()

        shuffled_password = "".join(random.sample(password, len(password)))
        return shuffled_password
