import qrcode

def generate_qr_code(data, filename="qrcode.png", version=1, box_size=10, border=4):
    """
    Generate a QR code from input data and save as image
    
    Parameters:
    data (str): Data to encode in QR code
    filename (str): Output filename (default: qrcode.png)
    version (int): QR code version (1-40, default: 1)
    box_size (int): Size of each box in pixels (default: 10)
    border (int): Border thickness in boxes (default: 4)
    """
    try:
        # Create QR code instance
        qr = qrcode.QRCode(
            version=version,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=box_size,
            border=border,
        )

        # Add data
        qr.add_data(data)
        qr.make(fit=True)

        # Create image and save
        img = qr.make_image(fill_color="black", back_color="white")
        img.save(filename)
        
        print(f"QR code generated successfully! Saved as {filename}")
        return True

    except Exception as e:
        print(f"Error generating QR code: {e}")
        return False

# Example usage
if __name__ == "__main__":
    input_data = input("Enter text/URL to encode: ") or "https://www.example.com"
    output_file = input("Enter output filename (default: qrcode.png): ") or "qrcode.png"
    
    generate_qr_code(
        data=input_data,
        filename=output_file,
        version=1,
        box_size=10,
        border=4
    )