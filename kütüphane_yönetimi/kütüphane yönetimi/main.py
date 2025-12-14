from service.book_service import BookService
from service.lending_service import LendingServices
from utils.penalties import StandartPenalty, NoPenalty,StrictPenalty
from models.book import Book
from models.user import User

def run():
    bs = BookService()
    ls = LendingServices(StrictPenalty())

    book1 = Book(1,"yaşamla mucadele","eren guzel")
    book2 = Book(2,"hayat mucadele","insanlar")
    book3 = Book(3,"okul mucadele","esra")
    book4 = Book(4,"para mucadele","kaaann")
    book5 = Book(5,"hocalarla mucadele","zeynep su ")

    user1 = User("kaan","student")
    user2 = User("ahmet","teacher")


    bs.add_book(book1)
    bs.add_book(book2)
    bs.add_book(book3)
    bs.add_book(book4)
    bs.add_book(book5)

    ls.lend(user1,book4)
    bs.find_book(book4.title)
    if book4.is_available is False:
        print("KİTAP ELİMİZDE YOK")

    ls.return_book(book4,days_late=15)
    bs.find_book(book4.title)
    
    if book4.is_available is True:
        print("KİTAP ELİMİZDE VAR")

run()