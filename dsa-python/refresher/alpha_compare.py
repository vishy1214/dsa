book_name_1_lc = "great expectations"
book_name_1_cc =  "Great Expectations"
book_name_1_uc = "GREAT EXPECTATIONS"

book_name_2_lc = "short abc"

if(book_name_1_lc ==  book_name_1_cc):
    print("lc & cc comparison are equal")

if(book_name_1_lc == book_name_1_cc):
    print("lc & uc comparison are also equal")

if(book_name_1_lc == book_name_2_lc):
    print("book1 and book2 are not equal")

if(book_name_1_lc < book_name_2_lc):
    print("book1 is lesser than book2")

if(book_name_1_lc > book_name_2_lc):
    print("book1 is greater than book2")

if ("a" < "g"):
    print("a is lesser than g")
else:
    print("a is greater than g")