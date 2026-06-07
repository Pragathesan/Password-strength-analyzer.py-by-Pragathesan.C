import string
import secrets

password=input('Enter a password')
score=0
feedback=[]
common=["password","123456","1234567890","0987654321","qwerty","abc123","password123","admin","letmein","welcome"]
score=max(score, 0)
def suggested_password(length=16):
    characters=string.ascii_letters+string.digits+string.punctuation
    return''.join(secrets.choice(characters) for _ in range(length))

if len(password)>=12:
    score+=1
else:
    feedback.append('too short-use at least 12 characters')
if any(c.isupper() for c in password):
    score+=1
else:
    feedback.append('add at least one uppercase letter')
if any(c.islower() for c in password):
    score+=1
else:
    feedback.append('Add at least one lowercase letter')
if any(n.isdigit() for n in password):
    score+=1
else:
    feedback.append('add at least one number')
if any(c in string.punctuation for c in password):
    score+=1
else:
    feedback.append('add at least one symbol')
if password.lower() in common:
    feedback.append('this is a commonly used password, avoid using this!')
    score-=1
if score<=2:
    strength='weak'
elif score==3:
    strength='medium'
else:
    strength='strong'
print(f'\nstrength: {strength} ({score}/5)')

if feedback:
    print('\nissues:')
    for item in feedback:
        print(f'-{item}')
print(f'\nsuggested Password: {suggested_password()}')

