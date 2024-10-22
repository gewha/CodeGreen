import os
from flask import Flask, render_template, request

application = Flask(__name__)

# 이미지 파일 저장 경로
img_dir = "static/images/"
if not os.path.exists(img_dir):
    os.makedirs(img_dir)

@application.route("/")
def hello():
    return render_template("index.html")

@application.route("/list")
def view_list():
    return render_template("list.html")

@application.route("/review")
def view_review():
    return render_template("review.html")

@application.route("/reg_items", methods=["GET", "POST"])
def reg_item():
    if request.method == "POST":
        # POST 요청일 때 입력받은 값들을 가져옵니다.
        name = request.form.get("name")
        seller = request.form.get("seller")
        addr = request.form.get("addr")
        email = request.form.get("email")
        category = request.form.get("category")
        card = request.form.get("card")
        status = request.form.get("status")
        phone = request.form.get("phone")

        # 이미지 파일 처리
        if 'file' not in request.files or request.files["file"].filename == '':
            return "No file selected"
        
        image_file = request.files["file"]
        img_path = f"static/images/{image_file.filename}"
        image_file.save(img_path)

        # 터미널 로그에 출력 (디버깅 용도)
        print(f"Name: {name}, Seller: {seller}, Address: {addr}, Email: {email}")
        print(f"Category: {category}, Credit Card: {card}, Status: {status}, Phone: {phone}")

        # 결과 페이지로 이동
        return render_template("result.html", 
                               name=name, 
                               seller=seller,
                               addr=addr,
                               email=email,
                               category=category,
                               card=card,
                               status=status,
                               phone=phone,
                               img_path=img_path)  # 이미지 경로 전달

    return render_template("reg_items.html")  # GET 요청 시 폼 보여주기

@application.route("/reg_reviews")
def reg_review():
    return render_template("reg_reviews.html")

if __name__ == "__main__":
    application.run(host='0.0.0.0', debug=True)
