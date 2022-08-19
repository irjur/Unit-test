from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    def test_type_book_rating_is_dict(self):
        collector = BooksCollector()
        assert type(collector.books_rating) == dict

    def test_type_favorites_is_list(self):
        collector = BooksCollector()
        assert type(collector.favorites) == list

    def test_type_book_rating_is_empty(self):
        collector = BooksCollector()
        assert len(collector.books_rating) == 0

    def test_type_favorites_is_empty(self):
        collector = BooksCollector()
        assert len(collector.favorites) == 0

    def test_add_new_book_book_rating_is_1_by_default(self):
        collector = BooksCollector()
        collector.add_new_book('Властелин колец: Братство кольца')
        assert collector.books_rating['Властелин колец: Братство кольца'] == 1

    def test_add_new_book_book_not_readded(self):
        collector = BooksCollector()
        collector.add_new_book('Властелин колец: Братство кольца')
        collector.add_new_book('Властелин колец: Братство кольца')
        assert len(collector.get_books_rating()) == 1

    def test_set_book_rating_rating_is_equal_entered_9(self):
        collector = BooksCollector()
        collector.add_new_book('Властелин колец: Братство кольца')
        collector.set_book_rating('Властелин колец: Братство кольца', 9)
        assert collector.books_rating['Властелин колец: Братство кольца'] == 9

    def test_set_book_rating_rating_less_than_1(self):
        collector = BooksCollector()
        collector.add_new_book('Властелин колец: Братство кольца')
        collector.set_book_rating('Властелин колец: Братство кольца', 0)
        assert collector.books_rating['Властелин колец: Братство кольца'] == 1

    def test_set_book_rating_rating_over_10(self):
        collector = BooksCollector()
        collector.add_new_book('Властелин колец: Братство кольца')
        collector.set_book_rating('Властелин колец: Братство кольца', 11)
        assert collector.books_rating['Властелин колец: Братство кольца'] == 1

    def test_set_book_rating_not_rating_for_non_existing_book(self):
        collector = BooksCollector()
        collector.add_new_book('Властелин колец: Братство кольца')
        collector.set_book_rating('Властелин колец: Две крепости', 9)
        assert collector.get_book_rating('Властелин колец: Две крепости') == None

    def test_get_book_rating_rating_for_existing_book(self):
        collector = BooksCollector()
        collector.add_new_book('Властелин колец: Братство кольца')
        assert collector.get_book_rating('Властелин колец: Братство кольца') == 1

    def test_get_book_rating_not_rating_for_non_existing_book(self):
        collector = BooksCollector()
        collector.add_new_book('Властелин колец: Братство кольца')
        assert collector.get_book_rating('Властелин колец: Две башни') == None

    def test_get_books_with_specific_rating_books_only_rating_9(self):
        collector = BooksCollector()
        collector.add_new_book('Властелин колец: Братство кольца')
        collector.add_new_book('Властелин колец: Две крепости')
        collector.add_new_book('Властелин колец: Возвращение короля')
        collector.set_book_rating('Властелин колец: Братство кольца', 9)
        collector.set_book_rating('Властелин колец: Две крепости', 8)
        collector.set_book_rating('Властелин колец: Возвращение короля', 9)
        assert len(collector.get_books_with_specific_rating(9)) == 2 \
               and 'Властелин колец: Братство кольца' in collector.books_rating \
               and 'Властелин колец: Возвращение короля' in collector.books_rating

    def test_get_books_with_specific_rating_for_dict_empty_0(self):
        collector = BooksCollector()
        assert len(collector.get_books_with_specific_rating(9)) == 0

    def test_get_books_rating_type_is_dict(self):
        collector = BooksCollector()
        collector.add_new_book('Властелин колец: Братство кольца')
        collector.add_new_book('Властелин колец: Две крепости')
        collector.add_new_book('Властелин колец: Возвращение короля')
        assert type(collector.books_rating) == dict

    def test_get_books_rating_dict_not_empty_len_3(self):
        collector = BooksCollector()
        collector.add_new_book('Властелин колец: Братство кольца')
        collector.add_new_book('Властелин колец: Две крепости')
        collector.add_new_book('Властелин колец: Возвращение короля')
        assert len(collector.books_rating) == 3

    def test_add_book_in_favorites_add_new_book(self):
        collector = BooksCollector()
        collector.add_new_book('Властелин колец: Братство кольца')
        collector.add_book_in_favorites('Властелин колец: Братство кольца')
        assert 'Властелин колец: Братство кольца' in collector.favorites

    def test_add_book_in_favorites_book_not_readded(self):
        collector = BooksCollector()
        collector.add_new_book('Властелин колец: Братство кольца')
        collector.add_book_in_favorites('Властелин колец: Братство кольца')
        collector.add_book_in_favorites('Властелин колец: Братство кольца')
        assert len(collector.favorites) == 1

    def test_add_book_in_favorites_book_not_in_books_rating(self):
        collector = BooksCollector()
        collector.add_new_book('Властелин колец: Братство кольца')
        collector.add_book_in_favorites('Властелин колец: Две крепости')
        assert len(collector.favorites) == 0

    def test_delete_book_from_favorites_delete_1_existing_book_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Властелин колец: Братство кольца')
        collector.add_book_in_favorites('Властелин колец: Братство кольца')
        collector.delete_book_from_favorites('Властелин колец: Братство кольца')
        assert len(collector.favorites) == 0

    def test_delete_book_from_favorites_not_delete_for_non_existing_book(self):
        collector = BooksCollector()
        collector.add_new_book('Властелин колец: Братство кольца')
        collector.add_book_in_favorites('Властелин колец: Братство кольца')
        collector.delete_book_from_favorites('Властелин колец: Две крепости')
        assert len(collector.favorites) == 1

    def test_get_list_of_favorites_books_type_is_list(self):
        collector = BooksCollector()
        collector.add_new_book('Властелин колец: Братство кольца')
        collector.add_book_in_favorites('Властелин колец: Братство кольца')
        collector.get_list_of_favorites_books()
        assert type(collector.favorites) == list

    def test_get_list_of_favorites_books_list_not_empty_len_1(self):
        collector = BooksCollector()
        collector.add_new_book('Властелин колец: Братство кольца')
        collector.add_book_in_favorites('Властелин колец: Братство кольца')
        collector.get_list_of_favorites_books()
        assert len(collector.books_rating) == 1