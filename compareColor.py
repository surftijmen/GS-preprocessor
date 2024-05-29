import cv2
import numpy as np
from skimage.metrics import structural_similarity as ssim
from skimage.color import rgb2lab, deltaE_cie76

# Load images
original = cv2.imread('comparison-input/normal.png')
recolored1 = cv2.imread('comparison-input/color.png')
recolored2 = cv2.imread('comparison-input/outputColor.png')
recolored3 = cv2.imread('comparison-input/recolored.png')

# Convert images to LAB color space for Delta E calculation
original_lab = cv2.cvtColor(original, cv2.COLOR_BGR2LAB)
recolored1_lab = cv2.cvtColor(recolored1, cv2.COLOR_BGR2LAB)
recolored2_lab = cv2.cvtColor(recolored2, cv2.COLOR_BGR2LAB)
recolored3_lab = cv2.cvtColor(recolored3, cv2.COLOR_BGR2LAB)

# Calculate Delta E
delta_e1 = np.mean(deltaE_cie76(original_lab, recolored1_lab))
delta_e2 = np.mean(deltaE_cie76(original_lab, recolored2_lab))
delta_e3 = np.mean(deltaE_cie76(original_lab, recolored3_lab))

# Calculate SSIM with a smaller window size and specifying the channel axis
ssim1, _ = ssim(original, recolored1, full=True, multichannel=True, win_size=3, channel_axis=2)
ssim2, _ = ssim(original, recolored2, full=True, multichannel=True, win_size=3, channel_axis=2)
ssim3, _ = ssim(original, recolored3, full=True, multichannel=True, win_size=3, channel_axis=2)

# Calculate PSNR
psnr1 = cv2.PSNR(original, recolored1)
psnr2 = cv2.PSNR(original, recolored2)
psnr3 = cv2.PSNR(original, recolored3)

print(f"Delta E (Method 1): {delta_e1}")
print(f"Delta E (Method 2): {delta_e2}")
print(f"Delta E (Method 3): {delta_e3}")
print(f"SSIM (Method 1): {ssim1}")
print(f"SSIM (Method 2): {ssim2}")
print(f"SSIM (Method 3): {ssim3}")
print(f"PSNR (Method 1): {psnr1}")
print(f"PSNR (Method 2): {psnr2}")
print(f"PSNR (Method 3): {psnr3}")
