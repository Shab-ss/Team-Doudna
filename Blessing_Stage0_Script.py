Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Hamming distance
>>> def hamming_dist (slack_username, twitter_handle):
	i = 0
	count = 0
	while(i < len (slack_username)):
		if(slack_username[i] != twitter_handle[i]):
			count += 1
		i += 1
	return count

>>> name= 'Blessing Olabosoye'
>>> email= 'bleznolap@gmail.com'
>>> slack_username= '@Blessing'
>>> biostack= 'Genomics'
>>> twitter_handle= '@Olabosoye_BP'
>>> ham = hamming_dist (slack_username, twitter_handle)
>>> print('Blessing Personal Bios below:\nName- {}\nEmail- {}\nSlack Username- {}\nBiostack- {}\nTwitter Handle- {}\nHamming Distance- {}'.format(name, email, slack_username, biostack, twitter_handle, ham))
Blessing Personal Bios below:
Name- Blessing Olabosoye
Email- bleznolap@gmail.com
Slack Username- @Blessing
Biostack- Genomics
Twitter Handle- @Olabosoye_BP
Hamming Distance- 7
>>> 