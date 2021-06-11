is_magician = False
is_expert = True

#check if magician and exper : "You  are a master magician"

#check if magician but not expert: "atleast you're getting there"

#check if you are not magician: "You need magic powers"

if is_magician and is_expert:
    print('You  are a master magician')
elif is_magician and not is_expert:
    print('atleast you are getting there')
elif not is_magician:
    print('You need magic powers')