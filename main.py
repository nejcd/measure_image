import cv2
import numpy as np

drawing = False
vertices = []
scaling_line = []
scaling_length = 0

def draw_polygon(image, vertices):
    pts = np.array(vertices, np.int32)
    pts = pts.reshape((-1, 1, 2))
    cv2.polylines(image, [pts], True, (0, 255, 0), 2)


def polygon_area(vertices):
    return 0.5 * np.abs(np.dot(vertices[:, 0], np.roll(vertices[:, 1], 1)) - np.dot(vertices[:, 1], np.roll(vertices[:, 0], 1)))

def euclidean_distance(pt1, pt2):
    return np.sqrt((pt1[0] - pt2[0])**2 + (pt1[1] - pt2[1])**2)

def mouse_callback(event, x, y, flags, param):
    global drawing, vertices, scaling_line

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True

        if len(scaling_line) < 2:
            scaling_line.append((x, y))
        else:
            vertices.append((x, y))

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False

        if len(scaling_line) == 2:
            cv2.line(image, scaling_line[0], scaling_line[1], (0, 0, 255), 2)
            cv2.imshow('Image with polygon', image)
        elif len(vertices) > 1:
            cv2.line(image, vertices[-2], vertices[-1], (0, 255, 0), 2)
            cv2.imshow('Image with polygon', image)

def main():
    global image, scaling_length

    # Read the image
    image_path = 'data/test.jpeg'
    image = cv2.imread(image_path)

    # Get the length of the scale from the user
    scaling_length = float(input("Enter the length of the scale: "))

    # Create a window and set the mouse callback function
    cv2.namedWindow('Image with polygon')
    cv2.setMouseCallback('Image with polygon', mouse_callback)

    # Display the image
    cv2.imshow('Image with polygon', image)

    # Wait for a key press
    while True:
        key = cv2.waitKey(1) & 0xFF

        if key == 13:  # Enter key to close the polygon and calculate the area
            if len(vertices) > 2:
                cv2.line(image, vertices[-1], vertices[0], (0, 255, 0), 2)
                draw_polygon(image, vertices)
                cv2.imshow('Image with polygon', image)

                break

        if key == 27:  # ESC key to exit
            break

    while True:
        key = cv2.waitKey(1) & 0xFF

        if key == 13:  # Enter key to close the polygon
            if len(vertices) > 2:
                cv2.line(image, vertices[-1], vertices[0], (0, 255, 0), 2)
                draw_polygon(image, vertices)
                cv2.imshow('Image with polygon', image)
                area_pixels = polygon_area(np.array(vertices))
                dist = euclidean_distance(scaling_line[0], scaling_line[1])
                scaling_factor = scaling_length / dist
                print(f'scaling_length: {scaling_length}, pixle distance: {dist}, scaling: {scaling_factor}')
                area_calibrated = area_pixels * scaling_factor**2

                print(f"Polygon area: {area_pixels} pixels, {area_calibrated} calibrated units")
                break

        if key == 27:  # ESC key to exit
            break

    # Close the window
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
