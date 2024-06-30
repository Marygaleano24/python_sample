posts = []

while True:
    print( "1から5の数字で評価を入力してください。終了する場合は「6」を入力してください" )
    point = input()
    if point.isdecimal():
        point = int(point)
        if point == 6:
            print( "終了します" )
            break
        elif 1 <= point <= 5:
            print( "コメントを入力してください" )
            comment = input()
            post = { 'point': point, 'comment': comment }
            posts.extend( post.items() )
            print( posts )
    else:
        print( "数字を入力してください" )