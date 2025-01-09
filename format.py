def format_duration(seconds):
    if seconds is None:
        return "Unknown"
    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)

    if h > 0:
        return f"{h}:{m:02}:{s:02}"
    return f"{m}:{s:02}"

def format_views(views):
    if views is None:
        return "Unknown"
    elif views >= 1_000_000:
        return f"{views / 1_000_000:.1f}M"
    elif views >= 1_000:
        return f"{views / 1_000:.1f}K"
    return str(views)

def format_filesize(size):
    if size > 0:
        if size >= 1024 ** 3:
            size_str = f"{size / (1024 ** 3):.2f} GB"
            return size_str
        elif size >= 1024 ** 2:
            size_str = f"{size / (1024 ** 2):.2f} MB"
            return size_str
        else:
            size_str = f"{size / 1024:.2f} KB"
            return size_str
    else:
        size_str = "Unknown"
        return size_str