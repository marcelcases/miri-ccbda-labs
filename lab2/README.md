# Lab session #2: Doors in the Cloud

## About

**Course**  
Cloud Computing and Big Data Analytics  (CCBDA-MIRI)  
FIB - Universitat Politècnica de Catalunya. BarcelonaTech  
March 2021

**Team**  
* Zofia Tarant
<zofia.tarant@estudiantat.upc.edu>
* Marcel Cases
<marcel.cases@estudiantat.upc.edu>

## Task 2.1: Getting Started with NLTK
### 2.1.1 Word Count 1
```bash
[('the', 1343), (',', 1251), ('.', 810), (')', 638), ('(', 637), ('of', 586), ('to', 491), ('a', 470), (':', 454), ('in', 417)]
25187
```
### 2.1.2 Remove punctuation
```bash
[('the', 1444), ('of', 586), ('to', 531), ('in', 506), ('a', 481), ('and', 346), ('is', 289), ('we', 279), ('that', 275), ('this', 268)]
19593
```

### 2.1.3 Stop Words
**Q213a: Why "Tensorflow" is not the most frequent word? Which are the Stop Words?**  
"TensorFlow" is not the most frequent word because it us used much less frequently
than prepositions or pronouns etc. - i.e. stop words.

*Stop words* are the words that are used
very frequently but do not carry much information. They are usually removed from
the set of the tokens - it is one of the most important steps of NLP. Once they
are filtered out, we can continue working with data that is more relevant.

```bash
[('tensorflow', 193), ('data', 102), ('tensor', 99), ('code', 90), ('learning', 81), ('function', 74), ('one', 73), ('use', 65), ('example', 64), ('available', 63)]
11220
```

## Task 2.2: Getting Started with ```tweepy```
### 2.2.1 Accessing your Twitter account information
First of, we install ```tweepy``` into our local machine. After adding the repository 
```C:\ProgramData\Anaconda3\Scripts\conda.exe config --append channels conda-forge``` 
to our system and installing SSL certificates ```libcrypto``` and ```libssl``` on the ```conda``` environment, 
```tweepy``` was installed properly.  

Then we have generated Consumer Keys and Authentication Tokens for a 
Twitter account, using an **OAuth 2.0 Bearer Token**. After these keys 
have been generated, we set it up to the OS by running 
the following script:
```python
import os
os.environ["CONSUMER_KEY"] = "xxxxx"
os.environ["CONSUMER_SECRET"] = "xxxxx"
os.environ["ACCESS_TOKEN"] = "xxxxx"
os.environ["ACCESS_SECRET"] = "xxxxx"
```

When all OAuth keys have been set up, we have run the script 
contained on ```Twitter_1.py``` and we have retrieved
the information:
```bash
Name: Marcel Cases
Location: 
Followers: 339
Created: 2010-05-09 16:51:14
Description: Estudio a la @fib_upc. Twits sobre tecnologia, AI, math, EVs, ciclisme, Human Rights | Supporter of all nations deprived of rights
```

**Q221: Is the data printed correctly? Is it yours?**  
The data retrieved from this personal Twitter account is printed correctly 
and up to date.


### 2.2.2: Accessing Tweets
We use ```Twitter_2.py``` to contain the scripts to access tweets 
and show information.  

We can read our own Twitter home timeline, limiting the number of showed tweets to 1. 
As an example, the script below
```python
for status in tweepy.Cursor(api.home_timeline).items(1):
    print(status.text)
```

shows that the most recent tweet is the following:
```bash
Una comunicació amb perspectiva de gènere i més èmfasi en el paper de la dona en les finances, part del pla d'… https://t.co/Bf6nprAuxS
```

