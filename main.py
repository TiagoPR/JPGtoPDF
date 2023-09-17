import os
from PIL import Image
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# Function to convert a folder of images into a PDF
def convert_folder_to_pdf(folder_path, pdf_path):
    images = []
    
    # Get a list of image files in the folder
    for filename in os.listdir(folder_path):
        if filename.endswith(".jpg"):
            img_path = os.path.join(folder_path, filename)
            images.append(img_path)
    
    if not images:
        print(f"No JPG images found in {folder_path}")
        return
    
    # Sort the images by filename
    images.sort()
    
    # Create a PDF from the sorted images
    c = canvas.Canvas(pdf_path, pagesize=letter)
    for img_path in images:
        img = Image.open(img_path)
        img_width, img_height = img.size
        c.setPageSize((img_width, img_height))
        c.drawImage(img_path, 0, 0, width=img_width, height=img_height)
        c.showPage()
    
    c.save()
    print(f"PDF saved to {pdf_path}")

# Specify the root folder containing subfolders with JPGs
root_folder = "/home/tiago/Tiago/Mangas/nurarihyon"

# Iterate through subfolders and convert each one to a PDF
for subfolder in os.listdir(root_folder):
    subfolder_path = os.path.join(root_folder, subfolder)
    if os.path.isdir(subfolder_path):
        pdf_name = f"{subfolder}.pdf"
        pdf_path = os.path.join(root_folder, pdf_name)
        convert_folder_to_pdf(subfolder_path, pdf_path)
