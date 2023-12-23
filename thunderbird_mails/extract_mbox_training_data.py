import mailbox
from bs4 import BeautifulSoup


def get_email_text(message):
    if message.is_multipart():
        # If the message is multipart, iterate over each part
        text = ""
        for part in message.walk():
            # Check if the part is text/plain
            if part.get_content_type() == 'text/plain':
                text = text + part.get_payload()
        return text
    else:
        # If the message is not multipart, just get the payload
        return message.get_payload()

def remove_html(text):
    soup = BeautifulSoup(text, 'html.parser')
    text_without_html = soup.get_text(separator=' ')
    # Remove newlines and carriage returns
    cleaned_string = text_without_html.replace('\n', ' ').replace('\r', ' ').replace('  ', ' ').replace('\t', ' ').replace(',', ' ')
    return cleaned_string

def append_line_to_file(file_path, sender, date, subject, message):
    try:
        line = date + "," + sender + "," + subject + ", " + message 
        with open(file_path, 'a') as file:
            file.write(line + '\n')
    except Exception as e:
        print(f"Error appending line to {file_path}: {e}")

def read_thunderbird_mailbox(mailbox_path):
    count = 0
    # Open the Thunderbird mailbox
    mbox = mailbox.mbox(mailbox_path)

    # Iterate through each message in the mailbox
    for message in mbox:
        # Extract and print the subject and sender
        subject = message['subject']
        sender = message['from']
        date = message['date']
        if subject and sender and date:
            try:
                body = remove_html(get_email_text(message))
                if body:
                    append_line_to_file("/Users/wolfgang/Downloads/out.csv", sender.replace(',', ' '), date.replace(',', ' '), subject.replace(',', ' '), body)
                    count = count + 1
            except Exception as e:
                print(f"An unexpected error occurred: {e}")
        '''
        print(f"Subject: {subject}")
        print(f"Sender: {sender}")
        print(f"Date: {date}")
        print(f"Body:\n{body}")
        print("-" * 50)
        '''
        print(count)



if __name__ == "__main__":
    # Replace 'path/to/your/mailbox' with the actual path to your Thunderbird mailbox file
    mailbox_path = '/Users/wolfgang/Downloads/tabshop-support/Posteingang'

    try:
        read_thunderbird_mailbox(mailbox_path)
    except FileNotFoundError:
        print(f"Error: The mailbox file '{mailbox_path}' was not found.")
    except mailbox.Error as e:
        print(f"Error: An error occurred while processing the mailbox - {e}")
