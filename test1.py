def line_algorithim():
    import turtle
    from MAIN import x0
    from MAIN import y0
    from MAIN import x1
    from MAIN import y1
    from MAIN import BoxSize
    from MAIN import loop1
    while loop1 == 1:
        def sign(a):
            if a > 0:
                ret = 1
            elif a < 0:
                ret = -1
            else:
                ret = 0
            return ret

        x = x0
        y = y0
        dx = abs(x1 - x)
        dy = abs(y1 - y)
        s1 = sign(x1 - x0)
        s2 = sign(y1 - y0)

        if dy > dx:
            dx, dy = dy, dx
            interchange = 1
        else:
            interchange = 0

        e = 2 * dy - dx
        # display list
        x_list = []
        y_list = []
        x_ = []
        y_ = []
        e_ = []
        for i in range(int(dx)):
            x_list.append(x)
            y_list.append(y)
            while e >= 0:
                if interchange == 1:
                    x = x + s1

                else:
                    y = y + s2

                e = e - 2 * dx
            if interchange == 1:
                y = y + s2

            else:
                x = x + s1
            turtle.end_fill()
            e = e + 2 * dy
            e_.append(e)
            turtle.penup()
            turtle.setpos(x * BoxSize, y * BoxSize)
            turtle.pendown()
            box = 1
            turtle.fillcolor("black")
            turtle.begin_fill()
            while box < 5:
                turtle.right(90)
                turtle.forward(BoxSize)
                box = box + 1
            turtle.end_fill()
        loop1 = 0