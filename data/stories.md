## greet + talk_customer
* want_software{"software_type":"accountancy"}
  - software_search_form
  - form{"name":"software_search_form"}
  - form{"name":null}
* goodbye
  - utter_goodbye


## greet + show_phones
* buy_phone_laptop{"category":"phone"}
  - product_search_form
  - form{"name":"product_search_form"}
  - form{"name":null}
* goodbye
  - utter_goodbye


## greet + show_latest_news
* latest_news_phones_laptops
  - action_show_latest_news
* goodbye
  - utter_goodbye


## greet
* greet
  - utter_how_can_I_help
