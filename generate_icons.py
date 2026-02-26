#!/usr/bin/env python3
"""
Shopath Android App - PNG Icon Generator
सभी mipmap sizes के लिए PNG icons बनाता है
"""

import os
import struct
import zlib

def create_png(width, height, r, g, b):
    """Simple PNG creator without external dependencies"""
    
    def png_chunk(chunk_type, data):
        chunk_len = len(data)
        chunk_data = chunk_type + data
        return (struct.pack('>I', chunk_len) + chunk_data + 
                struct.pack('>I', zlib.crc32(chunk_data) & 0xffffffff))
    
    # PNG signature
    signature = b'\x89PNG\r\n\x1a\n'
    
    # IHDR chunk
    ihdr_data = struct.pack('>IIBBBBB', width, height, 8, 2, 0, 0, 0)
    ihdr = png_chunk(b'IHDR', ihdr_data)
    
    # Image data - draw shopping bag icon on orange background
    raw_data = b''
    for y in range(height):
        raw_data += b'\x00'  # filter type
        for x in range(width):
            # Normalized coordinates
            nx = x / width
            ny = y / height
            
            # Orange background
            pr, pg, pb = r, g, b
            
            # Draw white shopping bag shape
            cx, cy = 0.5, 0.52
            
            # Bag body (rectangle)
            bx1, by1 = 0.25, 0.42
            bx2, by2 = 0.75, 0.78
            
            # Bag handle (arch)
            hx1, hy1 = 0.35, 0.28
            hx2, hy2 = 0.65, 0.44
            hthick = 0.08
            
            in_body = bx1 <= nx <= bx2 and by1 <= ny <= by2
            
            # Handle arch calculation
            hmx = (hx1 + hx2) / 2
            hmy = hy2
            hradius_x = (hx2 - hx1) / 2
            hradius_y = (hy2 - hy1)
            
            # Outer handle
            if hradius_x > 0 and hradius_y > 0:
                outer = ((nx - hmx) / hradius_x)**2 + ((ny - hmy) / hradius_y)**2
                inner = ((nx - hmx) / (hradius_x - hthick))**2 + ((ny - hmy) / (hradius_y - hthick))**2 if (hradius_x - hthick) > 0 and (hradius_y - hthick) > 0 else 999
            else:
                outer = 999
                inner = 999
            
            in_handle = (outer <= 1.0 and inner >= 1.0 and ny <= hmy)
            
            if in_body or in_handle:
                pr, pg, pb = 255, 255, 255  # white
            
            raw_data += bytes([pr, pg, pb])
    
    # Compress image data
    compressed = zlib.compress(raw_data)
    idat = png_chunk(b'IDAT', compressed)
    
    # IEND chunk
    iend = png_chunk(b'IEND', b'')
    
    return signature + ihdr + idat + iend

# Shopath Orange color
ORANGE_R, ORANGE_G, ORANGE_B = 255, 107, 53  # #FF6B35

# Icon sizes for each density
SIZES = {
    'mipmap-mdpi':    48,
    'mipmap-hdpi':    72,
    'mipmap-xhdpi':   96,
    'mipmap-xxhdpi':  144,
    'mipmap-xxxhdpi': 192,
}

base_path = '/var/www/shopath-android/app/src/main/res'

for folder, size in SIZES.items():
    folder_path = os.path.join(base_path, folder)
    os.makedirs(folder_path, exist_ok=True)
    
    png_data = create_png(size, size, ORANGE_R, ORANGE_G, ORANGE_B)
    
    # ic_launcher.png
    with open(os.path.join(folder_path, 'ic_launcher.png'), 'wb') as f:
        f.write(png_data)
    
    # ic_launcher_round.png (same icon)
    with open(os.path.join(folder_path, 'ic_launcher_round.png'), 'wb') as f:
        f.write(png_data)
    
    print(f"✅ {folder}: {size}x{size}px icons created")

print("\n🎉 सभी mipmap PNG icons तैयार हैं!")
