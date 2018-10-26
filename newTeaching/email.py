def is_valid_email(s):
	<<your code here>>

	
def filter_mail(emails):
	<<your code here>>


if __name__ == '__main__':
	n = int(raw_input())
	emails = []
	for _ in range(n):
	emails.append(raw_input())
	filtered_emails = filter_mail(emails)
	filtered_emails.sort()
	print filtered_emails 