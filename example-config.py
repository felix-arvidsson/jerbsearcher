#rename file to config.py

password = "gmail app password"
sender = "email_sender@gmail.com"
recipients = ["email_recipient1@gmail.com", "email_recipient2@umea.se"]


#occupation_field and kommun is taken from platsbanken.se URL parameters.
#https://arbetsformedlingen.se/platsbanken/annonser?p=4:apaJ_2ja_LuF <--- occupation &l=3:AvNB_uwa_6n6 <-- kommun'
#
##if you're unsure, run url_disector.py script.
#>python url_disector.py 'https://arbetsformedlingen.se/platsbanken/annonser?p=4:apaJ_2ja_LuF&l=3:AvNB_uwa_6n6'
occupation_fields = ["apaJ_2ja_LuF"] # all it jobs
kommuner = ["AvNB_uwa_6n6"] #stockholms kommun

