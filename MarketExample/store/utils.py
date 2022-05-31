def product_directory_path(instance, filename):
    import uuid 
    try:
        _ext = filename.split('.')[1]
        new_filename = f"{str(uuid.uuid4().hex)}.{_ext}"
    except Exception as e:
        print(f'Error:product_directory_path => {e}')
        new_filename = filename
    return f'{instance.slug}/{new_filename}'