We can also obtain metadata of the latest tweet in ```json``` format:
```json
{
  "created_at": "Thu Mar 04 18:07:46 +0000 2021",
  "id": 1367537264780271621,
  "id_str": "1367537264780271621",
  "text": "Una comunicaci\u00f3 amb perspectiva de g\u00e8nere i m\u00e9s \u00e8mfasi en el paper de la dona en les finances, part del pla d'\u2026 https://t.co/Bf6nprAuxS",
  "truncated": true,
  "entities": {
    "hashtags": [],
    "symbols": [],
    "user_mentions": [],
    "urls": [
      {
        "url": "https://t.co/Bf6nprAuxS",
        "expanded_url": "https://twitter.com/i/web/status/1367537264780271621",
        "display_url": "twitter.com/i/web/status/1\u2026",
        "indices": [
          112,
          135
        ]
      }
    ]
  },
  "source": "<a href=\"https://www.echobox.com\" rel=\"nofollow\">Echobox</a>",
  "in_reply_to_status_id": null,
  "in_reply_to_status_id_str": null,
  "in_reply_to_user_id": null,
  "in_reply_to_user_id_str": null,
  "in_reply_to_screen_name": null,
  "user": {
    "id": 1204681459,
    "id_str": "1204681459",
    "name": "VIA Empresa",
    "screen_name": "VIAEmpresa",
    "location": "Catalunya",
    "description": "El diari econ\u00f2mic i empresarial l\u00edder en catal\u00e0. Grup Totmedia | Twitter en castell\u00e0: @VIAEmpresa_es Segueix-nos!",
    "url": "https://t.co/CWESikyRtf",
    "entities": {
      "url": {
        "urls": [
          {
            "url": "https://t.co/CWESikyRtf",
            "expanded_url": "http://www.viaempresa.cat",
            "display_url": "viaempresa.cat",
            "indices": [
              0,
              23
            ]
          }
        ]
      },
      "description": {
        "urls": []
      }
    },
    "protected": false,
    "followers_count": 17907,
    "friends_count": 681,
    "listed_count": 619,
    "created_at": "Thu Feb 21 13:05:55 +0000 2013",
    "favourites_count": 11004,
    "utc_offset": null,
    "time_zone": null,
    "geo_enabled": true,
    "verified": false,
    "statuses_count": 72212,
    "lang": null,
    "contributors_enabled": false,
    "is_translator": false,
    "is_translation_enabled": false,
    "profile_background_color": "9AE4E8",
    "profile_background_image_url": "http://abs.twimg.com/images/themes/theme16/bg.gif",
    "profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme16/bg.gif",
    "profile_background_tile": true,
    "profile_image_url": "http://pbs.twimg.com/profile_images/1105002820183433216/Y6uE3UWh_normal.png",
    "profile_image_url_https": "https://pbs.twimg.com/profile_images/1105002820183433216/Y6uE3UWh_normal.png",
    "profile_banner_url": "https://pbs.twimg.com/profile_banners/1204681459/1549378270",
    "profile_link_color": "0084B4",
    "profile_sidebar_border_color": "BDDCAD",
    "profile_sidebar_fill_color": "DDFFCC",
    "profile_text_color": "333333",
    "profile_use_background_image": true,
    "has_extended_profile": false,
    "default_profile": false,
    "default_profile_image": false,
    "following": true,
    "follow_request_sent": false,
    "notifications": false,
    "translator_type": "regular"
  },
  "geo": null,
  "coordinates": null,
  "place": null,
  "contributors": null,
  "is_quote_status": false,
  "retweet_count": 0,
  "favorite_count": 0,
  "favorited": false,
  "retweeted": false,
  "possibly_sensitive": false,
  "possibly_sensitive_appealable": false,
  "lang": "ca"
}
```

We can also retrieve the username and display the names of the 10 most 
recently followed accounts with the script below:
```python
for follower in tweepy.Cursor(api.friends).items(10):
    print(follower.name, "\t\t", follower.screen_name)
```

With the following output:
```bash
Zosia Tarant 		 zosiatarant
Jordi 🏳️‍🌈🌍🚇 		 jooortx
Longhorn 		 never_released
FNEC UPC 		 fnecupc
Dídac Socunarbre d'Urgell 🏴󠁧󠁢󠁥󠁮󠁧󠁿 🏳️‍🌈 		 socunarbre
Jeff stuff 		 CatalanData
Pere Medina Martí 		 PereMMarti
Roger Mas cada dia 		 RMcadadia
Oriol de Balanzó 		 orioldebalanzo
ÈRIC PONS I LARROY 		 pons_21
```

We can print a list of tweets previously made by the account 
with the script:
```python
for tweet in tweepy.Cursor(api.user_timeline).items(8):
    print(tweet.text)
```

