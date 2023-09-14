"""
Напишите класс BankAccount, имеющий следующие свойства и методы:

- __init__(self, balance): конструктор, принимающий начальный баланс счета
- balance: свойство, которое возвращает текущий баланс счета
- deposit(self, amount): метод, который позволяет внести деньги на счет
- withdraw(self, amount): метод, который позволяет снять деньги со счета
- close(self): метод, который закрывает счет и возвращает оставшиеся на нем деньги

Для свойства balance используйте декоратор @property.
"""


class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    @property
    def balance(self):
        '''это геттер для приватного атрибута balance'''
        return self.__balance
    @balance.setter
    def balance(self, balance):
        '''это сеттер для приватного атрибута balance'''
        self.__balance = balance

    @balance.deleter
    def balance(self):
        '''это делитер для приватного атрибута balance '''
        del self.__balance

    def deposit(self, amount):
        self.balance = self.balance + amount
        return self.balance

    def withdraw(self, amount):
        self.balance = self.balance - amount
        return self.balance

    def close(self):
        print(f'у вас на балансе  {self.balance}, получите пожалуйста')
        self.balance = self.balance - self.balance
        return self.balance

account = BankAccount(1000)
print(account.balance)  # 1000

account.deposit(500)
print(account.balance)  # 1500

account.withdraw(200)
print(account.balance)  # 1300

account.close()
print(account.balance)  # 0

#Здесь вопрос: метод close по идее должен вызывать наверное делитер?.. как это сделать, и что получится в результате?
