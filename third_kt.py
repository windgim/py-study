def get_books(filename):
    # Задание 1
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.read().splitlines()
    
    data_lines = lines[1:]
    
    return list(map(
        lambda line: [
            line.split('|')[0],
            line.split('|')[1],
            line.split('|')[2],
            int(line.split('|')[3]),
            float(line.split('|')[4])
        ],
        data_lines
    ))


def filtered_books(books, search_string):
    # Задание 2
    return list(map(
        lambda book: [
            book[0],
            f"{book[1]}, {book[2]}",
            book[3],
            book[4]
        ],
        filter(
            lambda book: search_string.lower() in book[1].lower(),
            books
        )
    ))


def calculate_total_price(books):
    # Задание 3
    return list(map(
        lambda book: (book[0], round(book[3] * book[4], 2)),
        books
    ))


if __name__ == "__main__":
    print("ЗАДАНИЕ 1: Все книги")
    all_books = get_books("books.csv")
    for book in all_books:
        print(book)
    
    print("ЗАДАНИЕ 2: Фильтрация по 'python'")
    python_books = filtered_books(all_books, "python")
    for book in python_books:
        print(book)
    
    print("ЗАДАНИЕ 3: Общая стоимость книг по Python")
    total_prices = calculate_total_price(python_books)
    for item in total_prices:
        print(item)
