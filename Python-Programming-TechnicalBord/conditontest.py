print('Question: if your age less than 18 then you cannot see this video. ')

client_age = int(input('What Is your age: '))

if (client_age <= 18):
    print('Your age is less than 18..')
else:
    print('You can see this video. but you need to pass some step. then you can entry here. i hope you are ready for next step:')
    client_terms = input("type yes for accepting all Term and conditions ")
    if(client_terms == "yes"):
        print('Wow you pass 2nd Rouned. Are you ready for next rouned?')
    else:
        print('Sorry we need to must true response for next path continue. i hope you could good . Thank You so much.')