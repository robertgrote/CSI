#Description: Low Cost Mortage Loans for Couples Program
#Author: ROBERT GROTE
#Date: 8 February 2016

points=0

print 'This program screens for couples seeking low cost mortgage loans'
print'Couples need 5 points to qualify'

print 'For the applicants'
age_1=int(raw_input('Person One, Enter your age: '))
if age_1<23:
    print 'Sorry.', points, 'points. You did not qualify.' #stop the program if this happens
    quit() #okay to use quit? or should the shell keep running?
elif age_1>35:
    print 'Sorry.', points, 'points. You did not qualify.' #stop the program if this happens
    quit()
age_2=int(raw_input('Person Two, Enter your age: '))
if age_1>=25 and age_1<=30:
    if age_2>=23 and age_2<=35:
        points+=1
elif age_1>=23 and age_1<=35:
    if age_2>=25 and age_2<=30:
        points+=1
if points<1:
    print 'Sorry.', points, 'points. You did not qualify.' #stop the program if this happens
    quit()
    
print 'For the loan officer:'
median_home_price=float(raw_input('Enter the median price in dollars for homes in the area for the past twelve months: '))
print 'For the applicants'
marriage_time=int(raw_input('Enter the number of years that the couple has been connected in a marriage or civil union: '))
if marriage_time<=5 and marriage_time>=1:
    points+=1
if points<2:
    print 'Sorry.', points, 'points. You did not qualify.' #stop the program if this happens
    quit()

employ_time=raw_input('Both gainfully employed for 48 week, Y or N? ')
if employ_time.lower()=='y':
    points+=1
if points<3:
    print 'Sorry.', points, 'points. You did not qualify.' #stop the program if this happens
    quit()

home_price=float(raw_input('Enter the price, in dollars, of the home the couple is looking to buy: '))
if home_price<=(median_home_price-5000):
    points+=1
if points<4:
    print 'Sorry.', points, 'points. You did not qualify.' #stop the program if this happens
    quit()

print 'Enter credit scores. They must be between 300 and 850'
credit_score_1=int(raw_input("Enter person one's credit score: "))
credit_score_2=int(raw_input("Enter person two's credit score: "))
if credit_score_1>=300 and credit_score_1<=850 and credit_score_2>=300 and credit_score_2<=850:
    points+=1

if points<5:
    print 'Sorry.', points, 'points. You did not qualify.' #stop the program if this happens
    quit()

print 'Congratulations. You have qualified:', points, 'points'

print 'For the loan officer:'
present_interest_rate=float(raw_input('Please enter the present interest rate as a percent: '))

def rate(cred_score_1, cred_score_2, pres_rate):
    avg_score=(cred_score_1+cred_score_2)/2.0
    if avg_score>=800:
        discount=0.375
    elif avg_score>=775:
        discount=0.25
    elif avg_score>=750:
        discount=0.125
    else:
        discount=0
    final_rate=float(pres_rate-discount)
    return final_rate

print 'Your interest rate is ', rate(credit_score_1, credit_score_2, present_interest_rate) , '%'
