# By Kami Bigdely
# Decompose conditional: You have a complicated conditional(if-then-else) statement. Extract
# methods from the condition, then part, and else part(s).

def make_alert_sound():
    print('made alert sound.')
def make_accept_sound():
    print('made acceptance sound')

ingredients = ['sodium benzoate']
toxins = ['sodium benzoate',  'sodium nitrate', 'sodium oxide']

for i in ingredients:
    if i in toxins:
        print('!!!')
        print('there is a toxin in the food!')    
        print('!!!')
        make_alert_sound()

print('***')
print('Toxin Free')
print('***')
make_accept_sound()