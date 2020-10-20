import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders
import re
import os


def send_email(sender_mail, sender_password, mail_subject, mail_body, receiver_mail, sender_mail_site_smtp,
			   list_of_attachments):
	# An instance of MIMEMultipart
	mail_object = MIMEMultipart()

	# Initializing the parameters for the mail
	# Sender's email address
	mail_object['From'] = sender_mail

	# Receiver's email address
	mail_object['To'] = receiver_mail

	# Subject line
	mail_object['Subject'] = mail_subject

	# Mail Body content
	body = mail_body

	# Attach mail body content to the mail object
	mail_object.attach(MIMEText(body, 'plain'))

	# If list of attachments has any attachments, then attach it to mail object
	if list_of_attachments:
		# Attach each attachment into mail object
		for file in list_of_attachments:
			filename = file
			part = MIMEBase('application', 'octet-stream')
			part.set_payload(open(filename, 'rb').read())
			encoders.encode_base64(part)
			part.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(filename))
			mail_object.attach(part)

	# SMTP session
	smtp_session = smtplib.SMTP(sender_mail_site_smtp, 587)

	# TLS for security
	smtp_session.starttls()

	# Authentication
	smtp_session.login(sender_mail, sender_password)

	# Converts the Multipart mail_object into a string
	text = mail_object.as_string()

	# sending the mail
	smtp_session.sendmail(sender_mail, receiver_mail, text)

	# terminating the session
	smtp_session.quit()


###################################

def get_mail_site_smtp(mail_address):
	mail_sites_smtp_list = {'gmail': 'smtp.gmail.com',
							'Outlook.com': 'smtp.live.com',
							'Office365.com': 'smtp.office365.com',
							'Yahoo Mail': 'smtp.mail.yahoo.com',
							'Yahoo Mail Plus': 'plus.smtp.mail.yahoo.com',
							'Yahoo UK': 'smtp.mail.yahoo.co.uk',
							'Yahoo Deutschland': 'smtp.mail.yahoo.com',
							'Yahoo AU/NZ': 'smtp.mail.yahoo.com.au',
							'O2': 'smtp.o2.ie',
							'O2.uk': 'smtp.o2.co.uk',
							'AOL.com': 'smtp.aol.com',
							'AT&T': 'smtp.att.yahoo.com',
							'NTL @ntlworld.com': 'smtp.ntlworld.com',
							'Orange': 'smtp.orange.net',
							'Orange.uk': 'smtp.orange.co.uk',
							'Wanadoo UK': 'smtp.wanadoo.co.uk',
							'Hotmail': 'smtp.live.com',
							'O2 Online Deutschland': 'securesmtp.t-online.de',
							'1&1 (1and1)': 'smtp.1and1.com',
							'1&1 Deutschland': 'smtp.1und1.de',
							'Comcast': 'smtp.comcast.net',
							'zoho Mail': 'smtp.zoho.com',
							'Mail.com': 'smtp.mail.com',
							'GMX.com': 'smtp.gmx.com',
							'Net@ddress by USA.NET': 'smtp.postoffice.net'}
	# Source: https://www.arclab.com/en/kb/email/list-of-smtp-and-pop3-servers-mailserver-list.html

	mail_pattern = r'([a-zA-Z0-9]+)@([a-zA-Z0-9]+).([a-zA-Z0-9]{3})'
	match = re.search(mail_pattern, mail_address)
	sender_mail_site = match.group(2)
	print('Can you please type the email site you are using from below list of sites?')
	if sender_mail_site in mail_sites_smtp_list.keys():
		for mail_site in mail_sites_smtp_list.keys():
			if sender_mail_site in mail_site:
				print(mail_site)
		choice1 = input(': ')
		return mail_sites_smtp_list[choice1]
	else:
		print(mail_sites_smtp_list.keys())
		print('Type "N" if you do not see your site listed')
		choice2 = input(': ')
		if choice2 in ['N', 'n']:
			return False


# Mail Address

print("Enter details:")
MAIL_ADDRESS = input('Your mail address: ')
mail_address_valid = False
while not mail_address_valid:
	mail_address_pattern = r'^[a-z0-9A-Z]+[._]?[a-z0-9A-Z]+[@]\w+[.]\w{2,3}$'
	if re.search(mail_address_pattern, MAIL_ADDRESS):
		mail_address_valid = True
	else:
		print('Please enter in the format: user@site.domain. Eg. john@somesitemail.com')

# Password
PASSWORD = input('Password: ')
print('## LOGIN Initialized ##')

# Subject
SUBJECT = input('Subject line: ')

# Mail body content
print('Reading mail body from mail_body.txt file ...')
mail_body_file = open('mail_body.txt', 'r')
BODY = mail_body_file.read()
mail_body_file.close()

# Preview
print('Mail preview: ')
print('#########################')
print('Subject: ' + SUBJECT)
print(BODY)
print('#########################')

# Mail recipients/receivers
print('Reading mail recipients from recipients.txt file ...')
recipients = open('recipients.txt', 'r')
ALL_RECIPIENTS = recipients.readlines()
recipients.close()
print('Total recipients found in recipients.txt: ' + str(len(ALL_RECIPIENTS)))

# Mail SMTP
MAIL_SMTP = get_mail_site_smtp(MAIL_ADDRESS)

# Attachments:
ATTACHMENTS = list()
choice = input('Do you want to attach files to the mail? Y/N:  ')
if choice in ['Y', 'y']:
	num_files = int(input('Number of files: '))
	for n in range(num_files):
		filefull = input('Enter file\'s absolute path: ')
		ATTACHMENTS.append(filefull)
########################################
proceed = input('Proceed? Y/N:  ')
if proceed in ['Y', 'y']:
	email_sent_count = 0
	for RECIPIENT in ALL_RECIPIENTS:
		send_email(MAIL_ADDRESS, PASSWORD, SUBJECT, BODY, RECIPIENT, MAIL_SMTP, ATTACHMENTS)
		email_sent_count += 1
		print(str(email_sent_count) + '. ' + RECIPIENT.strip() + ' --> Sent')

	print('TOTAL MAILS SENT: ' + str(email_sent_count))
else:
	print('Closing program ...')
