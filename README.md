
Using the images from "deskewed/" as a starting point;

1. Gaussian blur
2. Otsu Binarization

This will clean up the lines an make it easier to find the corners next...

    
    
    
FILES:    
fine_crop
    purpose: to manually inspect the top left corner identification and decide whether to crop the image.
    status: Used what I've learned so far to identify the top corners, rotate the image the way I want and crop off the edges
            in preparation for the next stage of slicing the images out.
    
detect_top_corners_and_rotate
    purpose: try to get a cleaner alignment by first detecting the top corners and then rotate so they share the same y-value.
status: 
    
top_left_corner_coordinate
    purpose: attempt to understand how to locate the top left corner
    status: Use the code in other steps, but don't use as a standalone script.
    
rotate
    purpose: an attempt to rotate and align the images automatically
    status: Don't use. Doesn't work as well as I had hoped. I need a better way to identify the proper rotation angle.
    
corner_detection
    purpose: trying to understand how to use the harris corner detector (and others)
    status: Don't use except for seeing the effects. Not useful as it is.
