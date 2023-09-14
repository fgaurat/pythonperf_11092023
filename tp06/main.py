from Rectangle import Rectangle
def main():
    
    r1 = Rectangle(1,2)
    r2 = Rectangle(3,5)
    r3 = Rectangle.build_from_str("2,3")
    print(Rectangle.get_cpt())
    print(r3.surface)


if __name__=='__main__':
    main()
