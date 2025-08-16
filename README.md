# Dự đoán loài hoa Iris với KNN

## 1. Giới thiệu
Trong bài viết này mình sẽ xây dựng một ứng dụng web nhỏ dự đoán loài hoa Iris từ 4 đặc trưng: ...

## 2. Dữ liệu
- Bộ dữ liệu Iris (150 mẫu, 3 loài hoa).
- Các cột: SepalLength, SepalWidth, PetalLength, PetalWidth.

## 3. Thuật toán KNN
KNN tìm k hàng xóm gần nhất bằng khoảng cách Euclidean. Mình chọn k=5.  

Công thức: D(p,q) = sqrt(sum((p_i - q_i)^2))

## 4. Xây dựng ứng dụng Flask
- Backend: Flask
- Frontend: HTML + CSS
- Input: 4 thông số
- Output: loài hoa

## 5. Demo giao diện
Ảnh chụp màn hình form nhập và kết quả dự đoán.
<img width="1902" height="945" alt="image" src="https://github.com/user-attachments/assets/bc53c65a-3e14-4e9d-a6ec-198a59e7f101" />
Kết quả
<img width="1901" height="967" alt="image" src="https://github.com/user-attachments/assets/655c8cfb-760f-4754-a8bd-e919f50163f4" />
Ma trận nhầm lẫn
<img width="1204" height="819" alt="image" src="https://github.com/user-attachments/assets/6c140fa5-4c0d-47d6-abdd-094ebec4c928" />
