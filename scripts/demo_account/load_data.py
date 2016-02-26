#!/usr/bin/env python
# must run on a clean empty db

# init
import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "site_repo.settings")
os.environ["DJANGO_SETTINGS_MODULE"] = "site_repo.settings"
django.setup()

# users
from site_repo.apps.users.API import register_user
from site_repo.apps.accounts.models import Account
from site_config.secrets import Duser1,Duser2
Duser1['account_code'] = ""
register_user(**Duser1)
account_code = Account.objects.get(pk=1).account_code
Duser2['account_code'] = account_code
register_user(**Duser2)

# expenses
import datetime
from itertools import cycle
from django.contrib.auth.models import User
from site_repo.apps.expenses.models import Expense
from site_repo.tests.load_data.data2 import expenses

Lpurchased_on = [
    (1,02),(1,05),(1,12),(1,16),(1,22),(1,24),(1,28),
    (2,1),(2,10),(2,12),(2,18),(2,26),
    (3,2),(3,8)]

Lmonth_balanced = [1,1,1,1,1,1,1,2,2,2,2,2,3,3]

users = {
    'user1':User.objects.get(username=Duser1['username']),
    'user2':User.objects.get(username=Duser2['username'])}
owners = cycle(['user1','user2'])

for m in range(len(expenses)):
        
        expense_tuple = expenses[m]
        purchased_on = Lpurchased_on[m]
        e = Expense(
                owner=users[owners.next()],
                date_purchased=datetime.date(2016,purchased_on[0],purchased_on[1]),
                expense_sum=expense_tuple[0],
                expense_divorcee_participate=expense_tuple[1],
                month_balanced=Lmonth_balanced[m],
                year_balanced=2016,
                desc=expense_tuple[2],
                place_of_purchase=expense_tuple[3],
                notes=expense_tuple[4])
        e.save()    
    


    

