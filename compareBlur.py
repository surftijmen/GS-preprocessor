import cv2
import numpy as np
from skimage.metrics import structural_similarity as ssim
from skimage.color import rgb2lab, deltaE_cie76

# Load images
original = cv2.imread('comparison-input/blurred.png')
recolored = cv2.imread('comparison-input/deblurred.png')

# Convert images to LAB color space for Delta E calculation
original_lab = cv2.cvtColor(original, cv2.COLOR_BGR2LAB)
recolored_lab = cv2.cvtColor(recolored, cv2.COLOR_BGR2LAB)

# Calculate Delta E
delta_e = np.mean(deltaE_cie76(original_lab, recolored_lab))

# Calculate SSIM with a smaller window size and specifying the channel axis
ssim_value, _ = ssim(original, recolored, full=True, multichannel=True, win_size=3, channel_axis=2)

# Calculate PSNR
psnr_value = cv2.PSNR(original, recolored)

# Generate LaTeX table
latex_table = f"""
\\begin{{table}}[H]
    \\centering
    \\begin{{tabular}}{{|c|c|c|c|}}
        \\hline
        Method & Color Accuracy (Delta E) & SSIM & PSNR \\\\
        \\hline
        Recolored Method & {delta_e:.2f} & {ssim_value:.2f} & {psnr_value:.2f} dB \\\\
        \\hline
    \\end{{tabular}}
    \\caption{{Quantitative comparison of the recoloring method.}}
    \\label{{tab:comparison}}
\\end{{table}}
"""

# Print LaTeX table
print(latex_table)
