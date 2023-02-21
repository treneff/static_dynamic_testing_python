### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:


  def check_for_ace(self, card):
  # use comparison operator instead of an assigment operator
    if card.value = 1:
      return True
  # missing colon from else statement
    else
      return False
   
  # typo in declaring the name of the method- should be def instead of dif
  # missing comma between card1 and card2
  dif highest_card(self, card1 card2):
  if card1.value > card2.value:
    # the statement returns card instead of card1
    return card
  else:
    return card2
  


def cards_total(self, cards):
  # the total variable is never initialized
  total
  for card in cards:
    total += card.value
  # indentation of the return statement is not in the correct place
    return "You have a total of" + total
  
```
