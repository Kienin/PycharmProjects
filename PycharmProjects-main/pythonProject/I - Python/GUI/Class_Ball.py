class Ball:

    def __init__(self, canvas, x, y, diameter, X_VELOCITY, Y_VELOCITY, color):
        self.canvas = canvas
        self.image = canvas.create_oval(x, y, diameter, diameter, fill= color)
        self.X_VELOCITY = X_VELOCITY
        self.Y_VELOCITY = Y_VELOCITY

    def move(self):
        coordinates = self.canvas.coords(self.image)
        #print(coordinates)

        if(coordinates[2]>=(self.canvas.winfo_width()) or coordinates[0]<0):
            self.X_VELOCITY = -self.X_VELOCITY
        if (coordinates[3] >= (self.canvas.winfo_height()) or coordinates[1] < 0):
            self.Y_VELOCITY = -self.Y_VELOCITY
        self.canvas.move(self.image, self.X_VELOCITY, self.Y_VELOCITY)
