'''
The res array contains test results, i.e. the number of points between 0 and 100. 
Create a function f(fnc,res) that filters the test results according to the criteria contained in the fnc function. 
The f function returns the difference between the highest and lowest test result. Example:
res = [95,90,20,50,70] 
fnc1 = lambda x: x>50
f(fnc1,res)  25
fnc2 = lambda x: x>30 and x<90
f(fnc2,res)  20
'''
res = [95,90,20,50,70] 
fnc = lambda x: x>50

def f(fnc, res):
    filtered_results = list(filter(fnc, res))
    if not filtered_results:
        return 0
    return max(filtered_results) - min(filtered_results)


print(f(fnc,res))