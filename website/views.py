from flask import Blueprint # Import Blueprint để tổ chức các định tuyến và hàm xem thành mô-đun độc lập.


views = Blueprint('views', __name__) # Tạo Blueprint tên 'views' để tổ chức các định tuyến.

@views.route('/')
def home():
    return 'This is the home page'