def f(amount_to_pay):
    piec = amount_to_pay//5
    amount_to_pay = amount_to_pay - piec*5
    dwa = amount_to_pay//2
    amount_to_pay = amount_to_pay - dwa*2
    jeden = amount_to_pay
    return piec+dwa+jeden


