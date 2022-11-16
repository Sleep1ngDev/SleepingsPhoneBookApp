from models import Contact, Phone


def phone_saver(name: str, phones: str) -> bool:
    if name and phones:
        contact = Contact.add(name)
        for phone in phones.split('\n'):
            Phone.add(phone, contact)
            return True
        return False
