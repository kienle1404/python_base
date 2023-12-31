def chuvi(length:float, width:float)->float:
    '''
    Hàm tính chu vi hình chữ nhật
    Args:
        length: chieu dai hinh chu nhat
        width: chieu rong hinh chu nhat
    Return:
        output: chu vi hinh chu nhat
    '''
    output = (length + width) * 2
    return output

if __name__ == "__main__":
    from hinhhoc.hinhchunhat.dientich import dientich
    from ..hinhtron.dientich import dientich
    