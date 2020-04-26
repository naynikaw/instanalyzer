from igramscraper.instagram import Instagram

import pandas as pd

instagram = Instagram()

# authentication supported
instagram.with_credentials('naynikaaa','Naynika@123')
instagram.login(True)

insta_list = ['muskansaiyyad','anisha2323','styleupwith_joyee','kouchpotateaux','himani_jadeja','zsk_makeup','melaninrani','kritibali','soul_blushh','i_shambhavi_i','sincerelyxbhavi','alluringfashionistas','anisha2323','thatlibranstyleblog','marjoriemofficial','themagicalmona','fatema_m92','whifffoflife','amanpreetkeshri','ruch_0202','yashasvi.____.srivastava25','myglammworldd','___roshniraj___','kajaal_yadav','sathyakamala','thekaurblog','tanyaadvani','shruti_rana_makeovers','snehasakya','flappergurrl','camkary_karuna','saloniii_','prakratikush','kritika.kkakkar','fahablog','arfashahid','makeupbyyhuda','fizzahiqbalmua','_.fatimahussain._','brokegirlseries','saniaarshadblog','hoorina1dani','meenus_studio','maryammabbas_','girlwithbigdreams____','sanamunyr','minsa_hassan','glowonfleek_','komalmangiblog','sheikha_zunaira','reeshaholic','theblogcouture','bhowmickbarnanaofficial','takkymorningstar','mariaa.sarfraz','iamkhadijazubair._','thataveragehijabi','theayeshaz._','karwaanzindaagika','blogs_by_qurat','iamayeshasattar','kafilwarrah','ramsharafiq21','hijab_khaan','kaleidoscope_of_my_life','mahasmantraa','blogitwithamina','iqra_ky_blogs','glow.beeteakay_14','shriya_gupta21','shauryaasnani','eena_anand','anishagodhwani','bhaskarmehta','versatile_pride','gameofstyles_sneha','mensgrace','jagrutipriyadarshanidas','helldrop_','officialprincepardhan_','zahrasarfraz','mariyatariqblog','lazy_girls_diary','itayyabkamran','iamkhadijazubair._','kikixbae','mahinxblog','shamaal_umairr','sammansblog','fashionworldpk_','heresheblogs','d_mariable','dr.heebah','blogbyshiz','sanaaa_mirrr','styled_by_harmain','venturesofkarachiite','blogbysheeraz','vintagegirlxx','vlog.naina','flashesofdelight_by_adina','abbiekaxmi','ham_glam','agirlfromkashmir','makeupby_midhat','blogthisoutwithyumna','hello_tothe_necessities_blog','javeriablogs','zainabshahwarkhan']
n = len(insta_list)
titles = ['ID','Username','Full Name','Biography','Number of posts','Number of followers','Number of follows']
ID = []
username = []
fullname = []
bio = []
num_posts = []
num_followers = []
num_follows = []
#Getting an account by id
for i in range(25):
    account = instagram.get_account(insta_list[i])
    ID.append(account.identifier)
    username.append(account.username)
    fullname.append(account.full_name)
    bio.append(account.biography)
    num_posts.append(account.media_count)    
    num_followers.append(account.followed_by_count)
    num_follows.append(account.follows_count)
    

accounts_values = [ID, username, fullname, bio, num_posts, num_followers, num_follows]
result = list(zip(titles,accounts_values))
result1 = dict(result)
df1 = pd.DataFrame(result1)
print(df1)
df1.to_csv('C:\\Users\\nayni\\Documents\\Instagram project\\first_test.csv')
