from faker import Faker

faker = Faker()


class GenerateCredentials:
    def generate_name():
        name = faker.name()
        return name

    def generate_email():
        random_digits = faker.random_int(min=100, max=999)
        email = f"lidia_chumbereva_32_{random_digits}@gmail.com"
        return email

    def generate_password():
        password = faker.password(length=8, special_chars=True)
        return password

    def generate_invalid_password():
        invalid_password = faker.password(length=4, special_chars=True)
        return invalid_password
