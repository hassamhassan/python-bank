class Bank(object):
    
    def __init__(self, amount, typ):
        self.Balance = amount
        self.account_type = typ
    def check_balance(self):
        print self.Balance
    def account_types(self):
        print "%s" % self.account_type
    def draw_money(self):
        print "how much money do u want to draw?"
        amount = int(raw_input(">"))
        self.Balance -= amount
        print "now you have only %s" %self.Balance," amount left in your account"
    def deposit_money(self):
        print "how much money do u want to deposit?"
        amount = int(raw_input(">"))
        self.Balance += amount
        print "now your Balance is %s" %self.Balance," amount in your account"
    def compare_account(self, acc2):
		comparison = cmp(int(self.Balance), int(acc2.Balance))
		if comparison == 0:
			print "account1 has equal balance in account2"
		elif comparison < 0:
			print "account1 has less balance than account2"
		else:
			print "account1 has more balance than account2"
    def transfer_funds(self, acc2):
        print "how much do you want to transfer?"
        amount_to_transfer = int(raw_input(">"))
        self.Balance -= amount_to_transfer
        acc2.Balance += amount_to_transfer
        print "balance in from account is %d"%self.Balance, " and balance in to account is %d"%acc2.Balance   
	
    
account1 = Bank(100000,"savings")
account2 = Bank(150000,"current")
account3 = Bank(150000,"current")
account1.account_types()
account2.account_types()
account1.check_balance()
account1.draw_money()
account1.deposit_money()
account1.compare_account(account2)
account2.compare_account(account1)
account2.compare_account(account3)
account2.transfer_funds(account1)

