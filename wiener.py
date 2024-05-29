import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from skimage import color, restoration
from scipy.signal import convolve2d as conv2

# Set up the random number generator
rng = np.random.default_rng()

# Load your own image
image_path = 'input/blur.png'  # Update this to the correct path
image = Image.open(image_path).convert('L')  # Convert to grayscale
astro = np.array(image)

# Normalize the image to the range [0, 1]
astro = astro / 255.0

# Apply a convolution with a point spread function (psf)
psf = np.ones((5, 5)) / 25
astro = conv2(astro, psf, 'same')

# Add noise to the image
astro += 0.1 * astro.std() * rng.standard_normal(astro.shape)

# Perform unsupervised Wiener deconvolution
deconvolved, _ = restoration.unsupervised_wiener(astro, psf)

# Plot the original and deconvolved images
fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(8, 5), sharex=True, sharey=True)
plt.gray()

ax[0].imshow(astro, vmin=deconvolved.min(), vmax=deconvolved.max())
ax[0].axis('off')
ax[0].set_title('Data')

ax[1].imshow(deconvolved)
ax[1].axis('off')
ax[1].set_title('Self tuned restoration')

fig.tight_layout()
plt.show()
