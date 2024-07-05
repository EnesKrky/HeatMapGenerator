# HeatMapGenerator
This code creating UI by using pygame module is used to create heat map of a given function.<br />
<br />
---Controls---<br />
m: Changes visualization type.<br />
q: Closes the program.<br />
c: Closes and opens contour.<br />
Enter: Submits changed function when new function is written.<br />
Mouse First Button:<br />
-It is used to select the function.<br />
-When it is low resolution and mouse cursor is on the map, you can drag the map by holding the button.<br />
-It can be used instead of enter by clicking once.<br />
Mouse Wheel:<br />
-When it is high resolution or when it is low resolution and mouse cursor is out of the map, it only changes which value contour is shown at.<br />
-When it is low resolution and mouse cursor is on the map, it zooms in or out the map.<br />
<br />
---Notes---<br />
-Function must be entered regarding to syntax of python. Otherwise, the code doesn't consider it.
-I suggest you that if there are singular points of your function, avoid them for the code not to give error while dragging and zooming out.
-If your key combinations are different for slash and brackets, you can change them in lines 319, 325, and 331. Even, you can add new keys combined with shift.
