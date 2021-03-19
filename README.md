# Basic
1. [Importar librerías ](#schema1)

# 1 Read

2. [Cargar una foto](#schema2)
3. [Cargar un video](#schema3)
4. [Cerrar todas las ventanas](#schema4)

# 2 Rescale
5. [Crear función de redimensionar](#schema5)

# 3. Draw
6. [Pintar un cuadro negro](#schema6)
7. [Pintar un cuadro cualquier color](#schema7)
8. [Pintar un rectágulo](#schema8)
9. [Pintar un cículo](#schema9)
10. [Pintar una línea](#schem10)
11. [Pintar una línea](#schema11)

<hr>

<a name="schema1"></a>

# 1. Importar librerías
En este curso vamos a usar la libreria `cv2`
~~~python
import cv2 as cv
~~~
<hr>

<a name="schema2"></a>

# 2. Cargar una foto
Para cargar una foto vamos a usar la función `.imread()`, la mostraremos con `.imshow("titulo", archivo)` y cuando pulsemo el `0` con la función `.waitKey()`se parará el programa.
~~~python
img = cv.imread("./photos/cat_large.jpg")
cv.imshow("Cat", img)
cv.waitKey(0)
~~~
<hr>

<a name="schema3"></a>

# 3. Cargar un video

La diferencia que hay con la lectura de un video es éste se lee frame a frame por eso hay que hacer un bucle.
~~~python
capture = cv.VideoCapture("./video/dog.mp4")

while True:
    isTrue, frame = capture.read()
    cv.imshow("video", frame)
    if cv.waitKey(20) & 0xFF == ord('d'):
        break
capture.release()
~~~

<hr>

<a name="schema4"></a>

# 4. Cerrar todas las ventanas

~~~python
cv.destroyAllWindows()
~~~
<hr>

<a name="schema5"></a>

## 5. Crear función de redimensionar
En esta función`rescaleFrame` hacemos una resescaldo de las imágenes y vídeos. Los vídeos tanto cargados como vídeos en directo.
~~~python
def rescaleFrame(frame, scale = 0.75):
    # images, videos and live video
    width = int(frame.shape[1] *scale)
    height = int(frame.shape[0] *scale)
    dimension = (width,height)
    return cv.resize(frame, dimension, interpolation = cv.INTER_AREA)

~~~
Con `changeRes` sólo podemos usarlo si son vídeos en directo.
~~~python
def changeRes(width,height):
    #live video
    capture.set(3,width)
    capture.set(4,height)
~~~

<hr>

<a name="schema6"></a>

# 6. Pintar un cuadro negro
~~~python
blank = np.zeros((500,500,3), dtype = "uint8")
cv. imshow("Blank",blank)
~~~
![blank](./images/001.png)
<hr>

<a name="schema7"></a>

# 7. Pintar un cuadro cualquier color
~~~python
blank[:] = 0,255,0 #green
cv.imshow("Green",blank)
~~~
![blank](./images/008.png)

<hr>

<a name="schema8"></a>

# 8. Pintar un rectágulo
Con `cv.rectangle(objet, origin,size, line thickness` pintamos rectágulos
~~~python
cv.rectangle(blank,(0,0), (250,250),(0,255,0), thickness = 3 )
cv.imshow("Rectangle",blank )
~~~
![blank](./images/002.png)

Con `thickness = cv.FILLED` rellenemos el rectágulo, también vale `thickness = -1`
~~~python
#Rectagle filled
cv.rectangle(blank,(0,0), (250,250),(0,255,0), thickness = cv.FILLED ) # same thickness = -1
cv.imshow("Rectangle Filled",blank )
~~~
![blank](./images/003.png)

<hr>

<a name="schema9"></a>

# 9. Pintar un cículo

Con `cv.circle(objet, origin,size, line thickness)`
~~~python

cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2),40, (0,0,250),thickness = -1)
cv.imshow("circle",blank)
~~~
![blank](./images/005.png)
<hr>

<a name="schema10"></a>

# 10. Pintar una línea

~~~python

cv.line(blank, (0,0),(blank.shape[1]//2, blank.shape[0]//2), (255,255,255),thickness = 3)
cv.imshow("line",blank)
~~~
![blank](./images/006.png)

<hr>

<a name="schema11"></a>

# 11. Pintar una línea

~~~python
cv.putText(blank,"Hello",(225,225),cv.FONT_HERSHEY_TRIPLEX, 1.0,(0,255,0),2)
cv.imshow("text", blank)
~~~
![blank](./images/007.png)