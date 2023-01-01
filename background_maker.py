import argparse
from os import makedirs, path
from PIL import Image


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("image", type=str, help="Input 1920x1080 resolution image")
    arg = parser.parse_args()

    try:
        image = Image.open(arg.image)
        width, height = image.size

        if width != 1920 or height != 1080:
            raise Exception("Supports only 1920x1080 resolution images")

        out_path = path.join(path.dirname(__file__), "resource/background/")
        if not path.exists(out_path):
            makedirs(out_path)

        step = 256
        w_index = ["a", "b", "c", "d", "e", "f", "g", "h"]

        for h in range(0, height, step):
            for w in range(0, width, step):
                part = image.crop((w, h, min(w + step, width), min(h + step, height)))
                filename = f"1920_{h // step + 1}_{w_index[w // step]}_loading.tga"
                part.save(path.join(out_path, filename))
    except Exception as e:
        print(e)
        exit(1)

    print("Transfer 'resource' to the game folder!")


if __name__ == "__main__":
    main()
