from django.shortcuts import render
from .models import NewsArticle

news_set = [
    {
        'title': 'Airbus mở cơ sở nghiên cứu hydro ở Anh, quyết tâm thúc đẩy nhiên liệu hàng không bền vững',
        'url': 'https://tinhte.vn/thread/airbus-mo-co-so-nghien-cuu-hydro-o-anh-quyet-tam-thuc-day-nhien-lieu-hang-khong-ben-vung.3523503/',
        'publisher': 'Tinhte.vn',
        'summary': "Airbus chuẩn bị khai trương một cơ sở nghiên cứu tại Vương quốc Anh, tập trung vào các công nghệ hydro, một động thái thể hiện nỗ lực mới nhất của hãng trong việc thiết kế thế hệ máy bay tiếp theo của mình. Airbus cho biết Trung tâm Phát triển Không phát thải (Zero Emission Development Centre - ZEDC) ở Filton, Bristol, đã bắt đầu làm việc để phát triển công nghệ này. Một trong những mục tiêu chính của cơ sở này sẽ xoay quanh việc nghiên cứu “hệ thống nhiên liệu đông lạnh cạnh tranh về chi phí” mà máy bay ZEROe của hãng cần để bay. Chi tiết về ba chiếc máy bay ý tưởng không phát thải với tên gọi ZEROe đã được công bố vào tháng Chín 2020. Airbus cho biết họ muốn phát triển 'máy bay thương mại không phát thải' vào năm 2035.",
        'top_image': 'https://imgproxy.k7.tinhte.vn/72Xybk9UlJmygysh140QPZLgqZ5fRdRffD5ZqYosdFs/h:460/plain/https://photo2.tinhte.vn/data/attachment-files/2022/05/6001760_cover_airbusfacility.jpg',
        'pub_date': 'May 29, 2022'
    }
]

def index(request):
    context = {
        'news_set': NewsArticle.objects.all()
    }
    
    return render(request, 'newsapp/index.html', context)