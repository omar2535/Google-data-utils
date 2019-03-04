from google_connect import GoogleConnector
from message_utils import MessageUtils
from email_parser import EmailParser
import pdb

def main():
    google_service = GoogleConnector().get_google_service()
    # labels = google_service.users().labels().list(userId='me').execute()
    # messages = Message().get_message(google_service)
    message_util = MessageUtils()
    mail_parser = EmailParser()
    
    messages = message_util.list_messages_matching_query('me', google_service, 'important')
    
    

    breakpoint()

if __name__ == '__main__':
    main()
