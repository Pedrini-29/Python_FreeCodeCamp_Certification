** start of main.py **

class Rectangle:
    def __init__(self,width:int,height:int)->None:
        self.width=width
        self.height=height
    
    def set_width(self,new_width):
        self.width=new_width
    def set_height(self,new_height):
        self.height=new_height
    #method to calculate perimeter of a rectangle
    def get_perimeter(self)->int:
        perimeter = 2*(self.width+self.height)
        return perimeter
    #method to calculate the area of a rectangle
    def get_area(self)->int:
        area=self.width*self.height
        return area
    #calculate the diagonal of the rectangle
    def get_diagonal(self)->float:
        diagonal=((self.width**2)+(self.height**2))**(0.5)
        return diagonal
    def get_amount_inside(self,shape)->int:
        if isinstance(shape, Square):
            #print(self,shape)
            v_times= self.height//shape.side
            #print(v_times)
            if v_times<=0: 
                return 0
            else: 
                w_times= self.width//shape.side
                #print(w_times)
                if w_times<=0:
                    return 0
                else:
                    return v_times*w_times
        elif isinstance(shape,Rectangle):
            result=[]
            height=shape.height
            width=shape.width
            for i in range(2):
                #print(i)
                #print(height,width)
                if i==1:
                    height,width=width,height
                #print(height,width)
                v_times= self.height//height
                if v_times<=0: 
                    continue
                else: 
                    w_times= self.width//width
                    if w_times<=0:
                        continue
                    else:
                        result.append(v_times*w_times)
                        #print(result)
            #print(result)
            if not result: return 0
            return max(result)
    #str call for rectangle
    def __str__(self):
        string=f"Rectangle(width={self.width}, height={self.height})"
        return string
    
    def get_picture(self)->str:
        string=""
        if self.width>50 or self.height>50:
            return "Too big for picture."
        for h in range(self.height):
            for w in range(self.width):
                string+="*"
            string+="\n"
        return string

class Square(Rectangle):
    def __init__(self,side):
        self.side=side
    def set_width(self,new_side):
        self.side=new_side
    def set_height(self,new_side):
        self.side=new_side
    def set_side(self,new_side:int):
        self.side=new_side
    #str call for square
    def __str__(self):
        string =f"Square(side={self.side})"
        return string
    #calculate the perimeter of the square
    def get_perimeter(self)->int:
        perimeter=self.side*4
        return perimeter
    #calculate the area of the square
    def get_area(self)->float:
        area=self.side**2
        return area
    def get_diagonal(self)->float:
        diagonal=((self.side**2)*2)**(0.5)
        return diagonal
    def get_picture(self)->str:
        string=""
        for s1 in range(self.side):
            for s2 in range(self.side):
                string+="*"
            string+="\n"
        return string


rect=Rectangle(2,3)
sqr=Square(4)
print(rect)
print(rect.get_picture())
print(rect.get_amount_inside(Rectangle(3,6)))

** end of main.py **

