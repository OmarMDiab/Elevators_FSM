from PIL import Image, ImageTk
import os
import tkinter as tk
from visual_automata.fa.nfa import VisualNFA


def animate(obj,input,Destroy_Flag): 
  root = tk.Tk()

  canvas = tk.Canvas(root, width=1920, height=1080,background="white")
  canvas.pack()
  mystring=input
  flag = False
  x=""
  imgno=1
  folder_path = "Images"
  for i in mystring:
    x = x + i
    obj.show_diagram(x,filename="Images\\"+str(imgno))
    if not flag:
        if imgno==8:
           flag=True
        imgno=imgno+1
        
    else:
       imgno="s"+str(imgno)
       flag=True

  photo_dict = {}
  # loop over all the files in the folder
  for i, filename in enumerate(os.listdir(folder_path)):
      if filename.endswith(".png"):
          # load the image and create a PhotoImage object
          img = Image.open(os.path.join(folder_path, filename))
          photo = ImageTk.PhotoImage(img)
          photo_dict[i] = photo
    
  # # create a label widget to display the images
      label = tk.Label(root)
      label.pack()
      label_text = "Symbols: -\nR: Request\np: passengerIn\nP: PassengerOut\nT: Target_Floor\n1: True\n0: False\n( + ): Floor + 1 & ( - ): Floor - 1"
      label_item = canvas.create_text(10, 10, text=label_text, anchor='nw', fill='black', font=('calibri', 15))
    # display each photo in the label widget
  for i in range(len(photo_dict)):
      image_item = canvas.create_image(100,200, image=photo_dict[i], anchor='nw')
      canvas.update()
      root.after(1200)
      # delete the old image item from the canvas
      if i!=len(photo_dict)-1:
       canvas.delete(image_item)
  #
  if Destroy_Flag: 
    root.destroy()
  else:
     root.mainloop()
  #print(photo_dict)



def reset():
    folder_path="Images"
    for filename in os.listdir(folder_path):
        if filename.endswith(".png"):
            os.remove(os.path.join(folder_path, filename))



Elevator_Select = VisualNFA(
    states={"IDLE", "Check", "Elevator_1", "Elevator_2"},
    input_symbols={"R", "0","1"},
    transitions={
        "IDLE": {"R": {"Check"}},
        "Check": {"1": {"Elevator_1"}, "0": {"Elevator_2"}},
        "Elevator_1": {},
        "Elevator_2": {}
    },
    initial_state="IDLE",
    final_states={"Elevator_1", "Elevator_2"},
)

Elevator_FSM = VisualNFA(
    states={"IDLE", "Above_req?","MoveDown(Req)","At_requested","OpenAtReq","MoveUp(Req)","Close_At_Target","CloseAtReq","AboveTarget?","MoveDown","MoveUp","AtTarget?","OpenAtTarget"},
    input_symbols={"R","1","0","p","T","+","-","P","E"},
    transitions={
        "IDLE": {'R': {"Above_req?"}},
        "Above_req?": {"1": {"MoveDown(Req)"}, "0": {"At_requested"}},
        "At_requested": {"1":{"OpenAtReq"},"0":{"MoveUp(Req)"}},
        "MoveUp(Req)": {"+":{"Above_req?"}},
        "MoveDown(Req)": {"-":{"Above_req?"}},
        "OpenAtReq": {"p":{"CloseAtReq"}},
        "CloseAtReq": {"T":{"AboveTarget?"}},
        "AboveTarget?": {"1":{"MoveDown"},"0":{"AtTarget?"}},
        "MoveDown": {"-":{"AboveTarget?"}},
        "MoveUp":{"+":{"AboveTarget?"}},
        "AtTarget?": {"0":{"MoveUp"},"1":{"OpenAtTarget"}},
        "OpenAtTarget": {"P":{"Close_At_Target"}},
        "Close_At_Target":{"E":{"IDLE"}}

    },
    initial_state="IDLE",
    final_states={"OpenAtReq", "OpenAtTarget","IDLE"},

)
#Elevator_FSM.show_diagram: U can configure fig size from here (ctrl + click ==> configure)

# Scenerio 1: sample Use (Arrived At Destination) using elevator 1: -
animate(Elevator_Select,"R1",1)
reset()
animate(Elevator_FSM,"R1-01pT00+01PE",0)

# Scenerio 2: Request elevator 2: -
#animate(Elevator_Select,"R0",1)
#reset()
#animate(Elevator_FSM,"R1-01",0)

# Scenerio 3: error Handling (someone pressed request button while it is already there) -
#Animate(Elevator_Select,"R0",1)
#reset()
#animate(Elevator_FSM,'R01pT01PE',0)

reset()