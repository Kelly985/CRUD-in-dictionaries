def crud_dictionaries():
    books = {
    '1':{
        'author': 'FaithK',
        'title': 'How to win',
        'year':2020,
        'ISBN': 100
        }, 
        '2':{
        'author': 'Kym',
        'title': 'How to Sleep',
        'year':2023,
        'ISBN': 10032
        }
}
    list_key= books['1']['author']

#add new book

    book2= {'3':{
        'author': 'dan',
        'title': 'How to code',
        'year':2023,
        'ISBN': 120
        }
        }
    books.update(book2)

# edit title
    books['3']['title']= 'python'


#delete book pop item(remove the last item)
    books.pop('1')
    print(books)


#retrieve book by author

    author = input("Enter the author's name: ")
    get_bk = []

    for book in books.values():
        if book['author'] == author:
            get_bk.append(book)

    if len(get_bk) > 0:
        for book in get_bk:
            print("Author:", book['author'])
            print("Title:", book['title'])
            print("Year:", book['year'])
            print("ISBN:", book['ISBN'])
            print()
    else:
        print("No books found for the author:", author)
    
#retrieve book by author
    isbn = int(input("Enter the book  ISBN: "))
    get_bk = []

    for book in books.values():
        if book['ISBN'] == isbn:
            get_bk.append(book)

    if len(get_bk) > 0:
        for book in get_bk:
            print("Author:", book['author'])
            print("Title:", book['title'])
            print("Year:", book['year'])
            print("ISBN:", book['ISBN'])
            print()
    else:
        print("No books found for the ISBN:", isbn)

crud_dictionaries()



