import sudokuSolver
from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.gridlayout import GridLayout

Window.size=(450,450)
class MyGridLayout(GridLayout):
    # Main grid
    def __init__(self, **kwargs):                       # Defining main grid
        super(MyGridLayout,self).__init__(**kwargs)
        self.cols = 3
        self.spacing = 1.7
        
        # Top left Grid
        self.topLeftGrid = GridLayout()
        self.topLeftGrid.cols= 3
        self.bx1 = TextInput(multiline=False)
        self.topLeftGrid.add_widget(self.bx1)
        self.bx2 = TextInput(multiline=False)
        self.topLeftGrid.add_widget(self.bx2)
        self.bx3 = TextInput(multiline=False)
        self.topLeftGrid.add_widget(self.bx3)
        self.bx4 = TextInput(multiline=False)
        self.topLeftGrid.add_widget(self.bx4)
        self.bx5 = TextInput(multiline=False)
        self.topLeftGrid.add_widget(self.bx5)
        self.bx6 = TextInput(multiline=False)
        self.topLeftGrid.add_widget(self.bx6)
        self.bx7 = TextInput(multiline=False)
        self.topLeftGrid.add_widget(self.bx7)
        self.bx8 = TextInput(multiline=False)
        self.topLeftGrid.add_widget(self.bx8)
        self.bx9 = TextInput(multiline=False)
        self.topLeftGrid.add_widget(self.bx9)

        # Top Middle Grid
        self.topMiddleGrid = GridLayout()
        self.topMiddleGrid.cols= 3
        self.bx10 = TextInput(multiline=False)
        self.topMiddleGrid.add_widget(self.bx10)
        self.bx11 = TextInput(multiline=False)
        self.topMiddleGrid.add_widget(self.bx11)
        self.bx12 = TextInput(multiline=False)
        self.topMiddleGrid.add_widget(self.bx12)
        self.bx13 = TextInput(multiline=False)
        self.topMiddleGrid.add_widget(self.bx13)
        self.bx14 = TextInput(multiline=False)
        self.topMiddleGrid.add_widget(self.bx14)
        self.bx15 = TextInput(multiline=False)
        self.topMiddleGrid.add_widget(self.bx15)
        self.bx16 = TextInput(multiline=False)
        self.topMiddleGrid.add_widget(self.bx16)
        self.bx17 = TextInput(multiline=False)
        self.topMiddleGrid.add_widget(self.bx17)
        self.bx18 = TextInput(multiline=False)
        self.topMiddleGrid.add_widget(self.bx18)

        # Top Right Grid
        self.topRightGrid = GridLayout()
        self.topRightGrid.cols= 3
        self.bx19 = TextInput(multiline=False)
        self.topRightGrid.add_widget(self.bx19)
        self.bx20 = TextInput(multiline=False)
        self.topRightGrid.add_widget(self.bx20)
        self.bx21 = TextInput(multiline=False)
        self.topRightGrid.add_widget(self.bx21)
        self.bx22 = TextInput(multiline=False)
        self.topRightGrid.add_widget(self.bx22)
        self.bx23 = TextInput(multiline=False)
        self.topRightGrid.add_widget(self.bx23)
        self.bx24 = TextInput(multiline=False)
        self.topRightGrid.add_widget(self.bx24)
        self.bx25 = TextInput(multiline=False)
        self.topRightGrid.add_widget(self.bx25)
        self.bx26 = TextInput(multiline=False)
        self.topRightGrid.add_widget(self.bx26)
        self.bx27 = TextInput(multiline=False)
        self.topRightGrid.add_widget(self.bx27)

        # Middle left Grid
        self.middleLeftGrid = GridLayout()
        self.middleLeftGrid.cols= 3
        self.bx28 = TextInput(multiline=False)
        self.middleLeftGrid.add_widget(self.bx28)
        self.bx29 = TextInput(multiline=False)
        self.middleLeftGrid.add_widget(self.bx29)
        self.bx30 = TextInput(multiline=False)
        self.middleLeftGrid.add_widget(self.bx30)
        self.bx31 = TextInput(multiline=False)
        self.middleLeftGrid.add_widget(self.bx31)
        self.bx32 = TextInput(multiline=False)
        self.middleLeftGrid.add_widget(self.bx32)
        self.bx33 = TextInput(multiline=False)
        self.middleLeftGrid.add_widget(self.bx33)
        self.bx34 = TextInput(multiline=False)
        self.middleLeftGrid.add_widget(self.bx34)
        self.bx35 = TextInput(multiline=False)
        self.middleLeftGrid.add_widget(self.bx35)
        self.bx36 = TextInput(multiline=False)
        self.middleLeftGrid.add_widget(self.bx36)

        # Middle middle Grid
        self.middleMiddleGrid = GridLayout()
        self.middleMiddleGrid.cols= 3
        self.bx37 = TextInput(multiline=False)
        self.middleMiddleGrid.add_widget(self.bx37)
        self.bx38 = TextInput(multiline=False)
        self.middleMiddleGrid.add_widget(self.bx38)
        self.bx39 = TextInput(multiline=False)
        self.middleMiddleGrid.add_widget(self.bx39)
        self.bx40 = TextInput(multiline=False)
        self.middleMiddleGrid.add_widget(self.bx40)
        self.bx41 = TextInput(multiline=False)
        self.middleMiddleGrid.add_widget(self.bx41)
        self.bx42 = TextInput(multiline=False)
        self.middleMiddleGrid.add_widget(self.bx42)
        self.bx43 = TextInput(multiline=False)
        self.middleMiddleGrid.add_widget(self.bx43)
        self.bx44 = TextInput(multiline=False)
        self.middleMiddleGrid.add_widget(self.bx44)
        self.bx45 = TextInput(multiline=False)
        self.middleMiddleGrid.add_widget(self.bx45)

        # Middle right Grid
        self.middleRightGrid = GridLayout()
        self.middleRightGrid.cols= 3
        self.bx46 = TextInput(multiline=False)
        self.middleRightGrid.add_widget(self.bx46)
        self.bx47 = TextInput(multiline=False)
        self.middleRightGrid.add_widget(self.bx47)
        self.bx48 = TextInput(multiline=False)
        self.middleRightGrid.add_widget(self.bx48)
        self.bx49 = TextInput(multiline=False)
        self.middleRightGrid.add_widget(self.bx49)
        self.bx50 = TextInput(multiline=False)
        self.middleRightGrid.add_widget(self.bx50)
        self.bx51 = TextInput(multiline=False)
        self.middleRightGrid.add_widget(self.bx51)
        self.bx52 = TextInput(multiline=False)
        self.middleRightGrid.add_widget(self.bx52)
        self.bx53 = TextInput(multiline=False)
        self.middleRightGrid.add_widget(self.bx53)
        self.bx54 = TextInput(multiline=False)
        self.middleRightGrid.add_widget(self.bx54)

        # Bottom left Grid
        self.buttomLeftGrid = GridLayout()
        self.buttomLeftGrid.cols= 3
        self.bx55 = TextInput(multiline=False)
        self.buttomLeftGrid.add_widget(self.bx55)
        self.bx56 = TextInput(multiline=False)
        self.buttomLeftGrid.add_widget(self.bx56)
        self.bx57 = TextInput(multiline=False)
        self.buttomLeftGrid.add_widget(self.bx57)
        self.bx58 = TextInput(multiline=False)
        self.buttomLeftGrid.add_widget(self.bx58)
        self.bx59 = TextInput(multiline=False)
        self.buttomLeftGrid.add_widget(self.bx59)
        self.bx60 = TextInput(multiline=False)
        self.buttomLeftGrid.add_widget(self.bx60)
        self.bx61 = TextInput(multiline=False)
        self.buttomLeftGrid.add_widget(self.bx61)
        self.bx62 = TextInput(multiline=False)
        self.buttomLeftGrid.add_widget(self.bx62)
        self.bx63 = TextInput(multiline=False)
        self.buttomLeftGrid.add_widget(self.bx63)

        # Bottom middle Grid
        self.buttomMiddleGrid = GridLayout()
        self.buttomMiddleGrid.cols= 3
        self.bx64 = TextInput(multiline=False)
        self.buttomMiddleGrid.add_widget(self.bx64)
        self.bx65 = TextInput(multiline=False)
        self.buttomMiddleGrid.add_widget(self.bx65)
        self.bx66 = TextInput(multiline=False)
        self.buttomMiddleGrid.add_widget(self.bx66)
        self.bx67 = TextInput(multiline=False)
        self.buttomMiddleGrid.add_widget(self.bx67)
        self.bx68 = TextInput(multiline=False)
        self.buttomMiddleGrid.add_widget(self.bx68)
        self.bx69 = TextInput(multiline=False)
        self.buttomMiddleGrid.add_widget(self.bx69)
        self.bx70 = TextInput(multiline=False)
        self.buttomMiddleGrid.add_widget(self.bx70)
        self.bx71 = TextInput(multiline=False)
        self.buttomMiddleGrid.add_widget(self.bx71)
        self.bx72 = TextInput(multiline=False)
        self.buttomMiddleGrid.add_widget(self.bx72)

        # Bottom right Grid
        self.buttomRightGrid = GridLayout()
        self.buttomRightGrid.cols= 3
        self.bx73 = TextInput(multiline=False)
        self.buttomRightGrid.add_widget(self.bx73)
        self.bx74 = TextInput(multiline=False)
        self.buttomRightGrid.add_widget(self.bx74)
        self.bx75 = TextInput(multiline=False)
        self.buttomRightGrid.add_widget(self.bx75)
        self.bx76 = TextInput(multiline=False)
        self.buttomRightGrid.add_widget(self.bx76)
        self.bx77 = TextInput(multiline=False)
        self.buttomRightGrid.add_widget(self.bx77)
        self.bx78 = TextInput(multiline=False)
        self.buttomRightGrid.add_widget(self.bx78)
        self.bx79 = TextInput(multiline=False)
        self.buttomRightGrid.add_widget(self.bx79)
        self.bx80 = TextInput(multiline=False)
        self.buttomRightGrid.add_widget(self.bx80)
        self.bx81 = TextInput(multiline=False)
        self.buttomRightGrid.add_widget(self.bx81)

        self.add_widget(self.topLeftGrid)               # Assigning all the individual subgrids into the main grid
        self.add_widget(self.topMiddleGrid)
        self.add_widget(self.topRightGrid)
        self.add_widget(self.middleLeftGrid)
        self.add_widget(self.middleMiddleGrid)
        self.add_widget(self.middleRightGrid)
        self.add_widget(self.buttomLeftGrid)
        self.add_widget(self.buttomMiddleGrid)
        self.add_widget(self.buttomRightGrid)
        
        self.buttons = GridLayout()                     # Adding buttons to main Grid
        self.buttons.cols= 2

        self.solveBtn = Button(text='Solve',on_press=(self.solvePuzzle))
        self.buttons.add_widget(self.solveBtn)
        
        self.restartBtn = Button(text='Restart',on_press=self.restart)
        self.buttons.add_widget(self.restartBtn)
        
        self.add_widget(self.buttons)

        
    # Restart Button    
    def restart(self,instace):
        boxVals= [self.bx1,self.bx2,self.bx3,self.bx4,self.bx5,self.bx6,self.bx7,self.bx8,self.bx9,
                  self.bx10,self.bx11,self.bx12,self.bx13,self.bx14,self.bx15,self.bx16,self.bx17,self.bx18,
                  self.bx19,self.bx20,self.bx21,self.bx22,self.bx23,self.bx24,self.bx25,self.bx26,self.bx27,
                  self.bx28,self.bx29,self.bx30,self.bx31,self.bx32,self.bx33,self.bx34,self.bx35,self.bx36,
                  self.bx37,self.bx38,self.bx39,self.bx40,self.bx41,self.bx42,self.bx43,self.bx44,self.bx45,
                  self.bx46,self.bx47,self.bx48,self.bx49,self.bx50,self.bx51,self.bx52,self.bx53,self.bx54,
                  self.bx55,self.bx56,self.bx57,self.bx58,self.bx59,self.bx60,self.bx61,self.bx62,self.bx63,
                  self.bx64,self.bx65,self.bx66,self.bx67,self.bx68,self.bx69,self.bx70,self.bx71,self.bx72,
                  self.bx73,self.bx74,self.bx75,self.bx76,self.bx77,self.bx78,self.bx79,self.bx80,self.bx81]
        
        for box in boxVals:
            box.text = '0'

    # Provide the solution to the puzzle
    def solvePuzzle(self,instance):
        # Obtain the correct puzzle
        boxValsInt = [
            [int(self.bx1.text),int(self.bx2.text),int(self.bx3.text),int(self.bx4.text),int(self.bx5.text),int(self.bx6.text),int(self.bx7.text),int(self.bx8.text),int(self.bx9.text)],
            [int(self.bx10.text), int(self.bx11.text), int(self.bx12.text), int(self.bx13.text), int(self.bx14.text), int(self.bx15.text), int(self.bx16.text), int(self.bx17.text), int(self.bx18.text)],
            [int(self.bx19.text), int(self.bx20.text), int(self.bx21.text), int(self.bx22.text), int(self.bx23.text), int(self.bx24.text), int(self.bx25.text), int(self.bx26.text), int(self.bx27.text)],
            [int(self.bx28.text), int(self.bx29.text), int(self.bx30.text), int(self.bx31.text), int(self.bx32.text), int(self.bx33.text), int(self.bx34.text), int(self.bx35.text), int(self.bx36.text)],
            [int(self.bx37.text), int(self.bx38.text), int(self.bx39.text), int(self.bx40.text), int(self.bx41.text), int(self.bx42.text), int(self.bx43.text), int(self.bx44.text), int(self.bx45.text)],
            [int(self.bx46.text), int(self.bx47.text), int(self.bx48.text), int(self.bx49.text), int(self.bx50.text), int(self.bx51.text), int(self.bx52.text), int(self.bx53.text), int(self.bx54.text)],
            [int(self.bx55.text), int(self.bx56.text), int(self.bx57.text), int(self.bx58.text), int(self.bx59.text), int(self.bx60.text), int(self.bx61.text), int(self.bx62.text), int(self.bx63.text)],
            [int(self.bx64.text), int(self.bx65.text), int(self.bx66.text), int(self.bx67.text), int(self.bx68.text), int(self.bx69.text), int(self.bx70.text), int(self.bx71.text), int(self.bx72.text)],
            [int(self.bx73.text), int(self.bx74.text), int(self.bx75.text), int(self.bx76.text), int(self.bx77.text), int(self.bx78.text), int(self.bx79.text), int(self.bx80.text), int(self.bx81.text)]
        ]
        # TroubleSooting
        for i in boxValsInt:
            for j in i:
                print(type(j))
        print(boxValsInt)

        solution = sudokuSolver.solve_sudoku(boxValsInt)
        boxVals = [self.bx1,self.bx2,self.bx3,self.bx4,self.bx5,self.bx6,self.bx7,self.bx8,self.bx9,
                  self.bx10,self.bx11,self.bx12,self.bx13,self.bx14,self.bx15,self.bx16,self.bx17,self.bx18,
                  self.bx19,self.bx20,self.bx21,self.bx22,self.bx23,self.bx24,self.bx25,self.bx26,self.bx27,
                  self.bx28,self.bx29,self.bx30,self.bx31,self.bx32,self.bx33,self.bx34,self.bx35,self.bx36,
                  self.bx37,self.bx38,self.bx39,self.bx40,self.bx41,self.bx42,self.bx43,self.bx44,self.bx45,
                  self.bx46,self.bx47,self.bx48,self.bx49,self.bx50,self.bx51,self.bx52,self.bx53,self.bx54,
                  self.bx55,self.bx56,self.bx57,self.bx58,self.bx59,self.bx60,self.bx61,self.bx62,self.bx63,
                  self.bx64,self.bx65,self.bx66,self.bx67,self.bx68,self.bx69,self.bx70,self.bx71,self.bx72,
                  self.bx73,self.bx74,self.bx75,self.bx76,self.bx77,self.bx78,self.bx79,self.bx80,self.bx81]
        boxValCounter = 0

        if solution is str:
            print('Invalid Puzzle')

        else:
            for x in range(9):
                for y in range(9):
                    print(f'({x},{y} is {solution[x][y]})')
                    boxVals[boxValCounter].text = str(solution[x][y])
                    boxValCounter+=1


class MyApp(App):
    def build(self):
        return MyGridLayout()
    
if __name__ == '__main__':
    app = MyApp()
    app.run()