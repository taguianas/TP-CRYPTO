from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

def analyse_images(original_path, encoded_path):
    
    orig = np.array(Image.open(original_path).convert("RGB"))
    mod  = np.array(Image.open(encoded_path).convert("RGB"))

   
    lsb_orig = orig & 1
    lsb_mod  = mod  & 1


    diff = np.abs(lsb_orig - lsb_mod)
    bits_modifies = np.sum(diff)

 
    mse = np.mean((orig - mod) ** 2)

    
    heatmap = np.sum(diff, axis=2)
    plt.imshow(heatmap, cmap="hot")
    plt.title("Heatmap des pixels modifiés")
    plt.colorbar()
    plt.show()

    print("Bits modifiés :", bits_modifies)
    print("MSE :", mse)


    fig, ax = plt.subplots(1, 2, figsize=(12, 5))
    ax[0].imshow(orig)
    ax[0].set_title("Image originale")
    ax[0].axis("off")

    ax[1].imshow(mod)
    ax[1].set_title("Image encodée")
    ax[1].axis("off")

    plt.show()

    return bits_modifies, mse

original = r"C:\Users\manag\Desktop\cloud-security-201908120550101.jpg"
encoded  = r"C:\Users\manag\Desktop\cloud-security-encoded.png"

analyse_images(original, encoded)
