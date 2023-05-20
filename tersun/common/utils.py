"""Common utilities file."""

def get_directory(instance, filename):
    """Determine the upload path for a file."""
    return "{}/{}_{}".format(
        instance.created_on.strftime("%Y/%m/%d"), instance.id, filename)
