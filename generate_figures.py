import os
import matplotlib.pyplot as plt


def main():
    data_folders = os.listdir(".")
    all_photos = []
    model_names = []
    for data_folder in data_folders:
        if data_folder.startswith("testing"):
            model_names.append(data_folder.split("testing_")[1])
            folder_photos = []
            data_folder_path = os.path.join(os.getcwd(), data_folder)
            data_files = os.listdir(data_folder_path)
            for data_file in data_files:
                data_file_path = os.path.join(data_folder_path, data_file)
                folder_photos.append(data_file_path)
            all_photos.append(folder_photos)

    p_idx = [1, 3, 4, 6]
    pic_names = ["Charge Controller", "Battery", "Inverter", "All Components"]
    # model_names = ["A", "B", "C", "D", "E"]
    fig, axes = plt.subplots(nrows=len(all_photos), ncols=len(p_idx))
    print(model_names)
    for axe, model_photos, model_name in zip(axes, all_photos, model_names):
        m_photos = [model_photos[i] for i in p_idx]
        for ax, photo in zip(axe, m_photos):
            ax.imshow(plt.imread(photo))
            plt.setp(ax.get_xticklabels(), visible=False)
            plt.setp(ax.get_yticklabels(), visible=False)
            ax.tick_params(axis="both", which="both", length=0)

    for ax, col in zip(axes[0], pic_names):
        ax.set_title(col)
    for ax, row in zip(axes[:, 0], model_names):
        print(row)
        ax.set_ylabel(row, rotation=90, size="large")
    fig.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
