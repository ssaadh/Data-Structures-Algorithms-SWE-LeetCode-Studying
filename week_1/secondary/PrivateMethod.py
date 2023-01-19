class PrivateMethod:
  def __init__(self):
    self.__secretKey = "MY_SOCIAL_SECURITY_NUMBER"

  def __privateMethod(self):
      return "SSN: " + self.__secretKey

  def privateMethod(self):
      return self.__privateMethod()

bankAcc = PrivateMethod()
print(bankAcc.privateMethod()) # -> MY_SOCIAL_SECURITY_NUMBER
#print(bankAcc.__privateMethod()) # fails with function not found error
#print(bankAcc.__secretKey) # fails with attribute not found error
print(bankAcc._PrivateMethod__privateMethod()) # -> MY_SOCIAL_SECURITY_NUMBER
print(bankAcc._PrivateMethod__secretKey) # -> MY_SOCIAL_SECURITY_NUMBER