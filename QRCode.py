#---------------------------
# Name: Lauren McMullen
# Program: QRCode.py
#---------------------------
# Purpose: This script uses the qrcode library to 
#          generate a simple QR Code for user inputted 
#          data. I have created this script for use in 
#          in marketing roles to allow my clients and multimedia projects
#          to make use of QR codes without paying fees.
#---------------------------
# Credied to:
# https://www.geeksforgeeks.org/generate-qr-code-using-qrcode-in-python/
#    and 
# https://pypi.org/project/qrcode/
# for the tutorials and documentiation for this script. 
#---------------------------

# Importing library
import qrcode
from PIL import Image

#----------------------------------------------------------------------------------------------------------------------
# Define makeQRCode:
    # This function creates the base QR code 
def generateQRBase(link, fileName):

    # Data to be encoded
    data = link 
    
    # Creating an instance of QRCode class
    qr = qrcode.QRCode(version = 10, box_size = 10, border = 3)
  
    # Adding data to the instance 'qr'
    qr.add_data(data)
    qr.make(fit = True)
    
    # QR colours
    img = qr.make_image(fill_color = (0,0,0), back_color = (139,35,50))
        
    return img

#----------------------------------------------------------------------------------------------------------------------

# Define prepareLogo
    # This function adjsust the logo to be added to the QR Code Base
def prepareLogo(img,centreimage):
    logo = Image.open(centreimage)
    basewidth = 100
    wpercent = (basewidth/float(logo.size[0]))
    hsize = int((float(logo.size[1])*float(wpercent)))
    logo = logo.resize((basewidth * 4, hsize * 4), Image.ANTIALIAS)
    img = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)
    return logo

#----------------------------------------------------------------------------------------------------------------------
# Manager function
    # Add desired QR link, desired save file name (.png), and file name of the logo in quotation marks, seperated by a comma
def makeQRCode(link, fileName, centreImage):
    img = generateQRBase(link, fileName) 
    
    #-------------------------------------------------------------
    # Optional Logo Add (do not use transparent backgrounds
    logo = prepareLogo(img, centreImage)
    # Find pos for logo 
    pos = ((img.size[0] - logo.size[0]) // 2, (img.size[1] - logo.size[1]) // 2)
    img.paste(logo, pos)
    #-------------------------------------------------------------

    
    # Saving as an image file
    img.show()
    #img.save(fileName)    
    return
#----------------------------------------------------------------------------------------------------------------------

makeQRCode("MacEwan.ca/sce/","Sixty-OneTenQR.png", "ConEd_logo_11x17horwhite.png") 


