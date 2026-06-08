
orders = [

    {'id': 'HD01', 'name': 'Dai ly Hoang Long', 'price': 45000000, 'status': 'Paid'},

    {'id': 'HD02', 'name': 'Tap hoa Minh Thu', 'price': 15000000, 'status': 'Unpaid'}

]


def render_orders(order):
    print("---- Danh sách đơn hàng đại lý ----")
    print(f"{"MÃ ĐƠN":<10} | {"TÊN ĐẠI LÝ ":<20} | {"GIÁ TRỊ (VND)":<16} | {"TRẠNG THÁI":<10} ")
    print("-" * 69)
    for list in order:
        print("{id:<10} | {name:<20} | {price:<16} | {status:<10}".format_map(list))
      
    if list == []:
        print("hệ thống hiện chưa có đơn hàng nào !")
    print("-" * 69)
    print()

def add_orders(orders):

    print("\n----- TẠO MỚI ĐƠN HÀNG -----")

    while True:
        order_id = input("Nhập mã đơn hàng: ").strip().upper()

        if order_id == "":
            print("Mã đơn hàng không được để trống!")
            continue

        break

    for order in orders:
        if order["id"] == order_id:
            print("ERR-01: Mã đơn hàng đã tồn tại!")
            return

    while True:
        order_name = input("Nhập tên đại lý: ").strip()

        if order_name == "":
            print("Tên đại lý không được để trống!")
            continue

        break

    while True:
        try:
            order_price = int(input("Nhập giá trị đơn hàng: "))

            if order_price <= 0:
                print("Giá trị đơn hàng phải > 0!")
                continue

            break

        except:
            print("Vui lòng nhập số nguyên!")

    orders.append({
        "id": order_id,
        "name": order_name,
        "price": order_price,
        "status": "Unpaid"
    })

    print("Tạo đơn hàng thành công!")


def update_orders(orders):

    print("\n----- CẬP NHẬT TRẠNG THÁI -----")

    order_id = input("Nhập mã đơn hàng: ").strip().upper()

    for order in orders:

        if order["id"] == order_id:

            if order["status"] == "Paid":
                print("ERR-04: Đơn hàng đã được thanh toán trước đó!")
                return

            order["status"] = "Paid"
            print("Cập nhật trạng thái thành công!")
            return

    print("ERR-03: Không tìm thấy mã đơn hàng!")


def calculate_revenue(orders):

    total_revenue = 0

    for order in orders:
        if order["status"] == "Paid":
            total_revenue += order["price"]

    if total_revenue >= 100000000:
        discount_percent = 5
    else:
        discount_percent = 0

    discount_money = total_revenue * discount_percent / 100

    return (
        total_revenue,
        discount_percent,
        discount_money
    )



def main():
    while True:
        choice = int(input("""=================================================
        QUẢN LÝ ĐƠN HÀNG - AGENT ORDER
=================================================

1. Xem danh sách đơn hàng hiện có
2. Tạo mới đơn hàng đại lý
3. Cập nhật trạng thái thanh toán
4. Tính tổng doanh thu & Chiết khấu
5. Thoát chương trình

=================================================
Hãy nhập lựa chọn của bạn : """))
        print()
        match choice:
            case 1:
                render_orders(orders)
            case 2:
                add_orders(orders)
            case 3:
                update_orders(orders)
            case 4:
                calculate_revenue(orders)
            case 5:
                print("thoát chương trình !! ")
                break
            case _:
                print("lỗi cú pháp !! vui lòng nhập lại lựa chọn...........")


main()