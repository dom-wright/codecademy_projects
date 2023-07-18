from contextlib import contextmanager


@contextmanager
def generic(card_type, sender, receiver):
    write_file = open(f"{sender}_generic.txt", 'w')
    try:
        write_file.write(f"Dear {receiver.title()}\n\n")
        yield write_file
    except Exception as e:
        print(e)
    finally:
        write_file.write(f"\n\nSincerely, {sender.title()}")
        write_file.close()


with generic("thankyou", "mwenda", "amanda") as first_order:
    read_file = open(f"thankyou_card.txt", 'r')
    first_order.write(read_file.read())


class Personalized:

    def __init__(self, sender, receiver):
        self.sender = sender
        self.receiver = receiver
        self.opened_file = open(f"{sender.title()}_personalized.txt", 'w')

    def __enter__(self):
        self.opened_file.write(f"Dear {self.receiver.title()}\n\n")
        return self.opened_file

    def __exit__(self, exc_type, exc_val, traceback):
        if isinstance(exc_val, TypeError):
            # Handle TypeError here...
            print("The exception has been handled")
            return True
        self.opened_file.write(f"\n\nSincerely, {self.sender.title()}")
        self.opened_file.close()


with Personalized('john', 'michael') as second_order:
    second_order.write("I am so proud of you! Being your friend for all these years has been nothing but a blessing. I don’t say it often but I just wanted to let you know that you inspire me and I love you! All the best. Always.")
