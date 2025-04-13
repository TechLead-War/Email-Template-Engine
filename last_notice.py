import os
import django

# 1. Set Django settings module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "email_engine.settings")

# 2. Setup Django
django.setup()

# 3. Import your sample email sender
from email_engine.views import send_sample_problem_email, last_notice

# 4. Define recipient list

users = [
    {'user_email': 'kirtipant005@gmail.com'},
    {'user_email': 'sinhaatharva@gmail.com'},
    {'user_email': 'techhchacker@gmail.com'},
    {'user_email': 'mgrsb.gg@gmail.com'},
    {'user_email': 'fmy9036@gmail.com'},
    {'user_email': 'saurabhjoshi904@gmail.com'},
    {'user_email': 'himanshunainwal83@gmail.com'},
    {'user_email': 'aashishgupta1100@gmail.com'},
    {'user_email': 'hemukalouni99@gmail.com'},
    {'user_email': 'nitinvishwkarma12312@gmail.com'},
    {'user_email': 'savitaandola1@gmail.com'},
    {'user_email': 'deepaksinghburathoki2019@gmail.com'},
    {'user_email': 'deepanshupathak36@gmail.com'},
    {'user_email': 'arpitjoshi564@gmail.com'},
    {'user_email': 'gaurav133133@gmail.com'},
    {'user_email': 'kamalkoranga.gehu@gmail.com'},
    {'user_email': 'gauravsharma190156@gmail.com'},
    {'user_email': 'kp6615856@gmail.com'},
    {'user_email': 'bhaveshtripathi3112@gmail.com'},
    {'user_email': 'utpalsharma110@gmail.com'},
    {'user_email': 'ypandey700@gmail.com'},
    {'user_email': 'padaliaanjali8@gmail.com'},
    {'user_email': 'priyanshikathayat30@gmail.com'},
    {'user_email': 'devj12093@gmail.com'},
    {'user_email': 'baman2326@gmail.com'},
    {'user_email': 'chiragdwivediji@gmail.com'},
    {'user_email': 'anurag.p00000@gmail.com'},
    {'user_email': 'shravangupta061203@gmail.com'},
    {'user_email': 'adhikariannu44@gmail.com'},
    {'user_email': 'gauravsinghdanu04@gmail.com'},
    {'user_email': 'hridyanshsati4321@gmail.com'},
    {'user_email': 'mayankrawat415x@gmail.com'},
    {'user_email': 'devang.kandari@gmail.com'},
    {'user_email': 'shubhamkarmyal95@gmail.com'},
    {'user_email': 'devesh.khati01@gmail.com'},
    {'user_email': 'bishtgauravsingh299@gmail.com'},
    {'user_email': 'luckysteve521@gmail.com'},
    {'user_email': 'bishtrahul183777@gmail.com'},
    {'user_email': 'priyanshubisht.dev@gmail.com'},
    {'user_email': 'yachnapathak2616@gmail.com'},
    {'user_email': 'shankarbisht1224@gmail.com'},
    {'user_email': 'seemajoshi9536@gmail.com'},
    {'user_email': 'bishtdeepaksingh861@gmail.com'},
    {'user_email': 'bishtmayank770@gmail.com'},
    {'user_email': 'thakurnaula001@gmail.com'},
    {'user_email': 'samikshavaish76@gmail.com'},
    {'user_email': 'sauravsinghtilara@gmail.com'},
    {'user_email': 'Amitagarwalrkt@gmail.com'},
    {'user_email': 'tripathidiya673@gmail.com'},
    {'user_email': 'lokeshpaneru20508@gmail.com'},
    {'user_email': 'am7011793@gmail.com'},
    {'user_email': 'harshitapathak0123@gmail.com'},
    {'user_email': 'bankotisahil986@gmail.com'},
    {'user_email': 'dheerajkhetwal1599@gmail.com'},
    {'user_email': 'karanpreetsingh.gaba@gmail.com'},
    {'user_email': 'kavyaupreti971@gmail.com'},
    {'user_email': 'rahulkathayat2006@gmail.com'},
    {'user_email': 'rajaarav272@gmail.com'},
    {'user_email': 'dhruv16carter@gmail.com'},
    {'user_email': 'shivanibansal9928031918@gmail.com'},
    {'user_email': 'pm2984048@gmail.com'},
    {'user_email': 'lakshyajeetjalal@duck.com'},
    {'user_email': 'vishalbhatiya959@gmail.com'},
    {'user_email': 'nikhilkashyap263@gmail.com'},
    {'user_email': 'harshitjoshi1557@gmail.com'},
    {'user_email': 'pawangaria1998@gmail.com'},
    {'user_email': 'kamalkoranga13@proton.me'},
    {'user_email': 'ankitd9988@gmail.com'},
    {'user_email': 'surajsharma60923@gmail.com'},
    {'user_email': 'ionspider50@gmail.com'},
    {'user_email': 'maynku07@gmail.com'},
    {'user_email': 'Ankitbisht00011@gmail.com'},
    {'user_email': 'SHRAVANGUPTA.230413486@gehu.ac.in'},
    {'user_email': 'atulmaurya2204@gmail.com'},
    {'user_email': 'deveshkhati10@gmail.com'},
    {'user_email': 'iambishtrahul@gmail.com'},
    {'user_email': 'sachinn10293@gmail.com'},
    {'user_email': 'surjeetmaini.230112063@gehu.ac.in'},
    {'user_email': 'dakshjoshi3333@gmail.com'},
    {'user_email': 'kamleshkanwal999@gmail.com'},
    {'user_email': 'sharmaujjwal9920@gmail.com'},
    {'user_email': 'dineshdumka874@gmail.com'},
    {'user_email': 'ramandeepkaur071003@gmail.com'},
    {'user_email': 'rautelapriyank72@gmail.com'},
    {'user_email': 'divyanshu58374@gmail.com'},
    {'user_email': 'negi2350@gmail.com'},
    {'user_email': 'rajaarav272@gamil.com'},
]


# 5. Send sample problem emails
for user in users:
    last_notice(
        user_email=user["user_email"],
    )
