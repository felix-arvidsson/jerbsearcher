#rename file to config.py

password = "gmail app password"
sender = "email_sender@gmail.com"
recipients = ["email_recipient1@gmail.com", "email_recipient2@umea.se"]


#occupation_field and kommun tas från URL parameters.
#https://arbetsformedlingen.se/platsbanken/annonser?p=4:apaJ_2ja_LuF <--- occupation &l=3:AvNB_uwa_6n6 <-- kommun'
#om osäker, kör url_disector.py script.
#>python url_disector.py 'https://arbetsformedlingen.se/platsbanken/annonser?p=4:apaJ_2ja_LuF&l=3:AvNB_uwa_6n6'
occupation_fields = ["apaJ_2ja_LuF"] # alla jobb i Data/IT kategorin 
kommuner = ["tUnW_mFo_Hvi", "QiGt_BLu_amP"] #Vilhelmina kommun, Umeå kommun

