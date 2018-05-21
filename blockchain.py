blockchain = [[1]]

def add_value(transaction_amount):
  blockchain.append([get_last_blockchain_value(), transaction_amount])
  print(blockchain)


def get_last_blockchain_value():
  blockchain[-1]


add_value(2)
add_value(0.9)
add_value(10.89)



