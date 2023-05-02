# Колун Дэнилэ 373732 (Вар 2)

import time
import cv2



# Первое задание

def gaussian():

    image = cv2.imread('images/variant-2.png')

    width = 800
    height = 600

    resolution = cv2.resize(image, (width, height), interpolation=cv2.INTER_LINEAR)
    image_blur = cv2.GaussianBlur(resolution, (15, 15), 0)

    cv2.imshow('img_blur_15', image_blur)


# Второе задание + доп. задание

def video_detect():

    points = (640, 480)
    capture = cv2.VideoCapture(0)
    file = open('coordinates.txt', 'w')
    coordinates = []
    i = 0

    image = cv2.imread('fly64.png')
    image = cv2.resize(image, (32, 32))
    image_height, image_width, _ = image.shape

    while True:
        rectangular, frame = capture.read()
        if not rectangular:
            break

        frame = cv2.resize(frame, points, interpolation=cv2.INTER_LINEAR)

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (21, 21), 0)

        rectangular, thresh = cv2.threshold(gray, 110, 255, cv2.THRESH_BINARY_INV)

        contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

        if len(contours) > 0:

            c = max(contours, key=cv2.contourArea)
            x, y, w, h = cv2.boundingRect(c)

            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            center = ((int(x + (w // 2) - 16)), int(y + (h // 2) - 16))

            xcenter = center[0]
            ycenter = center[1]

            frame[ycenter:ycenter + image_height, xcenter:xcenter + image_width] = image

            if i % 5 == 0:

                a = x + (w // 2)
                b = y + (h // 2)

                coordinates.append(a)
                coordinates.append(b)

                print(a, b)

                file.write(str(coordinates) + '\n')
                coordinates.clear()

        cv2.imshow('frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        time.sleep(0.1)
        i += 1

    capture.release()


if __name__ == '__main__':
    gaussian()
    video_detect()
    cv2.waitKey(0)
    cv2.destroyAllWindows()