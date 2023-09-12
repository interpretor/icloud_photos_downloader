"""Path functions"""
import os


def clean_filename(filename):
    """Replaces invalid chars in filenames with '_'"""
    result = filename.encode(
        "utf-8").decode("ascii", "ignore")
    invalid = '<>:"/\\|?*\0'

    for char in invalid:
        result = result.replace(char, '_')

    return result


def local_download_path(media, size, download_dir):
    """Returns the full download path, including size"""
    filename = filename_with_size(media, size)
    download_path = os.path.join(download_dir, filename)
    return download_path


def filename_with_size(media, size):
    """Returns the filename with size, e.g. IMG1234.jpg, IMG1234-small.jpg"""
    # Strip any non-ascii characters.
    filename = clean_filename(media.filename)
    if size == 'original':
        return filename
    return (f"-{size}.").join(filename.rsplit(".", 1))


def live_photo_download_path(media, size, download_dir):
    filename = filename_with_size(media, size)
    live_photo_filename = os.path.splitext(filename)[0] + "_HEVC.MOV"
    download_path = os.path.join(download_dir, live_photo_filename)
    return download_path
