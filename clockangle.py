import tkinter
import math

file = open("testfile.txt","r")
for line in file:
	if(len(line) == 6):
		if(line[5] == '\n'):
			if(line[0].isdigit() and line[1].isdigit() and line[3].isdigit() and line[4].isdigit() or (line[0] == 2 and line[1] == 4)):
				
				minute = int(line[3]+line[4])
				minDeg = 6*minute
				minAngle = (minDeg*math.pi)/180
				miny = 130 - (90*math.cos(minAngle))
				minx = (90*math.sin(minAngle)) + 150
				
				hour = int(line[0]+line[1])
				hrDeg = 0.5*(60*hour+minute)
				hrAngle = (hrDeg*math.pi)/180
				hry = 130 - (70*math.cos(hrAngle))
				hrx = (70*math.sin(hrAngle)) + 150
				
				realHour = hour
				if(hour>12):
					hour-=12
				
				if(hour <= 12 and minute <= 60):
					top = tkinter.Tk()
					C = tkinter.Canvas(top, height=300, width=300)
					coord = 10, 50, 240, 210
					oval = C.create_oval(30, 10, 270, 250, width=2)
			
					line = C.create_line(150, 15, 150, 20, width = 3)
					canvas_id = C.create_text(143, 20, anchor="nw")
					C.itemconfig(canvas_id, text="12")
			
					line = C.create_line(263, 130, 268, 130, width = 3)
					canvas_id = C.create_text(255, 124, anchor="nw")
					C.itemconfig(canvas_id, text="3")
			
					line = C.create_line(150, 242, 150, 247, width = 3)
					canvas_id = C.create_text(147, 227, anchor="nw")
					C.itemconfig(canvas_id, text="6")
			
					line = C.create_line(34, 130, 39, 130, width = 3)
					canvas_id = C.create_text(42, 124, anchor="nw")
					C.itemconfig(canvas_id, text="9")
			
			
					btAngle = math.fabs(minDeg-hrDeg)
					if(btAngle>180):
						btAngle = 360 - btAngle
					canvas_id = C.create_text(20, 275, anchor="nw")
					C.itemconfig(canvas_id, text="Angle : "+str(btAngle))
					
					if(realHour<10 and minute>10):
						canvas_id = C.create_text(200, 275, anchor="nw")
						C.itemconfig(canvas_id, text="Time : 0"+str(realHour)+":"+str(minute))
					elif(realHour<10 and minute<10):
						canvas_id = C.create_text(200, 275, anchor="nw")
						C.itemconfig(canvas_id, text="Time : 0"+str(realHour)+":0"+str(minute))
					elif(realHour>10 and minute<10):
						canvas_id = C.create_text(200, 275, anchor="nw")
						C.itemconfig(canvas_id, text="Time : "+str(realHour)+":0"+str(minute))
					elif(realHour>10 and minute>10):
						canvas_id = C.create_text(200, 275, anchor="nw")
						C.itemconfig(canvas_id, text="Time : "+str(realHour)+":"+str(minute))
				
					line = C.create_line(hrx, hry, 150, 130, width = 10, fill="Red")
					line = C.create_line(minx, miny, 150, 130, width = 8, fill="Blue")
					oval = C.create_oval(140, 120, 160, 140, width=2, fill="Black")
				
					C.pack()
				else:
					top = tkinter.Tk()
					C = tkinter.Canvas(top, height=300, width=300)
					canvas_id = C.create_text(130, 124, anchor="nw")
					C.itemconfig(canvas_id, text="Error: "+line)
					C.pack()
	elif(len(line) == 5):
		if(line[0].isdigit() and line[1].isdigit() and line[3].isdigit() and line[4].isdigit() or (line[0] == 2 and line[1] == 4)):
				
				minute = int(line[3]+line[4])
				minDeg = 6*minute
				minAngle = (minDeg*math.pi)/180
				miny = 130 - (90*math.cos(minAngle))
				minx = (90*math.sin(minAngle)) + 150
				
				hour = int(line[0]+line[1])
				hrDeg = 0.5*(60*hour+minute)
				hrAngle = (hrDeg*math.pi)/180
				hry = 130 - (70*math.cos(hrAngle))
				hrx = (70*math.sin(hrAngle)) + 150
				realHour = hour
				if(hour>12):
					hour-=12
				#print (hour)
				#print (minute)
				if(hour <= 12 and minute <= 60):
					top = tkinter.Tk()
					C = tkinter.Canvas(top, height=300, width=300)
					coord = 10, 50, 240, 210
					oval = C.create_oval(30, 10, 270, 250, width=2)
			
					line = C.create_line(150, 15, 150, 20, width = 3)
					canvas_id = C.create_text(143, 20, anchor="nw")
					C.itemconfig(canvas_id, text="12")
			
					line = C.create_line(263, 130, 268, 130, width = 3)
					canvas_id = C.create_text(255, 124, anchor="nw")
					C.itemconfig(canvas_id, text="3")
			
					line = C.create_line(150, 242, 150, 247, width = 3)
					canvas_id = C.create_text(147, 227, anchor="nw")
					C.itemconfig(canvas_id, text="6")
			
					line = C.create_line(34, 130, 39, 130, width = 3)
					canvas_id = C.create_text(42, 124, anchor="nw")
					C.itemconfig(canvas_id, text="9")
			
			
					btAngle = math.fabs(minDeg-hrDeg)
					if(btAngle>180):
						btAngle = 360 - btAngle
					canvas_id = C.create_text(20, 275, anchor="nw")
					C.itemconfig(canvas_id, text="Angle : "+str(btAngle))
				
					line = C.create_line(hrx, hry, 150, 130, width = 10, fill="Red")
					line = C.create_line(minx, miny, 150, 130, width = 8, fill="Blue")
					oval = C.create_oval(140, 120, 160, 140, width=2, fill="Black")
				
					if(realHour<10 and minute>10):
						canvas_id = C.create_text(200, 275, anchor="nw")
						C.itemconfig(canvas_id, text="Time : 0"+str(realHour)+":"+str(minute))
					elif(realHour<10 and minute<10):
						canvas_id = C.create_text(200, 275, anchor="nw")
						C.itemconfig(canvas_id, text="Time : 0"+str(realHour)+":0"+str(minute))
					elif(realHour>10 and minute<10):
						canvas_id = C.create_text(200, 275, anchor="nw")
						C.itemconfig(canvas_id, text="Time : "+str(realHour)+":0"+str(minute))
					elif(realHour>10 and minute>10):
						canvas_id = C.create_text(200, 275, anchor="nw")
						C.itemconfig(canvas_id, text="Time : "+str(realHour)+":"+str(minute))
				
					C.pack()
				else:
					top = tkinter.Tk()
					C = tkinter.Canvas(top, height=300, width=300)
					canvas_id = C.create_text(130, 124, anchor="nw")
					C.itemconfig(canvas_id, text="Error: "+line)
					C.pack()
	
	else:
		top = tkinter.Tk()
		C = tkinter.Canvas(top, height=300, width=300)
		canvas_id = C.create_text(130, 124, anchor="nw")
		C.itemconfig(canvas_id, text="Error: "+line)
		C.pack()
		
top.mainloop()
	