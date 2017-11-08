# Created by: Mr. Coxall
# Created on: Sep 2016
# Created for: ICS3U
# This program, shows a cartoon walking

import ui
import time

# first get a reference to the image you saved in your Python folder
walking_man_image = ui.Image.named('./assests/sprites/image1.BMP')
walking_man_imageview = ui.ImageView(frame=(30, 0, 180, 180))
walking_man_imageview.image = walking_man_image

@ui.in_background

def start_button_touch_up_inside(sender):
    image_counter = 1
    while image_counter <= 10:
        if image_counter == 1:
            walking_man_image = ui.Image.named('./assests/sprites/image1.BMP')
            walking_man_imageview.image = walking_man_image
        elif image_counter == 2:
            walking_man_image = ui.Image.named('./assests/sprites/image2.BMP')
            walking_man_imageview.image = walking_man_image
        elif image_counter == 3:
            walking_man_image = ui.Image.named('./assests/sprites/image3.BMP')
            walking_man_imageview.image = walking_man_image
        elif image_counter == 4:
            walking_man_image = ui.Image.named('./assests/sprites/image4.BMP')
            walking_man_imageview.image = walking_man_image
        elif image_counter == 5:
            walking_man_image = ui.Image.named('./assests/sprites/image5.BMP')
            walking_man_imageview.image = walking_man_image
        elif image_counter == 6:
            walking_man_image = ui.Image.named('./assests/sprites/image6.BMP')
            walking_man_imageview.image = walking_man_image
        elif image_counter == 7:
            walking_man_image = ui.Image.named('./assests/sprites/image7.BMP')
            walking_man_imageview.image = walking_man_image
        elif image_counter == 8:
            walking_man_image = ui.Image.named('./assests/sprites/image8.BMP')
            walking_man_imageview.image = walking_man_image
        elif image_counter == 9:
            walking_man_image = ui.Image.named('./assests/sprites/image9.BMP')
            walking_man_imageview.image = walking_man_image
        elif image_counter == 10:
            walking_man_image = ui.Image.named('./assests/sprites/image10.BMP')
            walking_man_imageview.image = walking_man_image
    
        # now wait for a fraction of second
        time.sleep(2.0/30.0)
        
        image_counter = image_counter + 1
        if image_counter == 10:
            image_counter = 1
        #print(image_counter)
        #view.set_needs_display()

view = ui.load_view()

# lastly, add the Imageview into the existing view
view.add_subview(walking_man_imageview)

view.present('sheet')

