 This app creates a banking app in django that allows the user to create account, deposit to the account, withdraw and aalso to view the transaction history

The app uses RESTFUL api to interact with database
Example of how to create account, deposit, view transaction history

## CREATE AN ACCOUNT with balance, the balanace is optional
curl -X POST http://127.0.0.1:8000/myapp/account/ -d 'name=dons' -d 'balance=3000'

This return and id of the account created 

#account_id":"270e39d5-b5d9-4731-8a42-740b37ae65a3"

## DEP0SIT INTO THE ACCOUNT
 curl -X POST http://127.0.0.1:8000/myapp/deposit/ -d "account_id=270e39d5-b5d9-4731-8a42-740b37ae65a3" -d 'deposit=35507.5'

## WITHDRAWWING FROM THE ACCOUNT
curl -X POST http://127.0.0.1:8000/myapp/withdraw/ -d "account_id=270e39d5-b5d9-4731-8a42-740b37ae65a3" -d 'withdraw=3071.5

## VIEW ALL THE TRANSACTION HISTORY
curl http://127.0.0.1:8000/myapp/account/?id=270e39d5-b5d9-4731-8a42-740b37ae65a3
