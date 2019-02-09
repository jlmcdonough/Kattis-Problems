values = input()
king,queen,rooks,bishops,knights,pawns = map(int, values.split(" ",6))
print(1-king, 1-queen, 2-rooks, 2-bishops, 2-knights, 8-pawns)
