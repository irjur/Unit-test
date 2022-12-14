# qa_python

### Тесты для метода __init__ (Создать пустой словарь book_rating и пустой список favorites)

1. **test_type_book_rating_is_dict** - тест проверяет, что метод по умолчанию создает переменную book_rating, тип которой - словарь
2. **test_type_favorites_is_list** - тест проверяет, что метод по умолчанию создает переменную favorites, тип которой - список
3. **test_type_book_rating_is_empty** - тест проверяет, что созданный словарь book_rating пустой
4. **test_type_favorites_is_empty** - тест проверяет, что созданный список favorites пустой

### Тесты для метода add_new_book (Добавить новую книгу с рейтингом по умолчанию - 1)

1. **test_add_new_book_book_rating_is_1_by_default** - тест проверяет, что рейтинг для вновь добавленной книги по умолчанию равен 1
2. **test_add_new_book_book_not_readded** - тест проверяет, что нельзя добавить дважды одну и ту же книгу

### Тесты для метода set_book_rating (Установить рейтинг для указанной книги от 1 до 10)

1. **test_set_book_rating_rating_is_equal_entered_9** - тест проверяет, что для указанной книги проставляется указанный рейтинг
2. **test_set_book_rating_rating_less_than_1** - тест, который проверяет значение рейтинга меньшее, чем значение нижней границы допустимого интервала от 1 до 10. 
Т.к. значение рейтинга не может быть меньше 1, то при передаче значения "0" в аргументе значение рейтинга по умолчанию не изменится и останется равным 1.
3. **test_set_book_rating_rating_over_10** - тест, который проверяет значение рейтинга большее, чем значение верхней границы допустимого интервала от 1 до 10.
Т.к. значение рейтинга не может быть больше 10, то при передаче значения "11"  в аргументе значение рейтинга по умолчанию не изменится и останется равным 1.
4. **test_set_book_rating_not_rating_for_non_existing_book** - тест, который проверяет, что нельзя установить рейтинг для книги, которой нет в словаре book_rating

### Тесты для метода get_book_rating (Получить рейтинг книги по ее названию)

1. **test_get_book_rating_rating_for_existing_book** - тест проверяет, что можно получить рейтинг книги, которая есть в словаре
2. **test_get_book_rating_not_rating_for_non_existing_book** - тест проверяет, что нельзя получить рейтинг книги, которой нет в словаре

### Тесты для метода get_books_with_specific_rating (Вывести список книг с указанным рейтингом)

1. **test_get_books_with_specific_rating_books_only_rating_9** - тест проверяет, что метод возвращает список книг с указанным рейтингом ("9"): в списке правильное количество и верные названия книг
2. **test_get_books_with_specific_rating_for_dict_empty_0** - тест проверяет, что для пустого словаря возвращается пустой список

### Тесты для метода get_books_rating (Получить словарь с названиями книг и их рейтингом)

1. **test_get_books_rating_type_is_dict** - тест проверяет, что тип переменной, которую возвращает метод - словарь
2. **test_get_books_rating_dict_not_empty_len_3** - тест проверяет, что метод возвращает не пустой словарь, если в него внесены данные, длина словаря равна количеству внесенных в него книг (3)

### Тесты для метода add_book_in_favorites (Добавить книгу в список избранных книг)

1. **test_add_book_in_favorites_add_new_book** - тест проверяет, что в Избранное можно добавить новую книгу, которая есть в рейтинге книг (словаре books_rating)
2. **test_add_book_in_favorites_book_not_readded** - тест проверяет, что в Избранное нельзя добавить дважды одну и ту же книгу
3. **test_add_book_in_favorites_book_not_in_books_rating** - тест проверяет, что книга, которой нет в рейтинге книг (словаре books_rating), не добавится в Избранное

### Тесты для метода delete_book_from_favorites (Удалить книгу из списка избранных книг)

1. **test_delete_book_from_favorites_delete_1_existing_book_from_favorites** - тест проверяет, что существующая книга удаляется из Избранного
2. **test_delete_book_from_favorites_not_delete_for_non_existing_book** - тест проверяет, что НЕ существующая книга НЕ удаляется из Избранного

### Тесты для метода get_list_of_favorites_books (Получить список избранных книг)

1. **test_get_list_of_favorites_books_type_is_list** - тест проверяет, что тип переменной, которую возвращает метод - список
2. **test_get_list_of_favorites_books_list_not_empty_len_1** - тест проверяет, что метод возвращает не пустой список, если в него внесены данные, длина списка равна количеству внесенных в него книг (1)
