# Basic
1. [Importar librerías ](#schema1)

## 1 Read

2. [Cargar una foto](#schema2)
3. [Cargar un video](#schema3)
4. [Cerrar todas las ventanas](#schema4)

## 2 Rescale
5. [Crear función de redimensionar](#schema5)

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