from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # path("<int:month>", views.monthly_challenge_by_number),
    # path("<str:month>", views.monthly_challenge, name="month-challenge"),
    path("login/", views.loginPage, name="login"),
    path("logout_user/", views.logout_user, name="logout_user"),
    path("", views.loginPage, name="login1"),
    path("home/", views.index, name="index"),
    path("register/", views.register, name="register"),
    path("contact/", views.contact, name="contact"),
    path("service/", views.service, name="service"),
    path("about/", views.about, name="about"),
    path("team/", views.team, name="team"),
    path("feature/", views.feature, name="feature"),
    path("testimonial/", views.testimonial, name="testimonial"),
    path("detect/", views.ajax, name="detect"),
    path("user/", views.UserView, name="user"),
    path("user/<int:item_id>/", views.TrashDetailView, name="trash_detail"),
    path("trial/", views.gen_Yolov8, name="trial"),
    path("trial1/", views.run_another_cam, name="trial1"),
    path("add_profile/", views.add_profile, name="add_profile"),
    path("update/", views.update_profile, name="update"),
    path("upload_image/", views.upload_image, name="upload_image"),
    path("voucher/", views.VoucherView.as_view(), name="voucher"),
    path("voucher/<int:pk>", views.VoucherDetailView.as_view(), name="voucher_detail"),
    path("buy_voucher/<int:pk>", views.buy_voucher, name="buy_voucher"),
    path("buy_voucher_fail/<int:pk>", views.buy_voucher_fail, name="buy_voucher_fail"),
    path(
        "change_password",
        views.change_password,
        name="change_password",
    ),
    path("password_success", views.password_success, name="password_success"),
    path(
        "post/voucher/<int:pk>/comment/",
        views.AddCommentView.as_view(),
        name="add_comment",
    ),
    path("camera/", views.camera, name="live_camera"),
    path("getdata/", views.getdata, name="getdata"),
    path("detecting/", views.detecting, name="detecting"),
    path("news/", views.NewsView.as_view(), name="news"),
    path("token/", views.token, name="token"),
    path("check_email_code/", views.check_email_code, name="check_email_code"),
    path("success", views.success, name="success"),
    path("qr/", views.qr, name="qr"),
    path("forget_password/", views.forget_password, name="forget_password"),
    path("send_code_reset/", views.send_code_reset, name="send_code_reset"),
    path(
        "check_code_reset_account/",
        views.check_code_reset_account,
        name="check_code_reset_account",
    ),
    path(
        "change_password_without_old/",
        views.change_password_without_old,
        name="change_password_without_old",
    ),
]
