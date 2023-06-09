{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "image segmentation  using OpenCV"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [],
   "source": [
    "import cv2\n",
    "import numpy as np\n",
    "# Draw rectangle based on the input selection\n",
    "def draw_rectangle(event, x, y, flags, params):\n",
    "    global x_init, y_init, drawing, top_left_pt, bottom_right_pt,img_orig\n",
    "    # Detecting mouse button down event\n",
    "    if event == cv2.EVENT_LBUTTONDOWN:\n",
    "        drawing = True\n",
    "        x_init, y_init = x, y\n",
    "        # Detecting mouse movement\n",
    "    elif event == cv2.EVENT_MOUSEMOVE:\n",
    "        if drawing:\n",
    "            top_left_pt, bottom_right_pt = (x_init,y_init), (x,y)\n",
    "            img[y_init:y, x_init:x] = 255 - img_orig[y_init:y,\n",
    "            x_init:x]\n",
    "            cv2.rectangle(img, top_left_pt, bottom_right_pt,\n",
    "            (0,255,0), 2)\n",
    "            # Detecting mouse button up event\n",
    "    elif event == cv2.EVENT_LBUTTONUP:\n",
    "        drawing = False\n",
    "        top_left_pt, bottom_right_pt = (x_init,y_init), (x,y)\n",
    "        img[y_init:y, x_init:x] = 255 - img[y_init:y, x_init:x]\n",
    "        cv2.rectangle(img, top_left_pt, bottom_right_pt,\n",
    "        (0,255,0), 2)\n",
    "        rect_final = (x_init, y_init, x-x_init, y-y_init)\n",
    "        # Run Grabcut on the region of interest\n",
    "        run_grabcut(img_orig, rect_final)\n",
    "        # Grabcut algorithm\n",
    "def run_grabcut(img_orig, rect_final):\n",
    "# Initialize the mask\n",
    "    mask = np.zeros(img_orig.shape[:2],np.uint8)\n",
    "    # Extract the rectangle and set the region of\n",
    "    # interest in the above mask\n",
    "    x,y,w,h = rect_final\n",
    "\n",
    "    mask[y:y+h, x:x+w] = 1\n",
    "    # Initialize background and foreground models\n",
    "    bgdModel = np.zeros((1,65), np.float64)\n",
    "    fgdModel = np.zeros((1,65), np.float64)\n",
    "    # Run Grabcut algorithm\n",
    "    cv2.grabCut(img_orig, mask, rect_final, bgdModel, fgdModel, 5,\n",
    "    cv2.GC_INIT_WITH_RECT)\n",
    "    # Extract new mask\n",
    "    mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')\n",
    "    # Apply the above mask to the image\n",
    "    img_orig = img_orig*mask2[:,:,np.newaxis]\n",
    "    # Display the image\n",
    "    cv2.imshow('Output', img_orig)\n",
    "if __name__=='__main__':\n",
    "    drawing = False\n",
    "    top_left_pt, bottom_right_pt = (-1,-1), (-1,-1)\n",
    "    # Read the input image\n",
    "    img_orig = cv2.imread(\"D://OpenCV//sundarpichai.jpg\")\n",
    "    img_orig = cv2.resize( img_orig ,(500,500))\n",
    "    img = img_orig.copy()\n",
    "    cv2.namedWindow('Input')\n",
    "    cv2.setMouseCallback('Input', draw_rectangle)\n",
    "    while True:\n",
    "        cv2.imshow('Input', img)\n",
    "        c = cv2.waitKey(1)\n",
    "        if c == 27:\n",
    "            break\n",
    "    cv2.destroyAllWindows()"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
