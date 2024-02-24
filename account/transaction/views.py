from django.shortcuts import render, get_object_or_404
from .models import Account, TransactionHistory
from rest_framework.views import APIView
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework import serializers
from django.views.decorators.cache import cache_page

from django.utils.decorators import method_decorator




class serializeTransaction(serializers.ModelSerializer):
    class Meta:
        model = TransactionHistory
        fields = ['id', 'withdraw', 'deposit', 'created_at']


# Create your views here.
class create_account(APIView):
    def post(self, request, format=None):
        '''
        create an account with the name and the balance sent from a form
        '''
        name = request.data.get('name')
        balance = request.data.get('balance')
        try:
            balance = float(balance)
        except Exception:
            return Response(f'Balance must be a number')
        new_account = Account.objects.create(name=name, balance=balance)
        return Response({'new_ccount': 
                                      { 'name': new_account.name,
                                          'balance': new_account.balance,
                                          'account_id': new_account.id}}, status=201)
    @method_decorator(cache_page(60*1))
    def get(self, request):
        '''
        get the full transaction history for that acount holder
        '''
        id = request.GET.get('id')
        obj = get_object_or_404(Account, pk=id)
        history = obj.transactionhistory_set.all()
        serial = serializeTransaction(history, many=True)

        return Response(serial.data)




class create_withdraw(APIView):
    '''
    with draw money from that account
    A signal is used to confirm that the amount withdrawn doesnt exceed the
    balance in the account, the signal also reduce the amount of money in the
    acount if the user if the withdraw succeseds
    '''
    def post(self, request, format=None):
        '''
        with draw from a user account
        '''
        id = request.data.get('account_id')
        account = get_object_or_404(Account, pk=id)
        withdraw = request.data.get('withdraw')
        try:
            withdraw=float(withdraw)
            trans=TransactionHistory(account=account, withdraw=withdraw)
            trans.save()
            return Response({'balance': trans.account.balance} ,201)
        except ValidationError:
            return Response(f'Insufficient balance to with {withdraw}')
        except Exception as e:
            return Response(f'{withdraw} must be a number', status=403)


class create_deposit(APIView):
    '''
    deposit money to the account of the user, a signal add the balance and the deposit
    '''
    def post(self, request, format=None):
        id = request.data.get('account_id')
        account = get_object_or_404(Account, pk=id)
        deposit = request.data.get('deposit')
        try:
            trans=TransactionHistory(account=account, deposit=float(deposit))
        except Exception:
            return Response('Deposit must be a number')
        trans.save()
        return Response({'balance': trans.account.balance} ,status=201)

