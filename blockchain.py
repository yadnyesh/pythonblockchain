blockchain = [10]

def get_last_blockchain_value():
  return blockchain[-1]

def add_value(transaction_amount, last_transaction=get_last_blockchain_value()):
  blockchain.append([last_transaction, transaction_amount])
  print(blockchain)


add_value(2, [1])
add_value(0.9, get_last_blockchain_value())
add_value(10.89, get_last_blockchain_value())