With the following output:
```bash
@AjuntamentBerga @lapatum Ja poden anar suspenent la Patum 2022. Un any després estem igual, i dos anys després també.
@marcbeldata Per això mai m’he fet Linkedin. Sempre ho he vist més com una xarxa social més a mantenir (amb la mand… https://t.co/KrWSrZulVf
RT @MetaDataCat: De 9 a 12 setmanes, el temps que necessites per passar-te al sector TIC amb un bootcamp i fer un canvi professional https:…
RT @jordimash: Cada cop més aspectes claus de la nostra vida seran decidits per màquines i algorismes. És absolutament clau la transparènci…
🐔🐓🦃  #L6ElDebat https://t.co/o8XKMFYRSj
@fibracat Què impedeix oferir eSIMs?
@carrizosacarlos @3gerardpique Carles, ets un quillo
RT @maxfras: What European language am I reading?

The only flow chart you need https://t.co/lyJdqT4uKw
```

## Task 2.3: Tweet pre-processing

**Q23: Add the code to `Twitter_2.py` and your comments to `README.md`.**  

The code added to `Twitter_2.py` retrieves the 10 most recent tweets 
in English of the user's home timeline and tokenizes the content 
in order to allow future language analysis.  

The output is the following:
```bash
['#BREAKING', 'New', '5.9', 'magnitude', 'quake', 'near', 'Greek', 'city', 'of', 'Larissa', ',', 'according', 'to', 'Athens', 'observatory', 'https://t.co/MZzZxSc7iX']
['EBay', 'said', 'it', 'is', 'working', 'to', 'prevent', 'the', 'resale', 'on', 'its', 'platform', 'of', 'six', 'Dr', '.', 'Seuss', 'books', 'that', 'will', 'no', 'longer', 'be', 'publish', '…', 'https://t.co/1U08mnfYl4']
['RT', '@UniStudios', ':', 'We', 'know', "you've", 'been', 'craving', 'this', '.', '😋', 'Beginning', 'March', '12,', 'come', 'enjoy', 'Taste', 'of', 'Universal', ',', 'an', 'all-new', ',', 'separately', 'ticketed', 'ev', '…']
['Chrome', 'Switches', 'Its', 'Release', 'Cycle', 'for', 'First', 'Time', 'in', 'a', 'Decade', 'https://t.co/Cym0ptuOKY']
['The', 'Arab', 'Coalition', 'destroyed', 'a', 'ballistic', 'missile', 'launched', 'by', 'Yemen', '’', 's', 'Iran-backed', '#Houthis', 'towards', '#SaudiArabia', '’', 's', 'so', '…', 'https://t.co/Aa3C011EvC']
['Leak', ':', 'Here', '’', 's', 'our', 'first', 'look', 'at', 'the', 'Sonos', 'Roam', ',', 'a', '$', '169', 'Bluetooth', 'speaker', '(', 'story', 'by', '@napilopez', ')', 'https://t.co/39KywYFP1M']
['A', 'U', '.', 'S', '.', '-', 'Mexico', 'corridor', 'of', 'renewable', 'energy', 'and', 'water', 'could', 'have', 'prevented', 'widespread', 'emergencies', 'in', 'Texas', '.', '|', 'Analys', '…', 'https://t.co/kI6wS1jFTX']
['The', 'days', 'of', 'knowing', 'how', 'big', 'a', 'movie', 'is', 'are', 'seemingly', 'over', 'in', 'a', 'streaming-first', 'era', 'https://t.co/5Qg7NV3ots', 'https://t.co/E2wcjFKY0Q']
['This', 'massive', 'wave', 'pool', 'is', 'exactly', 'where', 'we', 'want', 'to', 'be', 'https://t.co/nxoUMOgEvR']
['First', 'you', 'curse', ',', 'then', 'you', 'recurse', '.', '#CodingIn6Words']
```
 As can be observed, spaces are ignored. This tokenization is not case-sensitive. The emoticons are
kept in the  original format, while the URLs, hashtags and mentions are standalone tokens.
 
**Q24: How long have you been working on this session? What have been the main difficulties you have faced and how have you solved them?**  
We have been working with this lab assignment ~4h in order to 
get everything done.  
The most complicated aspects have been the following:
* **Setup of the environment**. One of the libraries used (`tweepy`) gave us some struggles when installing and was not installed. After some time we found out that there was a missing repository for the `conda`environment, so we added it. Furthermore, there was a problem with the SSL certificates, so we manually added them to the corresponding folder. After these steps, `tweepy` was installed successfully.
* **Keeping the keys secret**. We worked on different operating systems (Linux and Windows), and each of them has a different way of handling with environment variables. Finally we could get to write a universal script that adds these variables to the OS using the library `os` from `Python`, and the keys were excluded from the repository.
